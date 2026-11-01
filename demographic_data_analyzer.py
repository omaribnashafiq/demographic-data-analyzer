
from pathlib import Path

import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read the dataset relative to this file so it works from any working directory.
    data_path = Path(__file__).resolve().parent / "adult.data.csv"
    df = pd.read_csv(data_path)

    # 1. Number of people in each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df[
        df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentage of people without advanced education earning >50K
    lower_education = df[
        ~df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # 6. Minimum number of working hours per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of minimum-hour workers earning >50K
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Country with the highest percentage of people earning >50K
    rich_people = df[df["salary"] == ">50K"]

    country_rich_percentage = (
        rich_people["native-country"].value_counts()
        / df["native-country"].value_counts()
        * 100
    )

    highest_earning_country = country_rich_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_rich_percentage.max(), 1
    )

    # 9. Most popular occupation among people earning >50K in India
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    # Display results
    if print_data:
        print("Number of each race:")
        print(race_count)

        print("Average age of men:", average_age_men)

        print("Percentage with Bachelor's degree:",
              percentage_bachelors)

        print("Percentage with advanced education earning >50K:",
              higher_education_rich)

        print("Percentage without advanced education earning >50K:",
              lower_education_rich)

        print("Minimum working hours:", min_work_hours)

        print("Percentage of minimum-hour workers earning >50K:",
              rich_percentage)

        print("Country with highest earning percentage:",
              highest_earning_country)

        print("Percentage of high earners in that country:",
              highest_earning_country_percentage)

        print("Most popular occupation in India among high earners:",
              top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
