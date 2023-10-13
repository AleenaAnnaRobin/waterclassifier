from django.shortcuts import redirect, render
from django.views import View
from .models import Register, QualityAnalysis,QualityResult
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from datetime import datetime
import random
# Create your views here.
class Profile(View):
    def get(self,request):
        try:
            
            analysis_list=[]
            analysis=QualityAnalysis.objects.filter(user=request.user.id)
                        
            for data in analysis:
                analysis_list.append(data.id)
            result=QualityResult.objects.filter(quality_analysis_id__in=analysis_list)
            return render(request,"profile.html",{"analysis":analysis,"results":result})
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
class Landing(View):
    def get(self,request):
        try:
             return render(request,"landing.html")
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    
class Signup(View):
    def get(self,request):
        try:
            return render(request,"signup.html")
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    def post(self,request):
        try:
            name=request.POST.get("name")
            email=request.POST.get("email")
            password=request.POST.get("password")
            user=User()
            
            user.first_name=name
            user.username=email
            user.password=make_password(password)
            user.is_superuser=False
            user.date_joined=datetime.now()
            user.save()

            reg=Register()
            reg.name=name
            reg.user=user
            reg.save()
            return render(request,"login.html")
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           

           
class QualityAnalysisView(View):

    def get(self,request):
        try:
            return render(request,"quality.html")
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    def post(self,request):
        try:
            result=[]
            pH=float(request.POST.get("ph"))
            oxygen=float(request.POST.get("oxygen"))
            temp=float(request.POST.get("temp"))
            cond=float(request.POST.get("cond"))
            turbidity=float(request.POST.get("turbidity"))
            tds=float(request.POST.get("tds"))
            chlorine=float(request.POST.get("chlorine"))
            print(pH,oxygen,temp,cond,turbidity,tds,chlorine)
            drinkstatus= self.drinkingWater(request,pH,oxygen,temp,cond,turbidity,tds,chlorine)
            domesticstatus=self.domesticWater(request,pH,oxygen,temp,cond,turbidity,tds,chlorine)
            agristatus=self.agriWater(request,pH,oxygen,temp,cond,turbidity,tds,chlorine)
            medicalstatus=self.medicalWater(request,pH,oxygen,temp,cond,turbidity,tds,chlorine)
            boilerstatus=self.boilerWater(request,pH,oxygen,temp,cond,turbidity,tds,chlorine)
            register=Register.objects.get(user=request.user.id)
            sample_id=self.generate_6_digit_char_field(request)
            if drinkstatus==True:
                result.append("Drinking and Hydration")
                self.savedetails(pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,"Drinking and Hydration",sample_id)
            if domesticstatus==True:
                result.append("Domestic use ")
                self.savedetails(pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,"Domestic use",sample_id)
            if agristatus==True:
                result.append("Agriculture and Irrigation")
                self.savedetails(pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,"Agriculture and Irrigation",sample_id)
            if medicalstatus==True:
                result.append("Medical Industry")
                self.savedetails(pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,"Medical Industry",sample_id)
            if boilerstatus==True:
                result.append("Boiler Feed")
                self.savedetails(pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,"Boiler Feed",sample_id)
            
            if drinkstatus==False and domesticstatus==False and agristatus==False and medicalstatus==False and boilerstatus==False:
                result.append("None")

                
                
            return render(request,"result.html",{"ph":pH,"oxygen":oxygen,"temp":temp,"cond":cond,"turbidity":turbidity,"tds":tds,"chlorine":chlorine,"result":result})
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           

    def drinkingWater(self,request,pH,oxygen,temp,cond,turbidity,tds,chlorine):
        try:

            if 6.5<=pH<=8.5 and 4<=oxygen<=8 and 10<=temp<=20 and 200<=cond<=800 and turbidity <1 and 500<tds<1000 and 0.2<=chlorine<=4:
                status=True
            else:
                status=False

            return status
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    def domesticWater(self,request,pH,oxygen,temp,cond,turbidity,tds,chlorine):
        try:
            if 6.5<=pH<=8.5 and 4<=oxygen<=8 and 10<=temp<=25 and 200<=cond<=800 and turbidity <1 and 500<tds<1000 and 0.2<=chlorine<=4:
                status=True
            else:
                status=False

            return status
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
        
    def agriWater(self,request,pH,oxygen,temp,cond,turbidity,tds,chlorine):
        try:
            if 6<=pH<=7.5 and 4<=oxygen<=12 and 5<=temp<=30 and 500<cond<=3000 and turbidity <10 and 500<tds<1000 and 0<=chlorine<=0.2:
               status=True
            else:
                status=False

            return status
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           

    def medicalWater(self,request,pH,oxygen,temp,cond,turbidity,tds,chlorine):
        try:
            if 5<=pH<=9 and oxygen>0 and temp>0 and cond>0 and turbidity <5 and tds<1000 and chlorine<=0.2:
                status=True
            else:
                status=False

            return status
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    def boilerWater(self,request,pH,oxygen,temp,cond,turbidity,tds,chlorine):
        try:
            if 8.5<=pH<=9.5 and oxygen<=2 and 70<=temp<=90 and cond<=1500 and turbidity <1 and tds<1500 and chlorine<=0.2:
                status=True
            else:
                status=False

            return status
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
       
    def savedetails(self,pH,oxygen,temp,cond,turbidity,tds,chlorine,register,request,waterresult,sample_id):
        try:
            
            quality=QualityAnalysis()
            quality.pH=pH
            quality.dissolved_oxygen=oxygen
            quality.temperature=temp
            quality.conductivity=cond
            quality.turbidity=turbidity
            quality.tds=tds
            quality.chlorine=chlorine
            quality.user=request.user
            quality.register=register
            quality.sample_id=sample_id
            quality.save()
            qualityresult=QualityResult()
            qualityresult.result=waterresult
            qualityresult.quality_analysis=quality
            qualityresult.user=request.user
            qualityresult.created_on=datetime.now()
            qualityresult.save()
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
           
    

    def generate_6_digit_char_field(self,request):
        try:
                
            """Generates a 6 digit char field."""
            characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            random_number = "".join([random.choice(characters) for _ in range(6)])
            return random_number
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})
        
class EditProfile(View):
    def get(self,request,data_id):
        try:
            print(data_id)
            quality=QualityAnalysis.objects.get(id=data_id)
            result=QualityResult.objects.filter(quality_analysis=quality.id)
            result.delete()
            quality.delete()
            # return render(request,"login.html")
            return redirect("/profile/")
        except Exception as e:
            return render(request,"error.html",{"error_message":str(e)})