from django import forms
from .models import Review, Order


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['vote', 'text']
        labels = {
            'vote': 'Проголосуйте',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'Ваш комментарий'})


class OrderForm(forms.ModelForm):

    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'start_time', 'order_date', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].label = 'Время начала занятий'
        self.fields['start_time'].help_text = 'Занятия будут проходить 2 часа каждый день, на протяжении одного месяца'