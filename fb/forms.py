from django.forms import ModelForm
from .models import Friends


class FriendsForm(ModelForm):
    class Meta:
        model = Friends
        fields = ['friend_one', 'friend_two']
