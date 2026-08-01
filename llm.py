import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()



def generate_insight(
        profile,
        quality,
        score
):


    client = OpenAI(
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )



    prompt = f"""

You are an expert Data Quality Analyst.

Analyze this dataset quality report.

Dataset Profile:

Rows:
{profile['rows']}

Columns:
{profile['columns']}


Missing Values:

{quality['missing'].to_string()}



Duplicate Information:

{quality['duplicates']}



Constant Columns:

{quality['constant_columns']}



Outlier Information:

{quality['outliers'].to_string()}



Quality Score:

Overall:
{score['Overall Score']}%

Completeness:
{score['Completeness']}%

Uniqueness:
{score['Uniqueness']}%

Consistency:
{score['Consistency']}%

Validity:
{score['Validity']}%



Provide:

1. Overall data quality summary

2. Major issues detected

3. Recommended cleaning steps

4. Final conclusion



Keep the explanation simple and professional.

"""


    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role":"system",
                "content":
                "You are a senior data analyst."
            },

            {
                "role":"user",
                "content":prompt
            }

        ],

        temperature=0.3

    )


    return response.choices[0].message.content