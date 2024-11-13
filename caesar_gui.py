import tkinter as tk
from tkinter import ttk

# Fungsi enkripsi dan dekripsi sederhana (Caesar Cipher)
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

# Fungsi yang dijalankan ketika tombol "Process Text" ditekan
def process_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_value.get())
    mode = mode_var.get()
    output_text.delete("1.0", tk.END)  # Clear previous output

    if mode == "encrypt":
        result = caesar_cipher(text, shift, 'encrypt')
    else:
        result = caesar_cipher(text, shift, 'decrypt')
    
    output_text.insert(tk.END, result)

# Warna tema pastel yang lebih lembut
bg_color = "#ECEFF1"   # Light gray pastel
fg_color = "#D7E8FF"   # Soft pastel blue

# Set up root window
root = tk.Tk()
root.title("Cipher Encryption Machine")
root.configure(bg=bg_color)
root.geometry("650x500")  # Ukuran jendela awal

# Frame untuk heading aplikasi
header_frame = tk.Frame(root, bg=fg_color, height=60)
header_frame.pack(fill="x")

# Heading
header_label = tk.Label(header_frame, text="Cipher Encryption Machine", font=("Arial", 18, "bold"), bg=fg_color, fg="#2F4F4F")
header_label.pack(pady=15)

# Judul aplikasi
title_label = tk.Label(root, text="Simple Caesar Cipher Tool", font=("Arial", 14, "italic"), bg=bg_color, fg="#455A64")
title_label.pack(pady=(10, 15))

# Frame untuk input nilai shift
shift_frame = tk.Frame(root, bg=bg_color)
shift_frame.pack(pady=5, fill="x", padx=20)

shift_label = tk.Label(shift_frame, text="Set Shift Value:", font=("Arial", 12), bg=bg_color)
shift_label.grid(row=0, column=0, sticky="w")

# Menggunakan Spinbox untuk Shift Value
shift_value = tk.StringVar(value="1")
shift_spinbox = tk.Spinbox(
    shift_frame, from_=1, to=25, textvariable=shift_value, width=5,
    font=("Arial", 12), relief="flat", bd=2, justify="center",
    bg=fg_color, fg="#2F4F4F", buttonbackground=bg_color
)
shift_spinbox.grid(row=0, column=1, padx=5, pady=5)

# Frame untuk area input teks
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=10, fill="both", expand=True, padx=20)

input_label = tk.Label(input_frame, text="Input Text to Encrypt/Decrypt", font=("Arial", 12), bg=bg_color)
input_label.pack(anchor="w")

input_text = tk.Text(input_frame, wrap="word", height=5, bd=2, relief="solid", bg=fg_color, font=("Arial", 12))
input_text.pack(fill="both", expand=True, pady=5)

# Frame untuk mode (Encrypt/Decrypt) dan tombol proses
mode_frame = tk.Frame(root, bg=bg_color)
mode_frame.pack(pady=10)

# Mengatur tampilan radio button dan tombol
style = ttk.Style()
style.configure("TRadiobutton", font=("Arial", 12, "bold"), background=bg_color)

mode_var = tk.StringVar(value="encrypt")
encrypt_radio = ttk.Radiobutton(mode_frame, text="ENCRYPT", variable=mode_var, value="encrypt", style="TRadiobutton")
decrypt_radio = ttk.Radiobutton(mode_frame, text="DECRYPT", variable=mode_var, value="decrypt", style="TRadiobutton")
encrypt_radio.grid(row=0, column=0, padx=15)
decrypt_radio.grid(row=0, column=1, padx=15)

process_button = tk.Button(mode_frame, text="PROCESS TEXT", command=process_text, bg=fg_color, font=("Arial", 12, "bold"), relief="flat")
process_button.grid(row=0, column=2, padx=15)

# Frame untuk output teks
output_frame = tk.Frame(root, bg=bg_color)
output_frame.pack(pady=10, fill="both", expand=True, padx=20)

output_label = tk.Label(output_frame, text="Output", font=("Arial", 12), bg=bg_color)
output_label.pack(anchor="w")

output_text = tk.Text(output_frame, wrap="word", height=5, bd=2, relief="solid", bg=fg_color, font=("Arial", 12))
output_text.pack(fill="both", expand=True, pady=5)

# Fungsi untuk membuat layout responsif
def on_resize(event):
    window_width = event.width
    window_height = event.height
    shift_frame.grid_propagate(0)
    mode_frame.grid_propagate(0)
    output_frame.grid_propagate(0)
    input_text.config(width=window_width // 10)
    output_text.config(width=window_width // 10)

root.bind("<Configure>", on_resize)  # Mengikat event resize dengan fungsi on_resize

# Menjalankan aplikasi
root.mainloop()
