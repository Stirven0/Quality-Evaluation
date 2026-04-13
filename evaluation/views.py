from django.shortcuts import render

# Create your views here.
def home(request):
    """Vista de la página de inicio"""
    context = {
        'titulo': 'Evaluación de Calidad de Software',
        'subtitulo': 'Análisis de Instagram mediante Modelos Estándar',
    }
    return render(request, 'home.html', context)

def modelos(request):
    """Vista explicativa de los modelos de calidad"""
    return render(request, 'modelos.html')

def mccall(request):
    """Evaluación según modelo McCall"""
    metricas = []
    for m in [
        {'nombre': 'Corrección', 'pregunta': '¿El software cumple especificaciones?', 'esperado': 10, 'obtenido': 9},
        {'nombre': 'Fiabilidad', 'pregunta': '¿Frecuencia de fallos?', 'esperado': 10, 'obtenido': 8},
        {'nombre': 'Eficiencia', 'pregunta': '¿Uso óptimo de recursos?', 'esperado': 10, 'obtenido': 9},
        {'nombre': 'Integridad', 'pregunta': '¿Control de acceso seguro?', 'esperado': 10, 'obtenido': 9},
        {'nombre': 'Usabilidad', 'pregunta': '¿Es fácil de aprender y usar?', 'esperado': 10, 'obtenido': 10},
        {'nombre': 'Mantenibilidad', 'pregunta': '¿Fácil de modificar?', 'esperado': 10, 'obtenido': 8},
        {'nombre': 'Flexibilidad', 'pregunta': '¿Adaptable a cambios?', 'esperado': 10, 'obtenido': 9},
        {'nombre': 'Verificabilidad', 'pregunta': '¿Fácil de probar?', 'esperado': 10, 'obtenido': 8},
        {'nombre': 'Portabilidad', 'pregunta': '¿Funciona en diferentes plataformas?', 'esperado': 10, 'obtenido': 10},
        {'nombre': 'Reusabilidad', 'pregunta': '¿Componentes reutilizables?', 'esperado': 10, 'obtenido': 8},
    ]:
        m['porcentaje'] = int((m['obtenido'] / m['esperado']) * 100)
        metricas.append(m)

    
    total_esperado = sum(m['esperado'] for m in metricas)
    total_obtenido = sum(m['obtenido'] for m in metricas)
    
    context = {
        'metricas': metricas,
        'total_esperado': total_esperado,
        'total_obtenido': total_obtenido,
        'porcentaje': round((total_obtenido/total_esperado)*100, 1)
    }
    return render(request, 'mccall.html', context)

def boehm(request):
    """Evaluación según modelo Boehm"""
    factores = [
        {'nombre': 'Portabilidad', 'descripcion': 'Capacidad de adaptación a diferentes entornos', 'puntaje': 85},
        {'nombre': 'Utilidad', 'descripcion': 'Utilidad general para los usuarios', 'puntaje': 88},
        {'nombre': 'Mantenibilidad', 'descripcion': 'Facilidad de mantenimiento y corrección', 'puntaje': 82},
        {'nombre': 'Interacción', 'descripcion': 'Comunicación efectiva con el usuario', 'puntaje': 90},
        {'nombre': 'Confiabilidad', 'descripcion': 'Disponibilidad y ausencia de fallos', 'puntaje': 83},
        {'nombre': 'Eficiencia', 'descripcion': 'Uso de recursos de hardware', 'puntaje': 78},
        {'nombre': 'Integridad', 'descripcion': 'Seguridad y protección de datos', 'puntaje': 86},
    ]
    
    total = sum(f['puntaje'] for f in factores)
    promedio = round(total / len(factores), 1)
    
    context = {
        'factores': factores,
        'total': promedio,
        'escala': round((promedio/100)*100)
    }
    return render(request, 'boehm.html', context)

def furps(request):
    """Evaluación según modelo FURPS"""
    categorias = [
        {
            'nombre': 'Funcionalidad',
            'items': [
                {'item': 'Características', 'puntaje': 9},
                {'item': 'Seguridad', 'puntaje': 8},
                {'item': 'Interoperabilidad', 'puntaje': 8},
            ],
            'total': 25,
            'maximo': 30
        },
        {
            'nombre': 'Usabilidad',
            'items': [
                {'item': 'Interfaz intuitiva', 'puntaje': 9},
                {'item': 'Documentación', 'puntaje': 8},
                {'item': 'Accesibilidad', 'puntaje': 8},
            ],
            'total': 25,
            'maximo': 30
        },
        {
            'nombre': 'Confiabilidad',
            'items': [
                {'item': 'Frecuencia de fallos', 'puntaje': 8},
                {'item': 'Capacidad de recuperación', 'puntaje': 9},
                {'item': 'Precisión', 'puntaje': 9},
            ],
            'total': 26,
            'maximo': 30
        },
        {
            'nombre': 'Rendimiento',
            'items': [
                {'item': 'Tiempo de respuesta', 'puntaje': 7},
                {'item': 'Uso de recursos', 'puntaje': 8},
                {'item': 'Capacidad', 'puntaje': 8},
            ],
            'total': 23,
            'maximo': 30
        },
        {
            'nombre': 'Soporte',
            'items': [
                {'item': 'Mantenibilidad', 'puntaje': 8},
                {'item': 'Flexibilidad', 'puntaje': 7},
                {'item': 'Facilidad de prueba', 'puntaje': 8},
            ],
            'total': 23,
            'maximo': 30
        }
    ]
    for categoria in categorias:
        for item in categoria['items']:
            item['porcentaje'] = int((item['puntaje'] / 10) * 100)
            
    
    total_obtenido = sum(c['total'] for c in categorias)
    total_maximo = sum(c['maximo'] for c in categorias)
    
    context = {
        'categorias': categorias,
        'total_obtenido': total_obtenido,
        'total_maximo': total_maximo,
        'porcentaje': round((total_obtenido/total_maximo)*100)
    }
    return render(request, 'furps.html', context)

def comparacion(request):
    """Comparación de modelos con gráficos"""
    datos = {
        'mccall': 88,
        'boehm': 84,
        'furps': 85
    }
    
    context = {
        'datos': datos,
        'promedio': round(sum(datos.values())/3, 1)
    }
    return render(request, 'comparacion.html', context)

def conclusiones(request):
    """Conclusiones del análisis"""
    return render(request, 'conclusiones.html')

