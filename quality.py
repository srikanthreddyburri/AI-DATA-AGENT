import pandas as pd
import numpy as np


def missing_value_analysis(df):

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum().values,
        "Missing Percentage": (
            df.isnull().mean().values * 100
        ).round(2)
    })


    missing = missing[
        missing["Missing Count"] > 0
    ]


    return missing



def duplicate_analysis(df):

    duplicates = df.duplicated().sum()

    return {
        "duplicate_rows": duplicates,
        "duplicate_percentage":
            round(
                (duplicates / len(df)) * 100,
                2
            )
    }



def constant_columns(df):

    constant = []

    for col in df.columns:

        if df[col].nunique() <= 1:
            constant.append(col)


    return constant



def outlier_analysis(df):

    outlier_summary = []


    numeric_columns = (
        df.select_dtypes(
            include=np.number
        )
        .columns
    )


    for col in numeric_columns:


        Q1 = df[col].quantile(0.25)

        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1


        lower = Q1 - 1.5 * IQR

        upper = Q3 + 1.5 * IQR


        outliers = df[
            (df[col] < lower) |
            (df[col] > upper)
        ].shape[0]


        if outliers > 0:

            outlier_summary.append({

                "Column": col,

                "Outliers": outliers,

                "Percentage":
                round(
                    (outliers / len(df))*100,
                    2
                )

            })


    return pd.DataFrame(outlier_summary)



def quality_report(df):

    report = {}


    report["missing"] = (
        missing_value_analysis(df)
    )


    report["duplicates"] = (
        duplicate_analysis(df)
    )


    report["constant_columns"] = (
        constant_columns(df)
    )


    report["outliers"] = (
        outlier_analysis(df)
    )


    return report