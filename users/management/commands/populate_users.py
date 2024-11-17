from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        owners_group, _ = Group.objects.get_or_create(name='Owners')
        clients_group, _ = Group.objects.get_or_create(name='Clients')

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='admin',
                first_name='Admin',
                last_name='Admin',
                email='admin@admin.cz',
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created with password "admin".'))

        if not User.objects.filter(username='ingrid.cmielova').exists():
            ingrid = User.objects.create_user(
                username='ingrid.cmielova',
                password='ingrid',
                first_name='Ingrid',
                last_name='Cmielova',
                email='ingrid@cimelova.cz'
            )

            ingrid.is_staff = True
            ingrid.groups.add(owners_group)
            ingrid.save()
            self.stdout.write(self.style.SUCCESS('Staff user  "ingrid.cmielova" created with password "ingrid".'))

        for i in range(20):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f'{first_name.lower()}.{last_name.lower()}'
            email = f'{first_name.lower()}@{last_name.lower()}.cz'

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password='client',
                email=email,
                )
            user.groups.add(clients_group)
        self.stdout.write(self.style.SUCCESS('20 Clients created with group assignments.'))

