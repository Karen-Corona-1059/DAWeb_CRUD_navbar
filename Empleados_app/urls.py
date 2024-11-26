from django.urls import path
from Empleados_app import views
urlpatterns = [
    path('empleados', views.inicio_vistaEmpleado, name="empleados"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<int:id_empleado>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/<int:id_empleado>",views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<int:id_empleado>",views.borrarEmpleado,name="borrarEmpleado"),
]