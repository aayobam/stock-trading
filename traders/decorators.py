from django.shortcuts import redirect


def admin_super_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func