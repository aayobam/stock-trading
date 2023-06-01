from users.models import CustomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if CustomUser.objects.filter(email="adminuser@mail.com").exists():
            self.stdout.write(self.style.WARNING(f"adminuser@mail.com already exists."))
            exit()
        admin_user = CustomUser.objects.create_superuser(
            email="adminuser@mail.com",
            first_name='admin',
            last_name="user",
            password="adminpassword"
        )
        admin_user.set_password("adminpassword")
        admin_user.save()
        self.stdout.write(self.style.SUCCESS(f"Admin {admin_user.email} created"))