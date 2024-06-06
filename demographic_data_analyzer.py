import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().round(1)

    # What is the average age of men?
    men=df[df['sex']== 'Male']
    average_age_men = men['age'].mean().round(1)
    

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_df= df[df['education']== 'Bachelors']
    bachelors_count= bachelors_df.shape[0]
    total_count=df.shape[0]

    
    percentage_bachelors = round((bachelors_count/total_count)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education']== 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    # percentage with salary >50K
    higher_count= higher_education.shape[0]
    higher_ed_more=  higher_education[higher_education['salary'] == '>50K']
    count_rich_higher= higher_ed_more.shape[0]

    higher_education_rich = round ((count_rich_higher/higher_count)*100,1)

    lower_count=lower_education.shape[0]
    lower_ed_more= lower_education[lower_education['salary']== '>50K']
    count_rich_lower=lower_ed_more.shape[0]


    lower_education_rich = round((count_rich_lower/lower_count)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    
    min_work_hours = df['hours-per-week'].min().round(1)


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    peoplemin=df[df['hours-per-week']== min_work_hours]
    num_min_workers = peoplemin.shape[0]


    rich=peoplemin[peoplemin['salary']=='>50K']
    count_rich=rich.shape[0]

    rich_percentage = round((count_rich/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    peoplemore50=df[df['salary']=='>50K']
    peoplemore50percountry=peoplemore50['native-country'].value_counts()
    totalpeoplepercountry=df['native-country'].value_counts() 
    percentagepercountry= round((peoplemore50percountry/totalpeoplepercountry)*100,1)
    

    highest_earning_country = percentagepercountry.idxmax()
    highest_earning_country_percentage = percentagepercountry.max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    richindia=peoplemore50[peoplemore50['native-country']=='India']
    occu= richindia['occupation'].value_counts()

    top_IN_occupation = occu.idxmax()




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


calculate_demographic_data(print_data=True)