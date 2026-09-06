import qrcode

text = input("Enter text or URL: ")

img = qrcode.make(text)

filename = "qr_code.png"
img.save(filename)

print("\n===== QR CODE GENERATOR =====")
print("QR Code generated successfully!")
print("Saved as:", filename)
print("=============================")