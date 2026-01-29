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
    /* Fondo general */
    .main { background-color: #0b0d11; }
    
    /* Estilo para las tarjetas de métricas */
    [data-testid="stMetric"] {
        background-color: #161b22;
        border: 2px solid #ff4b4b; /* Rojo neón, puedes cambiar a #00ffcc para cian */
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 0px 15px rgba(255, 75, 75, 0.3);
    }
    
    /* Títulos y textos */
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', monospace; }
    
    /* El botón de reclamar XP */
    .stButton>button {
        background-image: linear-gradient(to right, #ff4b4b, #ff00ff);
        color: white;
        border-radius: 20px;
        border: none;
        font-weight: bold;
        width: 100%;
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
