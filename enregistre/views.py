
from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from pyexpat import model

from .models import enregistrement

# Create your views here.

def  enregistrements(request):
    
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        contact = request.POST['contact']
        code_ticket = request.POST['code_ticket']
        if nom == "" or prenom == "" or contact == "" or code_ticket == "":
            messages.error(request, "Verifier les champs svp !!")
            return render(request, "enregistrement.html")
        else:
            enregistrement.objects.create(nom = nom,prenom=prenom,contact=contact,code_ticket=code_ticket).save()
            messages.success(request, "Enregistrement effectué avec succèss")
    return render(request, 'enregistrement.html')

def  verification(request):
    # donnee = enregistrement.objects.all()
    if request.method == "POST":
        ticket = request.POST['code_ticket']
        # datas = enregistrement.objects.filter(code_ticket=ticket).values().count()
        name_db = {'nom':'nom', 'prenom':'prenom', 'contact':'contact', 'code_ticket':'code_ticket'}
        datas = enregistrement.objects.raw('SELECT * FROM enregistre_enregistrement', translations=name_db)
        for data in datas:
            print(f'je suis {data.nom} {data.prenom} avec un numero de {data.contact}')
            
            if data.code_ticket !=  ticket  :   
                messages.error(request, "code incorrecte !!!")
                
            else:
                messages.success(request, "Code validé !!")
    context = {
            'ticket':  datas,
            'code': ticket 
            
    }
    return render(request, 'verification.html', context)
