import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("System")  # Aparência
ctk.set_default_color_theme("blue")  # Tema

# Janela principal
root = ctk.CTk()
root.geometry("400x300")

# Frame para centralização
frame = ctk.CTkFrame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Configurar o grid do frame para centralização
frame.grid_rowconfigure(0, weight=1)  # Expande a linha
frame.grid_columnconfigure(0, weight=1)  # Expande a coluna

# Adicionar um widget no centro do frame
button = ctk.CTkButton(frame, text="Clique aqui")
button.grid(row=0, column=0, sticky="")  # Centralizado no grid

# Configurar o grid principal para expandir o frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Loop principal
root.mainloop()
