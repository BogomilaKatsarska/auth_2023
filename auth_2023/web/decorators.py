def allow_groups(groups=None):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, ** kwargs)
        return wrapper
    print(groups)
    if callable(groups):
        view_func = groups
        groups = []
        return decorator(view_func)
    return decorator
