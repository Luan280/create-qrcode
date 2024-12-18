import customtkinter as ctk
from PIL import Image
from index import create_qrcode


def chama_qrcode():
    create_qrcode(data=url.get(),size_qrcode= size_qrcode.get(),size_box= size_box.get(),
                  size_border=size_border.get(), bg_color=background_color.get())

    imagem = ctk.CTkImage(light_image=Image.open('qrcode.png'), size=(1000, 1000))
    # display image with a CTkLabel
    image_label = ctk.CTkLabel(app, image=imagem, text="")
    image_label.grid(row=0, column=2)


app = ctk.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('1920x1080')

frame_main = ctk.CTkFrame(app)
frame_main.grid(column=0, row=0, sticky="")

# Configurar o grid do frame para centralização
frame_main.grid_columnconfigure(0, weight=1)  # Expande a coluna
frame_main.grid_rowconfigure(0, weight=1)  # Expande a linha


lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']


size_width = 300
size_height = 30

text_url = ctk.CTkLabel(frame_main, text="Digite a URL ou código PIX")
text_url.place(x=20, y=0)

url = ctk.CTkEntry(frame_main, placeholder_text="Digite a URL ou código PIX",
                   width=size_width, height=size_height)
url.grid(row=1, column=0, padx=20, pady=20, sticky="", columnspan=10)

text_qrcode = ctk.CTkLabel(frame_main, text="Digite o tamanho do qrcode")
text_qrcode.place(x=20, y=60)

size_qrcode = ctk.CTkComboBox(
    frame_main, values=lista, width=size_width, height=size_height)
size_qrcode.grid(row=2, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_qrcode.set(1)

text_box = ctk.CTkLabel(
    frame_main, text="Digite o tamanho do quadrado dentro do qrcode")
text_box.place(x=20, y=130)

size_box = ctk.CTkComboBox(
    frame_main, values=lista[:20], width=size_width, height=size_height)
size_box.grid(row=3, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_box.set(10)

text_border = ctk.CTkLabel(
    frame_main, text="Digite o tamanho da borda do qrcode")
text_border.place(x=20, y=200)

size_border = ctk.CTkComboBox(
    frame_main, values=lista[4:20], width=size_width, height=size_height)
size_border.grid(row=4, column=0, padx=20, pady=20, sticky="", columnspan=10)
size_border.set(4)

text_fill_color = ctk.CTkLabel(
    frame_main, text="Digite o código hexadecimal da cor que você quer de fundo")
text_fill_color.place(x=20, y=270)

background_color = ctk.CTkEntry(
    frame_main, placeholder_text="#ffa7ff", width=size_width, height=size_height)
background_color.grid(row=5, column=0, padx=20, pady=20, sticky="", columnspan=10)


test_button = ctk.CTkButton(
    frame_main, text="MOSTRAR QRCODE", command=chama_qrcode)
test_button.grid(row=6, column=0, padx=20, pady=20, sticky="")

download_button = ctk.CTkButton(frame_main, text="DOWNLOAD QRCODE")
download_button.grid(row=6, column=1, padx=20, pady=20, sticky="")


app.mainloop()