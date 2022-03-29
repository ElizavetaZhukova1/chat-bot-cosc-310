from googletrans import Translator
class Translator:
    """A class for translating the sentence from user's language to english"""
    _translate = Translator()
    def __init__(self, user_text):
        self.utrans=self._translate.translate(user_text)
    def utrans_text(self):
        return self.utrans.text.lower()
    def get_ulang(self):
        return self.utrans.src
    def trans_resp(self, response):
        self.btrans=self._translate.translate(response, dest=self.get_ulang())
        return self.btrans.text

