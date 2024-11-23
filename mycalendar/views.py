from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mycalendar.forms import EventsForm #NotificationsForm
from mycalendar.models import SportEvents #Notifications


# class NotificationsCreateView(CreateView):
#     model = Notifications
#     form_class = NotificationsForm
#     success_url = reverse_lazy('mycalendar:notifications_list')
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
# class NotificationsListView(ListView):
#     model = Notifications
#     template_name = 'mycalendar/notifications_list.html'
#
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         if query:
#             object_list = Notifications.objects.filter(
#                 Q(header__icontains=query))
#             return object_list
#         else:
#             return Notifications.objects.all()
#
#
# class NotificationsDetailView(DetailView):
#     model = Notifications
#     template_name = 'mycalendar/notifications_detail.html'


class EventsListView(ListView):
    model = SportEvents
    template_name = 'mycalendar/sportevents_list.html'
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


class AboutTemplateView(TemplateView):
    template_name = 'mycalendar/About.html'
