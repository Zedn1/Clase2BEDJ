from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de la app2</h1>")

def pagina2(request):
    html="""
    <h1>Soy la pagina 2 de la app2</h1>
    <a href="/app2/index">Volver</a>
    """
    return HttpResponse(html)