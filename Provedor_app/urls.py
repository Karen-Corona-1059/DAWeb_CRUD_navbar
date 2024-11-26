from django.urls import path
from Provedor_app import views

urlpatterns = [
    path('provedor', views.inicio_vistaProvedor, name="provedor"),
    path("registrarProvedor/",views.registrarProvedor,name="registrarProvedor"),
    path("seleccionarProvedor/<int:id_provedor>",views.seleccionarProvedor,name="seleccionarProvedor"),
    path("editarProvedor/",views.editarProvedor,name="editarProvedor"),
    path("borrarProvedor/<int:id_provedor>",views.borrarProvedor,name="borrarProvedor"),
]