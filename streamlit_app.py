import streamlit as st
import base64
import time
# ... cualquier otro import que tengas

# --- AQUÍ VA EL MOTOR DE AUDIO (Paso 2) ---
def play_sound(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        # Si el archivo no existe, no hace nada (evita que la app pete)
        pass

# --- DESPUÉS VIENE EL RESTO DE TU CÓDIGO ---
st.set_page_config(page_title="BEAUCHEF RPG", layout="wide")

# ... (Tu CSS RGB, tus pestañas, etc.)

# 1. CONFIGURACIÓN DE PÁGINA (Estética Dark Mode)
st.set_page_config(
    page_title="BEAUCHEF RPG - HUD",
    page_icon="🚀",
    layout="wide"
)

# Estilo personalizado con CSS para neones
st.markdown("""
    <style>
    /* 1. Cambiamos a una fuente más elegante: Orbitron */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    * {
        font-family: 'Orbitron', sans-serif !important;
        color: #00FFCC;
    }

    .main { background-color: #050505; }

    /* 2. Animación RGB Mejorada (Borde + Sombra) */
    @keyframes rgb-full {
        0%   { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; }
        33%  { border-color: #00ff00; box-shadow: 0 0 15px #00ff00; }
        66%  { border-color: #0000ff; box-shadow: 0 0 15px #0000ff; }
        100% { border-color: #ff0000; box-shadow: 0 0 15px #ff0000; }
    }

    [data-testid="stMetric"] {
        background-color: #111111 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        /* Quitamos el color fijo y dejamos que la animación mande */
        border: 2px solid transparent !important; 
        animation: rgb-full 4s linear infinite !important;
    }

    /* Estilo para los títulos de los atributos */
    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
        letter-spacing: 2px;
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
# --- SISTEMA DE PESTAÑAS ---
tab1, tab2 = st.tabs(["🎮 Dashboard Principal", "⏳ Módulo Pomodoro"])

with tab1:
    # Mueve aquí todo el código de tus Quests y Stats
    st.subheader("⚔️ Estado del Jugador")
    # ... (el resto de tu código actual)

with tab2:
    st.subheader("🍅 Temporizador de Concentración")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        tiempo_base = st.number_input("Minutos de estudio:", value=25)
    with col_t2:
        st.write("Estado: **En Pausa**")

    # Lógica simple de cronómetro (Streamlit refresca la página, 
    # por lo que para un cronómetro pro necesitaríamos 'session_state')
    if st.button("🚀 INICIAR SESIÓN"):
        with st.empty():
            import time
            secs = tiempo_base * 60
            while secs > 0:
                mm, ss = divmod(secs, 60)
                st.metric("Tiempo Restante", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
                secs -= 1
            st.success("¡Sesión completada! Ganas +10 XP de INT")
            st.balloons()

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
