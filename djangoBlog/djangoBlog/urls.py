from django.contrib import admin
from django.urls import path , inlcude
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home),
    path('articles/', include('articles.urls'))

]
