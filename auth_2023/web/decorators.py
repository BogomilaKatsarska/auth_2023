from django.http import HttpResponse


def allow_groups(groups=None):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponse('Not authenticated')

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            if not user_groups:
                return HttpResponse('Not in any of the groups')
            return view_func(request, *args, ** kwargs)
        return wrapper
    print(groups)
    if callable(groups):
        view_func = groups
        groups = []
        return decorator(view_func)
    return decorator
