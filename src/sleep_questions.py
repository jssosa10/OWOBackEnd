import datetime

def resolve_question(question_number, events_data):
    for entry in events_data :
        entry['date'] = get_datetime(entry['date'])
    sorted(events_data)
    group_by_email = {}
    for entry in events_data:
        email = entry['email']
        group_by_email[email] = group_by_email.get(email, [])
        group_by_email[email].append(entry)
    sueno  = []
    for user in group_by_email:
        hour  = -1
        for entry in user:
            if hour ==-1 and entry['type']=='start':
                hour = entry['date'].hour

    return questions[question_number](events_data)
def question1(events_data):
    weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    res = [[weekday_name[i],0] for i in range(7)]
    for entry in events_data:
        day =  entry['date'].weekday()
        res[day][1] +=1
    return res
def question2(events_data):
    pass
def question3(events_data):
    pass
def question4(events_data):
    pass
def question5(events_data):
    pass
questions = [question1,question2,question3,question4,question5]
date_template = "%Y-%m-%dT%H:%M:%SZ"

def get_datetime(date):
    return datetime.datetime.strptime(date,date_template)