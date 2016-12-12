from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
import datetime

from fb.models import Register


class MyBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        pwd_valid = check_password(password, user.password)
        if not pwd_valid:
            user = None
        else:
            now = datetime.datetime.now()
            out = datetime.time()
            r = Register.objects.create(user=user, log_in=now)
            r.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
