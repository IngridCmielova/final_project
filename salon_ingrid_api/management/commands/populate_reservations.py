from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from salon_ingrid_api.models import Reservation, Procedure
from random import choice, randint
from datetime import datetime, timedelta, time


class Command(BaseCommand):
    help = 'Create 3 random reservations for each client with random future dates and procedures'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        procedures = Procedure.objects.all()

        if not procedures.exists():
            self.stdout.write(self.style.ERROR('No procedures found. Please ensure procedures exist in the database.'))
            return

        for user in users:
            for _ in range(3):
                random_date = datetime.now().date() + timedelta(days=randint(1, 365))
                random_time = time(hour=randint(9, 17))
                random_procedure = choice(procedures)

                # Create a new reservation
                reservation = Reservation.objects.create(
                    date=random_date,
                    time=random_time,
                    procedure=random_procedure,
                    user=user
                )
                self.stdout.write(self.style.SUCCESS(f'Reservation created for user {user.username} on '
                                                     f'{reservation.date} at {reservation.time} for procedure '
                                                     f'{random_procedure.name}.'))
