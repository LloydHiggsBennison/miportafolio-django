from django.urls import path
from .views import ProyectoListaView, ProyectoDetalleView, TareaCrearView
urlpatterns = [
    path("", ProyectoListaView.as_view(), name="proyecto_lista"),
    path("<int:pk>/", ProyectoDetalleView.as_view(), name="proyecto_detalle"),
    path("<int:pk>/tareas/nueva/", TareaCrearView.as_view(), name="tarea_crear"),
]
