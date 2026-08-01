import pandas as pd



def completeness_score(df):

    total_cells = df.shape[0] * df.shape[1]

    missing_cells = df.isnull().sum().sum()


    score = (
        1 - (missing_cells / total_cells)
    ) * 100


    return round(score, 2)



def uniqueness_score(df):

    total_rows = len(df)

    duplicate_rows = (
        df.duplicated()
        .sum()
    )


    score = (
        1 - (duplicate_rows / total_rows)
    ) * 100


    return round(score, 2)



def consistency_score(df):

    issues = 0


    # Check constant columns

    for col in df.columns:

        if df[col].nunique() <= 1:

            issues += 1



    total_columns = len(df.columns)


    score = (
        1 - (issues / total_columns)
    ) * 100


    return round(score,2)



def validity_score(df):

    invalid = 0


    numeric_columns = (
        df.select_dtypes(
            include="number"
        )
        .columns
    )


    for col in numeric_columns:

        if df[col].isnull().sum() > 0:

            invalid += 1



    total_numeric = len(numeric_columns)


    if total_numeric == 0:

        return 100



    score = (
        1 - (invalid / total_numeric)
    ) * 100


    return round(score,2)



def calculate_quality_score(df):


    completeness = completeness_score(df)

    uniqueness = uniqueness_score(df)

    consistency = consistency_score(df)

    validity = validity_score(df)



    overall = (

        completeness * 0.30 +

        uniqueness * 0.25 +

        consistency * 0.25 +

        validity * 0.20

    )


    return {

        "Overall Score": round(overall,2),

        "Completeness": completeness,

        "Uniqueness": uniqueness,

        "Consistency": consistency,

        "Validity": validity

    }