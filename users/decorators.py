from django.shortcuts import redirect


# Refuses a user from accessing a page once already logged in.
def is_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper_func