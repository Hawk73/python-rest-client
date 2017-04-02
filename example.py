import pythonrestclient

pythonrestclient.ServiceFactory.init_api_client('https://jsonplaceholder.typicode.com', 'username', 'password')

# Create resource - returns instance of PostModel
attributes = {'title': 'Test'}
pythonrestclient.PostModel.create(attributes)


# Manage by ID
post_id = 1
# get - returns instance of PostModel
pythonrestclient.PostModel.get(post_id)
# update - returns True if received ID equals post_id
new_attributes = {'title': 'Test2'}
pythonrestclient.PostModel.update_by_id(post_id, attributes)
# delete - returns True if response has no errors
pythonrestclient.PostModel.delete_by_id(post_id)


# Manage resource
post_id = 1
post = pythonrestclient.PostModel.get(post_id)

# update
# TODO: implement

# delete
post.delete()


# Manage resources
# get all
collection_of_posts = pythonrestclient.PostModel.all()
# get resource with filter, for example, get all items where userId=2
collection_of_posts = pythonrestclient.PostModel.filter({'userId': 2})

# delete all - delete all items from current collection
collection_of_posts.delete_all()


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
