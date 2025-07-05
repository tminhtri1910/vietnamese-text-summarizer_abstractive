import torch
from underthesea import word_tokenize
import re

class BARTphoSummarizer:
    def __init__(self):
        pass
    
    def summarize(self, content, tokenizer, model):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
    
        content = "summarize: " + word_tokenize(content, format="text") + "</s>"
        content_tokenize = tokenizer(content, max_length=1024, truncation=True, return_tensors = "pt")
        
        input_ids = content_tokenize["input_ids"].to(model.device)
        # print(f"len {i}:",len(input_ids[0]))
        attention_mask = content_tokenize["attention_mask"].to(model.device)

        with torch.no_grad():
            output_ids = model.generate(
                input_ids=input_ids, 
                attention_mask=attention_mask,
                num_beams=4,
                max_length=1024,
                # no_repeat_ngram_size=10,
                early_stopping=True,
            )
        # print(len(output_ids[0]))
        
        summary = tokenizer.decode(output_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        summary = summary.replace('_', ' ')
        summary = re.sub(r'"\s*([^"]*?)\s*"', r'"\1"', summary)
        # summary = re.sub(r'\(\s*([^)]*?)\s*\)', r'(\1)', summary)
        # summary = re.sub(r'\s+([/%;:])', r'\1', summary)


        return summary