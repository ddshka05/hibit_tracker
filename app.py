import json
from datetime import date, timedelta

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
    '''

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if name_of_habit in data:
        raise NameHabitError('Habit with this particular name exists!')
    
    data[name_of_habit] = {'description': habit_description,
                           'last_done': date.today().isoformat(),
                           'streak': 0
                           }
    
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

    return f'Success! Habit "{name_of_habit}" has been added to track list.'



def mark_done(name_of_habit):
    '''
    Mark habit as done

    Args:
    name_of_habit (str): name of habit

    Return:
     (str) : Messege of success process 

    Raise:
    NameHabitError: if habit with this name does not exist
    '''
    
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if name_of_habit not in data:
        raise NameHabitError('Habit with this name does not exist!')

    last_date = date.fromisoformat(data[name_of_habit]['last_done'])
    cur_date = date.today()

    delta = last_date - cur_date

    data[name_of_habit]['last_done'] = date.isoformat(cur_date)
    data[name_of_habit]['streak'] += delta.days

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    
    return f"Data have been updated! For {name_of_habit} you have {data[name_of_habit]['streak']} days streak."



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

def get_info_about_habit(name_of_habit):
    '''
    Gives the discription, last date when it was done and streak of \
        the habit tracked

    Args:
    name_of_habit (str): name of habit

    Return:
    (str): returns text with info about habit

    Raise:
    NameHabitError: if habit with this name does not exist

    to be continued...
    '''

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if name_of_habit not in data:
        raise NameHabitError('Habit with this name does not exist!')
    
    return f"{name_of_habit} - {data['description']}\nLast done: {data['last_done']}\nYour streak: {data['streak']}"

def del_habit(name_of_habit):
    '''
    Deletes the inputted habit

    Args:
    name_of_habit (str): name of habit

    Return:
    (str): returns text with info about habit

    Raise:
    NameHabitError: if habit with this name does not exist

    to be continued...
    '''

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if name_of_habit not in data:
        raise NameHabitError('Habit with this name does not exist!')
    
    del data[name_of_habit]

    return f'Habit {name_of_habit} has been deleated from the list of tracked habits!'

def get_all_info():
    '''
    Give all info from the json file about habits tracked

    Return:
    (str): success!

    to be continued...
    '''

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for key, value in data.items():
        print(f'{key}:')
        for k, v in value.items():
            print(f'\t{k}: {v}')
    
    return 'Success! Enjoy your habits!'
