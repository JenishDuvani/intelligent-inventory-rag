import pandas as pd

def read_uploaded_file(uploaded_file) -> str:
    """
    Reads uploaded CSV or TXT and converts to plain text
    """
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.to_string(index=False)

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file type")
