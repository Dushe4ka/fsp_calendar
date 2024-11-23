from django.urls import path
from django.views.decorators.cache import cache_page

from mycalendar.apps import MycalendarConfig
from mycalendar.views import EventsListView, EventsDetailView, AboutTemplateView # NotificationsDetailView, \
    #NotificationsListView, NotificationsCreateView

app_name = MycalendarConfig.name

urlpatterns = [
    path('', EventsListView.as_view(), name='list'),
    path('events/<int:pk>/', cache_page(60)(EventsDetailView.as_view()), name='view'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    # path('notification/<int:pk>/', cache_page(60)(NotificationsDetailView.as_view()), name='notifications_view'),
    # path('notifications/', NotificationsListView.as_view(), name='notifications_list'),
    # path('notifications/create/', NotificationsCreateView.as_view(), name='notifications_create'),
]
