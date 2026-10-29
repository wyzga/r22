#!/usr/bin/env python3
"""Publishes the stadium (stadion-wisla/) under /r22/ of the shared wyzga.com Firebase Hosting site.

The site hosts several apps, so this never replaces the whole site: it clones the live release,
drops the old /r22/ files, adds the new ones and publishes that. Everything else (/, cv,
/mistrzczasu/, /pixally/ ...) keeps its exact files and headers.

Needs: FIREBASE_SA_JSON (service-account key as a string, from a GitHub secret).
Usage in CI: python3 tools/deploy_r22.py
"""
import gzip, hashlib, json, os, sys, time
import urllib.error, urllib.parse, urllib.request
from pathlib import Path

PROJECT = "gen-lang-client-0339658958"
SITE = PROJECT
API = "https://firebasehosting.googleapis.com/v1beta1"
PREFIX = "/r22/"
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "stadion-wisla"


def access_token() -> str:
    """Exchange the service-account key for an OAuth token (no gcloud needed on the runner)."""
    import base64, subprocess, tempfile
    sa = json.loads(os.environ["FIREBASE_SA_JSON"])
    now = int(time.time())
    def b64(d: bytes) -> bytes:
        return base64.urlsafe_b64encode(d).rstrip(b"=")
    header = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claim = b64(json.dumps({
        "iss": sa["client_email"], "scope": "https://www.googleapis.com/auth/firebase https://www.googleapis.com/auth/cloud-platform",
        "aud": "https://oauth2.googleapis.com/token", "iat": now, "exp": now + 3000}).encode())
    unsigned = header + b"." + claim
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(sa["private_key"]); key = f.name
    try:
        sig = subprocess.check_output(["openssl", "dgst", "-sha256", "-sign", key], input=unsigned)
    finally:
        os.unlink(key)
    jwt = (unsigned + b"." + b64(sig)).decode()
    body = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": jwt}).encode()
    with urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=body), timeout=60) as r:
        return json.loads(r.read())["access_token"]


TOK: str = ""


def call(method, url, body=None, raw=None, ctype="application/json"):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + TOK, "x-goog-user-project": PROJECT, "Content-Type": ctype})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            t = r.read()
            return json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} {method} {url}\n{e.read().decode()[:800]}")


def main() -> None:
    global TOK
    if not SRC.joinpath("stadion.html").exists():
        sys.exit("stadion-wisla/stadion.html missing")
    TOK = access_token()

    rel = call("GET", f"{API}/sites/{SITE}/releases?pageSize=1")["releases"][0]
    old = rel["version"]["name"]; cfg = rel["version"].get("config", {})
    print("live release:", old.split("/")[-1], rel.get("releaseTime"))

    files, tok = {}, ""
    while True:
        r = call("GET", f"{API}/{old}/files?pageSize=1000" + (f"&pageToken={tok}" if tok else ""))
        for f in r.get("files", []):
            files[f["path"]] = f["hash"]
        tok = r.get("nextPageToken", "")
        if not tok:
            break
    kept = {p: h for p, h in files.items() if not p.startswith(PREFIX)}
    print(f"files: {len(files)} live, {len(files) - len(kept)} under {PREFIX} replaced, {len(kept)} kept")

    new, blobs = {}, {}
    pub = {"index.html": SRC / "stadion.html", "herb.svg": SRC / "herb.svg"}   # stadion.html is the source of index.html
    for sub in ("tex", "audio"):
        for p in sorted((SRC / sub).rglob("*")):
            if p.is_file():
                pub[f"{sub}/{p.relative_to(SRC / sub).as_posix()}"] = p
    for rel_p, p in pub.items():
        gz = gzip.compress(p.read_bytes(), mtime=0)
        h = hashlib.sha256(gz).hexdigest(); new[PREFIX + rel_p] = h; blobs[h] = gz
    print("new files:", len(new))

    cfg = dict(cfg)
    hdr = [h for h in cfg.get("headers", []) if not str(h.get("glob", "")).startswith(PREFIX)]
    hdr += [
        {"glob": PREFIX, "headers": {"Cache-Control": "no-cache"}},
        {"glob": PREFIX + "index.html", "headers": {"Cache-Control": "no-cache"}},
        {"glob": PREFIX + "tex/**", "headers": {"Cache-Control": "public, max-age=86400"}},
        {"glob": PREFIX + "audio/**", "headers": {"Cache-Control": "public, max-age=86400"}},
        {"glob": PREFIX + "herb.svg", "headers": {"Cache-Control": "public, max-age=86400"}},
    ]
    cfg["headers"] = hdr

    ver = call("POST", f"{API}/sites/{SITE}/versions", {"config": cfg})["name"]
    allf = dict(kept); allf.update(new)
    pop = call("POST", f"{API}/{ver}:populateFiles", {"files": allf})
    need, up = pop.get("uploadRequiredHashes", []), pop.get("uploadUrl")
    print("to upload:", len(need))
    for h in need:
        call("POST", f"{up}/{h}", raw=blobs[h], ctype="application/octet-stream")
    call("PATCH", f"{API}/{ver}?update_mask=status", {"status": "FINALIZED"})
    sha = os.environ.get("GITHUB_SHA", "local")[:7]
    r = call("POST", f"{API}/sites/{SITE}/releases?versionName={ver}", {"message": f"r22 {sha} (repo wyzga/r22)"})
    print("RELEASED:", r["name"].split("/")[-1], r.get("releaseTime"))


if __name__ == "__main__":
    main()
