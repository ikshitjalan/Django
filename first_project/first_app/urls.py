from django.conf.urls import url
from first_app import views

# Template Tagging
app_name = "first_app"

urlpatterns = [
    url(r'^$',views.index,name = "index"),
    url(r'^relative/$',views.relative,name = 'relative'),
    url(r'^other/$',views.other,name = 'other')
]
