import qrcode
import os

# Define Data
data = "🔍 Curious? Scan to Discover!"

# Create QR Code Object
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Generate QR Code Image
img = qr.make_image(fill_color="red", back_color="white")

# Save Path (Example: Saving in current directory)
save_path = "myqrcode.png"

# Ensure Directory Exists (optional for deeper directories)
os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)

# Save the Image
img.save(save_path)

print("QR Code saved successfully at:", os.path.abspath(save_path))
