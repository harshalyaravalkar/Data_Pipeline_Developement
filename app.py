# simple ETL pipeline (adapted for diabetes dataset)

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn import datasets


# ------------------ LOAD ------------------
def load_data():
    try:
        data = datasets.load_diabetes()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        print("dataset loaded")
        return df
    except:
        print("error loading dataset")
        return None


# ------------------ CLEAN + TRANSFORM ------------------
def process_data(df):

    print("processing started...")

    if df is None or df.shape[0] == 0:
        print("no data to process")
        return None

    num_cols = df.columns

    pipe = Pipeline([
        ("fill", SimpleImputer(strategy="mean")),  
        ("scale", StandardScaler())
    ])

    final_data = pipe.fit_transform(df)

    print("done processing")

    return final_data


# ------------------ SAVE ------------------
def save_output(data, out_file="cleaned.csv"):
    try:
        if data is None:
            return

        df = pd.DataFrame(data)
        df.to_csv(out_file, index=False)

        print("saved to", out_file)

    except Exception as e:
        print("error while saving:", e)


# ------------------ RUN EVERYTHING ------------------
def run():
    df = load_data()

    if df is None:
        return

    processed = process_data(df)
    save_output(processed)


# ------------------ ENTRY ------------------
if __name__ == "__main__":
    run()