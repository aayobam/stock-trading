import plotly.graph_objs as go
from django.views import generic
from django.contrib.auth import mixins
from traders.models import Trade
from django.urls import reverse_lazy



# User dashboard landing page
class UserDashboardView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'trades/user_dashboard.html'
    success_url = reverse_lazy('user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = [] # timestamp list: appends all the timestaps in the object's graph_data field.
        profit_loss = [] # profit/loss list: appends all the profit/loss in the object's graph_data field.
        trade = Trade.objects.filter(trader=self.request.user).first()

        for trades in trade.graph_data:
            timestamp.append(trades["timestamp"])
            profit_loss.append(trades["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title=f'Real-Time Profit/Loss.Your available balance is ${trade.balance}', 
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return itto the template
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
        context["graph"] = graph
        return context


# User real time trade graph view.
class UserDashboardGraphView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'partial/user_graph.html'
    success_url = reverse_lazy('user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = [] # timestamp list: appends all the timestaps in the object's graph_data field.
        profit_loss = [] # profit/loss list: appends all the profit/loss in the object's graph_data field.
        trade = Trade.objects.filter(trader=self.request.user).first()

        for trades in trade.graph_data:
            timestamp.append(trades["timestamp"])
            profit_loss.append(trades["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title=f'Real-Time Profit/Loss.Your available balance is ${trade.balance}',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
        context["graph"] = graph
        return context


# Admin dashboard landing page
class AdminDashboardTradeListView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'trades/admin_dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = [] # timestamp list: appends all the timestaps in the object's graph_data field.
        profit_loss = [] # profit/loss list: appends all the profit/loss in the object's graph_data field.

        trade_id = self.request.GET.get("trade-id", "")
        try:
            trade_obj = Trade.objects.filter(id__icontains=trade_id).first()
        except:
            trade_obj = None
 
        for graph_data in trade_obj.graph_data:
            timestamp.append(graph_data["timestamp"])
            profit_loss.append(graph_data["profit_loss"])

        # Create a scatter plot with the timestamp and profit/loss data
        data = go.Scatter(x=timestamp, y=profit_loss, mode='lines+markers', name='Profit/Loss')
        layout = go.Layout(
            title=f'Real-Time Profit/Loss for {trade_obj.trader} ${trade_obj.balance}', 
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=600, default_width=1000)

        trades = Trade.objects.all()
        context["trades"] = trades
        context["graph"] = graph
        return context


#Admin dashboard real time graph page
class AdminDashboardGraphView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.TemplateView):
    template_name = 'partial/admin_graph.html'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        timestamp = [] # timestamp list: appends all the timestaps in the object's graph_data field.
        profit_loss = [] # profit/loss list: appends all the profit/loss in the object's graph_data field.

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
            yaxis=dict(title='Profit/Loss')
        )
        
        # Create the figure and return it
        fig = go.Figure(data=data, layout=layout)
        graph = fig.to_html(full_html=False, default_height=600, default_width=1000)

        context["graph"] = graph
        return context
