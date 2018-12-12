import datetime

date_template = "%Y-%m-%dT%H:%M:%SZ"

def get_datetime(date):
    return datetime.datetime.strptime(date,date_template)

def resolve_question(question_number, events_data):
    for entry in events_data :
        entry['date'] = get_datetime(entry['date'])
    return questions[question_number](events_data)

def question1(events_data):
    # freq per day
    weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    res = [[weekday_name[i],0] for i in range(7)]
    for entry in events_data:
        day =  entry['date'].weekday()
        res[day][1] += 1
    # get percentage
    for i in range(len(res)):
        res[i][1] = (res[i][1] * 100) / len(events_data)
    return res

def question2(events_data):
    # group by type
    event_types = {}
    for entry in events_data:
        e_type = entry['type']
        event_types[e_type] = event_types.get(e_type, 0) + 1
    # get percentage
    for e_type in event_types.keys():
        event_types[e_type] = (event_types[e_type] * 100) / len(events_data)
    return [[e_type, freq] for e_type, freq in event_types.items()]

def question3(events_data):
    # freq per hour
    get_hour = lambda x : '%2d:00' % x
    hours = [[get_hour(i), 0] for i in range(24)]
    for entry in events_data:
        hour = entry['date'].hour
        hours[hour][1] += 1
    return hours

def question4(events_data):
    # freq per week per type
    weeks = [['Week %2d' % i, 0] for i in range(53)]
    for entry in events_data:
        week_num = entry['date'].isocalendar()[1] - 1
        weeks[week_num][1] += 1
    return weeks

def question5(events_data):
    # freq per day
    month_name = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    all_months = [[month_name[i],0] for i in range(12)]
    for entry in events_data:
        month =  entry['date'].month - 1
        all_months[month][1] += 1
    return all_months

questions = [question1, question2, question3, question4, question5]