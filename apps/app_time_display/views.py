# from django.shortcuts import render, HttpResponse
# def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")

from django.shortcuts import render,HttpResponse
from time import gmtime, strftime
# current data&time
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'app_time_display/index.html', context)