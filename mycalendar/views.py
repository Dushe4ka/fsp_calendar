from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mycalendar.forms import EventsForm
from mycalendar.models import SportEvents


class EventsListView(ListView):
    model = SportEvents
    template_name = 'mycalendar/sportsevent_list.html'
    paginate_by = 20

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        if query:
            object_list = SportEvents.objects.filter(
                Q(type__icontains=query))
            return object_list
        else:
            return SportEvents.objects.all()


class EventsDetailView(DetailView):
    model = SportEvents
