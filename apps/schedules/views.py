from django.shortcuts import render
from django.views import generic

from apps.schedules.models import Time


class TimeListView(generic.ListView):
    model = Time
    template_name = 'time-table.html'
