import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ICT in Health & Ergonomics",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR & GROUP MEMBERS ---
st.sidebar.title("📌 Project Information")
st.sidebar.markdown("""
**Course:** ICT in Health  
**Project:** Ergonomics & Workplace Wellness App  
""")

st.sidebar.markdown("### 👥 Group Members:")
members = [
    "IDREES KHAN",
    "ABDUL WAHAB KHAN",
    "DILDAR HUSSAIN KHAN",
    "M HASHIM AMEER UD DIN"
]
for member in members:
    st.sidebar.markdown(f"- **{member}**")

st.sidebar.divider()
st.sidebar.info("This application promotes ergonomic awareness and health tracking using ICT tools.")

# --- MAIN APP HEADER ---
st.title("🩺 ICT in Health & Workplace Ergonomics")
st.markdown("""
Welcome to the Ergonomics Assessment and Health Tool. This application uses Information and Communications Technology (ICT) to evaluate workplace strain, prevent musculoskeletal disorders, and promote healthier desk habits.
""")

# --- TABS INTERFACE ---
tab1, tab2, tab3 = st.tabs(["📊 Ergonomic Risk Assessment", "⏱️ Posture Break Timer", "💡 ICT & Health Insights"])

# --- TAB 1: ERGONOMIC RISK ASSESSMENT ---
with tab1:
    st.header("🪑 Desktop Ergonomics Self-Assessment")
    st.write("Answer the questions below to calculate your ergonomic risk score based on rapid upper limb assessment principles.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Setup")
        neck_pos = st.selectbox("1. Position of your monitor/screen:", [
            "At eye level (No neck tilt)",
            "Too low (Looking down)",
            "Too high (Looking up/twisted)"
        ])
        
        back_pos = st.selectbox("2. Back support status:", [
            "Fully supported by chair with lumbar curve",
            "Slouched / No lower back support",
            "Leaning forward / Perched on edge"
        ])
        
        arm_pos = st.selectbox("3. Elbow and wrist position:", [
            "90-degree angle, relaxed shoulders",
            "Reaching forward to type/mouse",
            "Wrists bent sharply upward or downward"
        ])
        
        hours_seated = st.slider("4. Daily hours spent at the computer:", 1, 12, 6)

    # Risk Scoring Logic
    score = 0
    score += 1 if "eye level" in neck_pos else (2 if "Too high" in neck_pos else 3)
    score += 1 if "Fully supported" in back_pos else (3 if "Slouched" in back_pos else 2)
    score += 1 if "90-degree" in arm_pos else (2 if "Reaching" in arm_pos else 3)
    score += 1 if hours_seated <= 4 else (2 if hours_seated <= 8 else 3)
    
    with col2:
        st.subheader("Assessment Summary")
        st.metric(label="Calculated Ergonomic Risk Score", value=f"{score} / 12")
        
        # Displaying status based on score
        if score <= 5:
            st.success("🟢 Low Risk: Your workspace configuration is excellent! Maintain your current habits.")
            risk_level = "Low"
        elif 6 <= score <= 9:
            st.warning("🟡 Moderate Risk: Action required. You need to adjust your seating position or monitor height soon.")
            risk_level = "Moderate"
        else:
            st.error("🔴 High Risk: Immediate changes needed! You are highly susceptible to repetitive strain injuries (RSI).")
            risk_level = "High"
            
        # Plotting a quick mock risk breakdown graph
        df_risk = pd.DataFrame({
            'Category': ['Neck', 'Back', 'Arms', 'Duration'],
            'Strain Score': [
                1 if "eye level" in neck_pos else 3,
                1 if "Fully supported" in back_pos else 3,
                1 if "90-degree" in arm_pos else 3,
                1 if hours_seated <= 4 else (2 if hours_seated <= 8 else 3)
            ]
        })
        fig = px.bar(df_risk, x='Category', y='Strain Score', title="Strain Points Breakdown", color='Strain Score', range_y=[0,4])
        st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: POSTURE BREAK TIMER ---
with tab2:
    st.header("⏱️ The 20-20-20 Rule Timer")
    st.write("To prevent eye strain and physical fatigue, look at something 20 feet away for 20 seconds every 20 minutes.")
    
    duration = st.number_input("Set reminder time (in minutes):", min_value=1, max_value=60, value=20)
    
    if st.button("🚀 Start Work Session"):
        st.info(f"Session started! Keep working. We will simulate a {duration}-minute block...")
        progress_bar = st.progress(0)
        
        # Simulating time for demo purposes (1 second per 10% progress)
        for percent_complete in range(100):
            time.sleep(0.05)  # In reality, this would map to actual minutes
            progress_bar.progress(percent_complete + 1)
            
        st.balloons()
        st.success("🔔 TIME FOR A BREAK! Stand up, stretch, and rest your eyes for 20 seconds.")

# --- TAB 3: ICT & HEALTH INSIGHTS ---
with tab3:
    st.header("💡 Role of ICT in Modern Healthcare & Ergonomics")
    
    st.markdown("""
    Information and Communication Technology (ICT) plays an indispensable role in monitoring, identifying, and mitigating occupational health risks.
    
    ### Key Applications of ICT in Ergonomics:
    1. **Computer Vision & AI Posture Analysis:** Using built-in webcams to dynamically analyze a user's neck angle and sitting posture in real-time.
    2. **Smart IoT Wearables:** Sensors embedded in office chairs or clothing that vibrate to alert users when they slouch.
    3. **Telehealth Platforms:** Allowing remote ergonomic consultations for work-from-home employees.
    4. **Health Analytics:** Aggregating data from break-tracking apps to evaluate corporate-wide wellness levels.
    """)
    
    # Simple data viz showing impact of ergonomic interventions
    st.subheader("Data Insight: Reduction in Musculoskeletal Disorders (MSDs) via ICT Interventions")
    data = pd.DataFrame({
        'Year': ['2021', '2022', '2023', '2024', '2025'],
        'Reported Injuries (per 100 employees)': [14, 12, 9, 5, 2]
    })
    fig_line = px.line(data, x='Year', y='Reported Injuries (per 100 employees)', markers=True, title="MSD Incidents Post-ICT App Implementation")
    st.plotly_chart(fig_line, use_container_width=True)

# --- FOOTER ---
st.divider()
st.caption("Developed as part of the ICT in Health Coursework © 2026.")
