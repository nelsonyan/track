

from django.db import models
from django.urls import reverse
from employee.models import EmployeeList
from django.contrib.admin.widgets import AdminDateWidget


class Category(models.Model):
    category = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.category

class Status(models.Model):
    status = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.status

class SellSheet(models.Model):
    sell_sheet = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.sell_sheet

class PogRender(models.Model):
    pog_render = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.pog_render

class ArtworkDesign(models.Model):
    artwork_design = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.artwork_design

class Mockup(models.Model):
    mockup = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.mockup

class PublicComment(models.Model):
    public_comments = models.CharField(max_length = 50000, blank = True)
    def __int__(self):
        return self.pk

class TrackHeader(models.Model):
    report_key = models.AutoField(primary_key=True)

    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True)
    task_name = models.CharField(max_length = 80, blank = True)
    dead_line = models.CharField(null = True, blank = True, max_length = 50)
    requested_by = models.ForeignKey(EmployeeList, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'requested_by')
    date_requested = models.CharField(null = True, blank = True, max_length = 50)
    assigned_to = models.ForeignKey(EmployeeList, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'assigned_to')
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null = True, blank = True)
    sku_count = models.CharField(max_length = 100, blank = True)
    sell_sheet = models.ForeignKey(SellSheet, on_delete = models.SET_NULL, null = True, blank = True)
    pog_render = models.ForeignKey(PogRender, on_delete = models.SET_NULL, null = True, blank = True)
    artwork_design = models.ForeignKey(ArtworkDesign, on_delete = models.SET_NULL, null = True, blank = True)
    mockup = models.ForeignKey(Mockup, on_delete = models.SET_NULL, null = True, blank = True)
    google_url = models.CharField(max_length = 500, blank = True)
    google_url_name = models.CharField(max_length = 500, blank = True)
    marklyn_url = models.CharField(max_length = 500, blank = True)
    marklyn_url_name = models.CharField(max_length = 500, blank = True)
    comments = models.TextField(max_length = 5000, blank = True)


    def get_absolute_url(self):
        return reverse('report:track_report')


    def __str__(self):
        return str(self.report_key)
    
