import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Disaster e-Health Digital Twin", layout="wide")

st.title("Serverless Healthcare Digital Twin Pipeline")
st.caption("Real-Time Disaster e-Health Logistics & Medical Supply Chain Optimization")

st.sidebar.header("Crisis Configuration")
selected_network = st.sidebar.selectbox("Active Digital Twin Zone", ["Auckland Metro Health Network", "Wellington Regional Acute Care", "Christchurch Emergency Logistics"])
disaster_severity = st.sidebar.slider("Simulate Disaster Shock Severity", 1, 10, 6)
run_simulation = st.sidebar.button("Initialize e-Health Digital Twin")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Hospital IoT -> AWS Serverless Sync -> Machine Learning Triage")

if run_simulation:
    st.subheader(f"Active Regional Monitoring: {selected_network}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_admissions = col1.empty()
    metric_supplies = col2.empty()
    metric_twin = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(1818)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    admission_rates = []
    medical_supplies = []
    
    base_admissions = 100
    base_supplies = 10000 
    
    for i in range(100):
        if i < 30:
            current_admin = base_admissions + int(np.random.uniform(-5, 10))
            current_supplies = base_supplies - int(np.random.uniform(10, 50))
            status = "STABLE"
            twin_sync = "100.0%"
        elif i >= 30 and i < 70:
            current_admin = base_admissions + int((i - 30) * (15 * disaster_severity)) + int(np.random.uniform(-20, 50))
            current_supplies = base_supplies - int((i - 30) * (200 * disaster_severity)) - int(np.random.uniform(100, 500))
            status = "DISASTER SHOCK DETECTED"
            twin_sync = f"{np.random.uniform(98.5, 99.9):.1f}%"
        else:
            current_admin = current_admin + int(np.random.uniform(-20, 20))
            current_supplies = current_supplies + int(np.random.uniform(1000, 3000)) 
            status = "AUTONOMOUS REROUTING ACTIVE"
            twin_sync = "100.0%"
            
        current_supplies = max(0, current_supplies)
            
        admission_rates.append(current_admin)
        medical_supplies.append(current_supplies)
        
        metric_admissions.metric("Acute Care Admissions/hr", f"{current_admin:,}")
        metric_supplies.metric("Critical Medical Supply Index", f"{current_supplies:,} Units")
        metric_twin.metric("Digital Twin Sync Fidelity", twin_sync, "AWS Kinesis Link")
        
        if status == "DISASTER SHOCK DETECTED":
            metric_status.metric("Network Orchestration", "PREDICTING COLLAPSE", "High Risk")
        elif status == "AUTONOMOUS REROUTING ACTIVE":
            metric_status.metric("Network Orchestration", "LOGISTICS DIVERTED", "Recovering")
        else:
            metric_status.metric("Network Orchestration", "STANDARD FLOW", "Normal")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=admission_rates, mode='lines', name='Patient Admission Rate', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=medical_supplies, mode='lines', name='Medical Supply Index', yaxis='y2', line=dict(color='blue', dash='dot')))
        
        fig.update_layout(
            title="Disaster e-Health Digital Twin: Mass-Casualty Inflow vs Healthcare Logistics Outflow",
            xaxis=dict(title="High-Frequency Crisis Timeline"),
            yaxis=dict(title="Patient Admissions"),
            yaxis2=dict(title="Supply Index", overlaying='y', side='right', range=[0, 10500]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "DISASTER SHOCK DETECTED" and i == 30:
            log_placeholder.error(f"CRISIS ALERT: Severe disaster shock detected at {time_steps[i].strftime('%H:%M:%S')}. Patient admissions breaching hospital capacity. Digital Twin forecasting imminent supply chain failure.")
        elif status == "AUTONOMOUS REROUTING ACTIVE" and i == 70:
            log_placeholder.success(f"ORCHESTRATION SUCCESS: Machine learning inference engine successfully rerouted cross-regional medical logistics to the affected zone. Supply index stabilizing.")
        elif status == "STABLE" and i % 5 == 0:
            log_placeholder.info(f"Log: Healthcare IoT telemetry tick {i} ingested. Digital Twin operating in perfect harmony with physical reality.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless e-Health pipeline successfully maintained Digital Twin fidelity and optimized medical logistics during a catastrophic disaster shock.")
else:
    st.info("Click 'Initialize e-Health Digital Twin' in the sidebar to simulate high-velocity disaster informatics data ingestion.")