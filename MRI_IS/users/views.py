from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(
                request, 'Вы зарегистрированы! Теперь вы можете войти')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return HttpResponseNotFound()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')