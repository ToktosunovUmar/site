from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female')
    )
    phone_number = models.CharField(max_length=17, default='+996')
    exp = models.PositiveIntegerField(default=10,
                                      validators=[
                                          MaxValueValidator(8),
                                          MinValueValidator(1),
                                      ])
    gender = models.CharField(max_length=10, choices=GENDER)
    club = models.CharField(max_length=100, default="Опыт не определен")


@receiver(post_save, sender=CustomUser)
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
            instance.club = 'Опыт не определен'
        instance.save()
