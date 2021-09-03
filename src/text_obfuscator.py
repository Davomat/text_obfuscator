from core.obfuscator import Obfuscator
import PySimpleGUI as sg
import threading

layout = [[sg.Multiline(size=(100, 20), key='source_text')],  # identify the multiline via key option
          [sg.Text("Iterations:", font='Lucida'),
           sg.Slider(orientation='horizontal', key='iter_slider', range=(1, 20))],
          [sg.Button('Obfuscate')],
          [sg.ProgressBar(100, orientation='h', size=(65, 20), border_width=4, key='progbar',
                          bar_color=['Green', 'Grey'])],
          [sg.Multiline(size=(100, 20), key='destination_text')],
          [sg.Button('Close Application')]]


def run_obfuscation(source_text: str, iterations: int):
    progress_var = [0]

    text_obfuscated = obf.obfuscate(source_text, iterations, window['progbar'])
    window['destination_text'].update(text_obfuscated)


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

        if event in 'Obfuscate':
            # reset progbar value
            progress_var = [0]

            # start threaded obfuscation
            thread = threading.Thread(target=run_obfuscation, args=(values['source_text'], values['iter_slider']))
            thread.daemon = True
            thread.start()

    window.close()
