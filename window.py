# # https://pypi.org/project/PySimpleGUI/
import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [
    [sg.Text("Jak masz na imię?")],     # Part 2 - The Layout
    [sg.Input()],
    [sg.Button('Ok')]
]

# Create the window
window = sg.Window('Nazwa okna', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Po wykonaniu eventów wykona się dalsza częśc programu

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window