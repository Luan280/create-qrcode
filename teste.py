import customtkinter
app = customtkinter.CTk()
app.title("CRIADOR DE QRCODE")
app.geometry('500x500')


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")


combobox_callback()

app.mainloop()