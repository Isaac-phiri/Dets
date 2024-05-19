from django.shortcuts import render, redirect
from .forms import UserCreattionForm


def create_user(request):
    if request.method == 'POST':
        form = UserCreattionForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreattionForm()
    return render(request, 'registration/register.html', {'form': form})  
