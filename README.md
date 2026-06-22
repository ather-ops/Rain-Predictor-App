# Rain Tomorrow Predictor

A machine learning web app that predicts the probability of rain based on weather inputs. Built with Logistic Regression and deployed via Streamlit.

**Live App:** [your-app.streamlit.app](https://your-app.streamlit.app)

---

## About

You input five weather measurements — temperature, humidity, wind speed, cloud cover, and pressure — and the model returns a probability of rain tomorrow. The UI shows a live gauge chart, a confidence score, and a color-coded result (green = no rain, red = rain).

---

## Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 62% |
| Precision (Rain) | 0.65 |
| Recall (Rain) | 0.64 |
| F1 Score (Rain) | 0.64 |
| Dataset | 550 samples, 50/50 balanced |

The model is trained on a 550-row dataset with equal rain and no-rain samples. Logistic Regression was chosen for interpretability — feature coefficients map directly to meteorological logic (high humidity and low pressure increase rain probability).

---

## Tech Stack

| Tool | Role |
|------|------|
| Python 3.13 | Core language |
| Pandas / NumPy | Data cleaning and preprocessing |
| Scikit-Learn | Model training, scaling, metrics |
| Matplotlib | EDA visualizations |
| Joblib | Saving and loading model files |
| Streamlit | Web app deployment |

---

## How to Run

```bash
git clone https://github.com/ather-ops/Rain-Predictor-App
cd Rain-Predictor-App
pip install -r requirements.txt

# Run training pipeline (generates pkl files)
python rain_prediction.py

# Launch app
streamlit run app.py
```

---

## License

MIT
