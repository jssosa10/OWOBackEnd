import datetime

buckets = 20
date_template = "yyyy-MM-dd'T'HH:mm:ss'Z'"

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
        average = sum(diff_dates, datetime.timedelta(0)) / float(len(diff_dates))
        all_average.append(average)
    all_average.sort()
    # get time delta
    min_average = all_average[0]
    max_average = all_average[-1]
    delta_average = max(1, (max_average - min_average) / buckets)
    # get time buckets
    time_buckets = [0 for _ in range(buckets)]
    # place info in time buckets
    i = 0
    curr_time = 0
    for average in all_average:
        while int(curr_time + delta_average) < average:
            curr_time = int(curr_time + delta_average)
            i += 1
        i = min(i, len(time_buckets) - 1)
        time_buckets[i] += 1
    return time_buckets

def question2(campus_data):
    # count freqs
    days = [0 for _ in range(366)]
    for entry in campus_data:
        day = date.timetuple().tm_yday - 1
        days[day] += 1
    # preffix sum
    for i in range(len(1, days)):
        days[i] += days[i - 1]

def question3(campus_data):
    # count freqs
    hours = [0 for _ in range(24)]
    for entry in campus_data:
        hour = entry['date'].hour
        hours[hour] += 1
    return hours

def question4(campus_data):
    # count freqs
    week_days = [0 for _ in range(7)]
    for entry in campus_data:
        day = entry['date'].weekday()
        week_days[day] += 1
    return week_days

questions = [question1, question2, question3, question4]

def get_datetime(date):
    return datetime.datetime.strptime(date_template, date)