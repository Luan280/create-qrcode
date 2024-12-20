import customtkinter as ctk
from PIL import Image
from index import create_qrcode


def chama_qrcode():
    respose = create_qrcode(data=url.get(), size_qrcode= size_qrcode.get(), size_box= size_box.get(),
                  size_border=size_border.get(), bg_color=background_color.get())
    print(respose)

    imagem = ctk.CTkImage(light_image=Image.open('qrcode.png'), size=(500, 500))
    image_label = ctk.CTkLabel(app, image=imagem, text="")
    image_label.place(x= 800, y=100)


app = ctk.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('1920x1080')

frame_main = ctk.CTkFrame(app)
frame_main.place(x=100, y=100)

# Configurar o grid do frame para centralização
frame_main.grid_columnconfigure(0, weight=1)  # Expande a coluna
frame_main.grid_rowconfigure(0, weight=1)  # Expande a linha


lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

TEXT_ALING_X = 30
SIZE_WIDTH = 500
SIZE_HEIGHT = 40
msg_image = ""

text_url = ctk.CTkLabel(frame_main, text="URL ou código PIX", font=("Arial", 20))
text_url.grid(row=0,column=0, padx=20, sticky="w")

url = ctk.CTkEntry(frame_main, placeholder_text="https://www.instagram.com/luan_lima280/",
                   width=SIZE_WIDTH, height=SIZE_HEIGHT)
url.grid(row=1, column=0, padx=20, pady=20, sticky="w")

text_qrcode = ctk.CTkLabel(frame_main, text="Tamanho do QR Code", font=("Arial", 20))
text_qrcode.grid(row=2,column=0, padx=20, sticky="w")

size_qrcode = ctk.CTkComboBox(
    frame_main, values=lista, width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_qrcode.grid(row=3, column=0, padx=20, pady=20, sticky="w")
size_qrcode.set(1)

text_box = ctk.CTkLabel(
    frame_main, text="Tamanho do quadrado dentro do QR Code", font=("Arial", 20))
text_box.grid(row=4,column=0, padx=20, sticky="w")

size_box = ctk.CTkComboBox(
    frame_main, values=lista[:20], width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_box.grid(row=5,column=0, padx=20, pady=20, sticky="w")
size_box.set(10)

text_border = ctk.CTkLabel(
    frame_main, text="Tamanho da borda do QR Code", font=("Arial", 20))
text_border.grid(row=6,column=0, padx=20, sticky="w")

size_border = ctk.CTkComboBox(
    frame_main, values=lista[4:20], width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_border.grid(row=7, column=0, padx=20, pady=20, sticky="w")
size_border.set(4)

text_fill_color = ctk.CTkLabel(
    frame_main, text="Código Hexadecimal da cor de fundo", font=("Arial", 20))
text_fill_color.grid(row=8,column=0, padx=20, sticky="w")

background_color = ctk.CTkEntry(
    frame_main, placeholder_text="#ffa7ff", width=SIZE_WIDTH, height=SIZE_HEIGHT)
background_color.grid(row=9, column=0, padx=20, pady=20, sticky="w")

frame_button = ctk.CTkFrame(frame_main)
frame_button.grid(row=10,column=0)

test_button = ctk.CTkButton(
    frame_button, text="MOSTRAR QR CODE", command=chama_qrcode)
test_button.grid(row=0, column=0, padx=20, pady=20, sticky='w')

download_button = ctk.CTkButton(frame_button, text="DOWNLOAD QRCODE")
download_button.grid(row=0, column=1, padx=20, pady=20, sticky='e')

text_image
app.mainloop()