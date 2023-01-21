# https://pypi.org/project/PySimpleGUI/
import PySimpleGUI as sg
import do_request
import sys
import os
sys.path.append(os.path.abspath('./src/page'))
import page
import time


# Define the window's contents
layout = [
    [sg.Text("Podaj URL")],
    [sg.Input(key='-URL-')],
    [sg.Text("Podaj ilość wątków")],
    [sg.Input(key='-THREADS-CNT-')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Text(size=(60,1), key='-CALC-')],
    [sg.Button('Start'), sg.Button('Quit')]
]

# Create the window
window = sg.Window('Duży pyton atakuje', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    doRequest = do_request.DoRequest()

    myPage = page.Page(str(values['-URL-']), int(values['-THREADS-CNT-']))

    for i in range(1, 10):
        window['-CALC-'].update('Zaczynamy za ' + str(11 - i) + ' sek')
        time.sleep(1)
        window.refresh()

    doRequest.run_threads(myPage, window['-CALC-'], window)
    # Output a message to the window
    #window['-OUTPUT-'].update('Witaj ' + values['-INPUT-'] + "! Kiler dostał zlecenie na Pana.")
    #window['-CALC-'].update(str(int(values['-VALUE-']) * 2))

# Finish up by removing from the screen
window.close()