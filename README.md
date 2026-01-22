# 📚 APP COLEGIOS 2026 - Generador de Contenidos Educativos DBA

Sistema automatizado para la creación de contenidos educativos alineados con los **Derechos Básicos de Aprendizaje (DBA)** de Colombia.

## 📁 Estructura del Proyecto

```
APP COLEGIOS 2026/
├── contenidos/          # Contenidos educativos base y referencias DBA
├── templates/           # Plantillas y ejemplos de contenido
├── output/              # Contenido generado (por tema y grado)
├── recursos/            # Recursos adicionales (imágenes, documentos)
├── scripts/             # Scripts de generación
│   └── generador_contenido.py
└── README.md
```

## 🎯 Características

- ✅ Generación automática de contenido educativo
- ✅ Alineado con DBA Colombia
- ✅ Contexto y ejemplos colombianos (regiones, cultura)
- ✅ Diagramas Mermaid.js integrados
- ✅ Prompts para generación de imágenes educativas (DALL-E)
- ✅ Talleres evaluativos con claves de respuesta
- ✅ Estructura milimétrica para procesamiento automatizado

## 🚀 Uso Rápido

### Instalación

```bash
cd "d:\APP COLEGIOS 2026"
pip install google-generativeai
```

### Ejecución

```bash
cd scripts
python generador_contenido.py
```

### Uso Programático

```python
from scripts.generador_contenido import GeneradorContenidoEducativo

# Inicializar
generador = GeneradorContenidoEducativo(api_key="TU_API_KEY")

# Generar contenido
contenido = generador.generar_contenido(
    tema="El ciclo del agua",
    grado="4°"
)

# Parsear y guardar
secciones = generador.parsear_contenido(contenido)
generador.guardar_contenido(secciones, "El ciclo del agua", "4°")
```

## 📋 Secciones Generadas

Cada contenido incluye:

### 1. **THEORIA**
- Pregunta orientadora (contexto colombiano)
- Desarrollo profundo con 3 subtítulos
- Conceptos en negrilla
- 3 ejemplos locales de Colombia
- Citación del DBA correspondiente

### 2. **VISUALIZACION**
- Código Mermaid.js (mapa conceptual/diagrama de flujo)
- Prompt para DALL-E 3 (ilustración educativa)

### 3. **ACTIVIDADES**
- Nombre de la actividad
- Objetivos de aprendizaje
- Materiales de fácil acceso en Colombia
- Instrucciones paso a paso
- Taller evaluativo (5-7 preguntas)
- Clave de respuestas

### 4. **METADATOS**
- Título de la unidad
- Grado sugerido
- Eje temático
- Fecha de creación

## 📂 Salida de Archivos

Para cada tema generado se crea una carpeta con:

```
output/
└── 4°_El_ciclo_del_agua/
    ├── contenido_completo.txt  # Todo el contenido
    ├── teoria.md               # Sección teórica
    ├── actividades.md          # Actividades y taller
    ├── metadatos.txt           # Información metadata
    ├── diagrama.mmd            # Código Mermaid
    └── prompt_dalle.txt        # Prompt para imagen
```

## 🔧 Requisitos

- Python 3.8+
- `google-generativeai` (Gemini API)
- API Key de Google Gemini

## 📖 Ejemplos de Temas

- Ciencias Naturales: "El ciclo del agua", "La fotosíntesis", "El sistema solar"
- Matemáticas: "Fracciones", "Geometría básica", "Operaciones con decimales"
- Sociales: "Regiones de Colombia", "Cultura indígena", "Geografía colombiana"
- Lenguaje: "La narración", "Comprensión lectora", "Gramática española"

## ⚙️ Configuración API

1. Obtén tu API Key de Google AI Studio: https://makersuite.google.com/app/apikey
2. Al ejecutar el script, ingresa tu API Key cuando se solicite
3. O configúrala en tu código:

```python
generador = GeneradorContenidoEducativo(api_key="tu-api-key-aquí")
```

## 🎨 Visualizaciones

- Los archivos `.mmd` pueden visualizarse en: https://mermaid.live
- Los prompts DALL-E pueden usarse en OpenAI o Microsoft Designer

## 📝 Notas Importantes

- La estructura de salida es **milimétrica** para permitir parsing automatizado
- Todo el contenido se alinea con los DBA de Colombia
- Los ejemplos y contextos son específicos de Colombia (regiones, cultura, geografía)
- Los materiales sugeridos son de fácil acceso en contexto colombiano

## 🤝 Contribuir

Este es un proyecto para mejorar la educación en Colombia. Si tienes sugerencias o mejoras, son bienvenidas.

## 📜 Licencia

Proyecto educativo para instituciones colombianas.

---

**Desarrollado con ❤️ para la educación colombiana**
