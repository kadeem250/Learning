import qrcode
import image

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)

# The data that you want to store
data = str(input("Enter a text or URL: "))
name =str(input("What would you like to save the time file as?"))
# Add data
qr.add_data(data)
qr.make(fit=True)

# Creates an image the QR code image
img = qr.make_image()

# Save it somewhere, change the extension as needed:
#Saves in in directory as py file
img.save(name +".jpg")