from django.shortcuts import render,redirect,get_object_or_404
from .models import Sucursal
# Create your views here.

def inicio_vistaSucursal(request):
    lasSucursales=Sucursal.objects.all()
    return render(request,"gestionarSucursal.html",{"misSucursales":lasSucursales})

def registrarSucursal(request):
    id_sucursal=request.POST["id_sucursal"]
    nombre=request.POST["nombre"]
    Direccion=request.POST["Direccion"]
    Numero=request.POST["Numero"]
    HorarioE=request.POST["HorarioE"]
    HorarioS=request.POST["HorarioS"]
    Correo=request.POST["Correo"]
    
    guardarsucursal=Sucursal.objects.create(id_sucursal=id_sucursal,nombre=nombre,Direccion=Direccion,Numero=Numero,HorarioE=HorarioE,HorarioS=HorarioS,Correo=Correo)
    return redirect("sucursal")

def seleccionarSucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"sucursal": sucursal})

def editarSucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)

    if request.method == "POST":
        sucursal.nombre = request.POST.get("nombre")
        sucursal.Direccion = request.POST.get("Direccion")
        sucursal.Numero = request.POST.get("Numero")
        sucursal.HorarioE = request.POST.get("HorarioE")
        sucursal.HorarioS = request.POST.get("HorarioS")
        sucursal.Correo = request.POST.get("Correo")
        sucursal.save()
        return redirect("sucursal") 
    
    return render(request, "editarSucursal.html", {"sucursal": sucursal})



def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursal")