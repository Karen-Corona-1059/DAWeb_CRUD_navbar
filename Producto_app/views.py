from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.

def inicio_vistaProductos(request):
    losProductos=Productos.objects.all()
    return render(request,"gestionarProductos.html",{"misProductos":losProductos})

def registrarProducto(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    descripcion = request.POST["descripcion"]
    categoria = request.POST["categoria"]
    id_provedor = request.POST["id_provedor"]
    guardarproducto=Productos.objects.create(id=id,nombre=nombre,precio=float(precio),cantidad=int(cantidad),descripcion=descripcion,categoria=categoria,id_provedor=int(id_provedor),)
    return redirect("productos")

def seleccionarProducto(request,id):
    producto=Productos.objects.get(id=id)
    return render(request,"editarProductos.html",{"misProductos":producto})

def editarProducto(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    descripcion = request.POST["descripcion"]
    categoria = request.POST["categoria"]
    id_provedor = request.POST["id_provedor"]

    producto=Productos.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = float(precio)
    producto.cantidad = int(cantidad)
    producto.descripcion = descripcion
    producto.categoria = categoria
    producto.id_provedor = int(id_provedor)
    producto.save()
    return redirect("productos")

def borrarProducto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect("productos")