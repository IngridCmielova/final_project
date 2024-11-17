from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from salon_ingrid_api.models import Reservation  # Replace 'your_app' with the actual app name


class Command(BaseCommand):
    help = 'Configure permissions for the owners and clients groups'

    def handle(self, *args, **kwargs):
        # Create or get the groups
        owners_group, created = Group.objects.get_or_create(name='Owners')
        clients_group, created = Group.objects.get_or_create(name='Clients')

        # Get all permissions
        all_permissions = Permission.objects.all()

        # Assign all permissions to owners group
        owners_group.permissions.set(all_permissions)
        self.stdout.write(self.style.SUCCESS('All permissions assigned to the "owners" group.'))

        # Filter non-delete permissions
        non_delete_permissions = all_permissions.exclude(codename__icontains='delete')

        # Add the specific permission to delete reservations
        reservation_content_type = ContentType.objects.get_for_model(Reservation)
        delete_reservation_permission = Permission.objects.get(
            codename='delete_reservation',
            content_type=reservation_content_type
        )

        # Assign filtered permissions and add the specific delete permission for reservations
        clients_group.permissions.set(non_delete_permissions)
        clients_group.permissions.add(delete_reservation_permission)
        self.stdout.write(self.style.SUCCESS('Non-delete permissions and delete reservation permission '
                                             'assigned to the "clients" group.'))

        # Save the groups (if necessary, usually permissions are automatically saved)
        owners_group.save()
        clients_group.save()
