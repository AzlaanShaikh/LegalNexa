from django.shortcuts import render,redirect
from .forms import PDFUploadForm
from .models import UploadedPDF # Import your model
def Pdfquery(request):
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
            return render(request, 'pdfquery.html', {'form': form,'result':result},)
    else:
        form = PDFUploadForm()
    return render(request,'pdfquery.html', {'form': form})

def process_file(request):
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
            print('Page uploaded')
        return get_text_chunks(extracted_text)
    except Exception as e:
        # Handle exceptions (e.g., log the error)
        print(f"Error processing PDF: {e}")
        return None
    
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    get_vector_store(chunks)
    
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    