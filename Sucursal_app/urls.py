from django.urls import path
from Sucursal_app import views
urlpatterns = [
    path('sucursal', views.inicio_vistaSucursal, name="sucursal"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<int:id_sucursal>",views.seleccionarSucursal,name="seleccionarSucursal"),
    path("editarSucursal/<int:id_sucursal>",views.editarSucursal,name="editarSucursal"),
    path("borrarSucursal/<int:id_sucursal>",views.borrarSucursal,name="borrarSucursal"),
]