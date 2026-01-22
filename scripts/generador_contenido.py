"""
Generador de Contenidos Educativos - Alineado con DBA Colombia
Desarrollado para crear contenido instruccional estructurado
"""

import os
from datetime import datetime
from typing import Dict
import google.generativeai as genai


class GeneradorContenidoEducativo:
    def __init__(self, api_key: str = None):
        """Inicializa el generador con la API de Gemini"""
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        
    def generar_contenido(self, tema: str, grado: str) -> str:
        """
        Genera contenido educativo estructurado según el template
        
        Args:
            tema: El tema educativo a desarrollar
            grado: El grado escolar (ej: "3°", "5°", "9°")
            
        Returns:
            str: Contenido formateado con delimitadores exactos
        """
        
        prompt = f"""# ROLE
Actúa como un Experto en Diseño Instruccional de Colombia y Desarrollador de Contenidos Digitales. Tu salida será procesada por un script de Python, por lo que la estructura debe ser MILIMÉTRICA.

# INPUT PARAMS
- Tema: {tema}
- Grado: {grado}

# REGLAS DE ORO PARA LA SALIDA
1. NO escribas introducciones (ej: "Aquí tienes...") ni despedidas.
2. Usa estrictamente los delimitadores de sección: ###SECTION_START: [NOMBRE]### y ###SECTION_END###.
3. El contenido debe estar alineado a los Derechos Básicos de Aprendizaje (DBA) de Colombia.
4. El contenido teórico debe ser DENSO, DETALLADO y PROFUNDO, apropiado para el nivel educativo.

---

###SECTION_START: THEORIA###
[INSTRUCCIONES DETALLADAS PARA LA TEORÍA:]

1. INTRODUCCIÓN (1-2 párrafos):
   - Contextualiza el tema y su importancia
   - Menciona la relevancia para Colombia

2. DESARROLLO PROFUNDO (mínimo 4-6 secciones numeradas):
   Para CADA concepto principal:
   - Título descriptivo con numeración
   - Definición científica precisa
   - **Fundamento científico:** Explicación de los principios subyacentes (física, química, biología según aplique)
   - **Ejemplos en Colombia:** Mínimo 3-4 ejemplos específicos de DIFERENTES regiones colombianas (Caribe, Pacífico, Andina, Amazonía, Orinoquía)
   - Para cada ejemplo, incluye: ubicación específica, datos concretos (temperatura, medidas, estadísticas), fenómenos observables
   - **Dato importante:** Estadística o fact relevante de Colombia

3. PROFUNDIDAD REQUERIDA:
   - Usa vocabulario técnico apropiado para el grado (pero siempre explicado)
   - Incluye cifras, datos cuantitativos, comparaciones
   - Menciona procesos, causas, consecuencias
   - Relaciona conceptos entre sí
   - Total: mínimo 800-1200 palabras para primaria, 1500-2000 para secundaria

4. CONEXIÓN CON COLOMBIA:
   - Nombres de departamentos, ciudades, ecosistemas, ríos, montañas
   - Culturas indígenas relevantes si aplica
   - Industrias, economía local relacionada  
   - Biodiversidad o geografía específica

5. CIERRE:
   - Resumen de la importancia del tema para Colombia
   - Relación con la vida cotidiana

6. DBA:
   - Cita el DBA específico entre comillas
   - Añade "Competencias desarrolladas:" con 3-4 items

FORMATO: Usa markdown con headers (##, ###), negrillas (**texto**), listas con guiones, y separadores (---) entre secciones principales.

###SECTION_END###

###SECTION_START: VISUALIZACION###
---CODIGO_MERMAID_START---
[Genera un código Mermaid.js COMPLETO y válido (graph TD o flowchart) con:
- Mínimo 10-15 nodos
- Incluye emojis en los nodos para hacerlo visual
- Etiquetas en español
- Conexiones que muestren el proceso/relación
- Usa styling con fill/color si es apropiado]
---CODIGO_MERMAID_END---

---PROMPT_DALLE_START---
[Prompt detallado en inglés para DALL-E 3 (100-150 palabras):
- Describe la escena con elementos colombianos (paisajes, personas, flora/fauna)
- Estilo: "Educational illustration, vibrant colors, child-friendly" (para primaria) o "Professional educational diagram, scientific accuracy" (para secundaria)
- Especifica qué elementos visuales incluir
- Menciona "Colombian context" explícitamente
- Termina con: "4k quality, clean background"]
---PROMPT_DALLE_END---
###SECTION_END###

###SECTION_START: ACTIVIDADES###
[ESTRUCTURA OBLIGATORIA:]

## 🎨 [Nombre creativo de la actividad]

**Objetivo:** [Qué aprenderá el estudiante]

### Materiales (TODOS de fácil acceso en Colombia):
- [Lista de 5-8 materiales con nombres locales]
- [Preferir materiales reciclados o de bajo costo]

### Instrucciones (paso a paso):
1. [Paso 1 muy específico]
2. [Paso 2...]
[...mínimo 6-8 pasos]

### Tiempo estimado: [X minutos]

### 📝 Taller Evaluativo

[Mínimo 5-7 preguntas variadas:]
- 2-3 de comprensión/definición
- 2-3 de aplicación (problemas, situaciones)  
- 1-2 de reflexión o relación con Colombia

### ✅ Clave de Respuestas:
1. [Respuesta detallada]
2. [...]

###SECTION_END###

###SECTION_START: METADATOS###
**Título de la Unidad:** [Nombre descriptivo]
**Grado Sugerido:** {grado}
**Área:** [Ciencias Naturales/Matemáticas/Sociales/etc]
**Eje Temático:** [Según DBA]
**Duración estimada:** [X horas de clase]
**Fecha de Creación:** {datetime.now().strftime("%Y-%m-%d")}
**Palabras clave:** [5-6 palabras separadas por comas]
**Región(es) de Colombia mencionadas:** [Lista]
###SECTION_END###"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error al generar contenido: {str(e)}"
    
    def parsear_contenido(self, contenido: str) -> Dict[str, str]:
        """
        Parsea el contenido generado en secciones
        
        Args:
            contenido: String con el contenido completo generado
            
        Returns:
            Dict con las secciones parseadas
        """
        secciones = {}
        
        # Parsear cada sección
        secciones_nombres = ['THEORIA', 'VISUALIZACION', 'ACTIVIDADES', 'METADATOS']
        
        for seccion in secciones_nombres:
            inicio = f"###SECTION_START: {seccion}###"
            fin = "###SECTION_END###"
            
            try:
                start_idx = contenido.index(inicio) + len(inicio)
                end_idx = contenido.index(fin, start_idx)
                secciones[seccion] = contenido[start_idx:end_idx].strip()
            except ValueError:
                secciones[seccion] = f"Error: Sección {seccion} no encontrada"
        
        # Parsear subsecciones de VISUALIZACION
        if 'VISUALIZACION' in secciones:
            vis_content = secciones['VISUALIZACION']
            
            # Extraer código Mermaid
            try:
                mermaid_start = vis_content.index("---CODIGO_MERMAID_START---") + len("---CODIGO_MERMAID_START---")
                mermaid_end = vis_content.index("---CODIGO_MERMAID_END---")
                secciones['MERMAID'] = vis_content[mermaid_start:mermaid_end].strip()
            except ValueError:
                secciones['MERMAID'] = "Error: Código Mermaid no encontrado"
            
            # Extraer prompt DALL-E
            try:
                dalle_start = vis_content.index("---PROMPT_DALLE_START---") + len("---PROMPT_DALLE_START---")
                dalle_end = vis_content.index("---PROMPT_DALLE_END---")
                secciones['DALLE_PROMPT'] = vis_content[dalle_start:dalle_end].strip()
            except ValueError:
                secciones['DALLE_PROMPT'] = "Error: Prompt DALL-E no encontrado"
        
        return secciones
    
    def guardar_contenido(self, secciones: Dict[str, str], tema: str, grado: str, output_dir: str = "../output"):
        """
        Guarda el contenido parseado en archivos separados
        
        Args:
            secciones: Diccionario con las secciones parseadas
            tema: Nombre del tema
            grado: Grado escolar
            output_dir: Directorio de salida
        """
        # Crear nombre de carpeta seguro
        nombre_limpio = tema.replace(" ", "_").replace("/", "-")
        carpeta_tema = os.path.join(output_dir, f"{grado}_{nombre_limpio}")
        
        os.makedirs(carpeta_tema, exist_ok=True)
        
        # Guardar contenido completo
        with open(os.path.join(carpeta_tema, "contenido_completo.txt"), "w", encoding="utf-8") as f:
            for seccion, contenido in secciones.items():
                f.write(f"\n{'='*80}\n")
                f.write(f"SECCIÓN: {seccion}\n")
                f.write(f"{'='*80}\n\n")
                f.write(contenido)
                f.write("\n\n")
        
        # Guardar secciones individuales
        with open(os.path.join(carpeta_tema, "teoria.md"), "w", encoding="utf-8") as f:
            f.write(secciones.get('THEORIA', ''))
        
        with open(os.path.join(carpeta_tema, "actividades.md"), "w", encoding="utf-8") as f:
            f.write(secciones.get('ACTIVIDADES', ''))
        
        with open(os.path.join(carpeta_tema, "metadatos.txt"), "w", encoding="utf-8") as f:
            f.write(secciones.get('METADATOS', ''))
        
        with open(os.path.join(carpeta_tema, "diagrama.mmd"), "w", encoding="utf-8") as f:
            f.write(secciones.get('MERMAID', ''))
        
        with open(os.path.join(carpeta_tema, "prompt_dalle.txt"), "w", encoding="utf-8") as f:
            f.write(secciones.get('DALLE_PROMPT', ''))
        
        print(f"\n✓ Contenido guardado en: {carpeta_tema}")
        return carpeta_tema


def main():
    """Función principal para uso interactivo"""
    print("="*80)
    print("GENERADOR DE CONTENIDOS EDUCATIVOS - COLOMBIA DBA")
    print("="*80)
    
    # Solicitar API key
    api_key = input("\nIngresa tu API Key de Google Gemini: ").strip()
    if not api_key:
        print("Error: API Key requerida")
        return
    
    generador = GeneradorContenidoEducativo(api_key)
    
    # Solicitar tema y grado
    tema = input("\nIngresa el tema educativo: ").strip()
    grado = input("Ingresa el grado (ej: 3°, 5°, 9°): ").strip()
    
    print(f"\n🔄 Generando contenido para: {tema} - Grado {grado}")
    print("⏳ Esto puede tomar unos momentos...\n")
    
    # Generar contenido
    contenido = generador.generar_contenido(tema, grado)
    
    # Parsear contenido
    secciones = generador.parsear_contenido(contenido)
    
    # Guardar contenido
    carpeta = generador.guardar_contenido(secciones, tema, grado)
    
    print("\n" + "="*80)
    print("✅ GENERACIÓN COMPLETADA")
    print("="*80)
    print(f"\nArchivos creados:")
    print(f"  📁 {carpeta}/")
    print(f"    📄 contenido_completo.txt")
    print(f"    📄 teoria.md")
    print(f"    📄 actividades.md")
    print(f"    📄 metadatos.txt")
    print(f"    📄 diagrama.mmd")
    print(f"    📄 prompt_dalle.txt")


if __name__ == "__main__":
    main()
