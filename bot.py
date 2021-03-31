from pprint import pprint
import vk_api

vk = vk_api.VkApi('89190628433', 'юра12042006')
vk.auth()

group_id = input('Введите id группы: ')

json = vk.method('wall.get', {'owner_id': '-' + str(group_id),
                              'count': 100})
count_posts = json['count']

list_post_ids = []
set_peoples = set()

try:
    for i in range(100):
        list_post_ids.append(json['items'][i]['id'])
except:
    pass

num_post = 2
for num in list_post_ids:
    post_id = num

    list_users = vk.method('likes.getList', {'type': 'post',
                                             'owner_id': '-' + str(group_id),
                                             'item_id': int(post_id)})

    for user in list_users['items']:
        if 'https://vk.com/id' + str(user) in set_peoples:
            pass
        else:
            set_peoples.add('https://vk.com/id' + str(user))
            print('https://vk.com/id' + str(user))
    
    print("_______________________")
    print('Пост № ' + str(num_post))
    num_post += 1

a = input()
