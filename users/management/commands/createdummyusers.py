from django.core.management import BaseCommand
from users.models import CustomUser
import time



# Automatic creation of dummy users for trade simulation.
class Command(BaseCommand):
    help = "auto creates dummy users for trading simulation"

    def handle(self, *args, **options) :
        first_name = "test"
        last_name="user"
        email = first_name + last_name
        password = "password"
        for count in range(1, 11):
            # admin_user.save()
            if CustomUser.objects.filter(email=email+str(count)+"@mail.com").exists():
                self.stdout.write(self.style.WARNING(f"account for {email+str(count)+'@mail.com'} already exists."))
                continue
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name+str(count),
                email=email+str(count)+"@mail.com",
                password=password+str(count)
            )
            user.is_active = True
            user.set_password(password+str(count))
            user.save()
            self.stdout.write(self.style.SUCCESS(f"account for {user.email} has been created."))
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
        self.stdout.write(self.style.SUCCESS(f"All dummy accounts have been created."))
        self.stdout.write(self.style.SUCCESS(f"Admin {admin_user.email} created"))