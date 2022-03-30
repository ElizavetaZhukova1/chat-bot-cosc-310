from googletrans import Translator
class Translator:
    """A class for translating the sentence from user's language to english"""
    _translate = Translator()
    def __init__(self, user_text):
        self.utrans=self._translate.translate(user_text)
    def utrans_text(self):
        """Returns the lowercased user's text translated to english"""
        return self.utrans.text.lower()
    def get_ulang(self):
        """Returns the language user used then typing a message"""
        return self.utrans.src
    def trans_resp(self, response):
        """Translates the bot's response to the user's language"""
        btrans=self._translate.translate(response, dest=self.get_ulang())
        return btrans.text

