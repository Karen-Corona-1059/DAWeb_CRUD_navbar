from django.urls import path
from Ventas_app import views
urlpatterns = [
    path('venta', views.inicio_vistaVentas, name="venta"),
    path("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path("seleccionarVenta/<int:id_venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVenta/<int:id_venta>",views.editarVenta,name="editarVenta"),
    path("borrarVenta/<int:id_venta>",views.borrarVenta,name="borrarVenta"),
]