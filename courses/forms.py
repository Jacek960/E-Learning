from django import forms

from courses.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product']
        labels = {
            'product': 'Wybierz rodzaj skubskrybcji'
        }
