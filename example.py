import api
import models.post


api_client = api.client.Client('https://jsonplaceholder.typicode.com', 'user', 'pass')
post_model = models.post.Post(api_client)

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
