import wikipedia
import spacy
PROH_WORDS=["define", 'definition', 'know', 'mean', 'meaning']
class Wiki:
    """A class for identifying the word user needs a definition for and finding it on wikipedia"""
    _nlp = spacy.load("en_core_web_sm")
    def __init__(self, sentence):
        self.processed=self._nlp(sentence)
        self.term=self.get_term()
    def get_term(self):
        """Returns the string - the word user wants a definition for (using Spacy)"""
        res=""
        for token in self.processed:
            if (token.pos_ == "PROPN" or token.pos_ == "NOUN"):
                if(token.text.lower() not in PROH_WORDS):
                    res=res+" "+token.text
        return res

    def find_article(self):
        """Searches for the tem on Wikipedia and returns the first result as a string"""
        return wikipedia.search(self.term)[0]
    def get_full_summary(self):
        """Returns the summary of a specified Wikipedia page (as a string)"""
        try:
            article=self.find_article()
            return wikipedia.summary(article, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError:
            try:
                return wikipedia.summary("Academic " + article)
            except:
                return "Sorry, I could not find the Wikipedia page for your request"
        except:
            return "Sorry, I could not find the Wikipedia page for your request"
    def get_short_summary(self):
        """Gets the summary of the Wikipedia page and returns the first 3 sentences of the summary as a string"""
        full=self.get_full_summary()
        tokenized=self._nlp(full)
        return " ".join([sent.text for sent in tokenized.sents][:3])

