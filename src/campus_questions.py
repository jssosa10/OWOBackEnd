import datetime

buckets = 20
date_template = "%Y-%m-%dT%H:%M:%SZ"

def resolve_question(question_number, campus_data):
    for entry in campus_data:
        entry['date'] = get_datetime(entry['date'])
    return questions[question_number](campus_data)

def question1(campus_data):
    # group by email
    group_by_email = {}
    for entry in campus_data:
        email = entry['email']
        group_by_email[email] = group_by_email.get(email, [])
        group_by_email[email].append(entry['date'])
    # get all avg
    all_average = []
    for dates in group_by_email.values():
        diff_dates = [dates[i] - dates[i - 1] for i in range(1, len(dates))]
        average = sum(diff_dates, datetime.timedelta(0)) / len(diff_dates)
        all_average.append(average.days)
    all_average.sort()
    # get time delta
    min_average = all_average[0]
    max_average = all_average[-1]
    delta_average = max(1, (max_average - min_average) / buckets)
    # get time buckets
    time_buckets = [['', 0] for _ in range(buckets)]
    i = 0
    curr_time = 0
    while i < buckets:
        time_buckets[i][0] = '>= %d days' % curr_time
        curr_time = int(curr_time + delta_average)
        i += 1 
    # place info in time buckets
    i = 0
    curr_time = 0
    for average in all_average:
        while int(curr_time + delta_average) < average:
            curr_time = int(curr_time + delta_average)
            i += 1
        i = min(i, len(time_buckets) - 1)
        time_buckets[i][1] += 1
    return time_buckets

def question2(campus_data):
    # count freqs
    days = [[str(i + 1), 0] for i in range(366)]
    for entry in campus_data:
        day = entry['date'].timetuple().tm_yday - 1
        days[day][1] += 1
    # preffix sum
    for i in range(1, len(days)):
        days[i][1] += days[i - 1][1]
    # filter non change values
    all_days = []
    for i in range(len(days)):
        if i == 0 or i == len(days) - 1:
            all_days.append(days[i])
        elif days[i][1] != days[i - 1][1]:
            all_days.append(days[i - 1])
            all_days.append(days[i])
    return all_days

def question3(campus_data):
    # count freqs
    get_hour = lambda x : '%2d:00' % x
    hours = [[get_hour(i), 0] for i in range(24)]
    for entry in campus_data:
        hour = entry['date'].hour
        hours[hour][1] += 1
    return hours

def question4(campus_data):
    # count freqs
    weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_days = [[weekday_name[i], 0] for i in range(7)]
    for entry in campus_data:
        day = entry['date'].weekday()
        week_days[day][1] += 1
    return week_days

questions = [question1, question2, question3, question4]

def get_datetime(date):
    return datetime.datetime.strptime(date,date_template)