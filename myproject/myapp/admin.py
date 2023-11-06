from django.contrib import admin
from .models import test_Category, Pathology_Test,Pathology_Test_Master
# Register your models here.

admin.site.register(test_Category)
admin.site.register(Pathology_Test)
admin.site.register(Pathology_Test_Master)
