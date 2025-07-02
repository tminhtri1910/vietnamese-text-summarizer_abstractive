from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .preprocessing import split_into_sentences, sentences_to_vectors
import networkx as nx

class TextRankSummarizer:
    def __init__(self, num_sentences=3):
        self.num_sentences = num_sentences
        # self.similarity_matrix = None

    def build_similarity_matrix(self, content_vectors):
        self.similarity_matrix = cosine_similarity(content_vectors)

    def score_sentences(self, sentences):
        graph = nx.from_numpy_array(self.similarity_matrix) # Xây dựng đồ thị từ ma trận tương đồng
        sentences_scores = nx.pagerank(graph)
        ranked_sentences = sorted(((sentences_scores[i], s) for i, s in enumerate(sentences)), reverse=True)

        # sentences_scores = np.sum(self.similarity_matrix, axis=1)
        # ranked_sentences = [(sentences_scores[i],sentences[i]) for i in np.argsort(sentences_scores, axis=0)[::-1]]

        return ranked_sentences
    
    def summarize(self, text, ratio):
        sentences = split_into_sentences(text)
        content_vectors = sentences_to_vectors(sentences)

        self.build_similarity_matrix(content_vectors)
        ranked_sentences = self.score_sentences(sentences)
        n_sentences = max(round(len(sentences) * ratio), 1)
        summary = '. '.join([sentence for score, sentence in ranked_sentences[:n_sentences]]) + '.'

        # summary = '. '.join(ranked_sentences[:self.num_sentences]) + '.' if ranked_sentences else ''
        return summary