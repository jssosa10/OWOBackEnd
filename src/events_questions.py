import datetime

def resolve_question(question_number, events_data):
    for entry in events_data :
        entry['date'] = get_datetime(entry['date'])
    return questions[question_number](events_data)
def question1(events_data):
    res = [0 for x in range(7)]
    for entry in events_data:
        res[entry['date'].weekday()] = res[entry['date'].weekday()]+1
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
date_template = "yyyy-MM-dd'T'HH:mm:ss'Z'"

def get_datetime(date):
    return datetime.datetime.strptime(date_template, date)