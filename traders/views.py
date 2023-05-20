from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from traders.forms import RegisterForm, LoginForm
from traders.models import Trade
from django.views import generic
from django.contrib.auth import mixins
from django.contrib.auth import logout, authenticate, login
from plotly.offline import plot



class RegisterAccountView(generic.CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    model = User
    success_url = reverse_lazy('user_dashboard')


def user_login(request):
    form = LoginForm()
    template_name = "login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            print(f"USER TYPE: {user.is_superuser}")
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.success(request, "login success. welcome admin")
                    return redirect("admin_dashboard")
                login(request, user)
                messages.success(request, "login success.")
                return redirect("user_dashboard")
            messages.error(request, "invlaid credentials")
            return redirect("user_login")
    context = {"form":form}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    messages.success(request, "logut success.")
    return redirect('user_login')


class UserDashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'user_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trade = Trade.objects.get(trader_id=self.request.user.id)
        context['balance'] = trade.balance
        context['trader_name'] = trade.trader.username
        context['timestamp'] = trade.timestamp
        return context


class AdminDashboardView(mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trades = Trade.objects.all()
        profit_loss_data = []

        for trade in trades:
            trade_data = {
                'trader_name': trade.trader.username,
                'timestamp':trade.timestamp,
                'balance': trade.balance
            }
            profit_loss_data.append(trade_data)

        context['profit_loss_data'] = profit_loss_data
        return context
