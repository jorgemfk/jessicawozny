from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Member

def index(request):
    #members = Member.objects.all()
    #member_list_html = [f"<li>{member.name}</li>" for member in members]
    #return HttpResponse(f"<ul>{''.join(member_list_html)}</ul>")
    return render(request, 'wozny/index.html')

def add_member(request, member_name):
    Member.objects.create(name=member_name)
    return redirect('index')


def catalogo(request):
    return render(request, 'wozny/catalogo.html')