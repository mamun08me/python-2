
# Create your views here.
from django.shortcuts import render, redirect
from .models import Station, MeteringRun, MonthlyReading
from .forms import StationForm, MeteringRunForm, MonthlyReadingForm

# ড্যাশবোর্ড বা হোম পেজ যেখানে সব তথ্য দেখা যাবে
def dashboard(as_request):
    stations = Station.objects.all()
    readings = MonthlyReading.objects.all().order_by('-month_year')
    return render(as_request, 'dashboard.html', {'stations': stations, 'readings': readings})

# নতুন স্টেশন যুক্ত করার ভিউ
def add_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StationForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'নতুন স্টেশন যুক্ত করুন'})

# নতুন মিটারিং রান যুক্ত করার ভিউ
def add_metering_run(request):
    if request.method == 'POST':
        form = MeteringRunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MeteringRunForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'নতুন মিটারিং রান যুক্ত করুন'})

# মাসিক রিডিং ও ক্যালকুলেশন ইনপুট নেওয়ার ভিউ
def add_monthly_reading(request):
    if request.method == 'POST':
        form = MonthlyReadingForm(request.POST)
        if form.is_valid():
            form.save() # এখানে সেভ হওয়ার সাথে সাথে মডেলের save() মেথডের ক্যালকুলেশন রান করবে
            return redirect('dashboard')
    else:
        form = MonthlyReadingForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'মাসিক গ্যাস প্রবাহ ইনপুট'})



from django.http import JsonResponse

# স্টেশন ভিত্তিক মিটারিং রান লোড করার জন্য Ajax ভিউ
def load_metering_runs(request):
    station_id = request.GET.get('station_id')
    metering_runs = MeteringRun.objects.filter(station_id=station_id).values('id', 'name')
    return JsonResponse(list(metering_runs), safe=False)
