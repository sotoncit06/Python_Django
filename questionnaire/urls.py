from django.conf.urls import url, include
from.import views

urlpatterns = [
    url(r'^$', views.set_questions),
    url(r'^create/$', views.question_create, name="create"),

]