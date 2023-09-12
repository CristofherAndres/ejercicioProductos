from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"productosApp/index.html")

def electronica(request):
    data = {
        'titulo': 'Electronica',
        'producto1': 'Audifonos',
        'marca1': 'Phillips',
        'descripcion1': 'Sirve para escuchar musica',
        'producto2': 'Secador de pelo',
        'marca2': 'Phillips',
        'descripcion2': 'Sirve para secar pelo',
        'producto3': 'Mouse',
        'marca3': 'Phillips',
        'descripcion3': 'Sirve para mover el cursor',
    }
    return render(request, 'productosApp/productos.html',data)

def ropa(request):
    data = {
        'titulo': 'Ropa',
    }
    return render(request, 'productosApp/productos.html',data)

def consolas(request):
    data = {
        'titulo': 'Consola',
    }
    return render(request, 'productosApp/productos.html',data)