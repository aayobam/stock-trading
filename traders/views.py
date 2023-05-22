from email.mime import image
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from traders.forms import RegisterForm, LoginForm
from traders.models import Trade
from django.views import generic
from django.contrib.auth import mixins
from django.contrib.auth import logout, authenticate, login
from django_plotly_dash import DjangoDash
import plotly.graph_objs as go


class RegisterAccountView(generic.CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')
    

def user_login(request):
    form = LoginForm()
    template_name = "login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
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
    redirect_field_name = reverse_lazy("user_login")

    def get_context_data(self, **kwargs):
        timestamp = [] # timestamp list
        profit_loss = [] # profit/loss list
        context = super().get_context_data(**kwargs)
        trade = Trade.objects.filter(trader=self.request.user).first()

        for trades in trade.graph_data:
            timestamp.append(trades["timestamp"])
            profit_loss.append(trades["profit_loss"])
        graph = {"timesstamp":timestamp, "profit_loss":profit_loss}

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(title='Real-Time Profit/Loss', xaxis=dict(title='Timestamp'), yaxis=dict(title='Profit/Loss'))
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=700, default_width=1000)
        context["graph"] = graph
        return context


class AdminDashboardTradeListView(mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'admin_dashboard.html'
    queryset = Trade.objects.all()

    def test_func(self):
        return self.request.user.is_superuser
    

class AdminDashboardTradeDetailView(mixins.UserPassesTestMixin, generic.DetailView):
    template_name = 'admin_dashboard.html'
    queryset = Trade.objects.all()

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trade = get_object_or_404(Trade, id=self.id)
        context['balance'] = trade.balance
        context['graph_data'] = trade.graph_data
        return context