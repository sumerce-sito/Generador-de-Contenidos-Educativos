<<<<<<< HEAD
"""
🎓 GENERADOR DE CONTENIDOS EDUCATIVOS COLOMBIA
Interfaz inspirada en UNOi Colombia
Sistema de diseño instruccional alineado con DBA
"""

import streamlit as st
import sys
import os
import base64
from pathlib import Path
from datetime import datetime

# Agregar scripts al path
sys.path.append(str(Path(__file__).parent / "scripts"))

from generador_contenido import GeneradorContenidoEducativo

# Función para cargar imagen como base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# ==================== CONFIGURACIÓN DE PÁGINA ====================
st.set_page_config(
    page_title="Generador Educativo Colombia 🇨🇴",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Cargar imagen hero en base64
hero_image_path = Path(__file__).parent / "recursos" / "hero_image.png"
hero_image_base64 = get_base64_image(str(hero_image_path))

# ==================== ESTILOS UNOi-INSPIRED ====================
css_styles = f"""
<style>
    /* Importar fuente moderna similar a UNOi */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');
    
    /* Paleta de colores UNOi */
    :root {{
        --unoi-green: #00a884;
        --unoi-green-hover: #008c6e;
        --unoi-black: #000000;
        --unoi-white: #ffffff;
        --unoi-purple: #8b5cf6;
        --unoi-gradient: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
        --card-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
    }}
</style>
"""

st.markdown(css_styles, unsafe_allow_html=True)
st.markdown("""
<style>
        background-position: center;
        padding: 4rem 2rem;
        margin: -2rem -2rem 2rem -2rem;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320"><path fill="rgba(255,255,255,0.05)" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,154.7C960,171,1056,181,1152,165.3C1248,149,1344,107,1392,85.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') no-repeat bottom;
        background-size: cover;
        opacity: 0.3;
        z-index: 0;
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--unoi-green);
        margin-bottom: 0.5rem;
        text-align: center;
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.1rem;
        font-weight: 500;
        text-align: center;
        position: relative;
        z-index: 1;
    }
    
    /* Sidebar oscura estilo UNOi */
    section[data-testid="stSidebar"] {
        background: var(--unoi-black) !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    section[data-testid="stSidebar"] h3 {
        color: var(--unoi-green) !important;
        font-weight: 700;
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Inputs en sidebar */
    section[data-testid="stSidebar"] input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    section[data-testid="stSidebar"] input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Expanders en sidebar */
    section[data-testid="stSidebar"] .streamlit-expanderHeader {
        background: rgba(0, 168, 132, 0.1) !important;
        border: 1px solid rgba(0, 168, 132, 0.3) !important;
        color: var(--unoi-green) !important;
    }
    
    /* Cards estilo UNOi - limpias y modernas */
    .unoi-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--card-shadow);
        border: 1px solid #e9ecef;
        transition: all 0.3s ease;
    }
    
    .unoi-card:hover {
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    /* Títulos de sección */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--unoi-black);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .section-title::before {
        content: '';
        width: 4px;
        height: 30px;
        background: var(--unoi-green);
        border-radius: 2px;
    }
    
    /* Botón principal - Verde UNOi */
    .stButton > button {
        width: 100%;
        background: var(--unoi-green);
        color: white;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 168, 132, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: var(--unoi-green-hover);
        box-shadow: 0 6px 30px rgba(0, 168, 132, 0.4);
        transform: translateY(-2px);
    }
    
    .stButton > button:disabled {
        background: #cccccc;
        box-shadow: none;
        cursor: not-allowed;
    }
    
    /* Inputs modernos */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 12px;
        border: 2px solid #e9ecef;
        padding: 0.9rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: white;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--unoi-green);
        box-shadow: 0 0 0 3px rgba(0, 168, 132, 0.1);
        outline: none;
    }
    
    /* Labels */
    .stTextInput > label,
    .stSelectbox > label {
        font-weight: 700;
        color: var(--unoi-black);
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.85rem;
    }
    
    /* Tabs modernas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: white;
        border-radius: 12px;
        padding: 0.5rem;
        box-shadow: var(--card-shadow);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        color: #666;
        background: transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--unoi-green) !important;
        color: white !important;
    }
    
    /* Badges UNOi style */
    .unoi-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
        border: 2px solid;
    }
    
    .badge-green {
        background: rgba(0, 168, 132, 0.1);
        color: var(--unoi-green);
        border-color: var(--unoi-green);
    }
    
    .badge-purple {
        background: rgba(139, 92, 246, 0.1);
        color: var(--unoi-purple);
        border-color: var(--unoi-purple);
    }
    
    /* Info boxes */
    .stSuccess {
        background: rgba(0, 168, 132, 0.1);
        border-left: 4px solid var(--unoi-green);
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stInfo {
        background: rgba(99, 102, 241, 0.1);
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Spinner UNOi verde */
    .stSpinner > div {
        border-top-color: var(--unoi-green) !important;
    }
    
    /* Animaciones suaves */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Métricas */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: var(--card-shadow);
    }
    
    .stMetric label {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 600;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: var(--unoi-green) !important;
        font-size: 2rem !important;
        font-weight: 800;
    }
    
    /* Download buttons */
    .stDownloadButton > button {
        background: white;
        color: var(--unoi-green);
        border: 2px solid var(--unoi-green);
        border-radius: 12px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background: var(--unoi-green);
        color: white;
    }
    
    /* Code blocks */
    .stCodeBlock {
        border-radius: 12px;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INICIALIZACIÓN DE SESSION STATE ====================
if 'generador' not in st.session_state:
    st.session_state.generador = None
if 'contenido_generado' not in st.session_state:
    st.session_state.contenido_generado = None
if 'secciones' not in st.session_state:
    st.session_state.secciones = None
if 'tema_actual' not in st.session_state:
    st.session_state.tema_actual = ""
if 'grado_actual' not in st.session_state:
    st.session_state.grado_actual = ""

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-section fade-in">
    <h1 class="hero-title">🎓 Generador de Contenidos Educativos</h1>
    <p class="hero-subtitle">Alineado con los Derechos Básicos de Aprendizaje (DBA) de Colombia 🇨🇴</p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<h3 style="margin-top: 2rem;">⚙️ Configuración</h3>', unsafe_allow_html=True)
    
    # API Key input
    api_key = st.text_input(
        "API Key de Google Gemini",
        type="password",
        help="Obtén tu API Key en https://makersuite.google.com",
        placeholder="Pega tu API Key aquí..."
    )
    
    if api_key:
        if st.session_state.generador is None:
            st.session_state.generador = GeneradorContenidoEducativo(api_key=api_key)
            st.success("✅ API Key configurada")
    
    st.markdown("---")
    
    st.markdown("### 📚 Ejemplos de Temas")
    
    with st.expander("🔬 Ciencias Naturales"):
        st.markdown("""
        - El ciclo del agua
        - La fotosíntesis
        - Ecosistemas colombianos
        - El sistema solar
        - Estados de la materia
        """)
    
    with st.expander("🔢 Matemáticas"):
        st.markdown("""
        - Fracciones
        - Geometría básica
        - Operaciones decimales
        - Álgebra elemental
        - Probabilidad
        """)
    
    with st.expander("🌎 Ciencias Sociales"):
        st.markdown("""
        - Regiones de Colombia
        - Cultura indígena
        - Geografía colombiana
        - Historia de Colombia
        - Constitución política
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Estadísticas")
    if st.session_state.contenido_generado:
        st.metric("Contenidos Generados", "1", delta="✓ Sesión actual")
    else:
        st.metric("Contenidos Generados", "0")
    
    st.markdown("---")
    st.markdown('<p style="font-size: 0.85rem; opacity: 0.7;">Sistema de diseño instruccional automatizado para crear contenido educativo de calidad alineado con los DBA de Colombia.</p>', unsafe_allow_html=True)

# ==================== CONTENIDO PRINCIPAL ====================

# Tabs principales
tab1, tab2, tab3 = st.tabs(["🎨 Generar Contenido", "📖 Contenido Generado", "📘 Guía de Uso"])

with tab1:
    # Formulario en card
    st.markdown('<div class="unoi-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📝 Datos del Contenido</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        tema = st.text_input(
            "Tema Educativo",
            placeholder="Ejemplo: El ciclo del agua",
            help="Ingresa el tema que deseas desarrollar",
            key="tema_input"
        )
    
    with col2:
        grado = st.selectbox(
            "Grado Escolar",
            ["", "1°", "2°", "3°", "4°", "5°", "6°", "7°", "8°", "9°", "10°", "11°"],
            help="Selecciona el grado al que va dirigido el contenido",
            key="grado_select"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón de generar
    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    if st.button("🚀 Generar Contenido Educativo", disabled=(not api_key or not tema or not grado), key="generate_btn"):
        if not api_key:
            st.warning("⚠️ Por favor, ingresa tu API Key de Google Gemini en la barra lateral")
        elif not tema or not grado:
            st.warning("⚠️ Por favor, completa todos los campos")
        else:
            with st.spinner("🎨 Generando contenido educativo de alta calidad... Esto puede tomar unos momentos."):
                try:
                    # Generar contenido
                    contenido = st.session_state.generador.generar_contenido(tema, grado)
                    st.session_state.contenido_generado = contenido
                    st.session_state.tema_actual = tema
                    st.session_state.grado_actual = grado
                    
                    # Parsear
                    secciones = st.session_state.generador.parsear_contenido(contenido)
                    st.session_state.secciones = secciones
                    
                    # Guardar
                    carpeta = st.session_state.generador.guardar_contenido(secciones, tema, grado, output_dir="output")
                    
                    st.success(f"✅ ¡Contenido generado exitosamente para {tema} - Grado {grado}!")
                    st.info(f"📁 Archivos guardados en: `{carpeta}`")
                    
                except Exception as e:
                    st.error(f"❌ Error al generar contenido: {str(e)}")
    
    # Botón demo
    if st.button("🎭 Ver Contenido de Demostración", key="demo_btn", type="secondary"):
        # Contenido demo pre-cargado
        st.session_state.tema_actual = "El Ciclo del Agua"
        st.session_state.grado_actual = "4°"
        
        st.session_state.secciones = {
            'THEORIA': """## 🌊 ¿Cómo circula el agua en la naturaleza colombiana?

El **ciclo hidrológico** o **ciclo del agua** es uno de los procesos naturales más importantes para la vida en nuestro planeta. Este ciclo representa el movimiento continuo del agua entre la atmósfera, la superficie terrestre y el subsuelo, garantizando la disponibilidad de este recurso vital para todos los seres vivos. Colombia, por su ubicación geográfica privilegiada en la zona ecuatorial y su diversidad de ecosistemas, presenta manifestaciones únicas de este ciclo en sus diferentes regiones.

### **1. Evaporación: El Comienzo del Viaje del Agua**

La **evaporación** es el proceso físico mediante el cual el agua en estado líquido se transforma en vapor de agua (estado gaseoso) debido al aumento de temperatura provocado por la radiación solar. Este fenómeno ocurre constantemente en océanos, ríos, lagos, lagunas y hasta en el suelo húmedo.

**Fundamento científico:** Cuando las moléculas de agua (H₂O) reciben energía térmica del sol, aumentan su velocidad de movimiento hasta romper los enlaces de hidrógeno que las mantienen unidas en estado líquido, permitiendo que escapen a la atmósfera en forma de vapor.

**Ejemplos en Colombia:**

- **Costas del Caribe (La Guajira):** En el desierto de la Tatacoa y las salinas de Manaure, las altas temperaturas (que pueden superar los 40°C) generan tasas de evaporación extremadamente elevadas. El agua del Mar Caribe se evapora constantemente, creando una fuente importante de humedad atmosférica.

- **Cuenca Amazónica:** Los ríos como el Caquetá, Putumayo y Amazonas aportan enormes volúmenes de agua que se evaporan debido a las temperaturas cálidas constantes (25-28°C) y la alta radiación solar ecuatorial. Se estima que la Amazonía aporta el 20% del vapor de agua atmosférico de Sudamérica.

- **Páramos Andinos:** En ecosistemas como el Páramo de Sumapaz y el Nevado del Ruiz, la evaporación es menor debido a las bajas temperaturas, pero las lagunas glaciares y los humedales contribuyen significativamente al ciclo local del agua.

- **Valle del Cauca:** Las plantaciones de caña de azúcar y los espejos de agua en las zonas de cultivo experimentan altas tasas de evaporación, especialmente durante la época seca.

**Dato importante:** Colombia cuenta con aproximadamente 720,000 km² de superficie hídrica continental, lo que representa una fuente masiva de evaporación.

### **2. Condensación: La Formación de las Nubes**

La **condensación** es el proceso inverso a la evaporación, donde el vapor de agua se enfría y regresa al estado líquido, formando pequeñas gotas que se agrupan para crear las nubes. Este proceso ocurre cuando el aire cargado de humedad asciende a capas más altas y frías de la atmósfera.

**Fundamento científico:** Cuando el vapor de agua alcanza altitudes donde la temperatura es más baja (aproximadamente 6.5°C menos por cada 1,000 metros de altitud), las moléculas pierden energía cinética y se unen nuevamente, formando microgotas de agua alrededor de partículas microscópicas llamadas "núcleos de condensación" (polvo, sal marina, polen).

**Ejemplos en Colombia:**

- **Valle de Aburrá (Medellín):** La combinación de aire húmedo proveniente del Magdalena Medio y el enfriamiento nocturno en las montañas circundantes genera densas capas de nubes bajas que cubren la ciudad especialmente en las madrugadas. Este fenómeno es tan característico que afecta los patrones de temperatura diarios.

- **Sierra Nevada de Santa Marta:** Este macizo montañoso, que se eleva desde el nivel del mar hasta 5,775 metros en solo 42 km, crea un gradiente de condensación único. El aire húmedo del Caribe asciende por las laderas y se condensa constantemente, creando un cinturón de neblina permanente entre los 2,000 y 3,500 metros de altitud.

- **Llanos Orientales:** Durante la época de lluvias (abril a noviembre), las corrientes de aire húmedo provenientes de la Amazonía se encuentran con masas de aire más frío, generando formaciones nubosas masivas que pueden observarse desde gran distancia. Los llaneros conocen este fenómeno como "el invierno".

- **Región Andina:** Las tres cordilleras (Occidental, Central y Oriental) actúan como barreras naturales que fuerzan el ascenso del aire húmedo, provocando condensación continua. Esto explica por qué ciudades como Bogotá, Pasto y Manizales tienen cielos frecuentemente nublados.

**Dato importante:** Colombia tiene uno de los índices de nubosidad más altos del mundo, con un promedio de 60-70% de cobertura nubosa anual en la región Andina.

### **3. Precipitación: El Regreso del Agua a la Tierra**

La **precipitación** es la caída del agua desde las nubes hacia la superficie terrestre, manifestándose principalmente como lluvia, pero también como granizo, nieve o llovizna, dependiendo de las condiciones atmosféricas y la temperatura.

**Fundamento científico:** Cuando las gotas de agua en las nubes se fusionan y crecen hasta alcanzar un tamaño crítico (aproximadamente 5 mm de diámetro), vencen la resistencia del aire y caen por gravedad. En zonas con temperaturas bajo cero, el agua se congela formando cristales de hielo (nieve) o esferas de hielo (granizo).

**Ejemplos en Colombia:**

- **Chocó Biogeográfico:** Esta región es reconocida mundialmente como una de las más lluviosas del planeta. Municipios como Lloró y Tutunendo reciben entre 10,000 y 13,000 mm de lluvia al año (comparado con 1,000 mm en regiones secas). Las lluvias son casi diarias, creando el bosque húmedo tropical más biodiverso del mundo. Los vientos alisios del Pacífico chocan con la Cordillera Occidental, forzando el ascenso y condensación masiva de humedad.

- **Amazonía Colombiana:** Con precipitaciones de 3,000-4,000 mm anuales, la selva amazónica experimenta lluvias torrenciales casi diarias, especialmente en las tardes. Este patrón predecible se debe al calentamiento diurno que genera corrientes ascendentes de aire húmedo. La lluvia alimenta los grandes ríos que son vías fluviales esenciales para las comunidades indígenas.

- **Nevados de Los Andes:** El Nevado del Ruiz, Nevado del Tolima y Sierra Nevada del Cocuy experimentan precipitación en forma de nieve por encima de los 4,500 metros de altitud. Estas nieves perpetuas actúan como "torres de agua", almacenando agua sólida que se derrite gradualmente y alimenta ríos cruciales como el Magdalena y el Cauca.

- **Región Caribe semiárida:** La Guajira y parte de Cesar reciben menos de 500 mm de lluvia al año, creando ecosistemas de bosque seco y zonas desérticas. Este contraste con el Chocó demuestra la increíble variabilidad climática de Colombia en cortas distancias.

**Dato importante:** Colombia es el segundo país más lluvioso de Sudamérica después de Brasil, con un promedio nacional de 3,000 mm anuales.

### **4. Escorrentía y Filtración: El Camino del Agua Después de la Lluvia**

Una vez que el agua precipita, puede seguir dos caminos principales:

**Escorrentía superficial:** El agua fluye sobre la superficie del terreno formando arroyos, quebradas y ríos. Colombia tiene 5 grandes vertientes hidrográficas:
- Vertiente del Caribe (Magdalena, Cauca, Sinú, Atrato)
- Vertiente del Pacífico (San Juan, Patía, Baudó)
- Vertiente del Orinoco (Meta, Guaviare, Vichada)
- Vertiente del Amazonas (Caquetá, Putumayo, Vaupés)  
- Vertiente del Catatumbo (hacia el Lago de Maracaibo)

**Infiltración:** Parte del agua se filtra en el suelo, recargando acuíferos subterráneos. Los páramos colombianos son esenciales en este proceso, actuando como "esponjas naturales" que absorben agua de lluvia y la liberan gradualmente, regulando el caudal de los ríos durante todo el año.

### **Importancia del Ciclo del Agua para Colombia**

Colombia es uno de los países con mayor riqueza hídrica del mundo:
- **6to lugar mundial** en disponibilidad de agua dulce renovable
- **2,000 ríos** aproximadamente
- **1,600 lagunas** en ecosistemas de páramo
- **Más de 50 m³ de agua** por persona al día (promedio mundial: 7 m³)

Esta abundancia sostiene la agricultura (café, flores, caña), genera el 70% de la electricidad del país (hidroeléctricas) y mantiene ecosistemas únicos como los manglares del Pacífico y las ciénagas del Magdalena.

---

**DBA Relacionado (Grado 4°):** *"Comprende que los seres vivos (plantas, animales, hongos, bacterias) dependen del ciclo del agua y sus componentes (evaporación, condensación, precipitación, infiltración) para su supervivencia, y reconoce las adaptaciones de los organismos a las variaciones del ciclo en diferentes ecosistemas colombianos."*

**Competencias desarrolladas:**
- Explicar fenómenos naturales con base en evidencias científicas
- Relacionar procesos físicos con contextos regionales
- Valorar la riqueza hídrica nacional y su conservación""",
            
            'MERMAID': """graph TD
    A[☀️ Energía Solar] --> B[💧 Evaporación]
    B --> C[Ríos: Magdalena, Cauca]
    B --> D[Mar Caribe y Pacífico]
    C --> E[☁️ Vapor de Agua]
    D --> E
    E --> F[🌡️ Condensación]
    F --> G[☁️ Nubes sobre Andes]
    G --> H[🌧️ Precipitación]
    H --> I[Lluvia en el Chocó]
    H --> J[Nieve en Nevados]
    I --> C
    J --> C""",
            
            'DALLE_PROMPT': """Educational illustration of the water cycle in Colombian landscapes. Show Caribbean coast with water evaporating, clouds forming over Andes mountains, rain falling in Amazon rainforest, rivers flowing through valleys. Include Spanish labels: Evaporación, Condensación, Precipitación. Vibrant colors, child-friendly educational diagram style, warm sunny atmosphere.""",
            
            'ACTIVIDADES': """## 🎨 Actividad: Creando Nuestro Ciclo del Agua

**Objetivo:** Observar el ciclo del agua en un modelo a escala

### Materiales:
- 1 frasco de vidrio grande
- Agua
- Hielo
- 1 plato pequeño
- Papel aluminio

### Instrucciones:
1. Llena el frasco con 2 cm de agua
2. Coloca el plato pequeño boca abajo dentro
3. Cubre la boca con papel aluminio
4. Pon hielo sobre el aluminio
5. Deja al sol por 2 horas
6. Observa qué sucede

### 📝 Taller Evaluativo
1. ¿Qué pasa con el agua cuando la calientas?
2. ¿Por qué se forman gotitas en el aluminio?
3. Nombra 3 departamentos con mucha lluvia
4. ¿Dónde va el agua después de llover?
5. Dibuja el ciclo del agua""",
            
            'METADATOS': f"""**Título:** El Ciclo del Agua en Colombia
**Grado:** 4°
**Eje Temático:** Ciencias Naturales
**Fecha:** {datetime.now().strftime("%Y-%m-%d")}
**Región:** Nacional con ejemplos regionales"""
        }
        
        st.session_state.contenido_generado = "\n\n".join([
            f"=== {k} ===\n{v}" for k, v in st.session_state.secciones.items()
        ])
        
        st.success("✅ ¡Contenido demo cargado! Ve a la pestaña 'Contenido Generado' para verlo")
        st.info("💡 Esto es contenido de demostración. Para generar contenido personalizado, ingresa tu API Key.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Badges informativos
    st.markdown('<div class="unoi-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">✨ Características del Contenido</h2>', unsafe_allow_html=True)
    st.markdown("""
    <span class="unoi-badge badge-green">📚 Teoría con DBA</span>
    <span class="unoi-badge badge-green">🗺️ Ejemplos Colombianos</span>
    <span class="unoi-badge badge-green">📊 Diagramas Mermaid</span>
    <span class="unoi-badge badge-purple">🎨 Prompts DALL-E</span>
    <span class="unoi-badge badge-purple">✏️ Actividades Prácticas</span>
    <span class="unoi-badge badge-purple">📝 Taller Evaluativo</span>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if st.session_state.secciones:
        st.markdown(f'<h2 class="section-title">📖 {st.session_state.tema_actual} - Grado {st.session_state.grado_actual}</h2>', unsafe_allow_html=True)
        
        # Sub-tabs para cada sección
        sub_tab1, sub_tab2, sub_tab3, sub_tab4, sub_tab5 = st.tabs([
            "📚 Teoría", 
            "📊 Visualización", 
            "✏️ Actividades", 
            "📋 Metadatos",
            "💾 Descargar"
        ])
        
        with sub_tab1:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('THEORIA', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab2:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("#### 🗺️ Diagrama Mermaid")
            st.code(st.session_state.secciones.get('MERMAID', 'No disponible'), language='mermaid')
            st.info("💡 Visualiza este diagrama en: https://mermaid.live")
            
            st.markdown("---")
            
            st.markdown("#### 🎨 Prompt para DALL-E")
            st.code(st.session_state.secciones.get('DALLE_PROMPT', 'No disponible'), language='text')
            st.info("💡 Usa este prompt en OpenAI o Microsoft Designer")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab3:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('ACTIVIDADES', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab4:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('METADATOS', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab5:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("### 💾 Descargar Contenido")
            
            # Crear nombre de archivo limpio
            nombre_archivo = f"{st.session_state.grado_actual}_{st.session_state.tema_actual.replace(' ', '_')}"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📄 Descargar Contenido Completo (.txt)",
                    data=st.session_state.contenido_generado,
                    file_name=f"{nombre_archivo}_completo.txt",
                    mime="text/plain"
                )
            
            with col2:
                st.download_button(
                    label="📊 Descargar Diagrama Mermaid (.mmd)",
                    data=st.session_state.secciones.get('MERMAID', ''),
                    file_name=f"{nombre_archivo}_diagrama.mmd",
                    mime="text/plain"
                )
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Genera contenido en la pestaña 'Generar Contenido' para verlo aquí")

with tab3:
    st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 📘 Cómo Usar el Generador
    
    #### 1️⃣ Configurar API Key
    - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Crea o inicia sesión con tu cuenta de Google
    - Genera una nueva API Key
    - Pégala en el campo de la barra lateral
    
    #### 2️⃣ Ingresar Datos
    - **Tema**: El contenido educativo que deseas desarrollar (ej: "El ciclo del agua")
    - **Grado**: Selecciona el grado escolar (1° a 11°)
    
    #### 3️⃣ Generar Contenido
    - Haz clic en "🚀 Generar Contenido Educativo"
    - Espera unos momentos mientras la IA crea el contenido
    - El contenido se guardará automáticamente en la carpeta `output/`
    
    #### 4️⃣ Revisar y Descargar
    - Revisa cada sección en la pestaña "📖 Contenido Generado"
    - Descarga los archivos que necesites
    - Visualiza el diagrama Mermaid en [mermaid.live](https://mermaid.live)
    - Usa el prompt DALL-E para generar imágenes educativas
    
    ### 🎯 Secciones Incluidas
    
    ✅ **Teoría**: Contenido completo con contexto colombiano y DBA  
    ✅ **Visualización**: Diagramas Mermaid + Prompts para imágenes  
    ✅ **Actividades**: Talleres prácticos con materiales de fácil acceso  
    ✅ **Metadatos**: Información clasificatoria del contenido  
    
    ### 💡 Consejos
    
    - Sé específico con el tema para obtener mejores resultados
    - El contenido incluye ejemplos de regiones colombianas
    - Los materiales sugeridos son de fácil acceso en Colombia
    - Todo está alineado con los DBA oficiales
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; margin-top: 3rem;">
    <p style="font-weight: 600;">Desarrollado con ❤️ para la educación colombiana 🇨🇴</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Sumercesito | Alineado con DBA Colombia</p>
</div>
""", unsafe_allow_html=True)
=======
"""
🎓 GENERADOR DE CONTENIDOS EDUCATIVOS COLOMBIA
Interfaz inspirada en UNOi Colombia
Sistema de diseño instruccional alineado con DBA
"""

import streamlit as st
import sys
import os
import base64
from pathlib import Path
from datetime import datetime

# Agregar scripts al path
sys.path.append(str(Path(__file__).parent / "scripts"))

from generador_contenido import GeneradorContenidoEducativo

# Función para cargar imagen como base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# ==================== CONFIGURACIÓN DE PÁGINA ====================
st.set_page_config(
    page_title="Generador Educativo Colombia 🇨🇴",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Cargar imagen hero en base64
hero_image_path = Path(__file__).parent / "recursos" / "hero_image.png"
hero_image_base64 = get_base64_image(str(hero_image_path))

# ==================== ESTILOS UNOi-INSPIRED ====================
css_styles = f"""
<style>
    /* Importar fuente moderna similar a UNOi */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');
    
    /* Paleta de colores UNOi */
    :root {{
        --unoi-green: #00a884;
        --unoi-green-hover: #008c6e;
        --unoi-black: #000000;
        --unoi-white: #ffffff;
        --unoi-purple: #8b5cf6;
        --unoi-gradient: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
        --card-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
    }}
</style>
"""

st.markdown(css_styles, unsafe_allow_html=True)
st.markdown("""
<style>
        background-position: center;
        padding: 4rem 2rem;
        margin: -2rem -2rem 2rem -2rem;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320"><path fill="rgba(255,255,255,0.05)" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,154.7C960,171,1056,181,1152,165.3C1248,149,1344,107,1392,85.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') no-repeat bottom;
        background-size: cover;
        opacity: 0.3;
        z-index: 0;
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--unoi-green);
        margin-bottom: 0.5rem;
        text-align: center;
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.1rem;
        font-weight: 500;
        text-align: center;
        position: relative;
        z-index: 1;
    }
    
    /* Sidebar oscura estilo UNOi */
    section[data-testid="stSidebar"] {
        background: var(--unoi-black) !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    section[data-testid="stSidebar"] h3 {
        color: var(--unoi-green) !important;
        font-weight: 700;
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    /* Inputs en sidebar */
    section[data-testid="stSidebar"] input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    section[data-testid="stSidebar"] input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Expanders en sidebar */
    section[data-testid="stSidebar"] .streamlit-expanderHeader {
        background: rgba(0, 168, 132, 0.1) !important;
        border: 1px solid rgba(0, 168, 132, 0.3) !important;
        color: var(--unoi-green) !important;
    }
    
    /* Cards estilo UNOi - limpias y modernas */
    .unoi-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--card-shadow);
        border: 1px solid #e9ecef;
        transition: all 0.3s ease;
    }
    
    .unoi-card:hover {
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    /* Títulos de sección */
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--unoi-black);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .section-title::before {
        content: '';
        width: 4px;
        height: 30px;
        background: var(--unoi-green);
        border-radius: 2px;
    }
    
    /* Botón principal - Verde UNOi */
    .stButton > button {
        width: 100%;
        background: var(--unoi-green);
        color: white;
        border: none;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 168, 132, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: var(--unoi-green-hover);
        box-shadow: 0 6px 30px rgba(0, 168, 132, 0.4);
        transform: translateY(-2px);
    }
    
    .stButton > button:disabled {
        background: #cccccc;
        box-shadow: none;
        cursor: not-allowed;
    }
    
    /* Inputs modernos */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 12px;
        border: 2px solid #e9ecef;
        padding: 0.9rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: white;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--unoi-green);
        box-shadow: 0 0 0 3px rgba(0, 168, 132, 0.1);
        outline: none;
    }
    
    /* Labels */
    .stTextInput > label,
    .stSelectbox > label {
        font-weight: 700;
        color: var(--unoi-black);
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.85rem;
    }
    
    /* Tabs modernas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: white;
        border-radius: 12px;
        padding: 0.5rem;
        box-shadow: var(--card-shadow);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        color: #666;
        background: transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--unoi-green) !important;
        color: white !important;
    }
    
    /* Badges UNOi style */
    .unoi-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
        border: 2px solid;
    }
    
    .badge-green {
        background: rgba(0, 168, 132, 0.1);
        color: var(--unoi-green);
        border-color: var(--unoi-green);
    }
    
    .badge-purple {
        background: rgba(139, 92, 246, 0.1);
        color: var(--unoi-purple);
        border-color: var(--unoi-purple);
    }
    
    /* Info boxes */
    .stSuccess {
        background: rgba(0, 168, 132, 0.1);
        border-left: 4px solid var(--unoi-green);
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stInfo {
        background: rgba(99, 102, 241, 0.1);
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stWarning {
        background: rgba(245, 158, 11, 0.1);
        border-left: 4px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Spinner UNOi verde */
    .stSpinner > div {
        border-top-color: var(--unoi-green) !important;
    }
    
    /* Animaciones suaves */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Métricas */
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: var(--card-shadow);
    }
    
    .stMetric label {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 600;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: var(--unoi-green) !important;
        font-size: 2rem !important;
        font-weight: 800;
    }
    
    /* Download buttons */
    .stDownloadButton > button {
        background: white;
        color: var(--unoi-green);
        border: 2px solid var(--unoi-green);
        border-radius: 12px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background: var(--unoi-green);
        color: white;
    }
    
    /* Code blocks */
    .stCodeBlock {
        border-radius: 12px;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INICIALIZACIÓN DE SESSION STATE ====================
if 'generador' not in st.session_state:
    st.session_state.generador = None
if 'contenido_generado' not in st.session_state:
    st.session_state.contenido_generado = None
if 'secciones' not in st.session_state:
    st.session_state.secciones = None
if 'tema_actual' not in st.session_state:
    st.session_state.tema_actual = ""
if 'grado_actual' not in st.session_state:
    st.session_state.grado_actual = ""

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-section fade-in">
    <h1 class="hero-title">🎓 Generador de Contenidos Educativos</h1>
    <p class="hero-subtitle">Alineado con los Derechos Básicos de Aprendizaje (DBA) de Colombia 🇨🇴</p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown('<h3 style="margin-top: 2rem;">⚙️ Configuración</h3>', unsafe_allow_html=True)
    
    # API Key input
    api_key = st.text_input(
        "API Key de Google Gemini",
        type="password",
        help="Obtén tu API Key en https://makersuite.google.com",
        placeholder="Pega tu API Key aquí..."
    )
    
    if api_key:
        if st.session_state.generador is None:
            st.session_state.generador = GeneradorContenidoEducativo(api_key=api_key)
            st.success("✅ API Key configurada")
    
    st.markdown("---")
    
    st.markdown("### 📚 Ejemplos de Temas")
    
    with st.expander("🔬 Ciencias Naturales"):
        st.markdown("""
        - El ciclo del agua
        - La fotosíntesis
        - Ecosistemas colombianos
        - El sistema solar
        - Estados de la materia
        """)
    
    with st.expander("🔢 Matemáticas"):
        st.markdown("""
        - Fracciones
        - Geometría básica
        - Operaciones decimales
        - Álgebra elemental
        - Probabilidad
        """)
    
    with st.expander("🌎 Ciencias Sociales"):
        st.markdown("""
        - Regiones de Colombia
        - Cultura indígena
        - Geografía colombiana
        - Historia de Colombia
        - Constitución política
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Estadísticas")
    if st.session_state.contenido_generado:
        st.metric("Contenidos Generados", "1", delta="✓ Sesión actual")
    else:
        st.metric("Contenidos Generados", "0")
    
    st.markdown("---")
    st.markdown('<p style="font-size: 0.85rem; opacity: 0.7;">Sistema de diseño instruccional automatizado para crear contenido educativo de calidad alineado con los DBA de Colombia.</p>', unsafe_allow_html=True)

# ==================== CONTENIDO PRINCIPAL ====================

# Tabs principales
tab1, tab2, tab3 = st.tabs(["🎨 Generar Contenido", "📖 Contenido Generado", "📘 Guía de Uso"])

with tab1:
    # Formulario en card
    st.markdown('<div class="unoi-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📝 Datos del Contenido</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        tema = st.text_input(
            "Tema Educativo",
            placeholder="Ejemplo: El ciclo del agua",
            help="Ingresa el tema que deseas desarrollar",
            key="tema_input"
        )
    
    with col2:
        grado = st.selectbox(
            "Grado Escolar",
            ["", "1°", "2°", "3°", "4°", "5°", "6°", "7°", "8°", "9°", "10°", "11°"],
            help="Selecciona el grado al que va dirigido el contenido",
            key="grado_select"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Botón de generar
    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    if st.button("🚀 Generar Contenido Educativo", disabled=(not api_key or not tema or not grado), key="generate_btn"):
        if not api_key:
            st.warning("⚠️ Por favor, ingresa tu API Key de Google Gemini en la barra lateral")
        elif not tema or not grado:
            st.warning("⚠️ Por favor, completa todos los campos")
        else:
            with st.spinner("🎨 Generando contenido educativo de alta calidad... Esto puede tomar unos momentos."):
                try:
                    # Generar contenido
                    contenido = st.session_state.generador.generar_contenido(tema, grado)
                    st.session_state.contenido_generado = contenido
                    st.session_state.tema_actual = tema
                    st.session_state.grado_actual = grado
                    
                    # Parsear
                    secciones = st.session_state.generador.parsear_contenido(contenido)
                    st.session_state.secciones = secciones
                    
                    # Guardar
                    carpeta = st.session_state.generador.guardar_contenido(secciones, tema, grado, output_dir="output")
                    
                    st.success(f"✅ ¡Contenido generado exitosamente para {tema} - Grado {grado}!")
                    st.info(f"📁 Archivos guardados en: `{carpeta}`")
                    
                except Exception as e:
                    st.error(f"❌ Error al generar contenido: {str(e)}")
    
    # Botón demo
    if st.button("🎭 Ver Contenido de Demostración", key="demo_btn", type="secondary"):
        # Contenido demo pre-cargado
        st.session_state.tema_actual = "El Ciclo del Agua"
        st.session_state.grado_actual = "4°"
        
        st.session_state.secciones = {
            'THEORIA': """## 🌊 ¿Cómo circula el agua en la naturaleza colombiana?

El **ciclo hidrológico** o **ciclo del agua** es uno de los procesos naturales más importantes para la vida en nuestro planeta. Este ciclo representa el movimiento continuo del agua entre la atmósfera, la superficie terrestre y el subsuelo, garantizando la disponibilidad de este recurso vital para todos los seres vivos. Colombia, por su ubicación geográfica privilegiada en la zona ecuatorial y su diversidad de ecosistemas, presenta manifestaciones únicas de este ciclo en sus diferentes regiones.

### **1. Evaporación: El Comienzo del Viaje del Agua**

La **evaporación** es el proceso físico mediante el cual el agua en estado líquido se transforma en vapor de agua (estado gaseoso) debido al aumento de temperatura provocado por la radiación solar. Este fenómeno ocurre constantemente en océanos, ríos, lagos, lagunas y hasta en el suelo húmedo.

**Fundamento científico:** Cuando las moléculas de agua (H₂O) reciben energía térmica del sol, aumentan su velocidad de movimiento hasta romper los enlaces de hidrógeno que las mantienen unidas en estado líquido, permitiendo que escapen a la atmósfera en forma de vapor.

**Ejemplos en Colombia:**

- **Costas del Caribe (La Guajira):** En el desierto de la Tatacoa y las salinas de Manaure, las altas temperaturas (que pueden superar los 40°C) generan tasas de evaporación extremadamente elevadas. El agua del Mar Caribe se evapora constantemente, creando una fuente importante de humedad atmosférica.

- **Cuenca Amazónica:** Los ríos como el Caquetá, Putumayo y Amazonas aportan enormes volúmenes de agua que se evaporan debido a las temperaturas cálidas constantes (25-28°C) y la alta radiación solar ecuatorial. Se estima que la Amazonía aporta el 20% del vapor de agua atmosférico de Sudamérica.

- **Páramos Andinos:** En ecosistemas como el Páramo de Sumapaz y el Nevado del Ruiz, la evaporación es menor debido a las bajas temperaturas, pero las lagunas glaciares y los humedales contribuyen significativamente al ciclo local del agua.

- **Valle del Cauca:** Las plantaciones de caña de azúcar y los espejos de agua en las zonas de cultivo experimentan altas tasas de evaporación, especialmente durante la época seca.

**Dato importante:** Colombia cuenta con aproximadamente 720,000 km² de superficie hídrica continental, lo que representa una fuente masiva de evaporación.

### **2. Condensación: La Formación de las Nubes**

La **condensación** es el proceso inverso a la evaporación, donde el vapor de agua se enfría y regresa al estado líquido, formando pequeñas gotas que se agrupan para crear las nubes. Este proceso ocurre cuando el aire cargado de humedad asciende a capas más altas y frías de la atmósfera.

**Fundamento científico:** Cuando el vapor de agua alcanza altitudes donde la temperatura es más baja (aproximadamente 6.5°C menos por cada 1,000 metros de altitud), las moléculas pierden energía cinética y se unen nuevamente, formando microgotas de agua alrededor de partículas microscópicas llamadas "núcleos de condensación" (polvo, sal marina, polen).

**Ejemplos en Colombia:**

- **Valle de Aburrá (Medellín):** La combinación de aire húmedo proveniente del Magdalena Medio y el enfriamiento nocturno en las montañas circundantes genera densas capas de nubes bajas que cubren la ciudad especialmente en las madrugadas. Este fenómeno es tan característico que afecta los patrones de temperatura diarios.

- **Sierra Nevada de Santa Marta:** Este macizo montañoso, que se eleva desde el nivel del mar hasta 5,775 metros en solo 42 km, crea un gradiente de condensación único. El aire húmedo del Caribe asciende por las laderas y se condensa constantemente, creando un cinturón de neblina permanente entre los 2,000 y 3,500 metros de altitud.

- **Llanos Orientales:** Durante la época de lluvias (abril a noviembre), las corrientes de aire húmedo provenientes de la Amazonía se encuentran con masas de aire más frío, generando formaciones nubosas masivas que pueden observarse desde gran distancia. Los llaneros conocen este fenómeno como "el invierno".

- **Región Andina:** Las tres cordilleras (Occidental, Central y Oriental) actúan como barreras naturales que fuerzan el ascenso del aire húmedo, provocando condensación continua. Esto explica por qué ciudades como Bogotá, Pasto y Manizales tienen cielos frecuentemente nublados.

**Dato importante:** Colombia tiene uno de los índices de nubosidad más altos del mundo, con un promedio de 60-70% de cobertura nubosa anual en la región Andina.

### **3. Precipitación: El Regreso del Agua a la Tierra**

La **precipitación** es la caída del agua desde las nubes hacia la superficie terrestre, manifestándose principalmente como lluvia, pero también como granizo, nieve o llovizna, dependiendo de las condiciones atmosféricas y la temperatura.

**Fundamento científico:** Cuando las gotas de agua en las nubes se fusionan y crecen hasta alcanzar un tamaño crítico (aproximadamente 5 mm de diámetro), vencen la resistencia del aire y caen por gravedad. En zonas con temperaturas bajo cero, el agua se congela formando cristales de hielo (nieve) o esferas de hielo (granizo).

**Ejemplos en Colombia:**

- **Chocó Biogeográfico:** Esta región es reconocida mundialmente como una de las más lluviosas del planeta. Municipios como Lloró y Tutunendo reciben entre 10,000 y 13,000 mm de lluvia al año (comparado con 1,000 mm en regiones secas). Las lluvias son casi diarias, creando el bosque húmedo tropical más biodiverso del mundo. Los vientos alisios del Pacífico chocan con la Cordillera Occidental, forzando el ascenso y condensación masiva de humedad.

- **Amazonía Colombiana:** Con precipitaciones de 3,000-4,000 mm anuales, la selva amazónica experimenta lluvias torrenciales casi diarias, especialmente en las tardes. Este patrón predecible se debe al calentamiento diurno que genera corrientes ascendentes de aire húmedo. La lluvia alimenta los grandes ríos que son vías fluviales esenciales para las comunidades indígenas.

- **Nevados de Los Andes:** El Nevado del Ruiz, Nevado del Tolima y Sierra Nevada del Cocuy experimentan precipitación en forma de nieve por encima de los 4,500 metros de altitud. Estas nieves perpetuas actúan como "torres de agua", almacenando agua sólida que se derrite gradualmente y alimenta ríos cruciales como el Magdalena y el Cauca.

- **Región Caribe semiárida:** La Guajira y parte de Cesar reciben menos de 500 mm de lluvia al año, creando ecosistemas de bosque seco y zonas desérticas. Este contraste con el Chocó demuestra la increíble variabilidad climática de Colombia en cortas distancias.

**Dato importante:** Colombia es el segundo país más lluvioso de Sudamérica después de Brasil, con un promedio nacional de 3,000 mm anuales.

### **4. Escorrentía y Filtración: El Camino del Agua Después de la Lluvia**

Una vez que el agua precipita, puede seguir dos caminos principales:

**Escorrentía superficial:** El agua fluye sobre la superficie del terreno formando arroyos, quebradas y ríos. Colombia tiene 5 grandes vertientes hidrográficas:
- Vertiente del Caribe (Magdalena, Cauca, Sinú, Atrato)
- Vertiente del Pacífico (San Juan, Patía, Baudó)
- Vertiente del Orinoco (Meta, Guaviare, Vichada)
- Vertiente del Amazonas (Caquetá, Putumayo, Vaupés)  
- Vertiente del Catatumbo (hacia el Lago de Maracaibo)

**Infiltración:** Parte del agua se filtra en el suelo, recargando acuíferos subterráneos. Los páramos colombianos son esenciales en este proceso, actuando como "esponjas naturales" que absorben agua de lluvia y la liberan gradualmente, regulando el caudal de los ríos durante todo el año.

### **Importancia del Ciclo del Agua para Colombia**

Colombia es uno de los países con mayor riqueza hídrica del mundo:
- **6to lugar mundial** en disponibilidad de agua dulce renovable
- **2,000 ríos** aproximadamente
- **1,600 lagunas** en ecosistemas de páramo
- **Más de 50 m³ de agua** por persona al día (promedio mundial: 7 m³)

Esta abundancia sostiene la agricultura (café, flores, caña), genera el 70% de la electricidad del país (hidroeléctricas) y mantiene ecosistemas únicos como los manglares del Pacífico y las ciénagas del Magdalena.

---

**DBA Relacionado (Grado 4°):** *"Comprende que los seres vivos (plantas, animales, hongos, bacterias) dependen del ciclo del agua y sus componentes (evaporación, condensación, precipitación, infiltración) para su supervivencia, y reconoce las adaptaciones de los organismos a las variaciones del ciclo en diferentes ecosistemas colombianos."*

**Competencias desarrolladas:**
- Explicar fenómenos naturales con base en evidencias científicas
- Relacionar procesos físicos con contextos regionales
- Valorar la riqueza hídrica nacional y su conservación""",
            
            'MERMAID': """graph TD
    A[☀️ Energía Solar] --> B[💧 Evaporación]
    B --> C[Ríos: Magdalena, Cauca]
    B --> D[Mar Caribe y Pacífico]
    C --> E[☁️ Vapor de Agua]
    D --> E
    E --> F[🌡️ Condensación]
    F --> G[☁️ Nubes sobre Andes]
    G --> H[🌧️ Precipitación]
    H --> I[Lluvia en el Chocó]
    H --> J[Nieve en Nevados]
    I --> C
    J --> C""",
            
            'DALLE_PROMPT': """Educational illustration of the water cycle in Colombian landscapes. Show Caribbean coast with water evaporating, clouds forming over Andes mountains, rain falling in Amazon rainforest, rivers flowing through valleys. Include Spanish labels: Evaporación, Condensación, Precipitación. Vibrant colors, child-friendly educational diagram style, warm sunny atmosphere.""",
            
            'ACTIVIDADES': """## 🎨 Actividad: Creando Nuestro Ciclo del Agua

**Objetivo:** Observar el ciclo del agua en un modelo a escala

### Materiales:
- 1 frasco de vidrio grande
- Agua
- Hielo
- 1 plato pequeño
- Papel aluminio

### Instrucciones:
1. Llena el frasco con 2 cm de agua
2. Coloca el plato pequeño boca abajo dentro
3. Cubre la boca con papel aluminio
4. Pon hielo sobre el aluminio
5. Deja al sol por 2 horas
6. Observa qué sucede

### 📝 Taller Evaluativo
1. ¿Qué pasa con el agua cuando la calientas?
2. ¿Por qué se forman gotitas en el aluminio?
3. Nombra 3 departamentos con mucha lluvia
4. ¿Dónde va el agua después de llover?
5. Dibuja el ciclo del agua""",
            
            'METADATOS': f"""**Título:** El Ciclo del Agua en Colombia
**Grado:** 4°
**Eje Temático:** Ciencias Naturales
**Fecha:** {datetime.now().strftime("%Y-%m-%d")}
**Región:** Nacional con ejemplos regionales"""
        }
        
        st.session_state.contenido_generado = "\n\n".join([
            f"=== {k} ===\n{v}" for k, v in st.session_state.secciones.items()
        ])
        
        st.success("✅ ¡Contenido demo cargado! Ve a la pestaña 'Contenido Generado' para verlo")
        st.info("💡 Esto es contenido de demostración. Para generar contenido personalizado, ingresa tu API Key.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Badges informativos
    st.markdown('<div class="unoi-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">✨ Características del Contenido</h2>', unsafe_allow_html=True)
    st.markdown("""
    <span class="unoi-badge badge-green">📚 Teoría con DBA</span>
    <span class="unoi-badge badge-green">🗺️ Ejemplos Colombianos</span>
    <span class="unoi-badge badge-green">📊 Diagramas Mermaid</span>
    <span class="unoi-badge badge-purple">🎨 Prompts DALL-E</span>
    <span class="unoi-badge badge-purple">✏️ Actividades Prácticas</span>
    <span class="unoi-badge badge-purple">📝 Taller Evaluativo</span>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if st.session_state.secciones:
        st.markdown(f'<h2 class="section-title">📖 {st.session_state.tema_actual} - Grado {st.session_state.grado_actual}</h2>', unsafe_allow_html=True)
        
        # Sub-tabs para cada sección
        sub_tab1, sub_tab2, sub_tab3, sub_tab4, sub_tab5 = st.tabs([
            "📚 Teoría", 
            "📊 Visualización", 
            "✏️ Actividades", 
            "📋 Metadatos",
            "💾 Descargar"
        ])
        
        with sub_tab1:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('THEORIA', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab2:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("#### 🗺️ Diagrama Mermaid")
            st.code(st.session_state.secciones.get('MERMAID', 'No disponible'), language='mermaid')
            st.info("💡 Visualiza este diagrama en: https://mermaid.live")
            
            st.markdown("---")
            
            st.markdown("#### 🎨 Prompt para DALL-E")
            st.code(st.session_state.secciones.get('DALLE_PROMPT', 'No disponible'), language='text')
            st.info("💡 Usa este prompt en OpenAI o Microsoft Designer")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab3:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('ACTIVIDADES', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab4:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('METADATOS', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab5:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("### 💾 Descargar Contenido")
            
            # Crear nombre de archivo limpio
            nombre_archivo = f"{st.session_state.grado_actual}_{st.session_state.tema_actual.replace(' ', '_')}"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📄 Descargar Contenido Completo (.txt)",
                    data=st.session_state.contenido_generado,
                    file_name=f"{nombre_archivo}_completo.txt",
                    mime="text/plain"
                )
            
            with col2:
                st.download_button(
                    label="📊 Descargar Diagrama Mermaid (.mmd)",
                    data=st.session_state.secciones.get('MERMAID', ''),
                    file_name=f"{nombre_archivo}_diagrama.mmd",
                    mime="text/plain"
                )
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Genera contenido en la pestaña 'Generar Contenido' para verlo aquí")

with tab3:
    st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 📘 Cómo Usar el Generador
    
    #### 1️⃣ Configurar API Key
    - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Crea o inicia sesión con tu cuenta de Google
    - Genera una nueva API Key
    - Pégala en el campo de la barra lateral
    
    #### 2️⃣ Ingresar Datos
    - **Tema**: El contenido educativo que deseas desarrollar (ej: "El ciclo del agua")
    - **Grado**: Selecciona el grado escolar (1° a 11°)
    
    #### 3️⃣ Generar Contenido
    - Haz clic en "🚀 Generar Contenido Educativo"
    - Espera unos momentos mientras la IA crea el contenido
    - El contenido se guardará automáticamente en la carpeta `output/`
    
    #### 4️⃣ Revisar y Descargar
    - Revisa cada sección en la pestaña "📖 Contenido Generado"
    - Descarga los archivos que necesites
    - Visualiza el diagrama Mermaid en [mermaid.live](https://mermaid.live)
    - Usa el prompt DALL-E para generar imágenes educativas
    
    ### 🎯 Secciones Incluidas
    
    ✅ **Teoría**: Contenido completo con contexto colombiano y DBA  
    ✅ **Visualización**: Diagramas Mermaid + Prompts para imágenes  
    ✅ **Actividades**: Talleres prácticos con materiales de fácil acceso  
    ✅ **Metadatos**: Información clasificatoria del contenido  
    
    ### 💡 Consejos
    
    - Sé específico con el tema para obtener mejores resultados
    - El contenido incluye ejemplos de regiones colombianas

Colombia es uno de los países con mayor riqueza hídrica del mundo:
- **6to lugar mundial** en disponibilidad de agua dulce renovable
- **2,000 ríos** aproximadamente
- **1,600 lagunas** en ecosistemas de páramo
- **Más de 50 m³ de agua** por persona al día (promedio mundial: 7 m³)

Esta abundancia sostiene la agricultura (café, flores, caña), genera el 70% de la electricidad del país (hidroeléctricas) y mantiene ecosistemas únicos como los manglares del Pacífico y las ciénagas del Magdalena.

---

**DBA Relacionado (Grado 4°):** *"Comprende que los seres vivos (plantas, animales, hongos, bacterias) dependen del ciclo del agua y sus componentes (evaporación, condensación, precipitación, infiltración) para su supervivencia, y reconoce las adaptaciones de los organismos a las variaciones del ciclo en diferentes ecosistemas colombianos."*

**Competencias desarrolladas:**
- Explicar fenómenos naturales con base en evidencias científicas
- Relacionar procesos físicos con contextos regionales
- Valorar la riqueza hídrica nacional y su conservación""",
            
            'MERMAID': """graph TD
    A[☀️ Energía Solar] --> B[💧 Evaporación]
    B --> C[Ríos: Magdalena, Cauca]
    B --> D[Mar Caribe y Pacífico]
    C --> E[☁️ Vapor de Agua]
    D --> E
    E --> F[🌡️ Condensación]
    F --> G[☁️ Nubes sobre Andes]
    G --> H[🌧️ Precipitación]
    H --> I[Lluvia en el Chocó]
    H --> J[Nieve en Nevados]
    I --> C
    J --> C""",
            
            'DALLE_PROMPT': """Educational illustration of the water cycle in Colombian landscapes. Show Caribbean coast with water evaporating, clouds forming over Andes mountains, rain falling in Amazon rainforest, rivers flowing through valleys. Include Spanish labels: Evaporación, Condensación, Precipitación. Vibrant colors, child-friendly educational diagram style, warm sunny atmosphere.""",
            
            'ACTIVIDADES': """## 🎨 Actividad: Creando Nuestro Ciclo del Agua

**Objetivo:** Observar el ciclo del agua en un modelo a escala

### Materiales:
- 1 frasco de vidrio grande
- Agua
- Hielo
- 1 plato pequeño
- Papel aluminio

### Instrucciones:
1. Llena el frasco con 2 cm de agua
2. Coloca el plato pequeño boca abajo dentro
3. Cubre la boca con papel aluminio
4. Pon hielo sobre el aluminio
5. Deja al sol por 2 horas
6. Observa qué sucede

### 📝 Taller Evaluativo
1. ¿Qué pasa con el agua cuando la calientas?
2. ¿Por qué se forman gotitas en el aluminio?
3. Nombra 3 departamentos con mucha lluvia
4. ¿Dónde va el agua después de llover?
5. Dibuja el ciclo del agua""",
            
            'METADATOS': f"""**Título:** El Ciclo del Agua en Colombia
**Grado:** 4°
**Eje Temático:** Ciencias Naturales
**Fecha:** {datetime.now().strftime("%Y-%m-%d")}
**Región:** Nacional con ejemplos regionales"""
        }
        
        st.session_state.contenido_generado = "\n\n".join([
            f"=== {k} ===\n{v}" for k, v in st.session_state.secciones.items()
        ])
        
        st.success("✅ ¡Contenido demo cargado! Ve a la pestaña 'Contenido Generado' para verlo")
        st.info("💡 Esto es contenido de demostración. Para generar contenido personalizado, ingresa tu API Key.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Badges informativos
    st.markdown('<div class="unoi-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">✨ Características del Contenido</h2>', unsafe_allow_html=True)
    st.markdown("""
    <span class="unoi-badge badge-green">📚 Teoría con DBA</span>
    <span class="unoi-badge badge-green">🗺️ Ejemplos Colombianos</span>
    <span class="unoi-badge badge-green">📊 Diagramas Mermaid</span>
    <span class="unoi-badge badge-purple">🎨 Prompts DALL-E</span>
    <span class="unoi-badge badge-purple">✏️ Actividades Prácticas</span>
    <span class="unoi-badge badge-purple">📝 Taller Evaluativo</span>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if st.session_state.secciones:
        st.markdown(f'<h2 class="section-title">📖 {st.session_state.tema_actual} - Grado {st.session_state.grado_actual}</h2>', unsafe_allow_html=True)
        
        # Sub-tabs para cada sección
        sub_tab1, sub_tab2, sub_tab3, sub_tab4, sub_tab5 = st.tabs([
            "📚 Teoría", 
            "📊 Visualización", 
            "✏️ Actividades", 
            "📋 Metadatos",
            "💾 Descargar"
        ])
        
        with sub_tab1:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('THEORIA', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab2:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("#### 🗺️ Diagrama Mermaid")
            st.code(st.session_state.secciones.get('MERMAID', 'No disponible'), language='mermaid')
            st.info("💡 Visualiza este diagrama en: https://mermaid.live")
            
            st.markdown("---")
            
            st.markdown("#### 🎨 Prompt para DALL-E")
            st.code(st.session_state.secciones.get('DALLE_PROMPT', 'No disponible'), language='text')
            st.info("💡 Usa este prompt en OpenAI o Microsoft Designer")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab3:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('ACTIVIDADES', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab4:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown(st.session_state.secciones.get('METADATOS', 'No disponible'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with sub_tab5:
            st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
            st.markdown("### 💾 Descargar Contenido")
            
            # Crear nombre de archivo limpio
            nombre_archivo = f"{st.session_state.grado_actual}_{st.session_state.tema_actual.replace(' ', '_')}"
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📄 Descargar Contenido Completo (.txt)",
                    data=st.session_state.contenido_generado,
                    file_name=f"{nombre_archivo}_completo.txt",
                    mime="text/plain"
                )
            
            with col2:
                st.download_button(
                    label="📊 Descargar Diagrama Mermaid (.mmd)",
                    data=st.session_state.secciones.get('MERMAID', ''),
                    file_name=f"{nombre_archivo}_diagrama.mmd",
                    mime="text/plain"
                )
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("👈 Genera contenido en la pestaña 'Generar Contenido' para verlo aquí")

with tab3:
    st.markdown('<div class="unoi-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 📘 Cómo Usar el Generador
    
    #### 1️⃣ Configurar API Key
    - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Crea o inicia sesión con tu cuenta de Google
    - Genera una nueva API Key
    - Pégala en el campo de la barra lateral
    
    #### 2️⃣ Ingresar Datos
    - **Tema**: El contenido educativo que deseas desarrollar (ej: "El ciclo del agua")
    - **Grado**: Selecciona el grado escolar (1° a 11°)
    
    #### 3️⃣ Generar Contenido
    - Haz clic en "🚀 Generar Contenido Educativo"
    - Espera unos momentos mientras la IA crea el contenido
    - El contenido se guardará automáticamente en la carpeta `output/`
    
    #### 4️⃣ Revisar y Descargar
    - Revisa cada sección en la pestaña "📖 Contenido Generado"
    - Descarga los archivos que necesites
    - Visualiza el diagrama Mermaid en [mermaid.live](https://mermaid.live)
    - Usa el prompt DALL-E para generar imágenes educativas
    
    ### 🎯 Secciones Incluidas
    
    ✅ **Teoría**: Contenido completo con contexto colombiano y DBA  
    ✅ **Visualización**: Diagramas Mermaid + Prompts para imágenes  
    ✅ **Actividades**: Talleres prácticos con materiales de fácil acceso  
    ✅ **Metadatos**: Información clasificatoria del contenido  
    
    ### 💡 Consejos
    
    - Sé específico con el tema para obtener mejores resultados
    - El contenido incluye ejemplos de regiones colombianas
    - Los materiales sugeridos son de fácil acceso en Colombia
    - Todo está alineado con los DBA oficiales
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; margin-top: 3rem;">
    <p style="font-weight: 600;">Desarrollado con ❤️ para la educación colombiana 🇨🇴</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Sumercesito | Alineado con DBA Colombia</p>
</div>
""", unsafe_allow_html=True)
