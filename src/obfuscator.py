from googletrans import LANGUAGES
from googletrans import Translator
import random


class Obfuscator:

    def __init__(self):
        self._translator = Translator()

    def obfuscate(self, text: str, iterations: int):
        print(f"{iterations} iterations remaining.")

        # switch to inner recursive function
        translation = self._inner_obfuscate(text, iterations - 1)

        # back to first source language only in the outer function
        src_lang = self._translator.detect(text).lang
        translation = self._translator.translate(translation, dest=src_lang).text

        return translation

    def _inner_obfuscate(self, text: str, iterations: int):
        print(f"{iterations} iterations remaining.")

        translation = self._translator.translate(text, dest=random.choice(list(LANGUAGES.keys()))).text

        # recursive call with stop criteria
        if iterations > 0:
            translation = self._inner_obfuscate(translation, iterations-1)

        return translation


