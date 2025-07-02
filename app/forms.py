from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField, SubmitField
from wtforms.validators import Optional

class SummarizationForm(FlaskForm):
    text_input = TextAreaField('Input Text', validators=[Optional()], render_kw={"rows": 10, "cols": 50})
    file_upload = FileField('Upload File', validators=[Optional()])
    submit = SubmitField('Summarize')