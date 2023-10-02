from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from dotenv import load_dotenv

import os

load_dotenv()

# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

reader = PdfReader("./pdfs/input.pdf")

raw_text = ""
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

# print(raw_text)

# Split the huge text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)
# print(texts[1])

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)
# print(docsearch)

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "When was stephen hawkins born?"
docs = docsearch.similarity_search(query)
output = chain.run(input_documents=docs, question=query)
print(output)
