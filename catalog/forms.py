from django import forms
from catalog.models import Order, Product


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="Ім'я",
        widget=forms.TextInput(
            attrs={"placeholder": "Ім'я"}
        )
    )
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="Прізвище",
        widget=forms.TextInput(
            attrs={"placeholder": "Прізвище"}
        )
    )
    phone = forms.IntegerField(
        required=False,
        label="Телефон",
        widget=forms.TextInput(
            attrs={"placeholder": "0974536592"}
        )
    )
    department = forms.CharField(
        max_length=255,
        required=False,
        label="Адреса",
        widget=forms.TextInput(
            attrs={"placeholder": "Адреса відправки"}
        )
    )
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "phone", "department"]