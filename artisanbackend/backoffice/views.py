"""View methods for backoffice"""

from django import http
from django.conf import settings
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

User = get_user_model()


def login_view(request):
    """Login page for backoffice dashboard"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(request.GET.get('next', '/artisan'))
        return render(request, 'backoffice/login.html', {})

    email = request.POST.get('email')
    password = request.POST.get('password')
    if email is None or password is None:
        return http.HttpResponseBadRequest('email and password are required')

    error_data = {
        'error_message': 'Email or password is incorrect',
    }

    try:
        user = User.objects.get(email__exact=email)
    except User.DoesNotExist:
        return render(request, 'backoffice/login.html', error_data)

    password_is_correct = user.check_password(password)
    if not password_is_correct:
        return render(request, 'backoffice/login.html', error_data)

    login(request, user)
    return redirect(request.GET.get('next', '/artisan'))


def logout_view(request):
    """Log the user out and redirect to the login page"""
    logout(request)
    return redirect(settings.LOGIN_URL)


@login_required
def index(request):
    """Simple index view"""
    return render(request, 'backoffice/product-list.html')
