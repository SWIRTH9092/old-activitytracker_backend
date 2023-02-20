from django.db import models

# Create your models here.


class Activity(models.Model):
    act_id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activity'


class ActivityTracker(models.Model):
    act_trk_id = models.AutoField(primary_key=True)
    # act_main = models.ForeignKey(Activity, on_delete=models.CASCADE, null=False)
    act_main_id = models.IntegerField(Activity, blank=False, null=False)
    activity_date = models.DateField(blank=True, null=True)
    activity_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activity_tracker'
