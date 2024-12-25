from Crypto.Cipher import DES
import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi untuk padding
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Fungsi untuk enkripsi
def encrypt(plain_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return encrypted_text.hex()

# Fungsi untuk dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    encrypted_text_bytes = bytes.fromhex(encrypted_text)
    decrypted_text = des.decrypt(encrypted_text_bytes).decode('utf-8').rstrip(' ')
    return decrypted_text

# Fungsi untuk menangani enkripsi melalui GUI
def handle_encrypt():
    plain_text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key harus 8 karakter")
        return

    encrypted_text = encrypt(plain_text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", encrypted_text)

# Fungsi untuk menangani dekripsi melalui GUI
def handle_decrypt():
    encrypted_text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key harus 8 karakter")
        return

    decrypted_text = decrypt(encrypted_text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", decrypted_text)

# Tema GUI
bg_color = "#FFD1DC"  # Light pink background
fg_color = "#FFF0F5"  # Lavender blush for text area
button_color = "#FFC0CB"  # Pink for buttons
header_color = "#FFB6C1"  # Light pink for header

# Membuat GUI dengan tkinter
root = tk.Tk()
root.title("DES Encryption/Decryption")
root.configure(bg=bg_color)
root.geometry("700x500")

# Header
header_frame = tk.Frame(root, bg=header_color, height=60)
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame, text="DES Encryption/Decryption Tool",
    font=("Arial", 18, "bold"), bg=header_color, fg="#4B0082"
)
header_label.pack(pady=15)

# Key Entry
key_frame = tk.Frame(root, bg=bg_color)
key_frame.pack(pady=10, padx=20, fill="x")
key_label = tk.Label(key_frame, text="Key (8 karakter):", font=("Arial", 12), bg=bg_color, fg="#4B0082")
key_label.grid(row=0, column=0, sticky="w")
key_entry = tk.Entry(key_frame, font=("Arial", 12), width=40, relief="solid", bd=2, justify="center", bg=fg_color)
key_entry.grid(row=0, column=1, padx=5, pady=5)

# Input Text Area
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=10, fill="both", expand=True, padx=20)
input_label = tk.Label(input_frame, text="Input Text (Plain/Encrypted):", font=("Arial", 12), bg=bg_color, fg="#4B0082")
input_label.pack(anchor="w")
input_text = tk.Text(input_frame, wrap="word", height=6, bd=2, relief="solid", bg=fg_color, font=("Arial", 12))
input_text.pack(fill="both", expand=True, pady=5)

# Buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)
encrypt_button = tk.Button(
    button_frame, text="Encrypt", command=handle_encrypt,
    font=("Arial", 12, "bold"), bg=button_color, relief="flat", fg="#4B0082"
)
decrypt_button = tk.Button(
    button_frame, text="Decrypt", command=handle_decrypt,
    font=("Arial", 12, "bold"), bg=button_color, relief="flat", fg="#4B0082"
)
encrypt_button.grid(row=0, column=0, padx=15, pady=5)
decrypt_button.grid(row=0, column=1, padx=15, pady=5)

# Output Text Area
output_frame = tk.Frame(root, bg=bg_color)
output_frame.pack(pady=10, fill="both", expand=True, padx=20)
output_label = tk.Label(output_frame, text="Output Text:", font=("Arial", 12), bg=bg_color, fg="#4B0082")
output_label.pack(anchor="w")
output_text = tk.Text(output_frame, wrap="word", height=6, bd=2, relief="solid", bg=fg_color, font=("Arial", 12))
output_text.pack(fill="both", expand=True, pady=5)

# Menjalankan GUI
root.mainloop()
