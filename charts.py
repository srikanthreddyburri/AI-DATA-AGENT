import matplotlib.pyplot as plt
import pandas as pd


def missing_values_chart(df):

    missing = (
        df.isnull()
        .sum()
    )


    missing = missing[
        missing > 0
    ]


    if len(missing) == 0:

        return None



    fig, ax = plt.subplots(
        figsize=(8,4)
    )


    missing.plot(
        kind="bar",
        ax=ax
    )


    ax.set_title(
        "Missing Values by Column"
    )


    ax.set_ylabel(
        "Count"
    )


    ax.set_xlabel(
        "Columns"
    )


    plt.xticks(
        rotation=45
    )


    return fig




def numeric_distribution(df):


    numeric_columns = (
        df.select_dtypes(
            include="number"
        )
        .columns
    )


    charts = {}



    for col in numeric_columns:


        fig, ax = plt.subplots(
            figsize=(6,4)
        )


        df[col].hist(
            ax=ax
        )


        ax.set_title(
            f"{col} Distribution"
        )


        ax.set_xlabel(
            col
        )


        ax.set_ylabel(
            "Frequency"
        )


        charts[col] = fig



    return charts




def correlation_heatmap(df):


    numeric_df = (
        df.select_dtypes(
            include="number"
        )
    )


    if numeric_df.shape[1] < 2:

        return None



    fig, ax = plt.subplots(
        figsize=(8,6)
    )


    correlation = (
        numeric_df.corr()
    )


    image = ax.imshow(
        correlation
    )


    ax.set_xticks(
        range(len(correlation.columns))
    )


    ax.set_yticks(
        range(len(correlation.columns))
    )


    ax.set_xticklabels(
        correlation.columns,
        rotation=45
    )


    ax.set_yticklabels(
        correlation.columns
    )


    fig.colorbar(
        image
    )


    ax.set_title(
        "Correlation Heatmap"
    )


    return fig