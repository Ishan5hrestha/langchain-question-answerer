# PDF Text Analysis and Question Answering

This Python script performs text analysis on a PDF document and provides a question-answering functionality using OpenAI's GPT-3 model. It utilizes various libraries to extract text from the PDF, split it into manageable chunks, generate embeddings, and perform document similarity search.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- PyPDF2
- langchain
- OpenAI Python package
- dotenv (for environment variables)

You can install the required packages using `pip`:

```bash
pip install PyPDF2 langchain openai dotenv
```

## Setup

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/pdf-text-analysis.git
```
Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```
Install the required packages:

```bash
pip install -r requirements.txt
```
Create a .env file in the project directory and set your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Place the PDF file you want to analyze in the pdfs directory with the name input.pdf.

2. Run the script:

```bash
python analyze_pdf.py
```
The script will extract text from the PDF, split it into chunks, generate embeddings, and perform a question-answering operation.

## Results

The results will be displayed in the console, including the answer to the provided question based on the content of the PDF.
Customization

You can customize the script by modifying the following variables in the analyze_pdf.py file:

   - chunk_size: Adjust the size of text chunks for processing.
   - chunk_overlap: Set the overlap between text chunks.
   - query: Change the question you want to ask about the document.

## License

This project is licensed under the MIT License.