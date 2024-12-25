import tkinter as tk
from tkinter import ttk

class Enigma:
    def __init__(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

    def process(self, text):
        # Simplified Enigma Process (reverse text for now)
        return text[::-1]

def process_text():
    text = text_input.get("1.0", tk.END).strip()
    rotor1 = int(entry_rotor1.get() or 0)
    rotor2 = int(entry_rotor2.get() or 0)
    rotor3 = int(entry_rotor3.get() or 0)
    
    enigma = Enigma(rotor1, rotor2, rotor3)
    result = enigma.process(text)
    
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

bg_color = "#FDFD96"  # Soft pastel yellow background
header_color = "#F1E15E"  # Light pastel yellow header
button_color = "#F4E04D"  # Soft yellow for buttons
frame_color = "#F9F9A5"  # Light yellow frame background
text_color = "#424242"  # Dark text color

# Setup root window
root = tk.Tk()
root.title("Enigma Steganography Tool")
root.configure(bg=bg_color)
root.geometry("800x500")
root.resizable(True, True)

# Heading
header_label = tk.Label(root, text="Enigma Steganography Tool", font=("Arial", 18, "bold"), bg=header_color, fg="black", pady=10)
header_label.pack(fill="x")

# Main Frame
frame_main = tk.Frame(root, bg=frame_color, bd=2, relief="groove", padx=20, pady=10)
frame_main.pack(expand=True, fill="both", padx=10, pady=10)

# Rotor Position Frame
frame_rotors = tk.Frame(frame_main, bg=frame_color)
frame_rotors.pack(pady=5, fill="x")

tk.Label(frame_rotors, text="Rotor 1 Position:", bg=frame_color, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5)
entry_rotor1 = tk.Entry(frame_rotors, width=5, font=("Arial", 12), bg="white", fg=text_color)
entry_rotor1.grid(row=0, column=1, padx=10)

tk.Label(frame_rotors, text="Rotor 2 Position:", bg=frame_color, font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5)
entry_rotor2 = tk.Entry(frame_rotors, width=5, font=("Arial", 12), bg="white", fg=text_color)
entry_rotor2.grid(row=0, column=3, padx=10)

tk.Label(frame_rotors, text="Rotor 3 Position:", bg=frame_color, font=("Arial", 10, "bold")).grid(row=0, column=4, sticky="w", padx=5)
entry_rotor3 = tk.Entry(frame_rotors, width=5, font=("Arial", 12), bg="white", fg=text_color)
entry_rotor3.grid(row=0, column=5, padx=10)

# Input Text Frame
frame_input = tk.Frame(frame_main, bg=frame_color)
frame_input.pack(pady=5, fill="both", expand=True)

tk.Label(frame_input, text="Input Text:", bg=frame_color, font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
text_input = tk.Text(frame_input, height=6, font=("Arial", 12), bg="white", fg=text_color, wrap="word")
text_input.pack(fill="both", expand=True, padx=5, pady=5)

# Process Button
process_btn = tk.Button(frame_main, text="Proses", command=lambda: process_text(), bg=button_color, fg="white",
                        font=("Arial", 12, "bold"), padx=10, pady=5)
process_btn.pack(pady=10)

# Output Text Frame
frame_output = tk.Frame(frame_main, bg=frame_color)
frame_output.pack(pady=5, fill="both", expand=True)

tk.Label(frame_output, text="Output:", bg=frame_color, font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
text_output = tk.Text(frame_output, height=6, font=("Arial", 12), bg="white", fg=text_color, wrap="word")
text_output.pack(fill="both", expand=True, padx=5, pady=5)

# Function to process text
def process_text():
    text = text_input.get("1.0", tk.END).strip()
    rotor1 = int(entry_rotor1.get() or 0)
    rotor2 = int(entry_rotor2.get() or 0)
    rotor3 = int(entry_rotor3.get() or 0)

    enigma = Enigma(rotor1, rotor2, rotor3)
    result = enigma.process(text)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)
    
# Responsive behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_main.columnconfigure(0, weight=1)

root.mainloop()
