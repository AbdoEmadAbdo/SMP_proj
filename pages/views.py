from django.shortcuts import render

from .forms import LoginForm

def index(request): 
    
    # the 3rd way   
    if request.method == 'POST':
       dataform= LoginForm(request.POST)
       if dataform.is_valid():
        dataform.save()
  
    else:
        dataform= LoginForm()

    '''
        # x                         from html  للطريقة الاولي فورم    
    # userName = request.POST.get('User-name')  # el  x  deh   shayla the value of username
    # passWord = request.POST.get('U_password')
    # email = request.POST.get('email')
    # Login(usernameL='userName', passwordL='passWord').save()
    
    ##? But for 2nd way ----> get(....)  will be from the {{{forms.py }}}
    #?  userName = request.POST.get('username')  # from forms.py  username, password
    #?  userName = request.POST.get('password')
    #?  email = request.POST.get('email')
        
   #?  dataform= Login(usernameL='userName', passwordL='passWord').save()    #data = Login.objects.all()
    #  dataform.save()
     '''
    
    return render(request ,'pages/index.html')

def search(request):
    query = request.GET.get('s')
    #client = MongoClient()
    #db = client['FTKP_DB']
    #results = db.my_collection.find({'$text': {'$search': query}})
    return render(request, 'search_results.html')  # , {'results': results}


def sign_in(request):
    return render(request , 'pages/sign_in.html')

def sign_up(request):
    return render(request , 'pages/sign_up.html')

def profile(request):
    return render(request , 'pages/profile.html')

def setting(request):
    return render(request, 'pages/setting.html')

def Companys(request):
    
    
    return render(request, 'pages/Companies.html')


def LastNews(request):
    return render(request, 'pages/LastNews.html')

def Trending(request):
    return render(request, 'pages/Trending.html')

def chart(request):
    return render(request, 'pages/Chart.html')

def Community(request):
    return render(request, 'pages/Community.html')















'''
#to render Jinja2 templates.    When the view is called, it will pass the my_data dictionary to the template, which will use the Jinja2 syntax to insert the name and age variables 
#                                   into the HTML output.     The final result will be a rendered HTML page that displays the name and age of the user.
def my_view(request):
    my_data = {'name': 'EAA', 'age': 30}
    return render(request, 'pages/my_template.html', my_data)



# for conn DB

from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
db = client[settings.DATABASES['default']['NAME']]

'''

# for FMP
'''
import requests
import json
#                                       function gets the historical stock prices for a given symbol from FMP API.
def get_stock_prices(symbol, days):
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={FMP_API_KEY}&serietype=line&timeseries={days}'
    r = requests.get(url)
    data = json.loads(r.content)
    prices = []
    for item in data['historical']:
        prices.append(item['close'])
    prices.reverse()
    return prices
'''


#from django.template import loader
#from .models import Login ,Stocks, Customer

'''
    def index(request): 
    
        # x                         from html  للطريقة الاولي فورم    
    # userName = request.POST.get('User-name')  # el  x  deh   shayla the value of username
    # passWord = request.POST.get('U_password')
    # email = request.POST.get('email')
    # Login(usernameL='userName', passwordL='passWord').save()
    
    ##? But for 2nd way ----> get(....)  will be from the {{{forms.py }}}
    #?  userName = request.POST.get('username')  # from forms.py  username, password
    #?  userName = request.POST.get('password')
    #?  email = request.POST.get('email')
        
   #?  dataform= Login(usernameL='userName', passwordL='passWord').save()    #data = Login.objects.all()
    #  dataform.save()

'''



'''
#? Here using the CustomUserSerializer.   ----> creates a new user with a username, email, and password

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#from .serializers(Not_Active) import CustomUserSerializer

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])

def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''