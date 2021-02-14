from django.shortcuts import render




def startpage(request):

    return render(request, 'main_app/base.html')