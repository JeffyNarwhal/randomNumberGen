import random
import webbrowser
import PySimpleGUI as sg
import pyperclip

randomlist = []
copylist = []

layout = [

    [sg.Text("Random Number Generator"), sg.Button(
        "Info", key="Info")],
    [sg.Input(size=(15, 1)),
     sg.Input(size=(15, 1)), sg.Button("Copy", key="Copy")],
    [sg.Text(key="Text")],
    [sg.Button("Generate", key="Gen"), sg.Button("Quit"), sg.Text(
        "Numbers Generated:"), sg.Input("1", size=(3, 1))]

]


window = sg.Window("Number Gen", layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "Info":
        webbrowser.open('https://www.youtube.com/channel/UCAOMblfh6EkuQQByFFgpCcQ', new=1)
    if event == "Gen":
        Max = values[1]
        Min = values[0]
        for i in range(int(values[2])):
            if int(Min) > int(Max):
                Min = values[1]
                Max = values[0]
            n = random.randint(int(Min), int(Max))
            randomlist.append(n)
            window["Text"].update(randomlist)
            copylist = randomlist
        randomlist = []
    if event == "Copy":
        pyperclip.copy(str(copylist))

window.close
