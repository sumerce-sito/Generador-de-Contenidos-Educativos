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
        
        prompt = f"""Genera contenido educativo sobre "{tema}" para grado {grado}.

FORMATO OBLIGATORIO - Copia exactamente esta estructura:

###SECTION_START: THEORIA###
[Escribe aquí contenido teórico denso de 1000+ palabras con: introducción contextualizando Colombia (2 párrafos), 4-5 secciones numeradas sobre {tema} (cada una con: definición, fundamento científico, 3+ ejemplos colombianos específicos con ubicaciones y datos cuantitativos), cierre sobre importancia para Colombia, DBA citado y competencias]
###SECTION_END###

###SECTION_START: VISUALIZACION###
---CODIGO_MERMAID_START---
[Código Mermaid.js válido tipo "graph TD" con 10-15 nodos sobre {tema}, con emojis y etiquetas en español]
---CODIGO_MERMAID_END---

---PROMPT_DALLE_START---
[Prompt en inglés de 100-150 palabras para DALL-E 3 describiendo ilustración educativa de {tema} con elementos colombianos, estilo "Educational illustration, vibrant colors, Colombian context, 4k quality"]
---PROMPT_DALLE_END---
###SECTION_END###

###SECTION_START: ACTIVIDADES###
[Escribe: "## 🎨 [nombre actividad]", "**Objetivo:**" [objetivo], "### Materiales:" lista de 5 materiales fáciles en Colombia, "### Instrucciones:" 6 pasos numerados, "### 📝 Taller Evaluativo" con 6 preguntas variadas, "### ✅ Clave:" 6 respuestas]
###SECTION_END###

###SECTION_START: METADATOS###
[Escribe: "**Título:**" [título], "**Grado:** {grado}", "**Área:**" [área], "**Fecha:** {datetime.now().strftime("%Y-%m-%d")}", "**Palabras clave:**" [5 keywords]]
###SECTION_END###

IMPORTANTE: NO escribas "Aquí tienes...", solo empieza directamente con ###SECTION_START: THEORIA###"""

        try:
            response = self.model.generate_content(prompt)
            contenido = response.text
            
            # Debug
            try:
                debug_path = os.path.join(os.path.dirname(__file__), "..", "debug_raw.txt")
                with open(debug_path, "w", encoding="utf-8") as f:
                    f.write("=== CONTENIDO CRUDO DE GEMINI ===\n\n")
                    f.write(contenido)
                    f.write("\n\n=== FIN CONTENIDO ===")
                print(f"\n[DEBUG] Contenido crudo guardado en: {debug_path}")
            except Exception as e:
                print(f"[DEBUG] Error guardando debug: {e}")
            
            return contenido
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
                print(f"[DEBUG] No se encontró la sección {seccion}")
                print(f"[DEBUG] Buscando: '{inicio}'")
        
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
                print("[DEBUG] No se encontró código Mermaid")
            
            # Extraer prompt DALL-E
            try:
                dalle_start = vis_content.index("---PROMPT_DALLE_START---") + len("---PROMPT_DALLE_START---")
                dalle_end = vis_content.index("---PROMPT_DALLE_END---")
                secciones['DALLE_PROMPT'] = vis_content[dalle_start:dalle_end].strip()
            except ValueError:
                secciones['DALLE_PROMPT'] = "Error: Prompt DALL-E no encontrado"
                print("[DEBUG] No se encontró prompt DALL-E")
        
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
