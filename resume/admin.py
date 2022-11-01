from django.contrib import admin
from . models import Language, Education, Expertise, Skills, Profile
# Register your models here.
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Expertise)
admin.site.register(Skills)
admin.site.register(Profile)