import customtkinter as ctk
from PIL import Image
from index import create_qrcode


def chama_qrcode():
    create_qrcode(url.get(), size_qrcode.get(), size_box.get(), size_border.get())

app = ctk.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('500x500')
# app.grid_rowconfigure(0, weight=1)
# app.grid_rowconfigure(1, weight=1)
# app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=0)

app.grid_columnconfigure(2, weight=0)

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
imagem = ctk.CTkImage(light_image=Image.open('qrcode.png'),size=(30, 30))

size_width = 300
size_height = 30
url = ctk.CTkEntry(app, placeholder_text="Digite a URL ou código PIX", width=size_width, height=size_height)
url.grid(row=1, column=0, padx=10, pady=10)

size_qrcode = ctk.CTkComboBox(app, width=size_width, height=size_height)
size_qrcode.grid(row=2, column=1, padx=10, pady=10)

size_box = ctk.CTkComboBox(app, width=size_width, height=size_height)
size_box.grid(row=3, column=1, padx=10, pady=10)

size_border = ctk.CTkComboBox(app, width=size_width, height=size_height)
size_border.grid(row=4, column=1, padx=10, pady=10)
size_border.configure(values=lista)

download_button = ctk.CTkButton(app, text="DOWNLOAD QRCODE")
download_button.grid(row=5, column=1, padx=10, pady=10)


test_button = ctk.CTkButton(app, text="MOSTRAR QRCODE", command=chama_qrcode)
test_button.grid(row=5, column=2, padx=10, pady=10 )



app.mainloop()