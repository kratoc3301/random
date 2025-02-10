import numpy as np
from PIL import Image

# Choose a new color
new_color = (205, 132, 232, 255)

# Load the image
image_path = "/home/panagiotis/Downloads/qwerty.png"
image = Image.open(image_path).convert("RGBA")

# Convert to numpy array
data = np.array(image)

# Replace pixels with the new color but only for non-transparent pixels
non_transparent = data[:, :, 3] > 0  # Check if pixel is not transparent
data[non_transparent] = new_color  # Apply the new color

# Convert back to image
colored_image = Image.fromarray(data)

# Save the colored image
new_name = image_path.split("/")[-1]
new_image_path = f"/home/panagiotis/Downloads/1colored{new_name}"
colored_image.save(new_image_path)

