import qrcode

def create_qrcode(data=None ,size_qrcode=1, size_box=10, size_border=4):
    # Dados que serão codificados no QR Code
    data = data # URL do site ou código pix

    # Criar QR Code
    qr = qrcode.QRCode(
        version=size_qrcode,  # Tamanho do QR Code (1 é o menor, 40 é o maior)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=size_box,  # Tamanho de cada "caixa" do QR Code
        border=size_border # Tamanho da borda (mínimo é 4)
    )

    # Adicionar dados ao QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Gerar imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Salvar a imagem
    img.save("qrcode.png")

    # Mostrar a imagem (opcional)
    # img.show()