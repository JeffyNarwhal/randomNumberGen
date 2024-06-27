import random
import webbrowser
import PySimpleGUI as sg
import pyperclip

randomlist = []
copylist = []

layout = [
    [sg.Text("Random Number Generator"), sg.Button(
        "Info", key="Info")],
    [sg.Input("1", size=(15, 1)),
     sg.Input("10", size=(15, 1)), sg.Button("Copy", key="Copy")],
    [sg.Text(key="Text")],
    [sg.Button("Generate", key="Gen"), sg.Button("Quit"), sg.Text(
        "Numbers Generated:"), sg.Input("1", size=(3, 1))]
]

window = sg.Window("Number Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "Info":
        webbrowser.open('https://github.com/JeffyNarwhal/randomNumberGen', new=1)
    if event == "Gen":
        try: 
            Min, Max = int(values[0]), int(values[1])
        except:
            window["Text"].update("One or more values are not an integer")
            continue
        for i in range(int(values[2])):
            if Min > Max:
                Min, Max = Max, Min
            n = random.randint(int(Min), int(Max))
            randomlist.append(n)
            window["Text"].update(randomlist)
            copylist = randomlist
        randomlist = []
    if event == "Copy":
        pyperclip.copy(str(copylist))

window.close