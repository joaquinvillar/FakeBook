import json
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Friends, Register
from django.contrib.auth.models import User
import datetime
import operator


class Index(generic.View):
    model = User
    template_name = 'fb/index.html'
    context_object_name = 'list'

    @method_decorator(login_required)
    def get(self, request):
        data = {}
        fri = {}
        user_active = request.user.id
        data["active"] = user_active
        data["name"] = User.objects.get(id=user_active).username
        friends = Friends.objects.filter(friend_one_id=user_active) | Friends.objects.filter(friend_two_id=user_active)
        for friend in friends:
            if friend.friend_one.id == user_active:
                fri[friend.friend_two.id] = User.objects.get(id=friend.friend_two.id).username
            else:
                fri[friend.friend_one.id] = User.objects.get(id=friend.friend_one.id).username
        data["fri"] = fri
        # Register.objects.extra(select={'time': 'log_out - log_in'}, order_by=('time',))
        # Register.objects.filter(user=2).annotate(total=Sum('total'))
        registro = {}
        users = User.objects.all()
        for user in users:
            total = datetime.timedelta(days=0)
            sec = datetime.timedelta(days=0)
            reg = Register.objects.filter(user=user)
            for re in reg:
                if re.log_out:
                    sec = re.log_out - re.log_in
                    total += sec
            registro[user.username] = total.total_seconds()
        registro_sort = sorted(registro.items(), key=operator.itemgetter(1))
        registro_sort = list(reversed(registro_sort))[:10]
        data['registro_sort'] = registro_sort
        return render(request, self.template_name, data)


class All(generic.View):
    template_name = 'fb/all_users.html'
    context_object_name = 'list'

    @method_decorator(login_required)
    def get(self, request):
        data = {}
        us = {}
        users = User.objects.all()
        for user in users:
            us[user.id] = user.username
        data["users"] = us
        return render(request, self.template_name, data)


# @method_decorator(login_required)
def add_friend(request, pk):
    user_active = request.user.id
    fri = Friends.objects.filter(friend_two_id=pk, friend_one_id=user_active) \
    | Friends.objects.filter(friend_two_id=user_active, friend_one_id=pk)
    if not fri:
        user_one = User.objects.get(id=user_active)
        user_two = User.objects.get(id=pk)
        fr = Friends.objects.create(friend_one=user_one, friend_two=user_two)
        fr.save()
    return redirect('fb:all')


# @method_decorator(login_required)
def register_login(request):
    # user_active = request.user.id
    # user = User.objects.get(id=user_active)
    # now = datetime.datetime.now()
    # out = datetime.time()
    # re = Register.objects.create(user=user, log_in=now, log_out=out)
    # re.save()
    return redirect('fb:index')


# @method_decorator(login_required)
def register_logout(request):
    user_active = request.user.id
    user = User.objects.get(id=user_active)
    now = datetime.datetime.now()
    r = Register.objects.filter(user=user).last()
    r.log_out = now
    r.save()
    return redirect('fb:logout')


def is_online(request):
    sal = {}
    sessions = Session.objects.filter(expire_date__gte=timezone.now())

    users = User.objects.all()
    for user in users:
        sal[user.id] = "Off line"

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        sal[data.get('_auth_user_id', None)] = "On line"

    return HttpResponse(json.dumps(sal), content_type="application/json")
