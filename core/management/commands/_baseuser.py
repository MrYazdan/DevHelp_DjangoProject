from argparse import ArgumentParser
from django.core.management import BaseCommand, CommandError
from core.models import User


class BaseUserCommand(BaseCommand):
    help = ""
    u: User = User

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('user_phone', metavar='UserPhoneNumber',
                            help="User Phonenumber")

    def handle(self, *args, **options):
        print("HAaaaaaandle")
        user_phone = options['user_phone']
        try:
            self.u = User.objects.get(phone=user_phone)
        except Exception as e:
            raise CommandError(e)

    def get_user(self):
        self.handle()
        return self.u
