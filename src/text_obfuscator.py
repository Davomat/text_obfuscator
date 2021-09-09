from core.obfuscator import Obfuscator
import PySimpleGUI as sg
import threading

from googletrans import LANGUAGES

choices = list(LANGUAGES.values())

layout = [
    [sg.Multiline(size=(100, 20), key='source_text')],
    [sg.Text("Languages:", font='Lucida'), sg.Listbox(choices, size=(15, 5), select_mode='extended', key='languages')],
    [sg.Text("Iterations:", font='Lucida'), sg.Slider(orientation='horizontal', key='iter_slider', range=(1, 20))],
    [sg.Button('Obfuscate', size=(20, 2)),
     sg.ProgressBar(100, orientation='h', size=(40, 20), border_width=4, key='progbar', bar_color=('Green', 'Grey'))],
    [sg.Multiline(size=(100, 2), key='language_list')],
    [sg.Multiline(size=(100, 20), key='destination_text')],
    [sg.Button('Close Application', size=(20, 2))]
]


def run_obfuscation(source_text: str, iterations: int, languages: [str]):
    text_obfuscated, obfuscation_languages = obf.obfuscate(source_text, iterations, window['progbar'], languages)
    window['destination_text'].update(text_obfuscated)
    window['language_list'].update(' -> '.join(obfuscation_languages))


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Text Obfuscator', layout, element_justification='c').Finalize()

    # Init the Obfuscator
    obf = Obfuscator()

    # Event Loop to process "events" and get the "values" of the inputs
    while True:

        event, values = window.read()
        if event in (None, 'Close Application'):  # if user closes window or clicks cancel
            break

        if event in 'Obfuscate':
            # reset progbar value and clear text fields
            progress_var = [0]
            window['language_list'].update('')
            window['destination_text'].update('')

            # start threaded obfuscation
            thread = threading.Thread(target=run_obfuscation,
                                      args=(values['source_text'], values['iter_slider'], values['languages']))
            thread.daemon = True
            thread.start()

    window.close()
