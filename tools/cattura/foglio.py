# Foglio provini: foglio.py out.png img1 img2 ... (griglia 2 colonne, ogni immagine larga 1000)
import sys
from PIL import Image, ImageDraw
out, files = sys.argv[1], sys.argv[2:]
W = 1000
ims = []
for f in files:
    im = Image.open(f).convert('RGB')
    h = int(im.height * W / im.width)
    ims.append((__import__('os').path.basename(f), im.resize((W, h))))
cols = 2
rows = (len(ims) + 1) // 2
rh = max(im.height for _, im in ims) + 30
sheet = Image.new('RGB', (W * cols + 10, rh * rows), 'white')
d = ImageDraw.Draw(sheet)
for i, (n, im) in enumerate(ims):
    x, y = (i % cols) * (W + 10), (i // cols) * rh
    d.text((x + 5, y + 5), n, fill='red')
    sheet.paste(im, (x, y + 25))
sheet.save(out)
