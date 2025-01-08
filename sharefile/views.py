from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NotesForm  # Correct import from forms.py
from .models import NotesForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request,'sharefile/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('dashboard_view')  # Redirect to dashboard or home page
            else:
                messages.error(request, 'Invalid credentials.')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'sharefile/login.html', {'form': form})
    

@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Associate the note with the logged-in user
            note.save()
            messages.success(request, "File uploaded successfully!")
            return redirect('dashboard_view')
    else:
        form = NotesForm()

    # Fetch all notes uploaded by the current user
    user_notes = NotesForm.objects.filter()

    return render(request, 'sharefile/dashboard.html', {
        'form': form,
        'notes': user_notes,
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('login_view')