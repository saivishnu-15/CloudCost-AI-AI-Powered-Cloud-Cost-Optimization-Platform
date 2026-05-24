# 🚀 CloudCost AI – AI-Powered Cloud Cost Optimization Platform

CloudCost AI is a full-stack AI-powered FinOps platform that helps startups and DevOps teams reduce unnecessary cloud expenditure by detecting idle resources, analyzing infrastructure utilization, and recommending cost optimizations.

---

## 📌 Problem Statement

Engineering teams often overspend on AWS/GCP/Azure because:
- Idle cloud resources remain active
- Underutilized instances waste money
- Cloud spending is difficult to monitor manually

CloudCost AI solves this by continuously monitoring cloud infrastructure and providing AI-powered optimization recommendations.

---

# ✨ Features

✅ Cloud resource monitoring  
✅ Detect idle and underutilized services  
✅ AI-powered optimization insights  
✅ Estimated monthly savings  
✅ Future spending prediction  
✅ Full-stack dashboard  
✅ REST API backend using FastAPI  

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- Axios

## Backend
- FastAPI
- SQLAlchemy
- SQLite

## Concepts Used
- FinOps
- Cloud Cost Optimization
- AI-based Recommendations
- REST APIs

---

# 📷 Demo Features

## Cloud Resource Dashboard
Displays:
- EC2 instances
- RDS databases
- CPU utilization
- Monthly infrastructure cost

## AI Optimization Insights
Detects:
- Idle resources
- Underutilized services

Provides:
- Cost-saving recommendations
- Estimated savings
- Future cost predictions

---

# 📂 Project Structure

cloud_cost_ai/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   ├── cost_engine.py
│   ├── cloud.db
│
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── index.html
│   ├── public/
          favicon.svg
          icons.svg
│   └── src/
│       ├── App.jsx
│       ├── api.js
│       ├── main.jsx
│       └── components/
│           └── Dashboard.jsx
│
└── README.md

Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/cloudcost-ai.git

Backend Setup
cd backend

python -m uvicorn main:app --reload

http://127.0.0.1:8000

Frontend Setup
cd frontend

npm install

npm run dev

http://localhost:5173
