from django_plotly_dash import DjangoDash
import plotly.graph_objs as go
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth import mixins
from traders.models import Trade
from django.contrib.auth.decorators import login_required



class UserDashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'trades/user_dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = [] # timestamp list
        profit_loss = [] # profit/loss list
        trade = Trade.objects.filter(trader=self.request.user).first()

        for trades in trade.graph_data:
            timestamp.append(trades["timestamp"])
            profit_loss.append(trades["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title='Real-Time Profit/Loss',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=700, default_width=1000)
        context["graph"] = graph
        return context


class UserDashboardGraphView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'partial/user_graph.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = [] # timestamp list
        profit_loss = [] # profit/loss list
        trade = Trade.objects.filter(trader=self.request.user).first()

        for trades in trade.graph_data:
            timestamp.append(trades["timestamp"])
            profit_loss.append(trades["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title='Real-Time Profit/Loss',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=700, default_width=1000)
        context["graph"] = graph
        return context


class AdminDashboardTradeListView(mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'trades/admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trades = Trade.objects.all()
        context["trades"] = trades
        return context


class AdminDashboardGraphView(mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'partial/admin_graph.html'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        timestamp = [] # timestamp list
        profit_loss = [] # profit/loss list

        trade_id = self.request.GET.get("trade-id", "")
        #trade_obj = Trade.objects.get(id=trade_id)

        trade_obj = Trade.objects.filter(id=trade_id).first()
 
        for graph_data in trade_obj.graph_data:
            timestamp.append(graph_data["timestamp"])
            profit_loss.append(graph_data["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title=f'Real-Time Profit/Loss for {trade_obj.trader} ${trade_obj.balance}', 
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss', range=[-10, 10])
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=700, default_width=1000)

        context["graph"] = graph
        return context
