"""
Generador de Contenidos Educativos - Alineado con DBA Colombia  
Desarrollado para crear contenido instruccional estructurado
"""

import os
from datetime import datetime
from typing import Dict
import google.genai as genai


class GeneradorContenidoEducativo:
    def __init__(self, api_key: str = None):
        """Inicializa el generador con la API de Gemini"""
        if api_key:
            self.client = genai.Client(api_key=api_key)
        self.model_id = 'gemini-1.5-flash'

        
    def generar_contenido(self, tema: str, grado: str) -> str:
        """
        Genera contenido educativo estructurado según el template
        
        Args:
            tema: El tema educativo a desarrollar
            grado: El grado escolar (ej: "3°", "5°", "9°")
            
        Returns:
            str: Contenido formateado con delimitadores exactos
        """
        
        prompt = f"""Genera contenido educativo sobre "{tema}" para grado {grado} siguiendo EXACTAMENTE este formato:

###SECTION_START: THEORIA###
Escribe contenido teórico detallado (mínimo 800 palabras) sobre {tema}. Incluye:
- Introducción de 2 párrafos contextualizando para Colombia
- 4-5 conceptos principales numerados (### 1. Título, ### 2. Título, etc.)
- Para cada concepto: definición, fundamento científico, y 3+ ejemplos colombianos con ubicaciones específicas
- Cierre sobre la importancia para Colombia
- DBA citado entre comillas y lista de competencias desarrolladas
###SECTION_END###

###SECTION_START: VISUALIZACION###
---CODIGO_MERMAID_START---
graph TD
    A[Inicio] --> B[Paso 2]
    B --> C[Paso 3]
    (Genera aquí un diagrama Mermaid válido tipo "graph TD" con 10-15 nodos sobre {tema}, usando emojis y etiquetas en español)
---CODIGO_MERMAID_END---

---PROMPT_DALLE_START---
Educational illustration showing {tema} in Colombian context. Include specific Colombian landscapes, vibrant colors, child-friendly style, 4k quality.
(Genera aquí un prompt en inglés de 100-150 palabras para DALL-E 3)
---PROMPT_DALLE_END---
###SECTION_END###

###SECTION_START: ACTIVIDADES###
## 🎨 [Nombre creativo de la actividad sobre {tema}]

**Objetivo:** [Objetivo claro de aprendizaje]

### Materiales:
- Material 1
- Material 2
- Material 3
- Material 4
- Material 5

### Instrucciones:
1. Paso 1
2. Paso 2
3. Paso 3
4. Paso 4
5. Paso 5
6. Paso 6

### 📝 Taller Evaluativo
1. Pregunta 1
2. Pregunta 2
3. Pregunta 3
4. Pregunta 4
5. Pregunta 5

### ✅ Clave de Respuestas:
1. Respuesta 1
2. Respuesta 2
3. Respuesta 3
4. Respuesta 4
5. Respuesta 5
###SECTION_END###

###SECTION_START: METADATOS###
**Título:** [Título sobre {tema}]
**Grado:** {grado}
**Área:** [Ciencias/Matemáticas/Sociales]
**Fecha:** {datetime.now().strftime("%Y-%m-%d")}
**Palabras clave:** [keyword1, keyword2, keyword3, keyword4, keyword5]
###SECTION_END###

CRÍTICO: Empieza tu respuesta directamente con ###SECTION_START: THEORIA### (sin introducción como "Aquí está...")"""

        import time

        try:
            # Función auxiliar para intentar generar con retries
            def intentar_generar(modelo, intentos=3):
                for i in range(intentos):
                    try:
                        print(f"[DEBUG] Intentando con modelo {modelo} (Intento {i+1}/{intentos})...")
                        return self.client.models.generate_content(
                            model=modelo,
                            contents=prompt
                        )
                    except Exception as e:
                        error_str = str(e)
                        if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                            if i < intentos - 1:
                                wait_time = 10 * (i + 1)
                                print(f"[DEBUG] Cuota excedida. Esperando {wait_time}s para reintentar...")
                                time.sleep(wait_time)
                                continue
                        raise e

            # Intentar generar con el modelo principal
            try:
                response = intentar_generar(self.model_id)
            except Exception as e1:
                print(f"[DEBUG] Falló modelo principal {self.model_id}: {e1}")
                # Fallback a gemini-2.0-flash si falla
                try:
                    print(f"[DEBUG] Intentando fallback con gemini-2.0-flash...")
                    response = intentar_generar('gemini-2.0-flash')
                except Exception as e2:
                    return f"Error: Límite de cuota excedido o modelo no disponible. Por favor espera 1 minuto e intenta de nuevo. Detalle: {e2}"
                
            contenido = response.text

            
            # Debug - guardar contenido raw
            try:
                debug_path = os.path.join(os.path.dirname(__file__), "..", "debug_raw.txt")
                with open(debug_path, "w", encoding="utf-8") as f:
                    f.write("=== CONTENIDO CRUDO DE GEMINI ===\n\n")
                    f.write(contenido)
                    f.write("\n\n=== FIN CONTENIDO ===")
                # Print safe for ascii terminals
                try:
                    print(f"\n[DEBUG] Contenido crudo guardado".encode('utf-8', errors='ignore').decode('utf-8'))
                except:
                    pass
            except Exception:
                pass 
            
            return contenido
        except Exception as e:
            return f"Error al generar contenido: {str(e)}"
    
    def parsear_contenido(self, contenido: str) -> Dict[str, str]:
        """
        Parsea el contenido generado en secciones con estrategia flexible
        
        Args:
            contenido: String con el contenido completo generado
            
        Returns:
            Dict con las secciones parseadas
        """
        import re
        secciones = {}
        
        # Estrategia 1: Intentar con delimitadores exactos
        secciones_nombres = ['THEORIA', 'VISUALIZACION', 'ACTIVIDADES', 'METADATOS']
        
        for seccion in secciones_nombres:
            inicio = f"###SECTION_START: {seccion}###"
            fin = "###SECTION_END###"
            
            try:
                start_idx = contenido.index(inicio) + len(inicio)
                end_idx = contenido.index(fin, start_idx)
                secciones[seccion] = contenido[start_idx:end_idx].strip()
                print(f"[DEBUG] ✓ Sección {seccion} encontrada con delimitadores exactos")
            except ValueError:
                # Estrategia 2: Buscar con regex más flexible
                pattern = rf"###\s*SECTION[_\s]*START\s*:\s*{seccion}\s*###(.*?)###\s*SECTION[_\s]*END\s*###"
                match = re.search(pattern, contenido, re.DOTALL | re.IGNORECASE)
                
                if match:
                    secciones[seccion] = match.group(1).strip()
                    print(f"[DEBUG] ✓ Sección {seccion} encontrada con regex flexible")
                else:
                    # Estrategia 3: Buscar por palabras clave comunes
                    if seccion == 'THEORIA':
                        # Buscar contenido entre inicio y primera actividad o mermaid
                        pattern_theoria = r"(?:teoría|theory|contenido teórico)(.*?)(?:###|actividad|mermaid|visualización)"
                        match = re.search(pattern_theoria, contenido, re.DOTALL | re.IGNORECASE)
                        if match:
                            secciones[seccion] = match.group(1).strip()
                            print(f"[DEBUG] ⚠ Sección {seccion} recuperada por palabras clave")
                        else:
                            secciones[seccion] = f"Error: Sección {seccion} no encontrada"
                            print(f"[DEBUG] ✗ Sección {seccion} NO encontrada")
                    else:
                        secciones[seccion] = f"Error: Sección {seccion} no encontrada"
                        print(f"[DEBUG] ✗ Sección {seccion} NO encontrada")
        
        # Parsear subsecciones de VISUALIZACION con flexibilidad
        if 'VISUALIZACION' in secciones and not secciones['VISUALIZACION'].startswith('Error'):
            vis_content = secciones['VISUALIZACION']
            
            # Extraer código Mermaid con regex flexible
            try:
                # Intentar delimitadores exactos primero
                mermaid_start = vis_content.index("---CODIGO_MERMAID_START---") + len("---CODIGO_MERMAID_START---")
                mermaid_end = vis_content.index("---CODIGO_MERMAID_END---")
                secciones['MERMAID'] = vis_content[mermaid_start:mermaid_end].strip()
            except ValueError:
                # Buscar con regex
                pattern_mermaid = r"(?:---\s*(?:CODIGO_)?MERMAID[_\s]*START\s*---)(.*?)(?:---\s*(?:CODIGO_)?MERMAID[_\s]*END\s*---)"
                match = re.search(pattern_mermaid, vis_content, re.DOTALL | re.IGNORECASE)
                if match:
                    secciones['MERMAID'] = match.group(1).strip()
                else:
                    # Buscar cualquier código que parezca mermaid
                    pattern_graph = r"(graph\s+(?:TD|LR|TB|RL).*?)(?:---|###|$)"
                    match = re.search(pattern_graph, vis_content, re.DOTALL | re.IGNORECASE)
                    if match:
                        secciones['MERMAID'] = match.group(1).strip()
                    else:
                        secciones['MERMAID'] = "Error: Código Mermaid no encontrado"
            
            # Extraer prompt DALL-E con regex flexible
            try:
                dalle_start = vis_content.index("---PROMPT_DALLE_START---") + len("---PROMPT_DALLE_START---")
                dalle_end = vis_content.index("---PROMPT_DALLE_END---")
                secciones['DALLE_PROMPT'] = vis_content[dalle_start:dalle_end].strip()
            except ValueError:
                pattern_dalle = r"(?:---\s*(?:PROMPT_)?DALLE[_\s]*START\s*---)(.*?)(?:---\s*(?:PROMPT_)?DALLE[_\s]*END\s*---)"
                match = re.search(pattern_dalle, vis_content, re.DOTALL | re.IGNORECASE)
                if match:
                    secciones['DALLE_PROMPT'] = match.group(1).strip()
                else:
                    # Buscar cualquier prompt en inglés después de mermaid
                    pattern_eng = r"(?:prompt|dall-e|image)[\s:]*([A-Z][^#]*?(?:illustration|background|style|quality)[^#]*)"
                    match = re.search(pattern_eng, vis_content, re.IGNORECASE)
                    if match:
                        secciones['DALLE_PROMPT'] = match.group(1).strip()
                    else:
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
