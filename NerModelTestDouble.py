class SpanTestDouble():
    def __init__(self, text, label_):
        self.text = text
        self.label_ = label_


class DocTestDouble():
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]


class NerModelTestDouble:
    """
    Test double for a spaCy NLP model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self,ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)