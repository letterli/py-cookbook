from django.http import HttpResponseRedirect


def requireLogin(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        return func(request, *args, **kwargs)
    return wrapper
