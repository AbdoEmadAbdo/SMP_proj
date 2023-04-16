from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('' ,views.index , name='INDEX'),
    
    path('profile/' ,views.profile , name='profile'),
    path('login/' ,views.sign_in ,name='S_IN'),
    
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path('setting/',views.setting , name="setting"),
   # path('dashboard/',views.Dashboard ,name='my dashboard'),
    
    path('Sup/' ,views.sign_up , name='signUp'),

    path('Companies/',views.Companys , name="Companies"),
    path('LastNews/',views.LastNews , name="LastNews"),
    path('Trending/',views.Trending , name="Trendings"),
    path('chart/',views.chart , name="chart"),
    path('Community/',views.Community , name="Community"),
    
    path('search/', views.search, name='search'),
    
]










# Note:-



#       {% load static %}
#    <a  href= "{% static 'css/anyFile.css' %}">   ---> inside the href=""            in any file html you want to appear css in
#     src=" {% static   'images/anyFile.jpg'   %}" alt="">    --->inside src=""       in any file html you want to appear Image in
# href=" {% url 'index' %} " 



#   if in:   project >> urls.py  --->   path('Index', include('pages.urls')),
    
#   and in:  App >> urls.py  --->    path('home/',views.index ,name='my_index'),
#       SO ,,,         ------>  user URL in wewbsite will be ---->  http://127.0.0.1:8000/Index/home/
