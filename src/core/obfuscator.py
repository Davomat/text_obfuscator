from googletrans import LANGUAGES
from googletrans import Translator
import random


class Obfuscator:

    def __init__(self):
        self._translator = Translator()
        self._languages = []

    def obfuscate(self, text: str, iterations: int, progbar, languages) -> (str, list):
        # catch zero length error
        if len(text) <= 1:
            return 'Please fill in some text in any language.', []

        # reset progress bar
        progbar.update_bar(0)

        # get source language
        src_lang = self._translator.detect(text).lang
        self._languages = [src_lang]

        # select languages
        lang_list = languages if len(languages) > 0 else list(LANGUAGES.values())

        # switch to inner recursive function
        translation = self._inner_obfuscate(text, iterations, 0, progbar, lang_list)

        # back to first source language only in the outer function
        translation = self._translator.translate(translation, dest=src_lang).text
        progbar.update_bar(100)
        self._languages.append(src_lang)

        return translation, self._languages

    def _inner_obfuscate(self, text: str, iterations: int, progress: int, progbar, languages) -> str:
        # stop criteria
        if iterations <= 0:
            return text

        # get next random translation
        language = random.choice(languages)
        translation = self._translator.translate(text, dest=language).text
        self._languages.append(language)

        # update progress
        progress += (100 - progress)/(iterations+1)
        print(f"{iterations} iterations remaining. Current language {language}. Progress: {progress} %")
        progbar.update_bar(progress)

        # recursive call
        translation = self._inner_obfuscate(translation, iterations-1, progress, progbar, languages)

        return translation
