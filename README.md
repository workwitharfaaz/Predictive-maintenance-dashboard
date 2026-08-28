Unplanned machine breakdowns cause catastrophic delays and cost industries billions every year,  
while replacing parts on a rigid calendar schedule wastes perfectly good equipment.  
This project solves that problem by using Machine Learning to analyze live sensor data like: temperature and vibration.  
So, you can predict exactly when an engine will fail before it actually breaks.  
By converting complex data streams into clear web alerts, it allows operators to schedule repairs only when truly needed,  
eliminating costly surprises and keeping operations running smoothly.  

  
#  IoT Predictive Maintenance System

An end-to-end industrial IoT system that ingests simulated jet engine sensor telemetry, predicts Remaining Useful Life (RUL) using an XGBoost regression model, and delivers real-time failure alerts via an interactive Streamlit dashboard.  
  
## Problem Overview

Industrial operations face a costly trade-off between two traditional maintenance strategies:

* **Reactive Maintenance:** Running equipment until failure leads to sudden operational downtime, severe hardware damage, and safety risks.
* **Preventative Maintenance:** Replacing components on fixed calendar schedules results in wasted assets and unnecessary labor costs.

**Solution:** This project implements **Condition-Based Predictive Maintenance**. By monitoring time-series sensor degradation patterns (temperatures, pressures, shaft speeds), the system predicts the exact number of operational flight cycles an engine has left before failure—allowing engineers to schedule repairs only when necessary.  
  
## 🏗 System Architecture  
1. **Telemetry Streaming:** Simulates live flight cycles from the NASA C-MAPSS jet engine dataset.
2. **Feature Pipeline:** Filters out non-informative static sensor channels and standardizes high-variance features.
3. **Machine Learning Engine:** Predicts continuous Remaining Useful Life ($RUL$) using an XGBoost Regressor trained on engine degradation trajectories.
4. **Web Dashboard:** Streams live metrics, dynamically updates engine health visualizations, and triggers visual high-risk alerts when estimated $RUL \le 20$ cycles.
  
## 🛠 Tech Stack  
  
* **Language:** Python 3.9+
* **Data Processing & Manipulation:** Pandas, NumPy
* **Machine Learning & Serialization:** XGBoost, Joblib
* **Web Dashboard:** Streamlit
  

## 📂 Project Structure
├── train_FD001.txt  --->       # NASA C-MAPSS run-to-failure training dataset  
├── test_FD001.txt   --->       # NASA C-MAPSS test sensor stream  
├── RUL_FD001.txt    --->       # Ground-truth remaining useful life answer key  
├── train_model.py   --->       # Data preprocessing and XGBoost training pipeline  
├── app.py           --->       # Live Streamlit dashboard application  
├── model.pkl        --->       # Serialized XGBoost model artifact  
├── features.pkl     --->       # Saved feature schema array  
└── README.md        --->       # Project documentation  
  


<img width="1920" height="1080" alt="Screenshot 2026-08-28 154829" src="https://github.com/user-attachments/assets/3854c5c8-af5c-41ea-87db-6cd4bd33c815" />
<img width="1920" height="1080" alt="Screenshot 2026-08-28 154906" src="https://github.com/user-attachments/assets/ed83c79d-9f4c-44b5-beb9-f7ede94f54e9" />

