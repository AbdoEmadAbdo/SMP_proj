#Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView

from . import views

from django.urls import path



urlpatterns = [
#path('', RedirectView.as_view(url='AiPred/', permanent=True)),
path('Pred/',views.Company , name="ModelP" , permanent=True),
path('train_model/', views.train_model, name='train_model'),

path('predict/', views.predict, name='predict'),
path('predict_api/', views.predict_api, name='predict_api'),
path('plot_predicrtions/', views.plot_predicrtions, name='plot_predicrtions'),
path('plot_predicrtions_api/', views.plot_predicrtions_api, name='plot_predicrtions_api'),


]

