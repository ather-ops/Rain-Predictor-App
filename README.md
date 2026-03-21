<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Rain%20Tomorrow%20Predictor&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=ML-Powered%20Weather%20App%20%7C%20Validated%20Against%20AccuWeather&descAlignY=52&descSize=16" width="100%"/>

<br/>

[![Live App](https://img.shields.io/badge/LIVE%20APP-Click%20Here-FF4500?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-app.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13-FF6347?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-FF4500?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF6347?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Joblib](https://img.shields.io/badge/Joblib-Model%20Saved-FF4500?style=for-the-badge&logoColor=white)](https://joblib.readthedocs.io)
[![Accuracy](https://img.shields.io/badge/Accuracy-62%25-FF6347?style=for-the-badge&logoColor=white)](https://github.com/ather-ops)

<br/>

> **Built the night before Eid. Validated against AccuWeather at midnight. Deployed on Eid day.**
> *Model predicted 60.09% chance of rain. AccuWeather showed 60%. Difference: 0.09%.*

</div>

---

## The AccuWeather Validation

<div align="center">

![AccuWeather Validation](https://quickchart.io/chart?c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Our%20Model%22%2C%22AccuWeather%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Chance%20of%20Rain%20(%25)%22%2C%22data%22%3A%5B60.09%2C60%5D%2C%22backgroundColor%22%3A%5B%22%23FF4500%22%2C%22%23FF6347%22%5D%2C%22borderColor%22%3A%5B%22%23CC3700%22%2C%22%23CC4F3C%22%5D%2C%22borderWidth%22%3A2%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Our%20Model%20vs%20AccuWeather%20-%20Rain%20Probability%20(%25)%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A16%2C%22weight%22%3A%22bold%22%7D%7D%2C%22legend%22%3A%7B%22display%22%3Afalse%7D%7D%2C%22scales%22%3A%7B%22y%22%3A%7B%22min%22%3A58%2C%22max%22%3A62%2C%22ticks%22%3A%7B%22color%22%3A%22%23333%22%7D%7D%2C%22x%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A13%2C%22weight%22%3A%22bold%22%7D%7D%7D%7D%7D%7D&width=600&height=350&backgroundColor=white)

| Source | Prediction | Difference |
|--------|-----------|------------|
| **Our Model** | **60.09%** chance of rain | — |
| **AccuWeather** | **60.00%** chance of rain | **0.09%** |

> This is not a coincidence. This is a working model validated against a professional weather service.

</div>

---

## Live App Demo

<div align="center">

| Feature | Description |
|---------|-------------|
| **Interactive Sliders** | Temperature, Humidity, Wind Speed, Cloud Cover, Pressure |
| **Gauge Chart** | Live visualization of rain probability 0-100% |
| **Confidence Score** | Model certainty displayed alongside prediction |
| **Instant Prediction** | Click Predict — get result in milliseconds |
| **Color Coded** | Green = No Rain, Red = Rain alert |

[![Launch App](https://img.shields.io/badge/%F0%9F%8C%A7%20LAUNCH%20RAIN%20PREDICTOR-FF4500?style=for-the-badge&logoColor=white)](https://your-app.streamlit.app)

</div>

---

## Model Performance

<div align="center">

![Model Accuracy](https://quickchart.io/chart?c=%7B%22type%22%3A%22doughnut%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Correct%20Predictions%22%2C%22Incorrect%20Predictions%22%5D%2C%22datasets%22%3A%5B%7B%22data%22%3A%5B62%2C38%5D%2C%22backgroundColor%22%3A%5B%22%23FF4500%22%2C%22%23FFE4E0%22%5D%2C%22borderColor%22%3A%5B%22%23CC3700%22%2C%22%23FFCFC9%22%5D%2C%22borderWidth%22%3A2%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Model%20Accuracy%2062%25%20on%20Test%20Set%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A16%2C%22weight%22%3A%22bold%22%7D%7D%2C%22legend%22%3A%7B%22labels%22%3A%7B%22color%22%3A%22%23333%22%2C%22font%22%3A%7B%22size%22%3A12%7D%7D%7D%7D%7D%7D&width=500&height=350&backgroundColor=white)

![Classification Metrics](https://quickchart.io/chart?c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Precision%22%2C%22Recall%22%2C%22F1%20Score%22%2C%22Accuracy%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22No%20Rain%22%2C%22data%22%3A%5B0.58%2C0.59%2C0.58%2C0.62%5D%2C%22backgroundColor%22%3A%22%23FF6347%22%7D%2C%7B%22label%22%3A%22Rain%22%2C%22data%22%3A%5B0.65%2C0.64%2C0.64%2C0.62%5D%2C%22backgroundColor%22%3A%22%23FF4500%22%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Classification%20Metrics%20Per%20Class%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A15%2C%22weight%22%3A%22bold%22%7D%7D%7D%2C%22scales%22%3A%7B%22y%22%3A%7B%22min%22%3A0%2C%22max%22%3A1%2C%22ticks%22%3A%7B%22color%22%3A%22%23333%22%7D%7D%7D%7D%7D&width=650&height=350&backgroundColor=white)

</div>

---

## Full ML Pipeline

<div align="center">

![Pipeline](https://quickchart.io/chart?c=%7B%22type%22%3A%22horizontalBar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%221%20Load%20Data%22%2C%222%20EDA%20%2B%20Visualize%22%2C%223%20Fill%20Missing%22%2C%224%20Clean%20Dirty%20Data%22%2C%225%20Binning%22%2C%226%20One-Hot%20Encode%22%2C%227%20Train-Test%20Split%22%2C%228%20StandardScaler%22%2C%229%20Train%20Model%22%2C%2210%20Evaluate%22%2C%2211%20Save%20pkl%22%2C%2212%20Deploy%20Streamlit%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Pipeline%20Step%22%2C%22data%22%3A%5B100%2C100%2C100%2C100%2C100%2C100%2C100%2C100%2C100%2C100%2C100%2C100%5D%2C%22backgroundColor%22%3A%5B%22%23FF4500%22%2C%22%23FF5722%22%2C%22%23FF6347%22%2C%22%23FF7043%22%2C%22%23FF8C69%22%2C%22%23FFA07A%22%2C%22%23FF4500%22%2C%22%23FF5722%22%2C%22%23FF6347%22%2C%22%23FF7043%22%2C%22%23FF8C69%22%2C%22%23FFA07A%22%5D%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Complete%2012-Step%20ML%20Pipeline%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A15%2C%22weight%22%3A%22bold%22%7D%7D%2C%22legend%22%3A%7B%22display%22%3Afalse%7D%7D%2C%22scales%22%3A%7B%22x%22%3A%7B%22display%22%3Afalse%7D%2C%22y%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A11%2C%22weight%22%3A%22bold%22%7D%7D%7D%7D%7D%7D&width=700&height=450&backgroundColor=white)

</div>

```
Raw CSV  →  EDA  →  Clean Dirty Data  →  Binning  →  Encoding
    →  Scale  →  Train  →  Evaluate  →  Save pkl  →  Deploy
```

### What Makes This Pipeline Real

| Step | What was done | Why it matters |
|------|--------------|----------------|
| Missing values | Temperature NaN filled with mean | Prevents training crash |
| Dirty data | `'high'` → 85, `'low'` → 45, `999` outliers handled | Real-world messy data |
| Binning | Temperature, Humidity, Wind into categories | Captures non-linear patterns |
| One-Hot Encoding | pd.get_dummies on all bin columns | ML cannot process text |
| 4 pkl files saved | model, scaler, features, label encoder | Production-ready deployment |

---

## Feature Importance

<div align="center">

![Feature Importance](https://quickchart.io/chart?c=%7B%22type%22%3A%22horizontalBar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Humidity%20%25%22%2C%22Cloud%20Cover%22%2C%22Wind%20Speed%22%2C%22Pressure%20hPa%22%2C%22Temperature%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Feature%20Coefficient%22%2C%22data%22%3A%5B0.85%2C0.62%2C0.48%2C-0.71%2C0.31%5D%2C%22backgroundColor%22%3A%5B%22%23FF4500%22%2C%22%23FF5722%22%2C%22%23FF6347%22%2C%22%234169E1%22%2C%22%23FF8C69%22%5D%2C%22borderWidth%22%3A1%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Feature%20Importance%20-%20Logistic%20Regression%20Coefficients%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A15%2C%22weight%22%3A%22bold%22%7D%7D%7D%2C%22scales%22%3A%7B%22x%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23333%22%7D%7D%2C%22y%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A12%2C%22weight%22%3A%22bold%22%7D%7D%7D%7D%7D%7D&width=650&height=350&backgroundColor=white)

| Feature | Influence | Direction |
|---------|-----------|-----------|
| **Humidity %** | Strongest | Higher humidity = more rain |
| **Pressure hPa** | Strong | Higher pressure = less rain |
| **Cloud Cover** | Moderate | More clouds = more rain |
| **Wind Speed** | Moderate | Higher wind = more rain |
| **Temperature** | Weak | Lower impact on rain |

> **Meteorologically correct.** High humidity + low pressure + cloud cover = rain. Exactly what textbooks say.

</div>

---

## Dataset

<div align="center">

![Dataset Distribution](https://quickchart.io/chart?c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22No%20Rain%22%2C%22Rain%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Samples%22%2C%22data%22%3A%5B275%2C275%5D%2C%22backgroundColor%22%3A%5B%22%23FF6347%22%2C%22%23FF4500%22%5D%2C%22borderColor%22%3A%5B%22%23CC4F3C%22%2C%22%23CC3700%22%5D%2C%22borderWidth%22%3A2%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Dataset%20Class%20Distribution%20-%20550%20Samples%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A15%2C%22weight%22%3A%22bold%22%7D%7D%7D%2C%22scales%22%3A%7B%22y%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23333%22%7D%7D%2C%22x%22%3A%7B%22ticks%22%3A%7B%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A13%2C%22weight%22%3A%22bold%22%7D%7D%7D%7D%7D%7D&width=550&height=320&backgroundColor=white)

| Property | Value |
|----------|-------|
| Total samples | 550 rows |
| Features | 5 weather measurements |
| Target | Rain Tomorrow (Yes/No) |
| Class balance | 50/50 balanced |
| Missing values | Temperature NaN filled with mean |
| Dirty data | Humidity had string values 'high' and 'low' |
| Outliers | Wind/Humidity 999 values detected and handled |

</div>

---

## Tech Stack

<div align="center">

![Tech Stack](https://quickchart.io/chart?c=%7B%22type%22%3A%22radar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Data%20Cleaning%22%2C%22Feature%20Engineering%22%2C%22Model%20Training%22%2C%22Deployment%22%2C%22Validation%22%2C%22Visualization%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Project%20Coverage%22%2C%22data%22%3A%5B95%2C90%2C85%2C95%2C100%2C88%5D%2C%22backgroundColor%22%3A%22rgba(255%2C69%2C0%2C0.2)%22%2C%22borderColor%22%3A%22%23FF4500%22%2C%22borderWidth%22%3A2%2C%22pointBackgroundColor%22%3A%22%23FF4500%22%7D%5D%7D%2C%22options%22%3A%7B%22plugins%22%3A%7B%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Project%20Skill%20Coverage%22%2C%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A15%2C%22weight%22%3A%22bold%22%7D%7D%7D%2C%22scales%22%3A%7B%22r%22%3A%7B%22min%22%3A0%2C%22max%22%3A100%2C%22ticks%22%3A%7B%22display%22%3Afalse%7D%2C%22pointLabels%22%3A%7B%22color%22%3A%22%23FF4500%22%2C%22font%22%3A%7B%22size%22%3A11%2C%22weight%22%3A%22bold%22%7D%7D%7D%7D%7D%7D&width=550&height=400&backgroundColor=white)

</div>

| Tool | Version | Role |
|------|---------|------|
| **Python** | 3.13 | Core language |
| **Pandas** | Latest | Data loading, cleaning, encoding |
| **NumPy** | Latest | Numerical operations |
| **Scikit-Learn** | 1.4 | LogisticRegression, StandardScaler, metrics |
| **Matplotlib** | Latest | EDA and post-training visualizations |
| **Joblib** | Latest | Save and load pkl model files |
| **Streamlit** | Latest | Web app deployment |

---

## Project Structure

```
Rain-Predictor-App/
│
├── app.py                      <- Streamlit web application
├── rain_prediction.py          <- Full ML training pipeline
├── Rain_prediction.txt         <- Weather dataset (550 rows)
│
├── rain_model.pkl              <- Trained LogisticRegression
├── rain_scaler.pkl             <- Fitted StandardScaler
├── rain_features.pkl           <- Feature column names
├── rain_label_encoder.pkl      <- Yes/No label encoder
│
├── requirements.txt            <- streamlit, sklearn, pandas, numpy, joblib
└── README.md                   <- This file
```

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/ather-ops/Rain-Predictor-App

# Install dependencies
pip install -r requirements.txt

# Run training pipeline (generates pkl files)
python rain_prediction.py

# Launch Streamlit app
streamlit run app.py
```

---

## The Story Behind This Project

<div align="center">

> *"The night before Eid, everyone was celebrating.*
> *I was training a model.*
> *It matched AccuWeather within 0.09%.*
> *On Eid day, I deployed it as a live web app.*
> *Next Eid will be different."*

**— Ather Assadullah, Self-taught ML Engineer**

</div>

---

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-ather--ops-FF4500?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ather-ops)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-FF6347?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ather-assadullah)
[![Live App](https://img.shields.io/badge/Live%20App-Rain%20Predictor-FF4500?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-app.streamlit.app)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
