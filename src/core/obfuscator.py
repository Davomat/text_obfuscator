from googletrans import LANGUAGES
from googletrans import Translator
import random


class Obfuscator:

    def __init__(self):
        self._translator = Translator()

    def obfuscate(self, text: str, iterations: int, progbar, languages) -> str:
        # catch zero length error
        if len(text) <= 1:
            return 'Please fill in some text in any language.'

        # init progress value
        progress_var = [0]

        # select languages
        lang_list = languages if len(languages) > 0 else list(LANGUAGES.values())

        # switch to inner recursive function
        translation = self._inner_obfuscate(text, iterations, progress_var, progbar, lang_list)

        # back to first source language only in the outer function
        src_lang = self._translator.detect(text).lang
        translation = self._translator.translate(translation, dest=src_lang).text

        return translation

    def _inner_obfuscate(self, text: str, iterations: int, progress: [int], progbar, languages) -> str:
        # stop criteria
        if iterations <= 0:
            return text

        language = random.choice(languages)
        translation = self._translator.translate(text, dest=language).text

        # update progress
        progress[0] += (100 - progress[0])/iterations
        print(f"{iterations} iterations remaining. Current language {language}. Progress: {progress[0]} %")
        progbar.update_bar(progress[0])

        # recursive call
        translation = self._inner_obfuscate(translation, iterations-1, progress, progbar, languages)

        return translation
