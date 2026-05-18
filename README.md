# Data_Pipeline_Developement

## Company Name
CODTECH IT SOLUTIONS

---

## Name
Harshal Laxman Yaravalkar

---

## Intern ID
CTIS8789

---

## Domain
Data Science

---

## Duration
4 Weeks

---

## Mentor
Neela Santhosh Kumar

---

# ETL Data Pipeline using Python and Scikit-learn

## Project Description

This project focuses on building a simple ETL (Extract, Transform, Load) data pipeline using Python, Pandas, and Scikit-learn. The main objective of the task was to automate the preprocessing and transformation of raw data so that it becomes suitable for machine learning and analytical tasks.

In many real-world machine learning projects, raw data cannot be directly used for prediction or analysis. Data often contains missing values, inconsistent formatting, unnecessary features, or unscaled numerical values. Because of this, preprocessing becomes an important step in the data science workflow. This project was designed to demonstrate how an ETL pipeline can simplify and automate these preprocessing operations.

For this task, the Diabetes dataset available from Scikit-learn was used. The dataset contains multiple numerical medical features commonly used for prediction and regression tasks. Since the dataset is already numerical, the project mainly focused on handling missing values and scaling the data using preprocessing pipelines.

The project was implemented using a modular structure where different stages of the ETL process were separated into functions. This improves readability and makes the pipeline reusable for other datasets in the future.

The first step in the pipeline was the extraction stage. In this stage, the dataset was loaded using Scikit-learn and converted into a Pandas DataFrame. After loading the data, basic validation checks were performed to ensure the dataset was correctly imported and contained usable rows and columns.

The second stage was the transformation phase. In this stage, preprocessing operations were performed using Scikit-learn pipelines. Missing values were handled using the `SimpleImputer` class with mean-based imputation. Although the Diabetes dataset did not contain major missing values, the imputation step was included to make the pipeline more practical and reusable for real-world datasets.

After handling missing values, numerical features were standardized using `StandardScaler`. Feature scaling is an important preprocessing step because it transforms features into a consistent scale, helping machine learning models perform more effectively. After scaling, the transformed values were centered around zero with a standard deviation close to one.

The transformation stage was implemented using Scikit-learn’s `Pipeline` functionality. Using pipelines helps reduce repetitive preprocessing code and keeps preprocessing steps organized in a clean workflow. Pipelines are widely used in machine learning systems because they improve maintainability and reduce errors during model training and testing.

The final stage of the project was the loading phase. After preprocessing and transformation, the processed data was exported into a CSV file named `cleaned.csv`. This output file can be directly used for machine learning model training or other analytical tasks.

The project demonstrates important concepts related to data engineering and preprocessing, including:
- automated preprocessing
- handling missing values
- feature scaling
- reusable ETL workflows
- modular Python programming

This task also helped in understanding how preprocessing pipelines are used in practical machine learning systems before model development begins.

The technologies used in this project include:
- Python
- Pandas
- NumPy
- Scikit-learn

Overall, this project successfully demonstrates the implementation of a basic ETL pipeline for preprocessing and transforming structured data using Python libraries commonly used in data science workflows.

---

# Project Structure

```bash
CODTECH-Task1-ETL-Pipeline/
│
├── etl_pipeline.py
├── cleaned.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

---

# How to Run

```bash
python app.py
```

After running the script, a processed CSV file named `cleaned.csv` will be generated automatically.

---

## Pipeline Execution

<img width="413" height="105" alt="Screenshot 2026-05-18 201326" src="https://github.com/user-attachments/assets/93262d83-1496-4e09-b3d7-4c2a764faeb1" />


---

## Dataset Transformation Result

<img width="1912" height="1017" alt="Screenshot 2026-05-18 202621" src="https://github.com/user-attachments/assets/68615abc-734a-432a-b307-35303f5a1b65" />

