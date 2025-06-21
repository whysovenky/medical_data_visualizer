# 🩺 Medical Data Visualizer

Analyze and visualize patient health data using **Pandas**, **Seaborn**, and **Matplotlib**.  
This project is part of the **freeCodeCamp Data Analysis with Python** certification.

---

## 📊 Project Overview

You’ll work with real patient data from medical exams to:
- Calculate **BMI** and flag **overweight** individuals
- Normalize values like **cholesterol** and **glucose**
- Visualize lifestyle impact using a **categorical plot**
- Show medical data relationships using a **correlation heatmap**

---

## 🗂 Dataset Info

- File: `medical_examination.csv`
- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- Rows = Patients, Columns = Features

**Key Columns:**

| Feature           | Column      | Description                          |
|------------------|-------------|--------------------------------------|
| Age              | `age`       | In days                              |
| Height           | `height`    | In cm                                |
| Weight           | `weight`    | In kg                                |
| Systolic BP      | `ap_hi`     | Systolic pressure                    |
| Diastolic BP     | `ap_lo`     | Diastolic pressure                   |
| Cholesterol      | `cholesterol`| 1 (normal), 2 (high), 3 (very high) |
| Glucose          | `gluc`      | 1 (normal), 2 (high), 3 (very high) |
| Smoking          | `smoke`     | Binary                               |
| Alcohol          | `alco`      | Binary                               |
| Physical Activity| `active`    | Binary                               |
| Cardiovascular Disease | `cardio` | 0 = No, 1 = Yes                   |

---

## 📌 What This Project Does

✅ Adds BMI calculation and flags overweight  
✅ Normalizes cholesterol/glucose (0 = good, 1 = bad)  
✅ Uses melted DataFrame to generate a **Seaborn categorical plot**  
✅ Cleans outliers and builds a **correlation heatmap**

---

## 📈 Visual Outputs

### 🟦 `catplot.png`

Shows lifestyle/health indicators by cardiovascular disease status:

| Feature        | Good (0) vs Bad (1) |
|----------------|---------------------|
| Cholesterol    | 🩸                  |
| Glucose        | 🍬                  |
| Smoking        | 🚬                  |
| Alcohol        | 🍷                  |
| Physical activity | 🏃‍♂️            |
| Overweight     | ⚖️                  |

---

### 🔥 `heatmap.png`

Displays correlation between all health variables after cleaning the data:

- Diastolic must be ≤ systolic
- Height/weight trimmed between 2.5%–97.5%

---

## 🧪 How to Run

```bash
pip install pandas matplotlib seaborn
python3 main.py
