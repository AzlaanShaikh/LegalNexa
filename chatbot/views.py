from django.shortcuts import render,redirect
from django.http import JsonResponse
from openai import OpenAI

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
# Create your views here.

openai_api_key = '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'

def ask_openai(message):
    
    print('chatbot openai')
    
    client = OpenAI(api_key='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')  # Replace 'YOUR_API_KEY_HERE'
    response = client.chat.completions.create(
        # select the Chat model
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a lawyer assistant. If user asks for anything that is not related to legal stuff please return response that you only answer legal related questions"},
            {"role": "user","content":message},
        ]
    )
    print(response)
    print('chatbot start')
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    print('chatbot start')
    if request.method == 'POST':
        # user prompt stored in variable message in fetch from chatbot.html
        message = request.POST.get('message')
        # Here we can return a variable with the response sent by openai
        response = ask_openai(message) # ask_openai(message)

        chat = Chat(user=request.user, message=message,response= response,created_at=timezone.now())
        chat.save()
        return JsonResponse({ 'message' : message, 'response' : response })
    return render(request, 'chatbot.html', {'chats':chats})

def login(request):
    if request.method == 'POST':
        # variable is requested from the form
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request,'login.html',{'error_message': error_message})
    else:
        return render(request,'login.html')

def register(request):
    # variable is requested from the form
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(username,email,password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
        
            except:
                error_message = 'Error Creating an account'
                return render(request,'register.html',{'error_message': error_message})

        else:
            error_message = 'Passwords dont match'
            return render(request,'register.html',{'error_message': error_message})

    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')