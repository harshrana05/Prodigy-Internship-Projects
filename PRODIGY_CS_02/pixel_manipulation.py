import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def swap_pixel_values(img_data):
    # Swap red and blue channels
    return [(pixel[2], pixel[1], pixel[0]) for pixel in img_data]

def encrypt_image(input_path, output_path):
    try:
        # Open the image
        img = Image.open(input_path)
        img = img.convert("RGB")  # Convert image to RGB mode if not already

        # Load image data
        img_data = list(img.getdata())

        # Encrypt the image by swapping pixel values
        encrypted_data = swap_pixel_values(img_data)

        # Create a new image with the encrypted data
        encrypted_img = Image.new("RGB", img.size)
        encrypted_img.putdata(encrypted_data)

        # Save the encrypted image
        encrypted_img.save(output_path)
        messagebox.showinfo("Success", "Image encrypted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error encrypting image: {e}")

def decrypt_image(input_path, output_path):
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        img = img.convert("RGB")  # Convert image to RGB mode if not already

        # Load image data
        img_data = list(img.getdata())

        # Decrypt the image by swapping pixel values back
        decrypted_data = swap_pixel_values(img_data)

        # Create a new image with the decrypted data
        decrypted_img = Image.new("RGB", img.size)
        decrypted_img.putdata(decrypted_data)

        # Save the decrypted image
        decrypted_img.save(output_path)
        messagebox.showinfo("Success", "Image decrypted successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error decrypting image: {e}")

def browse_file():
    return filedialog.askopenfilename()

def browse_save_file():
    return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

def encrypt_action():
    input_path = browse_file()
    if not input_path:
        return
    output_path = browse_save_file()
    if not output_path:
        return
    encrypt_image(input_path, output_path)

def decrypt_action():
    input_path = browse_file()
    if not input_path:
        return
    output_path = browse_save_file()
    if not output_path:
        return
    decrypt_image(input_path, output_path)

# Create the main window
root = tk.Tk()
root.title("Image Encryption and Decryption Tool")

# Create and place the widgets
mode_label = tk.Label(root, text="Select Mode:")
mode_label.grid(row=0, column=0, padx=10, pady=10)

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_action)
encrypt_button.grid(row=0, column=1, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_action)
decrypt_button.grid(row=0, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
