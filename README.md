# QR Code Generator with Logo

This script generates QR codes for a list of URLs provided in a text file and embeds a logo in the center of each QR code.

## Setup

1. **Install Dependencies:**
   Make sure you have Python 3 installed. Then, install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Input Files:**

    * **`urls.txt`**: Create a file named `urls.txt` in the same directory as the script. Each line in this file should contain one URL for which you want to generate a QR code.
    * **`logo.png`**: Place the logo image file named `logo.png` in the same directory as the script. This logo will be embedded in the center of the generated QR codes. Ensure the logo has a transparent background (RGBA) for best results, although RGB is also supported.

## Running the Script

Once the setup is complete, run the script from your terminal:

```bash
python qr-generator.py
```

## Output

The script will:

1. Read URLs from `urls.txt`.
2. Generate a QR code for each URL.
3. Resize the `logo.png` and embed it in the center of the QR code.
4. Save the generated QR codes as PNG files in the `qrcodes/` directory. The filenames will be derived from the URL paths, with non-alphanumeric characters replaced by underscores.
5. Print the path of each saved QR code to the console.

If `urls.txt` or `logo.png` are not found, the script will print an error message and exit.
