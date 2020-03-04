from builtins import object, print, property

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import MyModel
from django.http import JsonResponse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.



def index(request):


    return render(request, 'index.html')




def myModel_asJson(request):


    # /datatablesten gelen veri kümesi datatables degiskenine alindi
    if request.method == 'GET':
        datatables = request.GET
        print("get islemi gerceklesti")
    elif request.method == 'POST':
        datatables = request.POST
        print("post islemi gerceklesti")


    print(datatables)
     # /Sayfanın baska bir yerden istenmesi durumunda degerlerin None dönmemesi icin degerler try boklari icerisine alindi
    try:
        draw = int(datatables.get('draw'))
        print("draw degeri =", draw)
        # Ambil start
        start = int(datatables.get('start'))
        print("start degeri =", start)
        # Ambil length (limit)
        length = int(datatables.get('length'))
        print("lenght  degeri =", length)
        # Ambil data search
        search = datatables.get('search[value]')
        print("search degeri =", search)
    except:
        draw=1
        start=0
        length=10

    # object_list = MyModel.objects.all()

    # Test verisi elde edebilemek icin sisteme kayıt saglandi

    # for x in range(150):
    #     b = MyModel(name='İsmail Yegin', user='Admin.', value='Kobiltek')
    #     b.save()
    if search:
        modeldata = MyModel.objects.filter(Q(name__icontains=search)|Q(value__icontains=search)|Q(user__icontains=search))
        total=modeldata.count();
        print("gelen deger=",total)
        # length=1000
        # start=0
        # page=1



    else:
        modeldata = MyModel.objects.all()
        total = MyModel.objects.count()


    if length==-1:
        print("deger bekledigimiz gibi geldi")


    # /Sayfalama  islemleri ile gerekli bir sekil de istenilen sayfanın gönderilmesi gerçeklesitirildi.

    start = start + length
    page = start / length

    print("sayfa =", page)
    veri = [item.to_dict_json() for item in modeldata]
    paginator = Paginator(veri, length)
    print("paginator=",paginator)
    veri = paginator.page(page).object_list
    print("veri=",veri)




    # Veri istenildigi gibi paketlendi ve gönderildi
    response={
        'data':veri,
        'draw':draw,
        'recordsTotal': total,
        'recordsFiltered': total
    }
    print("response degeri =",response)
    return JsonResponse(response)


def myModelyedek(request):
    datatables = request.GET

    draw = datatables.get('draw')
    print("draw degeri =",draw)
    # Ambil start
    start = datatables.get('start')
    print("start degeri =",start)
    # Ambil length (limit)
    length =datatables.get('length')
    print("lenght  degeri =",length)
    # Ambil data search
    search = datatables.get('search[value]')
    print("search degeri =",search)


    print("datatablenin gelen bütün degerleri =",datatables)


    # json = serializers.serialize('json', object_list)
    # print("json",json)
    # kisiler= []
    #
    #
    class Person(object):
        """__init__() functions as the class constructor"""

        def __init__(self, user=None, value=None, name=None):
            self.name = name
            self.user = user
            self.value = value

    #
    # for x in object_list:
    #     print("x=",x)
    #     print("name=",x.name)
    #     print("value=", x.value)
    #     print("pk=", x.pk)
    #     kisiler.append(Person(x.user,x.value,x.name))

    #
    object_list = MyModel.objects.all()
    print('object_list=', object_list)
    data = serializers.serialize('json',object_list)
    print("jsonadata =",data)
    # json1 = json.dumps(data)
    # print("en son json denemesi =",json1)



    return HttpResponse(data, content_type='application/json')