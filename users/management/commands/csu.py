from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="user@example.com")
        user.is_staff = True
        user.active = True
        user.is_superuser = True
        user.set_password("qwe123")
        user.save()
