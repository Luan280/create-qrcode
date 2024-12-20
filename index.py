import qrcode
from PIL import Image

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


# create_qrcode(data="youtube.com", size_qrcode=20, size_box=40,
#               size_border=4, bg_color="#4d8f81", fill_color="white")
