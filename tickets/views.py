from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Member
import qrcode
from .forms import InputForm

#from django import forms
import os

# Create your views here.
import json




def tickets(request):
    if request.method == "POST":
        entered_number = request.POST.get('entered_number', '')
        try:
            count = int(entered_number)
            generate_qr_code(count)
            #return JsonResponse({'success': True, 'message': 'QR codes generated successfully'})

        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid input'})

    #template = loader.get_template("tickets.html")
    
    
    #return HttpResponse(template.render(request=request))
    return render(request, 'tickets.html')

def member(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
        }

    return HttpResponse(template.render(context, request))

def home(requests):
    template= loader.get_template('myfirst.html')
    return HttpResponse(template.render())





def generate_qr_code(count):
    qr_code_dir = 'static/qr_code/'
    os.makedirs(qr_code_dir, exist_ok=True)

    for i in range(count):
        data = f"JKM2014{i+1}"
        qr = qrcode.QRCode(version=1, box_size=10)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black')
        img.save(os.path.join(qr_code_dir, f"JKM2014{i+1}.png"))

    return count


def tickets_generator(request):
    #return render(request, 'tickets_generator')

    template = 'tickets_generator.html'
    return render(request, template, {})

    #template= loader.get_template('tickets_generator.html')
    #return HttpResponse(template.render())


