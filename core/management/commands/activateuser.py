from ._baseuser import BaseUserCommand


class Command(BaseUserCommand):
    help = "Activate user by phonenumber"

    u = super(BaseUserCommand).get_user()
    u.is_active = False
    u.save()
    print("This user : " + super().style.HTTP_NOT_MODIFIED(u.phone) + " activated!")