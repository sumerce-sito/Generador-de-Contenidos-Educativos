# 🚀 Guía de Inicio Rápido

## Paso 1: Instalar Dependencias

```bash
cd "d:\APP COLEGIOS 2026"
pip install -r requirements.txt
```

## Paso 2: Obtener API Key de Google Gemini

1. Ve a: https://makersuite.google.com/app/apikey
2. Crea o inicia sesión con tu cuenta de Google
3. Haz clic en "Create API Key"
4. Copia tu API Key (guárdala en un lugar seguro)

## Paso 3: Ejecutar el Generador

### Opción A: Modo Interactivo (Recomendado)

```bash
cd scripts
python generador_contenido.py
```

El programa te preguntará:
1. Tu API Key de Gemini
2. El tema educativo (ej: "El ciclo del agua")
3. El grado (ej: "4°")

### Opción B: Modo Programático

Crea un archivo `mi_generador.py`:

```python
from scripts.generador_contenido import GeneradorContenidoEducativo

# Tu API Key
API_KEY = "tu-api-key-aqui"

# Inicializar
gen = GeneradorContenidoEducativo(api_key=API_KEY)

# Generar contenido
contenido = gen.generar_contenido(
    tema="La fotosíntesis",
    grado="5°"
)

# Parsear y guardar
secciones = gen.parsear_contenido(contenido)
gen.guardar_contenido(secciones, "La fotosíntesis", "5°")
```

## Paso 4: Ver Resultados

Los archivos generados estarán en:
```
output/
└── 5°_La_fotosíntesis/
    ├── contenido_completo.txt
    ├── teoria.md
    ├── actividades.md
    ├── metadatos.txt
    ├── diagrama.mmd
    └── prompt_dalle.txt
```

## Paso 5: Usar los Diagramas Mermaid

1. Abre el archivo `diagrama.mmd`
2. Copia el contenido
3. Ve a: https://mermaid.live
4. Pega el código y visualiza/exporta

## Paso 6: Generar Imágenes con DALL-E

1. Abre el archivo `prompt_dalle.txt`
2. Copia el prompt
3. Úsalo en:
   - OpenAI (si tienes cuenta)
   - Microsoft Designer: https://designer.microsoft.com
   - Bing Image Creator

## 📝 Ejemplos de Temas por Grado

### Grado 3°
- "Los seres vivos y su entorno"
- "Los estados de la materia"
- "Las plantas y sus partes"

### Grado 4°
- "El ciclo del agua"
- "Fuentes de energía"
- "El sistema solar"

### Grado 5°
- "La fotosíntesis"
- "Ecosistemas colombianos"
- "La célula"

### Grado 6°-7°
- "La tabla periódica"
- "Biomas de Colombia"
- "Cambio climático"

### Grado 8°-9°
- "Reacciones químicas"
- "Genética básica"
- "Física: movimiento y fuerza"

### Grado 10°-11°
- "Biodiversidad colombiana"
- "Evolución"
- "Energías renovables en Colombia"

## ⚠️ Notas Importantes

1. **API Key**: Nunca compartas tu API Key. El archivo `.gitignore` ya está configurado para protegerla.

2. **Límites de la API**: Google Gemini tiene límites de uso gratuito. Revisa tu cuota en: https://makersuite.google.com

3. **Internet**: Necesitas conexión a internet para generar contenido.

4. **DBA**: El contenido generado se alinea automáticamente con los DBA de Colombia.

## 🆘 Solución de Problemas

### Error: "API Key inválida"
- Verifica que copiaste la API Key completa
- Asegúrate de que la API Key esté activa en Google AI Studio

### Error: "Module not found"
- Ejecuta: `pip install -r requirements.txt`

### El contenido no se genera
- Verifica tu conexión a internet
- Revisa que tienes cuota disponible en tu API Key

## 📧 Soporte

Si encuentras problemas, revisa:
1. El archivo `README.md` para documentación completa
2. El archivo `templates/ejemplo_output.txt` para ver un ejemplo
3. Los DBA oficiales: https://www.colombiaaprende.edu.co

---

**¡Listo para crear contenido educativo de calidad! 🎓📚**
