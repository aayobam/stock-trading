from django.core.management import BaseCommand
from users.models import CustomUser
import time



class Command(BaseCommand):
    help = "auto creates dummy users for trading simulation"

    def handle(self, *args, **options) :
        first_name = "test"
        last_name="user"
        email = first_name + last_name
        password = "password"
        for count in range(1, 11):
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
            time.sleep(1)
        self.stdout.write(self.style.SUCCESS(f"All dummy accounts have been created."))