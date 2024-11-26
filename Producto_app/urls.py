from django.urls import path
from Producto_app import views
urlpatterns = [
    path('productos', views.inicio_vistaProductos, name="productos"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<int:id>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<int:id>",views.borrarProducto,name="borrarProducto"),
]