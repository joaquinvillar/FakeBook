from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Friends(models.Model):
    friend_one = models.ForeignKey(User, related_name='friend_one', on_delete=models.CASCADE)
    friend_two = models.ForeignKey(User, related_name='friend_two', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.friend_one, self.friend_two)


class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_in = models.DateTimeField('Log in')
    log_out = models.DateTimeField('Log out', null=True)

    def _get_total(self):
        exi = 0
        if self.log_out > self.log_in:
            dif = self.log_out - self.log_in
            exi = dif.total_seconds()
        return exi
    total = property(_get_total)

    def __str__(self):
        return "%s - %s - %s" % (self.user, self.log_in, self.log_out)
