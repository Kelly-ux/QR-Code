import qrcode

# Parameters fo creating a QR code 
qr = qrcode.QRCode( # type: ignore
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, # type: ignore
    box_size=10,
    border=4,
)

# Provide redirective to link url
qr.add_data("https://photos.app.goo.gl/7RXjW38MoNT2459o6")

# Image declaration 
img = qr.make_image()

# Save image formate 
img.save("qrcode.png")