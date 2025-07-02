class Summarizer:
    def __init__(self, text):
        self.text = text

    def preprocess(self):
        raise NotImplementedError("Preprocessing method must be implemented.")

    def summarize(self):
        raise NotImplementedError("Summarization method must be implemented.")

    def evaluate(self, reference_summary):
        raise NotImplementedError("Evaluation method must be implemented.")