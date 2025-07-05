from flask import Blueprint, render_template, request, jsonify
from app.forms import SummarizationForm
from app.summarizers.kmeans import KMeansSummarizer
from app.summarizers.textrank import TextRankSummarizer
from app.summarizers.centroidbased import CentroidBasedSummarizer
from app.summarizers.vit5 import Vit5Summarizer
from app.summarizers.bartpho import BARTphoSummarizer

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.evaluation.rouge import calculate_rouge
import os
import flash

app = Blueprint('app', __name__, template_folder='templates')

tokenizer_t5 = AutoTokenizer.from_pretrained(r"app\data\vit5model_1\vit5model_1")
model_t5 = AutoModelForSeq2SeqLM.from_pretrained(r"app\data\vit5model_1\vit5model_1")

tokenizer_bartpho = AutoTokenizer.from_pretrained(r"app\data\vit5model_1\vit5model_1")
model_bartpho = AutoModelForSeq2SeqLM.from_pretrained(r"app\data\bartphomodel_1\bartphomodel_1")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SummarizationForm()
    text = kmeans_summary = textrank_summary = centroidbased_summary = ""
    vit5_summary = bartpho_summary = ""
    ratio = 1

    # if form.validate_on_submit():
    #     text = None
    #     if form.text_input.data:
    #         text = form.text_input.data
    #     elif form.file_upload.data:
    #         file = form.file_upload.data
    #         text = file.read().decode('utf-8')

    #     if not text:
    #         flash('Please provide either text input or upload a file')
    #         return render_template('index.html', form=form)

    #     kmeans_summarizer = KMeansSummarizer()
    #     textrank_summarizer = TextRankSummarizer()

    #     kmeans_summary = kmeans_summarizer.summarize(text)
    #     textrank_summary = textrank_summarizer.summarize(text)

    #     # rouge_scores = calculate_rouge(kmeans_summary, textrank_summary)

    #     # return render_template('results.html', 
    #     #                        kmeans_summary=kmeans_summary, 
    #     #                        textrank_summary=textrank_summary, 
    #     #                        rouge_scores=rouge_scores)

    if request.method == "POST":      
        if request.form["text_input"]:
            text = request.form["text_input"]
        else:
            file = request.form.get("file_upload")
            text = file.read().decode('utf-8')

        if request.form.get("summary_level"):
            level = request.form["summary_level"]
            if level == "short": ratio = 0.25
            elif level == "medium": ratio = 0.5
            else: ratio == 0.75

        # Summarizers
        kmeans_summarizer = KMeansSummarizer()  
        textrank_summarizer = TextRankSummarizer()
        centroidbased_summarizer = CentroidBasedSummarizer()
        vit5_summarizer = Vit5Summarizer()
        bartpho_summarizer = BARTphoSummarizer()

        n_sentences = 6
        # kmeans_summary = kmeans_summarizer.summarize(text, ratio)
        # textrank_summary = textrank_summarizer.summarize(text, ratio)
        # centroidbased_summary = centroidbased_summarizer.summarize(text, ratio)
        vit5_summary = vit5_summarizer.summarize(text, tokenizer_t5, model_t5)
        bartpho_summary = bartpho_summarizer.summarize(text, tokenizer_bartpho, model_bartpho)

    return render_template('index.html', 
                            form=form, 
                            text = text,
                            # kmeans_summary = kmeans_summary, 
                            # textrank_summary = textrank_summary,
                            # centroidbased_summary = centroidbased_summary,
                            vit5_summary = vit5_summary,
                            bartpho_summary = bartpho_summary
                            )
