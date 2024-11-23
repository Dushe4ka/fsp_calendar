from django.contrib import admin
from mycalendar.models import SportEvents


@admin.register(SportEvents)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "event_id", "type", "sport", "discip", "program", "gender_age",
                    "date_start", "date_end", "country", "subject", "city", "participants")
    list_filter = ("discip", "program", "sport", "discip", "country")
    search_fields = ("sport", "country",)

