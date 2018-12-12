import datetime

buckets = 20
date_template = "%Y-%m-%dT%H:%M:%SZ"

def resolve_question(question_number, bot_data):
    for entry in bot_data:
        entry['date'] = get_datetime(entry['date'])
    return questions[question_number](bot_data)

def question1(bot_data):
    # group by email
    group_by_type = {}
    for entry in bot_data:
        mode = entry['mode']
        if(mode=='manual'):
            continue
        type = entry['type'].split(":")[1]
        if(type in group_by_type):
            group_by_type[type] = group_by_type[type]+1
        else:
            group_by_type[type]=1
    # get all avg
    time_buckets = [['', 0] for _ in range(len(group_by_type))]
    i = 0
    for key, elem in group_by_type.items():
        time_buckets[i][0] = key
        time_buckets[i][1] = elem
        i+=1
    return time_buckets

def question2(bot_data):
    # group by email
    group_by_type = {}
    for entry in bot_data:
        mode = entry['mode']
        type = entry['type'].split(":")[1]
        if((mode+":"+type) in group_by_type):
            group_by_type[(mode+":"+type)] = group_by_type[(mode+":"+type)]+1
        else:
            group_by_type[(mode+":"+type)]=1
    # get all avg
    time_buckets = [['', 0] for _ in range(len(group_by_type))]
    i = 0
    for key, elem in group_by_type.items():
        time_buckets[i][0] = key
        time_buckets[i][1] = elem
        i+=1
    return time_buckets

def question3(bot_data):
    # group by email
    group_by_mode = {'manual':0, 'bot':0}
    for entry in bot_data:
        mode = entry['mode']
        if(mode=='manual'):
            group_by_mode['manual']=group_by_mode['manual']+1
        else:
            group_by_mode['bot']=group_by_mode['bot']+1
    # get all avg
    time_buckets = [['', 0] for _ in range(len(group_by_mode))]
    i = 0
    for key, elem in group_by_mode.items():
        time_buckets[i][0] = key
        time_buckets[i][1] = elem
        i+=1
    return time_buckets

questions = [question1, question2, question3]

def get_datetime(date):
    return datetime.datetime.strptime(date,date_template)