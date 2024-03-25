from django.shortcuts import render,redirect
from django.http import JsonResponse
from openai import OpenAI

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from .forms import ChatForm
from django.shortcuts import redirect

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





def chatbot(request, pk=None):
    # Retrieve session ID from request 
    if pk is None:
        # If pk is not provided, fetch the current session ID
        session_id = request.session.session_key
    else:
        # If pk is provided, set it as the session ID
        session_id = pk
        if session_id != request.session.session_key:
            # If pk is different from the current session ID, update the session ID
            request.session.cycle_key()  # Refresh the session ID
    # Filter chats based on user and session ID
    chats = Chat.objects.filter(user=request.user, session_id=session_id)

    # Check if a different session ID is provided
    

    if request.method == 'POST':
        # User prompt stored in variable message from chatbot.html
        message = request.POST.get('message')

        # variable with the response sent by openai
        response = ask_openai(message)  

        # Create a new chat entry with user, message, response, session_id, and current timestamp
        chat = Chat(user=request.user, message=message, response=response, session_id=session_id, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    # Retrieve distinct past session IDs
    past_session_ids = Chat.objects.values_list('session_id', flat=True).distinct()

    # Pass session_id to the template for further processing if needed
    return render(request, 'chatbot.html', {'chats': chats, 'session_id': session_id, 'past_session_ids': past_session_ids})

def createChat(request):
    form = ChatForm()
    
    context = {'form':form}
    return render(request,'newChat_form.html',context)

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

def map(request):

    return render(request,'map.html')

