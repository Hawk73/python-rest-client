import pythonrestclient

# Configuration API client
pythonrestclient.ServiceFactory.init_api_client('https://jsonplaceholder.typicode.com', 'username', 'password')


# Create resource - returns instance of PostModel
attributes = {'title': 'Test'}
pythonrestclient.PostModel.create(attributes)


# Manage by ID #
post_id = 1

# get - returns instance of PostModel
pythonrestclient.PostModel.get(post_id)

# update - returns True if received ID equals post_id
new_attributes = {'title': 'Test2'}
pythonrestclient.PostModel.update_by_id(post_id, attributes)

# delete - returns True if response has no errors
pythonrestclient.PostModel.delete_by_id(post_id)


# Manage resource #
post_id = 1
post = pythonrestclient.PostModel.get(post_id)

# update
new_attributes = {'title': 'Test2'}
post.update(new_attributes)

# delete
post.delete()


# Manage resources #

# get all
collection_of_posts = pythonrestclient.PostModel.all()

# get resource with filter, for example, get all items where userId=2
collection_of_posts = pythonrestclient.PostModel.filter({'userId': 2})

# delete all - delete all items from current collection
collection_of_posts.delete_all()

# Get first item and reset cursor
collection_of_posts.first()

# Get next item
collection_of_posts.iter()

# Get title for third item
collection_of_posts.items[3].attributes['title']


# TODO: complete example
# blog_post_items = api.PostModel.limit(10).page(2).items() #Получение конечного списка моделей с заданием постраничной навигации
