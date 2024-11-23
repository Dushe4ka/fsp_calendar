from django.forms import ModelForm, forms, BooleanField

from mycalendar.models import SportEvents

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class EventsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = SportEvents
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['type']
        for word in forbidden_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Тип не должен содержать запрещённых слов')
            else:
                return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['sport']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('Вид спорта не должен содержать запрещённых слов')
        return cleaned_data
