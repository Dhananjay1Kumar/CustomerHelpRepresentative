from django.shortcuts import redirect
from django.http import HttpResponse


def unauthorized_user(view_func):
    def wraper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wraper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wraper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group =request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not  authorized to view this page")
        return wraper_func
    return decorator


def admin_only(view_func):
    def wraper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group =request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user-page')
        elif group == 'admin':
             return view_func(request, *args, **kwargs)
        else:
            HttpResponse("User is not athenticated ")
    return wraper_function
