import qrcode
import customtkinter as ctk
from PIL import Image
import os
import shutil


def download_qrcode():
    arquivo_atual = os.getcwd()
    # Caminho do arquivo atual
    arquivo_atual += "/qrcode.png"
    # Caminho do novo destino
    novo_diretorio = "/home/luan-lima/Downloads"
    # Mover o arquivo
    shutil.move(arquivo_atual, novo_diretorio)


def create_qrcode(fill_color="black", bg_color="white", data=None, size_qrcode=1, size_box=10, size_border=4):
    # Dados que serão codificados no QR Code
    data = data  # URL do site ou código pix

    # Criar QR Code
    qr = qrcode.QRCode(
        version= size_qrcode,  # Tamanho do QR Code (1 é o menor, 40 é o maior)
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Nível de correção de erro
        box_size= size_box,  # Tamanho de cada "caixa" do QR Code
        border=size_border  # Tamanho da borda (mínimo é 4)
    )

    # Adicionar dados ao QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Gerar imagem do QR Code
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)

    # Salvar a imagem
    img.save("qrcode.png")

    # Abrir a imagem
    imagem = Image.open("qrcode.png")

    # Obter o tamanho (largura, altura)
    largura, altura = imagem.size
    return largura, altura


def show_data_qrcode():
    # Passa os dados de entrada e manda pra função que gera o QR Code, que retorna o tamanho do QR Code
    qrcode_image_size = create_qrcode(data=url.get(), size_qrcode= size_qrcode.get(), size_box= size_box.get(),
                  size_border=size_border.get(), fill_color=background_color.get())
    # Limita o tamanho do QR Code na tela
    if qrcode_image_size[0] > 700:
        image_limit = (700, 700)
    else:
        image_limit = qrcode_image_size
    # Abre o QR Code
    imagem = ctk.CTkImage(light_image=Image.open('qrcode.png'), size=(image_limit[0], image_limit[1]))
    # Mostra o QR Code na tela
    image_label = ctk.CTkLabel(frame_qrcode, image=imagem, text="")
    image_label.grid(row=1, column=2, columnspan=10, sticky="nsew")
    # Depois que recebe os dados do QR Code, mostra uma mensagem com o tamanho do QR Code
    text_image.configure(text=f"O tamanho do QR Code é {qrcode_image_size[:]} pixels", font=("Arial", 20))
    

app = ctk.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('1920x1080')

frame_main = ctk.CTkFrame(app, fg_color="transparent")
frame_main.place(x=100, y=100)

frame_qrcode = ctk.CTkFrame(app, fg_color="transparent")
frame_qrcode.place(x=800, y=30)

# Configurar o grid do frame para centralização
frame_main.grid_columnconfigure(0, weight=1)  # Expande a coluna
frame_main.grid_rowconfigure(0, weight=1)  # Expande a linha


lista = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'
]

TEXT_ALING_X = 30
SIZE_WIDTH = 500
SIZE_HEIGHT = 40
msg_image = ""

text_url = ctk.CTkLabel(frame_main, text="URL ou código PIX", font=("Arial", 20))
text_url.grid(row=1,column=0, padx=20, sticky="w")

url = ctk.CTkEntry(frame_main, placeholder_text="https://www.instagram.com/luan_lima280/",
                   width=SIZE_WIDTH, height=SIZE_HEIGHT)
url.grid(row=2, column=0, padx=20, pady=20, sticky="w")

text_qrcode = ctk.CTkLabel(frame_main, text="Tamanho do QR Code", font=("Arial", 20))
text_qrcode.grid(row=3,column=0, padx=20, sticky="w")

size_qrcode = ctk.CTkComboBox(
    frame_main, values=lista, width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_qrcode.grid(row=4, column=0, padx=20, pady=20, sticky="w")
size_qrcode.set(1)

text_box = ctk.CTkLabel(
    frame_main, text="Tamanho da caixa do QR Code", font=("Arial", 20))
text_box.grid(row=5,column=0, padx=20, sticky="w")

size_box = ctk.CTkComboBox(
    frame_main, values=lista[:20], width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_box.grid(row=6,column=0, padx=20, pady=20, sticky="w")
size_box.set(10)

text_border = ctk.CTkLabel(
    frame_main, text="Tamanho da borda do QR Code", font=("Arial", 20))
text_border.grid(row=7,column=0, padx=20, sticky="w")

size_border = ctk.CTkComboBox(
    frame_main, values=lista[3:20], width=SIZE_WIDTH, height=SIZE_HEIGHT)
size_border.grid(row=8, column=0, padx=20, pady=20, sticky="w")
size_border.set(4)

text_fill_color = ctk.CTkLabel(
    frame_main, text="Código Hexadecimal da cor do QR Code", font=("Arial", 20))
text_fill_color.grid(row=9,column=0, padx=20, sticky="w")

background_color = ctk.CTkEntry(
    frame_main, placeholder_text="#ffa7ff", width=SIZE_WIDTH, height=SIZE_HEIGHT)
background_color.grid(row=10, column=0, padx=20, pady=20, sticky="w")

frame_button = ctk.CTkFrame(frame_main, fg_color="transparent")
frame_button.grid(row=11, column=0)

test_button = ctk.CTkButton(
    frame_button, text="MOSTRAR QR CODE", command=show_data_qrcode, width=200, height=35)
test_button.grid(row=0, column=0, padx=20, pady=20, sticky='w')

download_button = ctk.CTkButton(frame_button, text="DOWNLOAD QRCODE", command=lambda: download_qrcode(), width=200, height=35)
download_button.grid(row=0, column=1, padx=20, pady=20, sticky='e')

text_image = ctk.CTkLabel(frame_qrcode, text=msg_image)
text_image.grid(row=0, column=2, columnspan=10, padx=20, pady=20, sticky="nsew")

app.mainloop()