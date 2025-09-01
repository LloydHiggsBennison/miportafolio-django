from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Proyecto, Tarea


class ProyectoListaView(ListView):
    model = Proyecto
    template_name = "proyectos/lista.html"
    context_object_name = "proyectos"
    queryset = Proyecto.objects.filter(activo=True).order_by("fecha_inicio")


class ProyectoDetalleView(DetailView):
    model = Proyecto
    template_name = "proyectos/detalle.html"
    context_object_name = "proyecto"


class TareaCrearView(CreateView):
    model = Tarea
    fields = ["titulo", "hecho"]                    # añade más campos si tu modelo los tiene
    template_name = "proyectos/lista_form.html"     # <- usando tu plantilla

    def dispatch(self, request, *args, **kwargs):
        # Cargamos el proyecto una sola vez y lo guardamos en self.proyecto
        self.proyecto = get_object_or_404(Proyecto, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Asignamos la FK antes de guardar
        form.instance.proyecto = self.proyecto
        return super().form_valid(form)

    def get_success_url(self):
        # Volver al detalle del proyecto al guardar
        return reverse_lazy("proyecto_detalle", kwargs={"pk": self.proyecto.pk})

    def get_context_data(self, **kwargs):
        # Pasamos el proyecto al contexto para mostrar su nombre en el form
        ctx = super().get_context_data(**kwargs)
        ctx["proyecto"] = self.proyecto
        return ctx
