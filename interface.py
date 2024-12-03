import customtkinter as ctk

windown = ctk.CTk()
windown.title("CRIADOR DE QRCODE")
windown.geometry('500x500')

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

size_width = 300
size_height = 30
url = ctk.CTkEntry(windown, placeholder_text="Digite a URL ou código PIX", width=size_width, height=size_height)
url.pack()

size_qrcode = ctk.CTkEntry(windown, placeholder_text="Digite o tamanho do qrcode", width=size_width, height=size_height)
size_qrcode.pack()

size_box = ctk.CTkEntry(windown, placeholder_text="Digite o tamanho da caixa", width=size_width, height=size_height)
size_box.pack()

size_border = ctk.CTkComboBox(windown, width=size_width, height=size_height)
size_border.pack()
size_border.configure(values=lista)

download_button = ctk.CTkButton(windown, text="DOWNLOAD QRCODE")
download_button.pack()


test_button = ctk.CTkButton(windown, text="MOSTRAR QRCODE")
test_button.pack()




windown.mainloop()