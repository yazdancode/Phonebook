# contacts/forms.py
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3"}),
            "phone": forms.TextInput(attrs={"class": "form-control mb-3"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("لطفاً نام خود را وارد کنید")
        if len(name) < 3:
            raise forms.ValidationError("نام باید حداقل ۳ کاراکتر باشد")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not email.endswith("@gmail.com"):
            raise forms.ValidationError("ایمیل باید از دامنه @example.com باشد")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if not phone.isdigit():
                raise forms.ValidationError("شماره تلفن فقط باید شامل عدد باشد")
            if len(phone) < 10:
                raise forms.ValidationError("شماره تلفن باید حداقل ۱۰ رقم باشد")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if not email and not phone:
            raise forms.ValidationError(
                "وارد کردن حداقل یکی از فیلدهای ایمیل یا شماره تلفن الزامی است"
            )

        return cleaned_data
