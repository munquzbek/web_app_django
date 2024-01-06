from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Command to create superuser, to run:python3 manage.py csu
    to delete exist users: python3 manage.py shell, from users.models import User,
    User.objects.all().delete()
    """
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='Skypro',
            is_staff=True,
            is_superuser=True
        )
        # setting password with encryption
        user.set_password('admin')
        user.save()
