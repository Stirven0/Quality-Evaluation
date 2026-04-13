# 📊 QualityEval - Evaluación de Calidad de Software

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Sistema web para la evaluación de calidad de software aplicando los modelos estándar **McCall**, **Boehm** y **FURPS**. 
Proyecto académico que evalúa la calidad de **Instagram** como caso de estudio.

![Vista previa](https://via.placeholder.com/800x400/0d6efd/ffffff?text=QualityEval+Screenshot)

## 🚀 Características

- ✅ **Modelo McCall**: 11 métricas de calidad (88/100)
- ✅ **Modelo Boehm**: Análisis jerárquico (84/100)  
- ✅ **Modelo FURPS**: 5 categorías de calidad (85/100)
- ✅ **Comparación visual** con Chart.js
- ✅ **Diseño responsive** con Bootstrap 5
- ✅ **Conclusiones académicas** documentadas

## 📋 Requisitos

- Python 3.10+
- Django 5.0+
- Navegador web moderno

## ⚡ Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/quality-evaluation.git
cd quality-evaluation

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Aplicar migraciones
python manage.py migrate

# 6. Ejecutar servidor
python manage.py runserver
```

Accede a: `http://127.0.0.1:8000/`

📁 Estructura del Proyecto

```
quality_evaluation/
├── quality_evaluation/     # Configuración principal Django
├── evaluation/            # App principal con lógica de evaluación
├── templates/             # HTML templates
├── static/               # CSS, JS, imágenes
├── manage.py
├── requirements.txt
└── README.md
```

🎯 Uso

1. Inicio: Presentación del proyecto y software evaluado
2. Modelos: Explicación teórica de McCall, Boehm y FURPS
3. Evaluaciones: Resultados detallados por modelo
4. Comparación: Gráficas comparativas entre modelos
5. Conclusiones: Análisis académico final

🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para:
- Correcciones de datos
- Mejoras en el diseño
- Nuevos modelos de calidad
- Optimizaciones de código

📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

👨‍💻 Autor

Tu Nombre - Proyecto Académico 2024
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

🙏 Agradecimientos

- Django Software Foundation
- Bootstrap Team
- Chart.js Contributors
- McCall, Boehm y HP/IBM por los modelos de calidad
