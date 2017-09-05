from django import forms
from .models import Item

from tuits.models import TuitLocation


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
                  'restaurant',
                  'name',
                  'contents',
                  'excludes',
                  'public'
                  ]

    def __init__(self, *args, **kwargs):
        # user = None
        user = kwargs.pop('user', None)
        # print(kwargs.pop('user'))
        # print(user)
        # print(kwargs.pop('instance'))
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = TuitLocation.objects.filter(owner=user) #.exclude(item_isnull = False)
