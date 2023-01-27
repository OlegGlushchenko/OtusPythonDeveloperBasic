from django.shortcuts import render
from django.views.generic import ListView, DetailView

from deals.models import Deal


# Create your views here.
class DealsListView(ListView):
    model = Deal
    template_name = 'deals/deals_list.html'
    context_object_name = 'deals'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['identification'] = self.request.user.username
        else:
            context['identification'] = "Гость"
        return context


class DealsDetailView(DetailView):
    model = Deal
    template_name = 'deals/deal_detail.html'
    context_object_name = 'deal'
