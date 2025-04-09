import qrcode  # Import the qrcode library to create QR codes
import os  # Import os library to handle file paths

# Define Data
data = "🔍 Curious? Scan to Discover!"  # The data (text) that will be encoded in the QR code

# Create QR Code Object
qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Create a QR code object with specified settings
qr.add_data(data)  # Add the data to the QR code object
qr.make(fit=True)  # Ensure the QR code fits the data

# Generate QR Code Image
img = qr.make_image(fill_color="red", back_color="white")  # Generate the QR code image with red color for the code and white background

# Save Path (Example: Saving in current directory)
save_path = "myqrcode.png"  # Define where to save the generated QR code image (in this case, the current directory)

# Ensure Directory Exists (optional for deeper directories)
os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)  # Create the directory if it doesn't exist (this is optional for deeper folder structures)

# Save the Image
img.save(save_path)  # Save the generated QR code image to the defined path

print("QR Code saved successfully at:", os.path.abspath(save_path))  # Print the absolute path where the QR code was saved
