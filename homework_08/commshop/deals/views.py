from django.shortcuts import render
from django.views.generic import ListView, DetailView

from deals.models import Deal


# Create your views here.
class DealsListView(ListView):
    model = Deal
    template_name = 'deals/deals_list.html'
    context_object_name = 'deals'


class DealsDetailView(DetailView):
    model = Deal
    template_name = 'deals/deal_detail.html'
    context_object_name = 'deal'
