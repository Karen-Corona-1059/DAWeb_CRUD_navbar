from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vistaClientes(request):
    losClientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html",{"misClientes":losClientes})

def registrarCliente(request):
    id_cliente = request.POST["id_cliente"]
    nombre = request.POST["nombre"]
    Telefono = request.POST["Telefono"]
    correo = request.POST["correo"]
    fecha = request.POST["fecha"]
    direccion = request.POST["direccion"]
    guardarcliente=Cliente.objects.create(id_cliente=id_cliente,nombre=nombre
    ,Telefono=Telefono,correo=correo,fecha=fecha,direccion=direccion)
    return redirect("clientes")

def seleccionarCliente(request,id_cliente):
    Clientes=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarClientes.html",{"misClientes":Clientes})

def editarCliente(request):
    id_cliente = request.POST["id_cliente"]
    nombre = request.POST["nombre"]
    Telefono = request.POST["Telefono"]
    correo = request.POST["correo"]
    fecha = request.POST["fecha"]
    direccion = request.POST["direccion"]  

    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.Telefono = Telefono
    cliente.correo = correo
    cliente.fecha = fecha
    cliente.direccion = direccion
    cliente.save()
    return redirect("clientes")

def borrarCliente(request,id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")