

from django.contrib import admin
from report.models import Category, Status, TrackHeader, Mockup, ArtworkDesign, PogRender, SellSheet, PublicComment

# Register your models here.

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(SellSheet)
admin.site.register(PogRender)
admin.site.register(ArtworkDesign)
admin.site.register(Mockup)
admin.site.register(PublicComment)
admin.site.register(TrackHeader)
