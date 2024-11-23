from django.urls import path
from django.views.decorators.cache import cache_page

from mycalendar.apps import MycalendarConfig
from mycalendar.views import EventsListView, EventsDetailView, AboutTemplateView

app_name = MycalendarConfig.name

urlpatterns = [
    path('', EventsListView.as_view(), name='list'),
    path('events/<int:pk>/', cache_page(60)(EventsDetailView.as_view()), name='view'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]
