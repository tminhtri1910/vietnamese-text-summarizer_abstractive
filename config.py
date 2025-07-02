import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    UPLOAD_FOLDER = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
    LANGUAGES = ['vi']  # Vietnamese language support
    SUMMARY_METHODS = ['kmeans', 'textrank']  # Available summarization methods
    ROUGE_METRICS = ['rouge-1', 'rouge-2', 'rouge-l']  # ROUGE metrics for evaluation

    @staticmethod
    def init_app(app):
        pass  # Additional app initialization can be done here if needed