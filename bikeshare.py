import time
import pandas as pd
import numpy as np
import datetime



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input(" please choose a City from the following (chicago,new york city,washington):").lower().strip()
        if city not in CITY_DATA :
            print("Invalid city name!")
        else :
            break
    # get user input for month (all, january, february, ... , june)
    while True :
        month = input(" please choose a month from the following (all, january, february, ... , june) :").lower().strip()
        my_months =["january","february","march","april","may","june"]
        if  month not in my_months and month != "all" :
            print("Invalid month!,please don't use any abbreviations or numbers")
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input(" please choose a day of week (all, monday, tuesday, ... sunday) :").lower().strip()
        days =['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day not in days and day != "all":
            print("Invalid day!,please don't use any abbreviations ")
        else :
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month:",df['month'].mode()[0])
    # display the most common day of week
    print('The most common day:',df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour:',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
# display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {popular_start_station}')

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: {popular_end_station}')

    # display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {popular_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("The mean travel time is", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    

    # Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
    else :
        print('this column does not exist !')
       


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns) :
        year = df['Birth Year']
        print(f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most common birth year is: {year.mode()[0]}')
    else :
        print('this column does not exist !') 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Asks user if he wants to display raw data and print 5 rows at time """
    raw = input('\nWould you like to diplay raw data? Enter yes or no.\n').lower().strip()
    while raw !='yes' :
        if raw == 'no':
                break   
        else :
            print('Invalid answer')
        raw = input('\nWould you like to diplay raw data? Enter yes or no.\n').lower().strip()
    if raw == 'yes':    
       num = 0
    while raw == 'yes':
            print(df.iloc[num: num+5])
            num += 5
            question = input('Next 5 raws?').lower().strip()
            if question == 'no':
                    break   
            while question !='yes' :
                  print('Invalid answer')
                  question = input('Next 5 raws?').lower().strip()
                   
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        while restart !='yes' :
            if restart == 'no':
                break   
            else :
                print('Invalid answer')
                restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart.lower().strip() != 'yes':
            break
  


if __name__ == "__main__":
	main()

