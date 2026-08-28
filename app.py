import streamlit as st
import pandas as pd
import joblib
import time

# Load trained model and features
model = joblib.load('model.pkl')
features = joblib.load('features.pkl')

st.set_page_config(page_title="IoT Predictive Maintenance", layout="wide")
st.title("Jet Engine Predictive Maintenance Monitor")

# Sidebar Controls
st.sidebar.header("Control Panel")
engine_id = st.sidebar.number_input("Select Engine ID (1 - 100)", min_value=1, max_value=100, value=1)
run_sim = st.sidebar.button("Run Simulation")

# Load test dataset
col_names = ['unit_nr', 'time_cycles', 'setting_1', 'setting_2', 'setting_3'] + [f's_{i}' for i in range(1, 22)]
test_df = pd.read_csv('data/test_FD001.txt', sep=r'\s+', header=None, names=col_names)
engine_data = test_df[test_df['unit_nr'] == engine_id].sort_values('time_cycles')

# --- FIX: Reserve static layout spots BEFORE the loop starts ---
metrics_placeholder = st.empty()
chart_placeholder = st.empty()
alert_placeholder = st.empty()

if run_sim:
    chart_data = pd.DataFrame(columns=["Cycle", "Predicted RUL"])

    for idx, row in engine_data.iterrows():
        current_cycle = int(row['time_cycles'])
        input_data = pd.DataFrame([row[features]])
        predicted_rul = int(model.predict(input_data)[0])

        # 1. Update Metrics Box in place
        with metrics_placeholder.container():
            col1, col2 = st.columns(2)
            col1.metric("Current Flight Cycle", f"{current_cycle}")
            col2.metric("Predicted RUL", f"{predicted_rul} cycles")

        # 2. Update Warning Banner in place
        with alert_placeholder.container():
            if predicted_rul <= 20:
                st.error(f"⚠️ ALERT: Engine #{engine_id} requires immediate maintenance!")
            else:
                st.info("Status: Operational within safe parameters.")

        # 3. Update Chart in place
        new_row = pd.DataFrame([{"Cycle": current_cycle, "Predicted RUL": predicted_rul}])
        chart_data = pd.concat([chart_data, new_row], ignore_index=True)
        
        with chart_placeholder.container():
            st.line_chart(chart_data.set_index("Cycle"))

        time.sleep(0.1) # Smooth delay