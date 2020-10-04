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

    def __and__(self, other_user):
        response = user1.friends(user1.id)
        dict_of_friends_user1 = user1.friendstodict(response)

        mutual_friends = {}

        response = other_user.friends(other_user.id)
        dict_of_friends_user2 = other_user.friendstodict(response)

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
        return mutual_friends


    def __str__(self):
        return f'https://vk.com/id{user1.id}'


print(user1.__and__(user2))
user1 = User(int(input('Write id of first user')))
user2 = User(int(input('Write id of second user')))
print(user1)
