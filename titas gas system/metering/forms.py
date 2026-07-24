from django import forms
from .models import Station, MeteringRun, MonthlyReading

# ১. স্টেশন তৈরির ফর্ম
class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'

# ২. মিটারিং রান তৈরির ফর্ম
class MeteringRunForm(forms.ModelForm):
    class Meta:
        model = MeteringRun
        fields = '__all__'

# ৩. মাসিক গ্যাস প্রবাহ ইনপুট ও ক্যালকুলেশন ফর্ম
class MonthlyReadingForm(forms.ModelForm):
    station = forms.ModelChoiceField(
        queryset=Station.objects.all(), 
        label="স্টেশন সিলেক্ট করুন", 
        empty_label="-- স্টেশন বাছুন --"
    )

    class Meta:
        model = MonthlyReading
        fields = ['station', 'metering_run', 'month_year', 'start_vbt', 'start_vmt', 'start_mechanical', 'end_vbt', 'end_vmt', 'end_mechanical']
        widgets = {
            'month_year': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['metering_run'].queryset = MeteringRun.objects.none()

        if 'station' in self.data:
            try:
                station_id = int(self.data.get('station'))
                self.fields['metering_run'].queryset = MeteringRun.objects.filter(station_id=station_id)
            except (ValueError, TypeError):
                pass
