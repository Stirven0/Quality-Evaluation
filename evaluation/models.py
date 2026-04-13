from django.db import models

# Create your models here.
class Evaluacion(models.Model):
    """Modelo base para almacenar evaluaciones de calidad"""
    MODELOS = [
        ('MCCALL', 'Modelo McCall'),
        ('BOEHM', 'Modelo Boehm'),
        ('FURPS', 'Modelo FURPS'),
    ]
    
    modelo = models.CharField(max_length=20, choices=MODELOS)
    metrica = models.CharField(max_length=100)
    puntaje = models.IntegerField(default=0)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
    
    def __str__(self):
        return f"{self.modelo} - {self.metrica}: {self.puntaje}"

