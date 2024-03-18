import os
import pytesseract
from pdf2image import convert_from_path
from django.shortcuts import render
from .forms import PDFUploadForm
from .models import UploadedPDF # Import your model
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken

import os 
open_api_key="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"
os.environ["OPENAI_API_KEY"]=open_api_key


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the model
            form.save()
            # Get the latest instance of the model (assuming it's the one just saved)
            print("====================================================")
            print("PDf Uploaded succesfully")
            latest_instance = UploadedPDF.objects.latest('id')
            result = process_file(latest_instance)
            # Handle the result, e.g., store it in a database
            print(result)
            return render(request, 'upload_pdf.html', {'form': form,'result':result},)
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def process_file(model_instance):
    try:
        print("=====================================================================")
        print("starting ti extract text from the pdf")
        # Path to Tesseract executable
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Path to Poppler bin directory
        poppler_path = r'C:\Program Files\poppler-24.02.0\Library\bin'

        # Access the PDF file field from the model instance
        pdf_path = model_instance.file.path

        # Convert the PDF to images with specified Poppler path
        pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)

        extracted_text = ""

        for page in pages:
            text = pytesseract.image_to_string(page, lang='eng')
            extracted_text += text + "\n"
            print('PDF uploaded')
        return summarizer(extracted_text)
    except Exception as e:
        # Handle exceptions (e.g., log the error)
        print(f"Error processing PDF: {e}")
        return None

def summarizer(text):
    print("Starting summary")
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=20)
    chunks = text_splitter.create_documents([text])
    print(chunks)
    chain = load_summarize_chain(
    llm,
    chain_type='map_reduce',
    verbose=False
    )
    summary = chain.run(chunks)

    return summary