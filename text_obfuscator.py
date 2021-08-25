from obfuscator import Obfuscator
import PySimpleGUI as sg

layout = [[sg.Multiline(size=(100, 20), key='source_text')],  # identify the multiline via key option
          [sg.Text("Iterations:",font='Lucida'), sg.Slider(orientation='horizontal', key='iter_slider', range=(1, 20))],
          [sg.Button('Obfuscate')],
          [sg.Multiline(size=(100, 20), key='destination_text')],
          [sg.Button('Close Application')]]


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Text Obfuscator', layout).Finalize()

    # Init the Obfuscator
    obf = Obfuscator()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Close Application'):  # if user closes window or clicks cancel
            break

        if event in ('Obfuscate'):
            text_obfuscated = obf.obfuscate(values['source_text'], values['iter_slider'])
            window['destination_text'].update(text_obfuscated)

    window.close()
