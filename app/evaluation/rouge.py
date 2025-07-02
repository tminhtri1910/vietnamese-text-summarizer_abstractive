from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def calculate_rouge(reference_summary, generated_summary):
    reference_tokens = reference_summary.split()
    generated_tokens = generated_summary.split()

    # Calculate precision, recall, and F1 score for ROUGE
    precision = precision_score(reference_tokens, generated_tokens, average='binary', zero_division=0)
    recall = recall_score(reference_tokens, generated_tokens, average='binary', zero_division=0)
    f1 = f1_score(reference_tokens, generated_tokens, average='binary', zero_division=0)

    return {
        'precision': precision,
        'recall': recall,
        'f1': f1
    }