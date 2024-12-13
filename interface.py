import customtkinter as ctk
from PIL import Image
from index import create_qrcode


def chama_qrcode():
    create_qrcode(url.get(), size_qrcode.get(), size_box.get(), size_border.get())
    imagem = ctk.CTkImage(light_image=Image.open('qrcode.png'),size=(30, 30))
    image_label = ctk.CTkLabel(app, image=imagem, text="")  # display image with a CTkLabel
    image_label.grid(row=2, column=3)

    
app = ctk.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('1920x1080')

frame_main = ctk.CTkFrame(app)
frame_main.grid(column=0,row=0, sticky="")

# Configurar o grid do frame para centralização
frame_main.grid_columnconfigure(0, weight=1)  # Expande a coluna
frame_main.grid_rowconfigure(0, weight=1)  # Expande a linha


lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']


size_width = 300
size_height = 30

url = ctk.CTkEntry(frame_main, placeholder_text="Digite a URL ou código PIX", width=size_width, height=size_height)
url.grid(row=0, column=0, padx=20, pady=20, sticky="", columnspan=10)

size_qrcode = ctk.CTkComboBox(frame_main, values=lista, width=size_width, height=size_height)
size_qrcode.grid(row=1, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_qrcode.set("Tamanho do qrcode")


size_box = ctk.CTkComboBox(frame_main, values=lista[:20] , width=size_width, height=size_height)
size_box.grid(row=2, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_box.set("Tamanho da caixa")

size_border = ctk.CTkComboBox(frame_main, values=lista[:20], width=size_width, height=size_height)
size_border.grid(row=3, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_border.set("Tamanho da borda")

test_button = ctk.CTkButton(frame_main, text="MOSTRAR QRCODE", command=chama_qrcode)
test_button.grid(row=4, column=0, padx=20, pady=20, sticky="")

download_button = ctk.CTkButton(frame_main, text="DOWNLOAD QRCODE")
download_button.grid(row=4, column=1, padx=20, pady=20, sticky="")


app.mainloop()