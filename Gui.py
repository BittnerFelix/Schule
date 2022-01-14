
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Bitte WiW Daten eingeben')],
            [sg.Text('WiW'), sg.InputText(key="wiw")],
            [sg.Text("Passwort"), sg.InputText(key="pswd")],
            [sg.Text('Bitte Kunden auswählen')],
            [sg.Radio('Autobahn',"Kunden", default=False, key="1")],
            [sg.Radio('NSI',"Kunden", default=False,key="2")],
            [sg.Radio('NVG',"Kunden", default=False,key="3")],
            [sg.Radio('HAKO',"Kunden", default=False,key="4")],
            [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
            [sg.Button('Ok')]]


# Create the Window
window = sg.Window('SLA - Reporte', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    elif event == "Ok":
        print(values=["-IN-"])
    print('You entered ', values["pswd"])
    Autobahn = values["1"]
    NSI = values["2"]
    if Autobahn == True:
        print("Autobahn")
    elif NSI == True:
        print("NSI")
    else:
        print("nicht vorhanden")
    break

window.close()

