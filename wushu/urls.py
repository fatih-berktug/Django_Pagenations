from django.conf.urls import url
from wushu.views import index,myModel_asJson



urlpatterns = [
    url(r'anasayfa/admin/$',myModel_asJson, name="my_ajax_url"),

    url('',index)

]

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the poll index.")