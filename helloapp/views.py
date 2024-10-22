from django.shortcuts import render

def index_listar(request):
    return render(request, 'index.html',{'nome': "Patrícia"})
