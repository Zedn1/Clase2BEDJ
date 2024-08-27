from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)

def prueba1(request):
    html="""
    <h1>Pagina de prueba</h1>
    <h2>Si!</h2>
    <ul>
        <li>Si - 2</li>
        <li>Si - 3</li>
        <li>Si - 4</li>
        <li>Si - 5</li>
    </ul>

    """
    return HttpResponse(html)