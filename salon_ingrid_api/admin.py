from django.contrib import admin
from .models import Procedure, Reservation


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'description')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'procedure', 'user')


admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Reservation, ReservationAdmin)
