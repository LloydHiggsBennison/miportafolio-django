from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,
related_name="tareas")
    titulo = models.CharField(max_length=150)
    hecho = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} ({self.proyecto_id})"
