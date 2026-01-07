import json

def load_file(filename):
    with open("/Users/amarjeet/Desktop/Data-Science/Python/randomdata.json","r") as f:
        return json.load(f)

def jsonfile(filename):
    with open("cleanedData.json", "w") as f:
        return json.dump(filename, f, indent=2)
    
def datacleaning(data):
    # removing the user id who don't have followers and liked pages
    data['users'] = [user for user in data['users'] if user['followers'] != [] or user['liked_pages'] != []]

    # removing duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    # in this dataset there is no user name if we want to remove blank user name
    # data['users'] = [user for user in data['users'] if user['name'].strip()]
    # and for checking if mail valid mail is in mail column we can check
    # if '@' in user['email'] and '.' in user['email'] and ' ' not in user['email']
    # with this aprroach we can drop rows with incomplete email and blank name
    return data


def friend_suggestion(user_id, data):
    friends_data = {}
    for user in data['users']:
        friends_data[user['id']] = set(user['friends'])

    if user_id not in friends_data:
        return []
    
    user_friends = friends_data[user_id]
    
    suggestion = {}
    for friend in user_friends:
        for mutual in friends_data[friend]:
            if mutual != user_id and mutual not in user_friends:
                suggestion[mutual] = suggestion.get(mutual,0)+1

    sort = sorted(suggestion.items(), key=lambda x:x[1], reverse=True)
    return [user for user,_ in sort] 



def page_suggestion(user_id, data):
    user_data = {}
    for page in data['users']:
        user_data[page['id']] = set(page['liked_pages'])
    
    if user_id not in user_data:
        return []
    
    user_liked_pages = list(user_data[user_id])

    page_sug = {}
    for page in user_liked_pages:
        for key, val in user_data.items():
            if key != user_id and page in val:
                page_sug[key] = user_data[key]
    
    pages_list = []
    for i in page_sug.values():
        pages_list.extend(i)
    
    suggested_pages = []
    for i in pages_list:
        if i not in user_liked_pages:
            suggested_pages.append(i)
    
    page_for_user = {}
    for i in suggested_pages:
        page_for_user[i] = suggested_pages.count(i)
    
    sorted_result = sorted(page_for_user.items(), key=lambda x:x[1], reverse=True)
    
    return [page for page, count in sorted_result]


data = load_file("/Users/amarjeet/Desktop/Data-Science/Python/randomdata.json")
data = datacleaning(data)
user_id = 1
print(friend_suggestion(user_id, data))
print(page_suggestion(user_id, data))
final_data = jsonfile(data)
