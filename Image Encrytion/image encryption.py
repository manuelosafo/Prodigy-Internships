from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Get the dimensions of the image
    width, height = img.size

    # Iterate over each pixel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Get the red, green, blue components of the pixel

            # Swapping red and blue channels
            encrypted_pixel = (b, g, r)  # Create new pixel with swapped red and blue

            # Update the pixel with the encrypted value
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    pixels = img.load()  # Load pixel data

    # Get the dimensions of the image
    width, height = img.size

    # Iterate over each pixel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Get the red, green, blue components of the pixel

            # Swapping red and blue channels back to original
            decrypted_pixel = (b, g, r)  # Create new pixel with swapped red and blue

            # Update the pixel with the decrypted value
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = r"D:\Prodigy Tech\Image Encrytion\Girl.jpg"
encrypted_image = r"D:\Prodigy Tech\Image Encrytion\encrypted_image.jpg"
decrypted_image = r"D:\Prodigy Tech\Image Encrytion\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)


# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
