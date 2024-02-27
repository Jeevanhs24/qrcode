import pyqrcode

def generate_linkedin_qr(linkedin_url, filename):
    qr = pyqrcode.create(linkedin_url)
    qr.png(filename, scale=8)

if __name__ == "__main__":
    linkedin_url = "https://www.linkedin.com/in/jeevan-h-s-3b119029b/"
    filename = "linkedin_qr_code.png"
    generate_linkedin_qr(linkedin_url, filename)
    print(f"QR Code for LinkedIn profile generated and saved as {filename}")
