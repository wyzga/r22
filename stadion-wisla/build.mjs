// Builds index.html — the stand-alone local copy — from stadion.html (the published page body).
// Textures and the optional crest are inlined as data: URIs, because browsers refuse to use
// images loaded from file:// as WebGL textures. Run: node build.mjs
import fs from 'node:fs';
import path from 'node:path';

const dir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const read = f => fs.readFileSync(path.join(dir, f));
const assets = {};
for (const f of ['tex/grass.jpg', 'tex/concrete.jpg', 'tex/facade.jpg', 'tex/roof.jpg', 'tex/park.jpg', 'tex/seat.jpg']) {
  assets[f] = 'data:image/jpeg;base64,' + read(f).toString('base64');
}
if (fs.existsSync(path.join(dir, 'herb.svg'))) assets['herb.svg'] = 'data:image/svg+xml;base64,' + read('herb.svg').toString('base64');

// the local copy drops the note under the title card
const body = read('stadion.html').toString('utf8').replace(/\s*<p class="src" id="srcNote">[^<]*<\/p>/, '');
const html = `<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>window.__ASSETS = ${JSON.stringify(assets)};</script>
${body}
</html>
`;
fs.writeFileSync(path.join(dir, 'index.html'), html);
console.log('index.html', Math.round(html.length / 1024), 'KB,', Object.keys(assets).length, 'assets inlined');
