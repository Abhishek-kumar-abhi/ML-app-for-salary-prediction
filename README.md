# 💰 Salary Prediction ML Web App

Application URL: https://salarypredictorabhi.streamlit.app/

A machine learning web application that predicts salary based on years of work experience using Streamlit.

## 🚀 Features

- **ML Model**: Trained scikit-learn regression model
- **Web UI**: Streamlit-based user interface
- **Fast Predictions**: Real-time salary predictions
- **Cloud Ready**: Optimized for Streamlit Cloud deployment
- **Production Optimized**: Minimal dependencies, fast startup

## 📁 Folder Structure

```
salary-prediction-app/
├── streamlit_app.py              # 🎯 Main Streamlit application
├── model.pkl                     # 📊 Pre-trained ML model
├── Salary_Data.csv               # 📈 Training dataset (reference)
├── requirements.txt              # 📦 Python dependencies (3 packages only!)
├── Dockerfile                    # 🐳 Docker container config
├── .streamlit/
│   └── config.toml              # ⚙️ Streamlit configuration
├── .gitignore                    # 🔒 Git ignore rules
└── README.md                     # 📖 This file
```

### ✨ What's NOT here (Removed for optimization)
- ❌ `templates/` & `static/` (Flask only)
- ❌ `app.py` & `apps.py` (Legacy Flask files)  
- ❌ Large Python packages (160→3 packages)
- ❌ Training scripts & artifacts
- ❌ Screenshots & temp files

## 📋 Prerequisites

- Python 3.9+
- `model.pkl` file (included)

## 🛠️ Local Installation & Setup

### 1️⃣ Clone & Enter Directory
```bash
git clone <your-repo-url>
cd salary-prediction-app
```

### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

```bash
streamlit run streamlit_app.py
```

**Result:** App opens at `http://localhost:8501`



## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | 2.2.3 | Numerical arrays |
| scikit-learn | 1.6.1 | ML predictions |
| streamlit | 1.42.1 | Web UI |

**Total size:** ~400MB (vs. 2GB before optimization)

## 🔧 Configuration

Edit `.streamlit/config.toml`:
- Theme colors
- Port settings
- Server behavior
- Logging level



## 📝 License

MIT License - Feel free to use and modify

## 👨‍💻 Author

Created by Abhishek Kumar

---
Feel free to try it and if any suggestions is there, share with me.

