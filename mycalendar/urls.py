from django.urls import path
from django.views.decorators.cache import cache_page

from mycalendar.apps import MycalendarConfig
from mycalendar.views import EventsListView, EventsDetailView

app_name = MycalendarConfig.name

urlpatterns = [
    path('', EventsListView.as_view(), name='list'),
    # path('create/', EventsCreateView.as_view(), name='create'),
    # path('delete/<int:pk>/', EventsDeleteView.as_view(), name='delete'),
    # path('edit/<int:pk>/', EventsUpdateView.as_view(), name='edit'),
    path('events/<int:pk>/', cache_page(60)(EventsDetailView.as_view()), name='view'),
]
