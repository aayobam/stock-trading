from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout, authenticate, login
from .forms import RegisterForm, LoginForm
from .decorators import is_authenticated
from django.utils.decorators import method_decorator


@method_decorator(is_authenticated, name="dispatch")
class RegisterAccountView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        messages.success(self.request, "registration successful")
        return super().form_valid(form)
    

@is_authenticated
def user_login(request):
    form = LoginForm()
    template_name = "users/login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    if "next" in request.POST:
                        return redirect(request.POST.get("next"))
                    messages.success(request, "login success. welcome admin")
                    return redirect("admin_dashboard")
                login(request, user)
                messages.success(request, "login success.")
                return redirect("user_dashboard")
            messages.error(request, "invalid credentials")
            return redirect("user_login")
    context = {"form":form}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    messages.success(request, "logout success.")
    return redirect('user_login')