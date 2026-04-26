import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(layout="wide")

# Title
st.title("📊 Systemic Risk Dashboard (CoVaR)")
st.markdown("Explore systemic risk across banks using CoVaR analysis")

# Load data
static_df = pd.read_csv("static_results.csv")
time_df = pd.read_csv("timevarying_results.csv", index_col=0)
stress_df = pd.read_csv("stress_results.csv")

# Sidebar controls
st.sidebar.header("⚙️ Controls")

bank = st.sidebar.selectbox("Select Bank", time_df.columns)
shock = st.sidebar.selectbox("Select Stress Scenario", stress_df['Shock_Type'].unique())

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Static", "📈 Time-Varying", "⚡ Stress"])

# -------------------------------
# TAB 1: Static CoVaR
# -------------------------------
with tab1:
    st.subheader("Systemic Risk Ranking")

    fig1 = px.bar(
        static_df.sort_values(by='Delta_CoVar'),
        x='Bank',
        y='Delta_CoVar',
        color='Delta_CoVar',
        color_continuous_scale='Reds'
    )

    st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# TAB 2: Time-Varying
# -------------------------------
with tab2:
    st.subheader(f"Time-Varying Risk: {bank}")

    fig2 = px.line(
        time_df,
        y=bank,
        title="ΔCoVaR over time"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# TAB 3: Stress Testing
# -------------------------------
with tab3:
    st.subheader("Stress Testing Results")

    filtered = stress_df[stress_df['Shock_Type'] == shock]

    fig3 = px.bar(
        filtered,
        x='Bank',
        y='Impact',
        color='Impact',
        color_continuous_scale='RdBu'
    )

    st.plotly_chart(fig3, use_container_width=True)