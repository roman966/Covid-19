from django import forms


class CountryForm (forms.Form):
    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)


class BasicForm(forms.Form):
    OPTIONS = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    Age = forms.IntegerField()
    Sex = forms.CharField(widget=forms.Select(choices=OPTIONS))
    Temparature = forms.DecimalField()


class InformationForm(forms.Form):
    OPTIONS = (
        ("1", "Breathing problem"),
        ("2", "Dry cough"),
        ("3", "Sore throat"),
        ("4", "Weakness"),
        ("5", "Runny nose"),
    )

    Information = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


class AdditionalInfoForm(forms.Form):
    OPTIONS = (
        ("1", "Abdominal pain"),
        ("2", "Vomiting"),
        ("3", "Diarrhoea"),
        ("4", "Chest pain or pressure"),
        ("5", "Muscle pain"),
        ("6", "Loss of taste or smell"),
        ("7", "Rash on skin, or discoloration of fingers or toes"),
        ("8", "Loss of speech or movement"),
    )

    AddiInfo = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
