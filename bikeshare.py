import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washigton? \n').lower()
        if city in CITY_DATA:
            #input correct, ready to exit the loop
            break
        else:
            print('\nInvalid input! Check your spelling and try again!')
            #continue si quiero que se acabe

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to see data from? All, January, February, March, April, May, or June? \n').lower()
        if month in MONTH_LIST:
            #input correct, ready to exit the loop
            break
        else:
            print('Invalid input! Try Again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich week day would you like to see data from? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n').lower()
        if day in DAY_LIST:
            #input correct, ready to exit the loop
            break
        else:
            print('Invalid input! Try Again.')

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
#load data into data frame
    df = pd.read_csv(CITY_DATA[city])
#convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
#extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

# SOLO PARA FILTRAR: filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        #month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()] #se hace con un boolean

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] #se hace con un boolean

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    month_count = df['month'].value_counts().max()

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    day_count = df['day_of_week'].value_counts().max()

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    hour_count = df['hour'].value_counts().max()

    print('Most common month: {} ({} times)\nMost common day of the week: {} ({} times)\nMost common hour: {} ({} times)'.format(popular_month, month_count, popular_day, day_count, popular_hour, hour_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    start_count = df['Start Station'].value_counts().max()

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    end_count = df['End Station'].value_counts().max()

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + ' - ' + df['End Station']
    pop_start_end = df['start_end'].mode()[0]
    start_end_count = df['start_end'].value_counts().max()

    print('Most common Start Station: {} ({}times) \nMost common End Station: {} ({} times)'.format(popular_start, start_count, popular_end, end_count))
    print('Most frequent combination of Start and End Station trip: {} ({} times)\n'.format(pop_start_end, start_end_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_time'] = df['End Time'] - df['Start Time']
    tot_travel_time = df['travel_time'].sum()
    print("The total travel time was: {}\n".format(tot_travel_time))

    # TO DO: display mean travel time
    mean_time = df['travel_time'].mean()
    print("The mean travel time was: {}\n".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types: \n{}\n'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
         gender_types = df['Gender'].value_counts()
         print('Gender Information: \n{}\n'.format(gender_types))
    else:
        print('Column "Gender" does not exist in this file\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth = int(df['Birth Year'].min())
        max_birth = int(df['Birth Year'].max())
        mode_birth = int(df['Birth Year'].mode()[0])
        print('The earliest, most recent, and most common year of birth are: \nEarliest: {}\nMost recent: {}\nMost Common: {}\n'.format(min_birth, max_birth, mode_birth))
    else:
        print('Column "Birth Date" does not exist in this file\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        tabla = input('\nWould you like to see the first five lines of data? Enter yes or no.\n')
        if tabla.lower() == 'yes':
            print(df.head())
            

        restart = input('\nWould you like to see more data? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
