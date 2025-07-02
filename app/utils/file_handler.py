def save_uploaded_file(uploaded_file):
    if uploaded_file.filename != '':
        file_path = f"app/static/uploads/{uploaded_file.filename}"
        uploaded_file.save(file_path)
        return file_path
    return None

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def is_valid_file_extension(filename):
    allowed_extensions = {'txt', 'pdf', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def delete_file(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)