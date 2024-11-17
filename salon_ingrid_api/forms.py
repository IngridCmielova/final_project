from django import forms
from salon_ingrid_api.models import Reservation, Procedure


class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Datum"
    )
    procedure = forms.ModelChoiceField(
        queryset=Procedure.objects.all(),
        empty_label="Vyberte proceduru",
        label="Procedura"
    )

    class Meta:
        model = Reservation
        fields = ['date', 'procedure']


