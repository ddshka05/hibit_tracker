import json
from datetime import datetime, date

class NameHabitError(Exception):
    pass

def add_habit(name_of_habit, habit_description):
    '''
    Get the name of the habit wanted to be tracked and description of the habit

    Args:
    name_of_habit (str): name of the habit
    habit_description (str): description of the habit

    Return:
    "Success! Habit has been added to track list." (str): Messege of successful complit

    Raise:
    NameHabitError: if habit with this name has already existed.

    >>> 
    
    '''
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if name_of_habit in data:
        raise NameHabitError('Habit with this particular name exists!')
    
    data[name_of_habit] = {'description': habit_description,
                           'last_done': date.today(),
                           'streak': 0
                           }
    
    return 'Success! Habit has been added to track list.'

def mark_done(name_of_habit):
    '''
    Mark habit as done

    Args:
    name_of_habit (str): name of habit

    Return:
    ... (mb text with successful process)

    Raise:
    ...

    to be continued...
    '''
    pass

def notify():
    '''
    Send notifications to user

    Args:
    ...

    Return:
    ... (mb text with successful process)

    Raise:
    ...

    to be continued...
    '''
    pass

def get_info(name_of_habit):
    '''
    Gives the discription, last date when it was done and streak of \
        the habit tracked

    Args:
    name_of_habit (str): name of habit

    Return:
    ... (mb text with successful process)

    Raise:
    ...

    to be continued...
    '''
    pass

def del_habit(name_of_habit):
    '''
    Deletes the inputted habit

    Args:
    name_of_habit (str): name of habit

    Return:
    ... (mb text with successful process)

    Raise:
    ...

    to be continued...
    '''