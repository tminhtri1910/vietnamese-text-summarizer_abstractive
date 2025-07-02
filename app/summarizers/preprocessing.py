import numpy as np
from gensim.models import KeyedVectors
from pyvi import ViTokenizer

# Tải mô hình word2vec
w2v = KeyedVectors.load_word2vec_format(r"app\data\vi.vec")
vocab = w2v.key_to_index #Danh sách các từ trong từ điển

# Load set stopword
with open(r"app\data\vietnamese-stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().splitlines())

def split_into_sentences(content):
    return [sentence for sentence in content.strip().split('.') if sentence]

def sentences_to_vectors(sentences):
    '''Trả về danh sách các vector đại diện và các câu của 1 văn bản'''
    #Sentences to vector
    content_vectors = [] #list chứa các vector các câu của 1 văn bản
    for sentence in sentences:
        sentence = sentence.lower()
        sentence_tokenized = ViTokenizer.tokenize(sentence) #tách từ trong câu
        words = sentence_tokenized.split(" ") # tạo list các từ
        words = [word.replace("_"," ") for word in words if word not in stopwords] #lọc bỏ stopword

        sentence_vector = np.zeros((100)) #tạo vector (np array) cho 1 câu có độ dài là 100 số 0
        if len(words) != 0:
            for word in words:
                if word in vocab:
                    sentence_vector += w2v[word] #vector của câu là tổng của vector của các từ trong câu

            sentence_vector /= len(words) #chia cho số từ trong câu để lấy trung bình

        content_vectors.append(sentence_vector)
    return content_vectors

