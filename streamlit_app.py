import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Estética Dark Mode)
st.set_page_config(
    page_title="BEAUCHEF RPG - HUD",
    page_icon="🚀",
    layout="wide"
)

# Estilo personalizado con CSS para neones
st.markdown("""
    <style>
    /* Importar una fuente tipo Pixel/Minecraft desde Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    /* Aplicar fuente Minecraft a toda la app */
    * {
        font-family: 'Press+Start+2P', cursive !important;
        font-size: 12px; /* Las fuentes pixeladas se ven mejor pequeñas */
        color: #00FFCC;
    }

    /* Fondo general oscuro profundo */
    .main {
        background-color: #050505;
    }

    /* Animación RGB para los bordes */
    @keyframes rgb-border {
        0% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; }
        33% { border-color: #00ff00; box-shadow: 0 0 10px #00ff00; }
        66% { border-color: #0000ff; box-shadow: 0 0 10px #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 10px #ff0000; }
    }

    /* Estilo de los recuadros de Atributos (Métricas) */
    [data-testid="stMetric"] {
        background-color: #111111 !important;
        border: 3px solid #ff0000 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        animation: rgb-border 3s linear infinite; /* Aquí ocurre la magia RGB */
    }

    /* Personalización de los Checkboxes (Misiones) */
    .stCheckbox {
        background-color: #1a1a1a;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;
        border-left: 5px solid #00FFCC;
    }

    /* Botón Reclamar XP estilo Arcade */
    .stButton>button {
        background-color: #ff00ff !important;
        color: white !important;
        border: 4px solid #ffffff !important;
        font-family: 'Press Start 2P', cursive !important;
        height: 50px;
        width: 100%;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #00ffff !important;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)



# --- ENCABEZADO ---
st.title("🌌 BEAUCHEF RPG: SURVIVAL MODE")
st.write(f"**Estado del Sistema:** Operativo | **Ubicación:** Beauchef, Santiago")

st.divider()

# --- PERFIL Y STATS ---
col_av, col_stats = st.columns([1, 3])

with col_av:
    # Imagen temporal (puedes subir la que te generé a GitHub y usar su link)
   st.image("avatar.png", caption="Clase: Ingeniero Matemático", width=200)
   st.progress(15, text="XP para Nivel 2 (Mechón)")

with col_stats:
    st.subheader("📊 Atributos Principales")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("INT (Estudio)", "10", "+2")
    c2.metric("STR (Gym)", "25", "+5")
    c3.metric("SOUL (Música)", "15", "0")
    c4.metric("CON (Hogar)", "40", "+1")

st.divider()

# --- MISIONES (QUESTS) ---
st.subheader("⚔️ Misiones Diarias (Quests)")

col_q1, col_q2 = st.columns(2)

with col_q1:
    st.markdown("### 💻 Main Quest")
    q1 = st.checkbox("Desplegar Dashboard en Streamlit Cloud (BOSS)")
    q2 = st.checkbox("Resolver dudas de instalación de Python")
    
with col_q2:
    st.markdown("### 🏠 Side Quests")
    q3 = st.checkbox("Entrenar en el gym del edificio (Fuerza)")
    q4 = st.checkbox("Batch Cooking: Preparar proteínas para la semana")
    q5 = st.checkbox("Producción: Abrir FL Studio (15 min mín.)")

# --- LÓGICA DE RECOMPENSA ---
st.divider()
if st.button("🏁 FINALIZAR JORNADA Y RECLAMAR XP"):
    completed = [q1, q2, q3, q4, q5]
    total = len(completed)
    done = sum(completed)
    
    if q1: # Recompensa especial por el despliegue
        st.balloons()
        st.success(f"¡LOGRO DESBLOQUEADO: Dev Ops Junior! Has completado {done}/{total} misiones.")
        st.info("Siguiente paso: Conectar base de datos para guardar progreso.")
    elif done > 0:
        st.success(f"Buen trabajo hoy. Has completado {done}/{total} misiones.")
    else:
        st.warning("El conocimiento no se adquiere por ósmosis. ¡A trabajar!")

# --- FOOTER ---
st.sidebar.markdown("### 🛠️ Configuración")
st.sidebar.write("Usuario: Estudiante FCFM")
st.sidebar.write("Meta: Boleros & Matemáticas")
