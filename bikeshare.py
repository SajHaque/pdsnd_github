import time
import pandas as pd
import numpy as np

#  Sources used:
#     - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html
#     - https://betterprogramming.pub/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e
#     - https://towardsdatascience.com/extract-rows-columns-from-a-dataframe-in-python-r-678e5b6743d6

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Enter a city from chicago, new york city or washington:')
        if city.lower() in ['chicago','new york city','washington']:
            break
        else: 
            print("Oops! Invalid Input. Please enter a city from: chicago, new_york_city or washington")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter a month from Jan Feb Mar Apr May Jun or all for no month filter:')
        if month.title() in ['All','Jan','Feb','Mar','Apr','May','Jun']:
            break
        else: 
            print("Oops! Invalid Input. Please enter a month from Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec or all for no month filter")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter a day of the week from Monday Tuesday Wednesday Thursday Friday Saturday Sunday or all for no week filter:')
        if day.title() in ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:
            break
        else: 
            print("Oops! Invalid Input. Please enter a day from: Monday Tuesday Wednesday Thursday Friday Satruday Sunday or all for no week filter")


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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour']=df['Start Time'].dt.hour
    df['Journey']=df['Start Station'] + ' to ' + df['End Station']
    
    if month != 'all':
        months = ['Jan','Feb','Mar','Apr','May','Jun']
        month = months.index(month.title())+1
        
        df=df[df['month'] == month]
    
    if day != 'all':
        df=df[df['day_of_week']==day.title()]
       
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month =='all':
        common_month= df['month'].mode()[0]
        month_list=['January','February','March','April','May','June']
        month_name=month_list[common_month-1]
        print('The most common month is: {}'.format(month_name))
       
          

    # TO DO: display the most common day of week
    if day == 'all':
        common_day= df['day_of_week'].mode()[0]
        print('The most common day is: {}'.format(common_day))
        

    # TO DO: display the most common start hour
    common_hour=df['start_hour'].mode()[0]
    print('The most common start hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    freq_start_station=df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(freq_start_station))

    # TO DO: display most commonly used end station
    freq_end_station=df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(freq_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    freq_journey=df['Journey'].mode()[0]
    print('The most common start and end station combination is: {}'.format(freq_journey))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('The total travel time is: {} minutes'.format(int(total_travel_time)))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()/60
    print('The mean travel time is: {} minutes'.format(round(avg_travel_time,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts().to_string()
    print('User type counts:\n',user_type_count,'\n')

    # TO DO: Display counts of gender
    if city =='washington':
        print('Gender data not available for washington')
    else: 
        gender_count = df['Gender'].value_counts().to_string()
        print('Gender counts:\n',gender_count,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city=='washington':
        print('Birth year data not available for washington')
    else:
        earliest_birth_year=df['Birth Year'].min()
        latest_birth_year=df['Birth Year'].max()
        frequent_birth_year=df['Birth Year'].mode()[0]
        
        print('Earliest year of birth is: {}'.format(int(earliest_birth_year)))
        print('Most recent year of birth is: {}'.format(int(latest_birth_year)))
        print('Most common year of birth is: {}'.format(int(frequent_birth_year)))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    row_index1=0
    row_index2=5
    while True:
        raw_prompt=input('Would you like to see 5 lines of raw data- y/n?')
        if raw_prompt.lower()=='n':
            break
        elif raw_prompt.lower()=='y':
            display=df.iloc[row_index1:row_index2,:]
            row_index1=row_index1+5
            row_index2=row_index1+5
            pd.set_option('display.max_columns',8)
            print(display)
        elif raw_prompt not in ['n','y']:
            print('Please enter y (yes) or n (no)')
            
       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()