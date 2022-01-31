from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# import Http Response from django
from django.shortcuts import render
  
def getno():
    return 5

def get_wm():
    return [1,2]


def sending(request):
    # recipient = request.POST.get('recipient','')
    return HttpResponse("you sent" + str(recipient))

# create a function
def index(request):
    # create a dictionary to pass
    # data to the template
    no = getno()
    context ={
        "cycle_data":"no of cycles" + str(no),
        "free_mac": str(get_wm())
    }
    # return response with template and context
    return render(request, "index.html", context)