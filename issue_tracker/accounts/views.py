from accounts.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url != 'None':
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['user_name'] = username
    else:
        context = {'next': request.GET.get('next')}
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', context={'form': form})

