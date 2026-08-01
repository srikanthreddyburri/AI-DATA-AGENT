import pandas as pd


def load_dataset(file):

    try:
        df = pd.read_csv(file)
        return df

    except Exception as e:
        return None



def dataset_profile(df):

    profile = {}

    # Shape
    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]


    # Column names
    profile["column_names"] = list(df.columns)


    # Data types
    profile["data_types"] = df.dtypes.astype(str)


    # Memory usage
    profile["memory_usage"] = (
        df.memory_usage(deep=True)
        .sum()
        /
        (1024 * 1024)
    )


    # Missing values
    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values,
        "Missing Percentage": (
            df.isnull().mean().values * 100
        ).round(2)
    })

    profile["missing_values"] = missing


    return profile