from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="স্টেশনের নাম") # উদা: তারাবো টিবিএস

    def __str__(self):
        return self.name

class MeteringRun(models.Model):
    METER_TYPES = [
        ('Turbine', 'টারবাইন মিটার'),
        ('Orifice', 'অরিফিস মিটার'),
    ]
    
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='metering_runs')
    name = models.CharField(max_length=100, verbose_name="মিটারিং রানের নাম") # উদা: লোকালগামী ১২ ইঞ্চি
    meter_type = models.CharField(max_length=10, choices=METER_TYPES, default='Turbine')
    size_inch = models.IntegerField(verbose_name="সাইজ (ইঞ্চি)") # উদা: ১২ বা ৮
    g_series = models.CharField(max_length=20, blank=True, null=True, verbose_name="জি সিরিজ") # উদা: জি-৪০০০
    is_evc = models.BooleanField(default=False, verbose_name="ইভিসি আছে কি না?")
    is_evc_active = models.BooleanField(default=False, verbose_name="ইভিসি কার্যকর কি না?")

    def __str__(self):
        return f"{self.station.name} - {self.name}"

class MonthlyReading(models.Model):
    metering_run = models.ForeignKey(MeteringRun, on_delete=models.CASCADE)
    month_year = models.DateField(verbose_name="মাস এবং বছর") # মাসের হিসাব রাখার জন্য
    
    # মাসের শুরুর রিডিং
    start_vbt = models.FloatField(default=0.0, verbose_name="শুরুর Vbt")
    start_vmt = models.FloatField(default=0.0, verbose_name="শুরুর Vmt")
    start_mechanical = models.FloatField(default=0.0, verbose_name="শুরুর মেকানিক্যাল ইনডেক্স")
    
    # মাস শেষের রিডিং
    end_vbt = models.FloatField(default=0.0, verbose_name="শেষের Vbt")
    end_vmt = models.FloatField(default=0.0, verbose_name="শেষের Vmt")
    end_mechanical = models.FloatField(default=0.0, verbose_name="শেষের মেকানিক্যাল ইনডেক্স")
    
    # অটো ক্যালকুলেট হওয়া টোটাল গ্যাস প্রবাহ
    total_flow = models.FloatField(blank=True, null=True, verbose_name="মোট গ্যাস প্রবাহ")

    def save(self, *args, **kwargs):
        # ২য় ধাপের ক্যালকুলেশন লজিক এখানে কাজ করবে
        diff_vbt = self.end_vbt - self.start_vbt
        diff_vmt = self.end_vmt - self.start_vmt
        diff_mech = self.end_mechanical - self.start_mechanical
        
        # ১. যদি টারবাইন মিটার হয় এবং ইভিসি কার্যকর থাকে
        if self.metering_run.meter_type == 'Turbine' and self.metering_run.is_evc_active:
            # মেকানিক্যাল পার্থক্য এবং vmt পার্থক্যের পরম মান (Absolute difference)
            if abs(diff_mech - diff_vmt) < 500:
                self.total_flow = diff_vbt
            else:
                # যদি ৫০০ বা তার বেশি হয় তবে ফ্যাক্টর গুণ হবে
                if diff_vmt != 0: # Zero Division Error এড়াতে
                    factor = diff_vbt / diff_vmt
                    self.total_flow = diff_mech * factor
                else:
                    self.total_flow = 0.0
        else:
            # ইভিসি অকার্যকর বা অন্য মিটারের জন্য সাধারণ মেকানিক্যাল পার্থক্য (আপনার প্রয়োজন অনুযায়ী পরিবর্তন করতে পারেন)
            self.total_flow = diff_mech
            
        super(MonthlyReading, self).save(*args, **kwargs)
