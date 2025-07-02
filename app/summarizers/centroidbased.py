import numpy as np
from .preprocessing import split_into_sentences, sentences_to_vectors

class CentroidBasedSummarizer:
    def __init__(self) -> None:
        pass

    def summarize(self, text, ratio):
        '''Trả về tóm tắt của văn bản dựa vào centroid-based'''
        sentences = split_into_sentences(text)
        content_vectors = sentences_to_vectors(sentences)

        centroid = np.mean([content_vector for content_vector in content_vectors], axis=0)

        distances = []
        for content_vector in content_vectors:
            distance = np.linalg.norm(content_vector - centroid) #tính khoảng cách dùng L2
            distances.append(distance)

        sorted_indices = np.argsort(distances)
        n_sentences = max(round(len(sentences) * ratio), 1)
        top_indices = sorted_indices[:n_sentences]

        summary = '. '.join([sentences[i] for i in top_indices]) + '.'
        return summary