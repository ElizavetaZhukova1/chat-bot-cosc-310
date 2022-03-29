import wikipedia
import spacy
PROH_WORDS=["define", 'definition', 'know', 'mean', 'meaning']
class Wiki:
    """A class for identifying the definition user needs and finding it on wikipedia"""
    _nlp = spacy.load("en_core_web_sm")
    def __init__(self, sentence):
        self.processed=self._nlp(sentence)
        self.term=self.get_term()
    def get_term(self):
        res=""
        for token in self.processed:
            if (token.pos_ == "PROPN" or token.pos_ == "NOUN"):
                if(token.text.lower() not in PROH_WORDS):
                    res=res+" "+token.text
        print(res)
        return res

    def find_article(self):
        print(wikipedia.search(self.term))
        return wikipedia.search(self.term)[0]
    def get_full_summary(self):
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
        full=self.get_full_summary()
        tokenized=self._nlp(full)
        return " ".join([sent.text for sent in tokenized.sents][:3])

