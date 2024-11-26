from django.shortcuts import render, redirect, get_object_or_404

from .models import Ventas

def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all()
    return render(request,"gestionarVenta.html",{"misVentas":lasVentas})

def registrarVenta(request):
    id_venta = request.POST["id_venta"]
    id_producto = request.POST["id_producto"]
    id_cliente = request.POST["id_cliente"]
    id_sucursal = request.POST["id_sucursal"]
    id_empleado = request.POST["id_empleado"]
    Total = request.POST["Total"]
    Fecha = request.POST["Fecha"]
    guardarventa=Ventas.objects.create(id_venta=id_venta,id_producto=id_producto,id_cliente=float(id_cliente),id_sucursal=int(id_sucursal),id_empleado=id_empleado,Total=Total,Fecha=Fecha)
    return redirect("venta")
    
    

def seleccionarVenta(request, id_venta):
    venta = get_object_or_404(Ventas, id_venta=id_venta)
    return render(request, "editarVenta.html", {"venta": venta})

def editarVenta(request, id_venta):
    venta = get_object_or_404(Ventas, id_venta=id_venta)

    if request.method == "POST":
        venta.id_producto = request.POST.get("id_producto")
        venta.id_cliente = request.POST.get("id_cliente")
        venta.id_sucursal = request.POST.get("id_sucursal")
        venta.id_empleado = request.POST.get("id_empleado")
        venta.Total = request.POST.get("Total")
        venta.Fecha = request.POST.get("Fecha")
        venta.save()
        return redirect("venta") 
    
    return render(request, "editarVenta.html", {"venta": venta})



def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("venta")