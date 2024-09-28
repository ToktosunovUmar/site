from django import forms
from . import models, rezka_parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'rezka.ag':
            rezka_pars = rezka_parser.parsing()
            for i in rezka_pars:
                models.RezkaFilm.objects.create(**i)
