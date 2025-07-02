from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from .preprocessing import split_into_sentences, sentences_to_vectors
from sklearn.metrics import pairwise_distances_argmin_min


class KMeansSummarizer:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters

    # def _vectorize_sentences(self, sentences):
    #     vectorizer = TfidfVectorizer()
    #     return vectorizer.fit_transform(sentences)

    def _get_average_sentence_indices(self, kmeans, n_sentences):
        avg_indices = []
        for i in range(n_sentences):
            cluster_indices = np.where(kmeans.labels_ == i)[0]
            avg_index = np.mean(cluster_indices)
            avg_indices.append(avg_index)
        return avg_indices

    def _generate_summary(self, kmeans, content_vectors, sentences, avg_indices, n_sentences):
        ordering = sorted(range(n_sentences), key=lambda k: avg_indices[k])
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, content_vectors) #lấy index của câu gần nhất với tâm cụm
        return '. '.join([sentences[closest[i]] for i in ordering]) + '.'
        
    def summarize(self, text, ratio):
        # sentences = self._split_into_sentences(text)
        # tfidf_matrix = self._vectorize_sentences(sentences)

        sentences = split_into_sentences(text)
        content_vectors = sentences_to_vectors(sentences)

        n_clusters = max(round(len(content_vectors) * ratio), 1)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans = kmeans.fit(content_vectors)

        avg_indices = []
        for i in range(n_clusters):
            cluster_indices = np.where(kmeans.labels_ == i)[0]
            avg_index = np.mean(cluster_indices)
            avg_indices.append(avg_index)
        # ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        ordering = np.argsort(avg_indices)

        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, content_vectors) #lấy index của câu gần nhất với tâm cụm

        summary = '. '.join([sentences[closest[i]] for i in ordering]) + '.'
        
        return summary