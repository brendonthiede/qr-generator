import os
import qrcode
from PIL import Image
from urllib.parse import urlparse

INPUT_FILE  = "urls.txt"
OUTPUT_DIR  = "qrcodes"
LOGO_PATH   = "logo.png"
LOGO_SCALE  = .25

has_error = False

if not os.path.isfile(INPUT_FILE):
    print(f"{INPUT_FILE} not found.")
    has_error = True

if not os.path.isfile(LOGO_PATH):
    print(f"{LOGO_PATH} not found.")
    has_error = True

if has_error:
    print("Please check the input file and logo path.")
    print(f"{INPUT_FILE} (list of URLs) and {LOGO_PATH} (logo to embed in the QR code) must exist.")
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

base_logo = Image.open(LOGO_PATH)

with open(INPUT_FILE) as f:
    for idx, line in enumerate(f):
        url = line.strip()
        if not url:
            continue

        # Generate QR with high error correction
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # open, resize, and paste the logo
        logo = base_logo.copy()
        qr_w, qr_h = qr_img.size

        # scale the logo based on the QR code size
        logo_size = qr_w * LOGO_SCALE
        logo.thumbnail((logo_size, logo_size), Image.ANTIALIAS)

        # compute position to center the logo
        pos = ((qr_w - logo.width) // 2, (qr_h - logo.height) // 2)
        qr_img.paste(logo, pos, mask=logo if logo.mode=='RGBA' else None)

        # for the filename, remove the https://<domain>/<first_segment>/ part and replace all non-alphanumeric characters with _
        parts = urlparse(url).path.strip("/").split("/")
        path = "/".join(parts[1:])
        safe = "".join(c if c.isalnum() else "_" for c in path)
        filename = f"{safe}.png"
        path = os.path.join(OUTPUT_DIR, filename)
        qr_img.save(path)
        print(f"QR code saved as  {path}")
print("Done!")
