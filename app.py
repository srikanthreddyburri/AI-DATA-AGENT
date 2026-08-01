import streamlit as st

from services.profiler import (
    load_dataset,
    dataset_profile
)

from services.quality import (
    quality_report
)

from services.score import (
    calculate_quality_score
)

from services.charts import (
    missing_values_chart,
    numeric_distribution,
    correlation_heatmap
)

from services.llm import (
    generate_insight
)


st.set_page_config(
    page_title="AI Data Quality Agent",
    layout="wide"
)


st.title(
    "🤖 AI Data Quality Agent"
)


uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)


if uploaded_file:


    df = load_dataset(uploaded_file)


    if df is not None:


        st.success(
            "Dataset uploaded successfully"
        )


        # =============================
        # DATA PREVIEW
        # =============================

        st.subheader(
            "Dataset Preview"
        )


        st.dataframe(
            df.head(10)
        )



        # =============================
        # PROFILING ENGINE
        # =============================

        profile = dataset_profile(df)



        st.subheader(
            "Dataset Overview"
        )


        col1, col2 = st.columns(2)



        with col1:

            st.metric(
                "Rows",
                profile["rows"]
            )


            st.metric(
                "Columns",
                profile["columns"]
            )



        with col2:

            st.metric(
                "Memory Usage",
                f"{profile['memory_usage']:.2f} MB"
            )



        st.subheader(
            "Column Names"
        )


        st.write(
            profile["column_names"]
        )



        st.subheader(
            "Data Types"
        )


        st.dataframe(
            profile["data_types"]
        )



        st.subheader(
            "Missing Values Analysis"
        )


        st.dataframe(
            profile["missing_values"]
        )



        # =============================
        # QUALITY ENGINE
        # =============================

        quality = quality_report(df)



        # =============================
        # SCORE ENGINE
        # =============================

        score = calculate_quality_score(df)



        # =============================
        # AI INSIGHT ENGINE
        # =============================

        with st.spinner(
            "Generating AI Data Analysis Report..."
        ):

            ai_insight = generate_insight(
                profile,
                quality,
                score
            )



        # =============================
        # CHART ENGINE
        # =============================

        missing_chart = missing_values_chart(df)

        distribution_charts = numeric_distribution(df)

        correlation_chart = correlation_heatmap(df)



        # =============================
        # QUALITY SCORE DASHBOARD
        # =============================


        st.subheader(
            "📊 Data Quality Score"
        )


        col1, col2, col3, col4, col5 = st.columns(5)



        with col1:

            st.metric(
                "Overall Score",
                f"{score['Overall Score']}%"
            )


        with col2:

            st.metric(
                "Completeness",
                f"{score['Completeness']}%"
            )


        with col3:

            st.metric(
                "Uniqueness",
                f"{score['Uniqueness']}%"
            )


        with col4:

            st.metric(
                "Consistency",
                f"{score['Consistency']}%"
            )


        with col5:

            st.metric(
                "Validity",
                f"{score['Validity']}%"
            )



        # =============================
        # AI REPORT
        # =============================

        st.subheader(
            "🧠 AI Data Analyst Report"
        )


        st.write(
            ai_insight
        )



        # =============================
        # VISUAL ANALYTICS
        # =============================


        st.subheader(
            "📈 Data Visualizations"
        )



        # Missing Values Chart

        st.write(
            "### Missing Values Chart"
        )


        if missing_chart:


            st.pyplot(
                missing_chart
            )


        else:


            st.success(
                "No missing values detected"
            )



        # Correlation Heatmap

        st.write(
            "### Correlation Analysis"
        )


        if correlation_chart:


            st.pyplot(
                correlation_chart
            )


        else:


            st.info(
                "Not enough numerical columns for correlation analysis"
            )



        # Distribution Charts

        st.write(
            "### Numerical Distributions"
        )


        if distribution_charts:


            for column, chart in distribution_charts.items():

                st.write(
                    f"#### {column}"
                )


                st.pyplot(
                    chart
                )


        else:


            st.info(
                "No numerical columns found"
            )



        # =============================
        # QUALITY DETAILS
        # =============================


        st.subheader(
            "🔍 Data Quality Analysis"
        )



        st.write(
            "### Duplicate Records"
        )


        st.json(
            quality["duplicates"]
        )



        st.write(
            "### Constant Columns"
        )


        if quality["constant_columns"]:


            st.warning(
                quality["constant_columns"]
            )


        else:


            st.success(
                "No constant columns found"
            )



        st.write(
            "### Outlier Detection"
        )


        if not quality["outliers"].empty:


            st.dataframe(
                quality["outliers"]
            )


        else:


            st.success(
                "No significant outliers detected"
            )



    else:


        st.error(
            "Unable to read file"
        )