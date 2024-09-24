from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('Male', 'male'),
    ('Female', 'female')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    exp = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'exp',
            'gender',
            'phone_number'
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print("Пользователь создан")

        exp = instance.exp
        if exp < 1:
            instance.club = 'Мало опыта!!'
        elif exp >= 1 and exp <= 2:
            instance.club = 'jun'
        elif exp >= 2 and exp <= 5:
            instance.club = 'midd'
        elif exp >= 5 and exp <= 8:
            instance.club = 'Sen'
        else:
            instance.club = 'Опыт не определен!!!!'
        instance.save()
