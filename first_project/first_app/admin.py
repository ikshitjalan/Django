from django.contrib import admin
from first_app.models import AccessRecord,Webpage,Topic,User,UserProfileInfo

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User)
admin.site.register(UserProfileInfo)
