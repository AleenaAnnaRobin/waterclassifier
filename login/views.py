from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from classifier.models import QualityAnalysis,QualityResult
# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        analysis_list=[]
        logout(request)
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            try:
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/profile/')
                        
                else:
                    return render(request,"login.html")
            except Exception as e:
                return render(request,"error.html",{"error_message":str(e)})
class Logout(View):
    def get(self, request):
        logout(request)
        return render(request,"login.html")