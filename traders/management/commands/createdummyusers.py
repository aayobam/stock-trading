from typing import Any, Optional
from django.core.management import BaseCommand, CommandError
from django.contrib.auth.models import User
import time



class Command(BaseCommand):
    help = "auto creates dummy users for trading simulation"

    def handle(self, *args, **options) :
        first_name = "test"
        last_name="user"
        username = first_name + last_name
        password = "password"
        for count in range(1, 11):
            if User.objects.filter(username=username+str(count)).exists():
                self.stdout.write(self.style.WARNING(f"account for {username+str(count)} already exists."))
                continue
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name+str(count),
                username=username+str(count),
                email=username+str(count)+"@mail.com",
                password=password+str(count)
            )
            user.is_active = True
            user.set_password(password+str(count))
            user.save()
            self.stdout.write(self.style.SUCCESS(f"account for {user.email} has been created."))
            time.sleep(1)
        self.stdout.write(self.style.SUCCESS(f"All dummy accounts have been created."))