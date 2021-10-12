import time
import pandas as pd
import numpy as np

#Creating a dictionary containing the data sources for the three cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    #Initializing an empty city string
    city = ''
    #repeat this step untill we get the correct input from the user
    while city not in CITY_DATA.keys():
        print("\nPlease enter the city name of your choice:")
        print("\n a. Chicago b. New York City c. Washington")
        print('\nPlease enter full name of the city; not case sensitive (e.g. chicago or CHICAGO)')
        print('\nPlease maintain space for New York City (e.g. new york city or NeW York City)')
        #convert user input to lower case
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nPlease check your input, it does not follow city input format criteria ")
            print("\nRestarting - CITY?...")

    print("\nYou have chosen {} as your city".format(city.title()))

    #Creating a dictionary to store all the months including the 'all' option
    MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ''
    while month not in MONTH_DATA:
        print("\nPlease enter the month, to filter the data")
        print("\nPlease enter full month name; not case sensitive (e.g. january or JANUARY)")
        print("\nFull month name in title case (e.g. April)")
        print("\nif you want to see all months data please type 'all' or 'All' or 'ALL' ")
        month = input().lower()

        if month not in MONTH_DATA:
            print("\nInvalid input. Please try again. please check the month input format")
            print("\nRestarting - MONTH?...")

    print("\nYou have chosen {} as your month".format(month.title()))

    #Creating a list to store all the days including the 'all' option
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week to filter the data:")
        print("\nDay name; not case sensitive (e.g. monday or MONDAY)")
        print("\nOr day name in title case (e.g. Monday).")
        print("\n(You can also type 'all' or 'All' or 'ALL' to view data for all days in a week.)")
        day = input().lower()

        if day not in DAY_LIST:
            print("\nInvalid input. Please try again in one of the accepted day input formats.")
            print("\nRestarting - Day of the week? ...")

    print(f"\nYou have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*90)
    #Returning the city, month and day selections
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading data...")
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # create a dictionary to map numerical months to string
    d_month = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    # chang numerical month to string month
    df['month'] = df['month'].map(d_month)
    # extract day of week from Start Time column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # map title case day of week into lower case
    d_day = {'Sunday':'sunday', 'Monday':'monday', 'Tuesday':'tuesday', 'Wednesday':'wednesday',
        'Thursday':'thursday', 'Friday':'friday', 'Saturday':'saturday'}
    df['day_of_week'] = df['day_of_week'].map(d_day)


    # filter by month if applicabl/'e
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nExtracting The Most Frequent Times of Travel...\n')
    #tick the time
    start_time = time.time()
    # display the most common month
    #calculate most frequent month and convert into title casse
    most_frequent_month = df['month'].mode()[0].title()

    print(f"\nMost Frequent Month: {most_frequent_month}")

    # display the most common day of week
    #calculate most frequent day and convert into title case
    most_frequent_day = df['day_of_week'].mode()[0].title()

    print(f"\nMost Frequent Day: {most_frequent_day}")

    # display the most common start hour
    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #calculate the most frequent hour
    most_frequent_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {most_frequent_hour}")

    #Prints the time taken to perform the calculation
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*90)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(f"\nMost common start station: {most_common_start.title()}")


    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(f"\nMost common end station: {most_common_end.title()}")

    # display most frequent combination of start station and end station trip
    df['Start_End_Staion'] = df['Start Station'].map(str)+' to '+ df['End Station'].map(str)
    most_common_start_end = df['Start_End_Staion'].mode()[0]
    print(f"\nMost common trip is: {most_common_start_end}")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*90)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_min, tot_sec = divmod(df['Trip Duration'].sum(), 60)
    tot_hr, tot_min = divmod(tot_min, 60)
    print(f"The total trip duration is {tot_hr} hours, {tot_min} minutes and {tot_sec} seconds")


    # display mean travel time
    avg_min, avg_sec = divmod(round(df['Trip Duration'].mean()), 60)
    avg_hr, avg_min = divmod(avg_min, 60)
    if avg_hr > 0:
        print(f"\nAverage trip duration is {avg_hr} hours, {avg_min} minutes and {avg_sec} seconds")

    else:
        print(f"\nAverage trip duration is {avg_min} minutes and {avg_sec} seconds")


    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*90)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f"\nThe number of users by type are:\n{df['User Type'].value_counts()}")


    # Display counts of gender
    # some data does not have gender column
    try:
        gender_counts = df['Gender'].value_counts()
        print(f"\nThe number of users by gender are:\n\n{gender_counts}")
    except:
        print("\nThere is no 'Gender' column in the slected data.")
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_yr = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest_birth_yr}")
        print(f"\nThe most recent year of birth: {recent_birth_year}")
        print(f"\nThe most common year of birth: {common_birth_year}")
    except:
        print("There are no birth year columns in the selected data.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('*'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
