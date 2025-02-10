import numpy as np
from PIL import Image

# Load the original image
image_path = "/.../.../.../..."
image = Image.open(image_path).convert("RGBA")

# Convert image to numpy array
data = np.array(image)

threshold = 200

# Make whites transparent
white_mask = (data[:, :, 0] > threshold) & (data[:, :, 1] > threshold) & (data[:, :, 2] > threshold)
data[white_mask] = [0, 0, 0, 0]  # Set white pixels to transparent

# Convert back to image
hollow_image = Image.fromarray(data)

# Save the processed image
new_name = image_path.split("/")[-1]
new_image_path = f"/.../.../.../...{new_name}"
hollow_image.save(new_image_path)
