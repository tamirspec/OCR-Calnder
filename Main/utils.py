import re
from datetime import datetime
def split_date(date_list):
    date_list = date_list[0].split('/')
    return date_list
def get_date_from_picture(text):
    if get_date_numeric(text):
        date = split_date(get_date_numeric(text))
        return date
    elif get_date_verbal(text):
        date = split_date(get_date_verbal(text))
        return date
def get_date_from_picture_to_google_format(text):
    return convert_date_to_google_format(get_date_from_picture(text))

def get_date_numeric(text):
    date = re.findall('[0-9]{1,2}[-|.\/]{1}[0-9]{1,2}[-|.\/]{1}[\d]{2,4}', text)
    return date

def get_date_verbal(text):
    date = re.findall('(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s{0,1}(\d{1,2})(?:rd|th|st|nd|)\s{0,1}(?:(\d{0,4}))',text.lower())
    date = convert_verbal_to_numeric(date)
    return date
def convert_verbal_to_numeric(dates):
    dates = dates[0]
    day = dates[1]
    month = dates[0]
    year = dates[2]
    if not year:
        year = datetime.today().year
    date = datetime.strptime(f'{day}-{month[0:3]}-{year}', '%d-%b-%Y')
    return date

def convert_date_to_google_format(date_list): #not orgenized !
    if int(date_list[2]) < 999:
        date_list [2] = f'20{date_list[2]}'
    # elif not date_list[2]: #will return the corrent year

    if int (date_list[0]) < 10: #checks the month and day and see if they are in google format
        date_list[0] = f'0{int(date_list[0])}'
    if int(date_list[1]) < 10:
        date_list[1] = f'0{int(date_list[1])}'

    if get_location() == 1:
        year = date_list[2]
        month = date_list[1]
        day = date_list[0]
        google_format_date = f'{year}-{month}-{day}T00:00:00%s'
    else:
        year = date_list[2]
        month = date_list[0]
        day = date_list[1]
        google_format_date = f'{year}-{month}-{day}T00:00:00%s'
    return google_format_date

def get_location():#will check the persons locaion us/europ
    return 1