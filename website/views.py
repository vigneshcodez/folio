from django.shortcuts import render
from .models import Project,Technologies,Myprofile,Services,Enquiry
# Create your views here.


def home(request):

    
    if request.method == "POST":
        print(request.POST['name'])
        print(request.POST['email'])
        print(request.POST['mobile'])
        print(request.POST['message'])
        newdata = Enquiry(
            name = request.POST['name'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            message = request.POST['message'],
        )

        newdata.save()
        data = {
            "name":request.POST['name'],
            "email":request.POST['email'],
            "mobile":request.POST['mobile'],
            "message":request.POST['message'],
        }
        return render(request,'webbase/success.html',{"data":data})
    
    technologies = Technologies.objects.all()
    project = Project.objects.all()
    profile = Myprofile.objects.first()
    services = Services.objects.all()
    return render(request,'webbase/base.html',{"data":technologies,"projects":project,"profile":profile,"services":services})



