
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Procedure
from django.contrib.auth.decorators import login_required
from datetime import time, datetime
from salon_ingrid_api.forms import ReservationForm


class PriceListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'salon_ingrid_api/price_list.html')


def date_procedure_selection_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            procedure = form.cleaned_data['procedure']
            procedure_id = procedure.pk

        return redirect('day_schedule', date=date, procedure_id=procedure_id)
    else:
        form = ReservationForm()

    return render(request, 'salon_ingrid_api/date_procedure_selection.html', {'form': form})


@login_required
def day_schedule_view(request, date, procedure_id):
    selected_date = datetime.strptime(date, '%Y-%m-%d').date()
    procedure = get_object_or_404(Procedure, pk=procedure_id)
    hours = [time(hour, 0) for hour in range(9, 17)]

    reservations = Reservation.objects.filter(date=selected_date)
    reserved_times = {reservation.time for reservation in reservations}

    schedule = [
        {
            'hour': hour,
            'status': 'Obsazeno' if hour in reserved_times else 'Volné',
            'procedure': procedure,
            'is_reserved': hour in reserved_times
        }
        for hour in hours
    ]

    if request.method == 'POST':
        selected_hours = request.POST.getlist('selected_hours')
        for hour_str in selected_hours:
            selected_hour = int(hour_str)
            selected_time = time(selected_hour, 0)

            if selected_time not in reserved_times:
                Reservation.objects.create(date=selected_date, time=selected_time, procedure=procedure,
                                           user=request.user)

        return redirect('/profile/')

    context = {
        'selected_date': selected_date,
        'schedule': schedule,
        'procedure': procedure
    }
    return render(request, 'salon_ingrid_api/day_schedule.html', context)


def my_reservations_view(request):
    if request.user.is_superuser:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'salon_ingrid_api/my_reservations.html',
                  {'reservations': reservations})


def delete_reservation_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'GET':
        return render(request, 'salon_ingrid_api/delete_reservation.html', {'reservation': reservation})
    elif request.method == 'POST':
        reservation.delete()
        return redirect('my_reservations')
