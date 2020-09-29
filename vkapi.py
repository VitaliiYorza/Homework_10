import requests
class User:
    def __init__(self, id):
        self.id = id

    def vkpage(self, user):
        return f'https://vk.com/id{user.id}'

    def friends(self, user_id):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c',
                'user_id': user_id,
                'fields': 'first_name',
                'v': 5.122
            })
        return response.json()

    def friendstodict(self, response):
        dict_of_friends_user1 = {}
        for i in range(0, len(response['response']['items'])):
            dict_of_friends_user1[response['response']['items'][i]['id']] = response['response']['items'][i][
                'first_name']
        return dict_of_friends_user1

user1 = User(int(input('Write id of first user')))
user2 = User(int(input('Write id of second user')))
response = user1.friends(user1.id)

dict_of_friends_user1 = user1.friendstodict(response)

mutual_friends = {}

response = user2.friends(user2.id)
dict_of_friends_user2 = user2.friendstodict(response)

mutual_friends_id = list(set(dict_of_friends_user1) & set(dict_of_friends_user2))

between = len(dict_of_friends_user1) > len(dict_of_friends_user2)
if between == True:
    less_dict = dict_of_friends_user2
else:
    less_dict = dict_of_friends_user1
for keys in mutual_friends_id:
    for k, v in less_dict.items():
        if keys == k:
            mutual_friends[keys] = v
print('Your mutual friends: ',mutual_friends)
print('Page vk is: ',user1.vkpage(user1))
#or
user = f'https://vk.com/id{user2.id}'
print(user)
