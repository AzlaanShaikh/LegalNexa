# views.py

from django.shortcuts import render, redirect
from .forms import PDFUploadForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_pdf=request.FILES['file']
            
            result=process_file(uploaded_pdf)
            print(result)  # Redirect to success page
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})




def process_file(uploaded_file):
    a ="wowoo"
    return a
