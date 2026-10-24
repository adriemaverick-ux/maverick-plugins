ObjC.import('CoreGraphics'); ObjC.import('Foundation');
const arr = ObjC.deepUnwrap(ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionOnScreenOnly, $.kCGNullWindowID)));
const out = [];
for (const w of arr) {
  if ((w.kCGWindowOwnerName||'').indexOf('Chrome') >= 0) {
    const b = w.kCGWindowBounds || {};
    out.push(`id=${w.kCGWindowNumber} capa=${w.kCGWindowLayer} x=${b.X} y=${b.Y} w=${b.Width} h=${b.Height} titulo=${(w.kCGWindowName||'').slice(0,40)}`);
  }
}
out.join('\n');
