import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = pd.Series(df['race']).value_counts()

    # What is the average age of men?

    sex_index = df.index[df['sex'] == 'Male'].tolist()
    men_age = []

    for i in sex_index:
        men_age.append(df['age'].loc[i])

    average_age_men = pd.Series(men_age).mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?

    baches = pd.Series(df['education']).value_counts()
    percentage_bachelors = ((baches['Bachelors'] * 100) / baches.sum()).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    sal_m50k = []
    sal_l50k = []
    for i in df['salary']:
        if i == '>50K':
            sal_m50k.append(i)
        else:
            sal_l50k.append(i)

    advc_ed_index = df.index[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].tolist()
    m50K = []

    for i in advc_ed_index:
        if df['salary'].loc[i] == '>50K':
            m50K.append(df['salary'].loc[i])

    percentage_advanceded_m50k = ((len(m50K) * 100) / len(advc_ed_index)).__round__(1)

    # What percentage of people without advanced education make more than 50K?
    not_advc_ed = df.index[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].tolist()
    not_aded_m50k = []

    for i in not_advc_ed:
        if df['salary'].loc[i] == '>50K':
            not_aded_m50k.append(df['salary'].loc[i])

    percentage_notadvanceded_m50k = ((len(not_aded_m50k) * 100) / len(not_advc_ed)).__round__(1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ((len(advc_ed_index) * 100) / len(df['education'])).__round__(1)
    lower_education = ((len(not_advc_ed) * 100) / len(df['education'])).__round__(1)

    # percentage with salary >50K
    higher_education_rich = percentage_advanceded_m50k
    lower_education_rich = percentage_notadvanceded_m50k

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_wor_50 = df[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)]
    num_min_wor = df[(df['hours-per-week'] == min_work_hours)]

    rich_percentage = ((len(num_min_wor_50) * 100) / len(num_min_wor)).__round__(1)

    # What country has the highest percentage of people that earn >50K?

    tota_per_country = df['native-country'].value_counts()
    s50K = df[(df['salary'] == '>50K')]
    high_ear_per_country = s50K['native-country'].value_counts()
    percentage = ((high_ear_per_country * 100) / tota_per_country)
    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = percentage.max().__round__(1)

    # Identify the most popular occupation for those who earn >50K in India.

    rich_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    rich_india_occupation = rich_india['occupation'].value_counts()

    top_IN_occupation = rich_india_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
