from ._baseuser import BaseUserCommand


class Command(BaseUserCommand):
    help = "Deactivate user by phonenumber"

    u = super().get_user()
    u.is_active = False
    u.save()
    print("This user : " + super().style.WARNING(u.phone) + " deactivated!")
