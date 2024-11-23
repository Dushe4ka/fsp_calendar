from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mycalendar.forms import EventsForm
from mycalendar.models import SportEvents


# class EventsCreateView(LoginRequiredMixin, CreateView):
#     model = SportEvents
#     form_class = EventsForm
#     success_url = reverse_lazy('mycalendar:list')
#
#     def form_valid(self, form):
#         context_data = self.get_context_data()
#         formset = context_data['formset']
#         form.instance.owner = self.request.user
#
#         if form.is_valid() and formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return super().form_valid(form)
#         else:
#             return self.render_to_response(self.get_context_data(form=form, formset=formset))
#
#
# class EventsUpdateView(LoginRequiredMixin, UpdateView):
#     model = SportEvents
#     form_class = EventsForm
#     success_url = reverse_lazy('mycalendar:list')
#
#     def form_valid(self, form):
#         context_data = self.get_context_data()
#         formset = context_data['formset']
#         if form.is_valid() and formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return super().form_valid(form)
#         else:
#             return self.render_to_response(self.get_context_data(form=form, formset=formset))


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


# class EventsDeleteView(LoginRequiredMixin, DeleteView):
#     model = SportEvents
#     success_url = reverse_lazy('mycalendar:list')
