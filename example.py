import pythonrestclient.api.client
import pythonrestclient.models.post


api_client = pythonrestclient.api.client.Client('https://jsonplaceholder.typicode.com', 'user', 'pass')
post_model = pythonrestclient.models.post.Post(api_client)


# Get resources
post_model.get_lists()

# Example:
# [
#   {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "qui est esse",
#     "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
#   },
#   ...
# ]


# Get resource by ID
post_id = 1
post_model.get(post_id)

# Example:
# {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }


# Create resource
params = {'title': 'Test'}
post_model.create(params)

# Example:
# {
#   "id": 101
# }


# Update resource
post_id = 1
params = {'id': post_id, 'title': 'Test2'}
post_model.update(id, params)

# Example:
# {
#   "id": 1
# }


# Delete resource by ID
post_id = 1
post_model.delete(post_id)

# Example:
# { }


# TODO: complete example
# blog_post = api.PostModel(title='Test') #создание записи
#
# blog_posts = api.PostModel.all() #получение всех записей
#
# blog_posts = api.PostModel.filter(userId=1) #получение класса коллекции записей c фильтром userId = 1
#
# blog_post = blog_posts.first() #первая запись из списка
#
# blog_post = blog_posts.iter() #получение следующую запись из выборки
#
# blog_post.update({'title': 'New name'}) #изменяем запись
#
# blog_post.delete() #Удаляем запись
#
# blog_post_items = api.PostModel.limit(10).page(2).items() #Получение конечного списка моделей с заданием постраничной навигации
#
# print(blog_post_items[3].title) #Получаем заголовок записи
