import customtkinter as ctk

ctk.set_appearence_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.Ctk()
root.geometry("500x350")

def login():
    print("Test")

frame = ctk.CtkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CtkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = ctk.CtkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CtkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()