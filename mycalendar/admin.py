from django.contrib import admin
from mycalendar.models import SportEvents #Notifications


@admin.register(SportEvents)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "event_id", "type", "sport", "discip", "program", "gender_age",
                    "date_start", "date_end", "country", "subject", "city", "participants")
    list_filter = ("discip", "program", "sport", "discip", "country")
    search_fields = ("sport", "country",)


# @admin.register(Notifications)
# class NotificationsAdmin(admin.ModelAdmin):
#     list_display = ("id", "header", "message", "event", "date_at", "created_at", "owner")
#     list_filter = ("event", "header")
#     search_fields = ("event", "header", "message", "date_at", "created_at")
#
