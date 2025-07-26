# Vietnamese Text Summarizer

This project is a web application built with Flask that provides advanced summarization capabilities for Vietnamese text. It allows users to input text directly or upload files, and it utilizes state-of-the-art pre-trained models—ViT5 and BARTpho—to generate high-quality summaries. The application also evaluates the summaries using ROUGE metrics.

<img width="1508" height="684" alt="image" src="https://github.com/user-attachments/assets/381e9c7b-abbf-4eed-b006-876efafdc3df" />


## Features

- Text area for direct input of Vietnamese text.
- File upload capability for summarizing text from documents.
- Summarization using ViT5 and BARTpho transformer-based models.
- ROUGE measure comparison to evaluate the quality of summaries.
- Loading indicator to enhance user experience during processing.
- Modular design allowing for the addition of new summarization methods and improvements in Vietnamese language processing.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vietnamese-text-summarizer.git
   cd vietnamese-text-summarizer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the text area to input Vietnamese text or upload a file containing text.

4. Click the "Summarize" button to generate summaries using the selected model (ViT5 or BARTpho).

5. View the results, including the generated summaries and ROUGE score comparisons.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
