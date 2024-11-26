from django.shortcuts import render,redirect
from .models import Provedores
# Create your views here.

def inicio_vistaProvedor(request):
    losProvedores=Provedores.objects.all()
    return render(request,"gestionarProvedores.html",{"misProvedores":losProvedores})

def registrarProvedor(request):
    id_provedor=request.POST["id_provedor"]
    nombre=request.POST["nombre"]
    Telefono=request.POST["Telefono"]
    sucursal=request.POST["sucursal"]
    direccion=request.POST["direccion"]
    HorarioE=request.POST["HorarioE"]
    HorarioS=request.POST["HorarioS"]
    id_producto=request.POST["id_producto"]
    guardarprovedor=Provedores.objects.create(id_provedor=id_provedor,nombre=nombre,Telefono=Telefono,sucursal=sucursal,direccion=direccion,HorarioE=HorarioE,HorarioS=HorarioS,id_producto=id_producto)
    return redirect("provedor")

def seleccionarProvedor(request,id_provedor):
    provedor=Provedores.objects.get(id_provedor=id_provedor)
    return render(request,"editarProvedores.html",{"misProvedores":provedor})

def editarProvedor(request):
    id_provedor=request.POST["id_provedor"]
    nombre=request.POST["nombre"]
    Telefono=request.POST["Telefono"]
    sucursal=request.POST["sucursal"]
    direccion=request.POST["direccion"]
    HorarioE=request.POST["HorarioE"]
    HorarioS=request.POST["HorarioS"]
    id_producto=request.POST["id_producto"]
    provedor=Provedores.objects.get(id_provedor=id_provedor)
    provedor.nombre=nombre
    provedor.Telefono=Telefono
    provedor.sucursal=sucursal
    provedor.direccion=direccion
    provedor.HorarioE = request.POST.get("HorarioE")
    provedor.HorarioS = request.POST.get("HorarioS")
    provedor.id_producto=id_producto
    provedor.save()
    return redirect("provedor")

def borrarProvedor(request, id_provedor):
    provedor = Provedores.objects.get(id_provedor=id_provedor)
    provedor.delete()
    return redirect("provedor")