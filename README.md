# 🎓 Generador de Contenidos Educativos Colombia

Sistema de diseño instruccional automatizado para crear contenido educativo de alta calidad alineado con los **Derechos Básicos de Aprendizaje (DBA)** de Colombia.

## ✨ Características

- 📚 **Contenido Denso y Detallado**: Genera teoría profunda con fundamentos científicos y ejemplos colombianos específicos
- 🗺️ **Contextualizado para Colombia**: Incluye ejemplos de todas las regiones (Caribe, Pacífico, Andina, Amazonía, Orinoquía)
- 📊 **Diagramas Mermaid**: Genera automáticamente mapas conceptuales y diagramas de flujo
- 🎨 **Prompts DALL-E**: Crea prompts optimizados para generar imágenes educativas
- ✏️ **Actividades Prácticas**: Talleres con materiales de fácil acceso en Colombia
- 📝 **Evaluaciones**: Taller evaluativo con clave de respuestas incluida
- 🎯 **Alineado con DBA**: Todo el contenido sigue los estándares oficiales del Ministerio de Educación
- 🖥️ **Interfaz Web Moderna**: Diseño inspirado en UNOi con estilo profesional

## 🚀 Instalación

### Requisitos
- Python 3.8+
- API Key de Google Gemini ([obtener aquí](https://makersuite.google.com/app/apikey))

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/sumerce-sito/Generador-de-Contenidos-Educativos.git
cd Generador-de-Contenidos-Educativos
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación**
```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

## 📖 Uso

### Interfaz Web (Recomendado)

1. **Configurar API Key**
   - Ingresa tu API Key de Google Gemini en la barra lateral

2. **Ingresar Datos**
   - **Tema**: Escribe el tema educativo (ej: "El ciclo del agua")
   - **Grado**: Selecciona el grado escolar (1° a 11°)

3. **Generar Contenido**
   - Haz clic en "🚀 Generar Contenido Educativo"
   - Espera 20-60 segundos mientras la IA genera el contenido

4. **Ver y Descargar**
   - Revisa el contenido en la pestaña "📖 Contenido Generado"
   - Descarga los archivos individuales que necesites

### Modo Demo

Haz clic en "🎭 Ver Contenido de Demostración" para explorar un ejemplo completo sin necesidad de API Key.

### Línea de Comandos

```bash
python scripts/generador_contenido.py
```

## 📦 Contenido Generado

Cada tema genera automáticamente:

- **`teoria.md`**: Contenido teórico denso (1000-2000 palabras) con:
  - Introducción contextualizada
  - 4-6 conceptos principales
  - Fundamentos científicos
  - 3-4 ejemplos por región colombiana
  - Datos estadísticos de Colombia
  - DBA citado y competencias

- **`diagrama.mmd`**: Código Mermaid para visualización

- **`prompt_dalle.txt`**: Prompt optimizado para generación de imágenes

- **`actividades.md`**: Taller práctico con:
  - Materiales de fácil acceso
  - Instrucciones paso a paso
  - Preguntas evaluativas
  - Clave de respuestas

- **`metadatos.txt`**: Información clasificatoria del contenido

- **`contenido_completo.txt`**: Todas las secciones juntas

## 🎨 Estructura del Proyecto

```
Generador-de-Contenidos-Educativos/
├── app.py                          # Interfaz web Streamlit
├── scripts/
│   └── generador_contenido.py     # Lógica de generación
├── templates/
│   └── ejemplo_output.txt         # Ejemplo de salida
├── recursos/
│   └── hero_image.png             # Imagen hero de la interfaz
├── output/                        # Contenidos generados
├── requirements.txt               # Dependencias Python
├── INICIO_RAPIDO.md              # Guía rápida
└── README.md                      # Este archivo
```

## 🌟 Ejemplos de Temas

### Ciencias Naturales
- El ciclo del agua
- La fotosíntesis
- Ecosistemas colombianos
- El sistema solar
- Estados de la materia

### Matemáticas
- Fracciones
- Geometría básica
- Álgebra elemental
- Probabilidad

### Ciencias Sociales
- Regiones de Colombia
- Geografía colombiana
- Historia de Colombia
- Constitución política

## 💡 Características de la Interfaz

- **Diseño UNOi-inspired**: Interfaz moderna con color verde esmeralda (#00a884)
- **Sidebar negra**: Configuración y ejemplos de temas
- **Cards limpias**: Contenedores blancos con sombras sutiles
- **Tabs organizadas**: Navegación clara entre secciones
- **Responsive**: Se adapta a diferentes tamaños de pantalla
- **Badges informativos**: Muestra características del contenido generado

## 🔧 Tecnologías

- **Backend**: Python 3.8+
- **IA**: Google Gemini 1.5 Pro
- **Interfaz**: Streamlit
- **Visualización**: Mermaid.js
- **Tipografía**: Montserrat (Google Fonts)

## 📝 Licencia

Este proyecto está desarrollado para apoyar la educación colombiana.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 👨‍💻 Autor

**Sumercesito**

Desarrollado con ❤️ para la educación colombiana 🇨🇴

## 🙏 Agradecimientos

- Ministerio de Educación de Colombia por los DBA
- Google Gemini por la API de IA
- Comunidad educativa colombiana

---

**Sumercesito | Alineado con DBA Colombia**
