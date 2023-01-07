import PySimpleGUI as sg
import qrcode


layout = [  [sg.Text('Generate QR code')],
            [sg.Text('Enter Text'), sg.InputText()],
            [sg.Button('Generate'), sg.Button('Cancel')] ]


window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Generate':
        img = qrcode.make(values[0])
        type(img)  # qrcode.image.pil.PilImage
        img.save("qrcode.png")
        sg.popup('Here is QRcode', image="qrcode.png")

window.close()