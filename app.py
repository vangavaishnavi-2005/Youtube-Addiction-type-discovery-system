import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="YouTube Addiction Type Discovery System", page_icon="📊", layout="wide")

# ---------- Status Function ----------
def get_status(score):
    if score < 30:
        return "Normal User"
    elif score < 60:
        return "Moderate Usage"
    else:
        return "High Addiction Risk"

# ---------- Custom UI Styling ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1e0030 0%, #0d001a 100%);
    color: #ffffff !important;
}

h1, h2, h3, h4, .stMarkdown p {
    color: #ffffff !important;
}

div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 15px;
}

section[data-testid="stSidebar"] {
    background-color: rgba(20,0,30,0.95);
}
</style>
""", unsafe_allow_html=True)

st.title("📊 YouTube Addiction Type Discovery System")
st.markdown("Discover your YouTube viewing habits and addiction risk score.")

# ---------- Load Dataset ----------
@st.cache_data
def load_data():
    return pd.read_csv("youtube_users_final.csv")

df = load_data()

# ---------- Cluster Labels ----------
cluster_mapping = {
    0: "Balanced / Casual Consumer 😌",
    1: "Night Owl 🦉",
    2: "Weekend Binger 🍿",
    3: "Shorts Scroller 📱"
}

# ---------- Sidebar ----------
st.sidebar.header("User Selection")
user_input = st.sidebar.text_input("Enter User Index", value="0")

try:
    user_id = int(user_input)
    if user_id < 0 or user_id >= len(df):
        st.sidebar.error(f"Please enter an index between 0 and {len(df)-1}")
        user_id = 0
except ValueError:
    st.sidebar.error("Please enter a valid numeric index.")
    user_id = 0

user = df.iloc[user_id]

risk_score = float(user['addiction_risk_score'])
user_status = get_status(risk_score)

# ---------- Top Metrics ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Risk Score", value=f"{risk_score:.1f}/100")

with col2:
    addiction_type = cluster_mapping.get(int(user['cluster']), f"Type {int(user['cluster'])}")
    st.metric(label="Addiction Type", value=addiction_type)

with col3:
    if user_status == "High Addiction Risk":
        status_color = "#f5576c"
    elif user_status == "Moderate Usage":
        status_color = "#fee140"
    else:
        status_color = "#00f2fe"

    st.markdown(
        "<div style='color:#b3b3b3;font-size:1.1rem;font-weight:600;'>User Status</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='color:{status_color};font-size:2.2rem;font-weight:800'>{user_status}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------- Future Risk Prediction ----------
st.subheader("🔮 Future Addiction Risk Prediction")

future_risk = risk_score + (user["late_night_ratio"] * 20) + (user["shorts_ratio"] * 15)
future_risk = min(future_risk, 100)

if future_risk > 75:
    st.error("⚠️ If your current behavior continues, your addiction risk could become very high in the future.")
elif future_risk > 50:
    st.warning("⚠️ Your current habits may increase addiction risk over time.")
else:
    st.success("✅ Your viewing behavior is unlikely to lead to addiction if maintained.")

st.markdown("---")

# ---------- Behaviour Summary ----------
col_behavior, col_graph = st.columns([1, 2])

with col_behavior:
    st.subheader("📌 Behaviour Summary")

    late_ratio_pct = int(user['late_night_ratio'] * 100)
    st.markdown(f"Late Night Usage ({late_ratio_pct}%)")
    st.progress(float(user['late_night_ratio']))

    shorts_ratio_pct = int(user['shorts_ratio'] * 100)
    st.markdown(f"Shorts Ratio ({shorts_ratio_pct}%)")
    st.progress(float(user['shorts_ratio']))

    binge_pct = int(user['binge_session_length'] * 100)
    st.markdown(f"Binge Session Length ({binge_pct}%)")
    st.progress(float(user['binge_session_length']))

    st.markdown(f"Sessions per Day: {round(user['sessions_per_day'], 2)}")
    st.markdown(f"Weekend Ratio: {round(user['weekend_ratio'], 2)}")

with col_graph:
    st.subheader("📍 Where You Stand")

    df['cluster_name'] = df['cluster'].map(cluster_mapping)

    fig = px.scatter(
        df,
        x="shorts_ratio",
        y="addiction_risk_score",
        color="cluster_name",
        hover_data=["sessions_per_day"],
        opacity=0.7,
        title="Addiction Risk vs Shorts Ratio"
    )

    fig.add_trace(
        go.Scatter(
            x=[user["shorts_ratio"]],
            y=[risk_score],
            mode="markers+text",
            marker={"color": "white", "size": 16},
            name="YOU",
            text=["YOU"],
            textposition="top center"
        )
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"}
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------- Addiction Gauge ----------
st.subheader("🎯 Addiction Risk Meter")

gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_score,
    title={'text': "Addiction Risk Score"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#00f2fe"},
        'steps': [
            {'range': [0, 30], 'color': "#00f2fe"},
            {'range': [30, 60], 'color': "#fee140"},
            {'range': [60, 100], 'color': "#f5576c"}
        ],
        'threshold': {
            'line': {'color': "white", 'width': 4},
            'thickness': 0.75,
            'value': risk_score
        }
    }
))

st.plotly_chart(gauge_fig, use_container_width=True)
