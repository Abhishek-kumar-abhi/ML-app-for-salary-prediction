# 💰 Salary Prediction ML Web App

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

## 📤 Deploy on Streamlit Cloud (Recommended)

### Step 1: Prepare Repository
```bash
git add .
git commit -m "Production-ready Streamlit app"
git push origin main
```

### Step 2: Deploy
1. Go to [**share.streamlit.io**](https://share.streamlit.io)
2. Click **"New app"**
3. Connect your GitHub account
4. Select repository and branch
5. Main file path: `streamlit_app.py`
6. Click **"Deploy"**

✅ **Done!** App is live in 2 minutes.

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t salary-app .
```

### Run Locally  
```bash
docker run -p 8501:8501 salary-app
```

### Deploy to Cloud
- **Azure Container Instances:** `az container create ...`
- **AWS ECS/Fargate:** Push to ECR
- **Google Cloud Run:** `gcloud run deploy ...`

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

## 🌐 Public URL

Once deployed on Streamlit Cloud, your app will have a public URL:
```
https://your-username-salary-app.streamlit.app/
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Ensure `model.pkl` in root directory |
| Import errors | Run `pip install -r requirements.txt` |
| Port in use | `streamlit run streamlit_app.py --server.port 8502` |
| Slow startup | First run caches model (~5s) |

## 📝 License

MIT License - Feel free to modify and deploy

## 📞 Support

For issues with:
- **Streamlit:** [streamlit.io/docs](https://streamlit.io/docs)
- **Deployment:** Check platform-specific docs
- **ML Model:** Verify `model.pkl` compatibility

---

**✨ Ready to deploy?** Follow Streamlit Cloud steps above!

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub account
4. Select your repository
5. Set main file path to: `streamlit_app.py`
6. Click "Deploy"

**That's it!** Your app is live.

## 📁 Project Structure

```
.
├── streamlit_app.py          # Main Streamlit app (use this!)
├── apps.py                   # Alternative Streamlit app
├── app.py                    # Legacy Flask app (not used)
├── model.pkl                 # Trained ML model
├── requirements.txt          # Python dependencies (optimized)
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🔧 Configuration

Edit `.streamlit/config.toml` to customize:
- Theme colors
- Port number
- Logging level
- Server behavior

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | 2.2.3 | Numerical computing |
| scikit-learn | 1.6.1 | ML model predictions |
| streamlit | 1.42.1 | Web UI framework |

## 🐛 Troubleshooting

### Model file not found
- Ensure `model.pkl` is in the project root
- Check file permissions

### Import errors
```bash
pip install --upgrade -r requirements.txt
```

### Port already in use
```bash
streamlit run streamlit_app.py --server.port 8502
```

## 🌐 Environment Variables (Optional)

For Streamlit Cloud, add secrets in the dashboard:
- No required environment variables for basic functionality

## 📝 License

MIT License - Feel free to use and modify

## 👨‍💻 Author

Created with ❤️ for salary predictions

---

**Ready to deploy?** Follow the "Deploy on Streamlit Cloud" section above!
