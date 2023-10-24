from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(requests, *args, **kwargs):
        if requests.user.is_authenticated:
            return redirect('home')
        else:

            return view_func(requests, *args, **kwargs)
    return wrapper_func