# ВНИМАНИЕ: Скрипт работает на незаполненной БД!
# Импортируем модели
from django.contrib.auth.models import User
from news.models import *

# Создаем пользователей
user1 = User.objects.create_user('user_1')
user2 = User.objects.create_user('user_2')

# Создаем авторов
author1 = Author.objects.create(id_user = user1, rating = 0)
author2 = Author.objects.create(id_user = user2, rating = 0)

# Создаем 4 категории
cat1 = Category.objects.create(name = "Наука")
cat2 = Category.objects.create(name = "Культура")
cat3 = Category.objects.create(name = "Политика")
cat4 = Category.objects.create(name = "Спорт")

# Создаем 2 статьи и 1 новость
post1 = Post.objects.create(id_author = author1, type = Post.article, header = "Заголовок статьи про спорт", text = "Текст статьи про спорт. блаблаблаблаблаблаблаблаблаблаблабла", rating = 0)
post2 = Post.objects.create(id_author = author1, type = Post.news, header = "Заголовок новости про науку и культуру", text = "Текст новости про науку и культуру", rating = 0)
post3 = Post.objects.create(id_author = author2, type = Post.article, header = "Заголовок статьи про политику", text = "Текст статьи про политику", rating = 0)

# Связываем статьи и категории
PostCategory.objects.create(id_post = post1, id_category = cat4)
PostCategory.objects.create(id_post = post2, id_category = cat1)
PostCategory.objects.create(id_post = post2, id_category = cat2)
PostCategory.objects.create(id_post = post3, id_category = cat3)

# Создаем 4 комментария
comment1 = Comment.objects.create(id_post = post1, id_user = user1, text = "Комментарий user1 к статье про спорт", rating = 0)
comment2 = Comment.objects.create(id_post = post2, id_user = user2, text = "Комментарий user2 к новости про науку и культуру", rating = 0)
comment3 = Comment.objects.create(id_post = post3, id_user = user1, text = "Комментарий user1 к статье про политику", rating = 0)
comment4 = Comment.objects.create(id_post = post3, id_user = user2, text = "Комментарий user2 к статье про политику", rating = 0)

# Проставляем рейтинг 1 статье
post1.like()
post1.like() # Рейтинг +2

# Проставляем рейтинг 2 статье
post2.dislike()
post2.dislike() # Рейтинг -2

# Проставляем рейтинг 3 статье
post3.like()
post3.like()
post3.dislike() # Рейтинг +1

# Проставляем рейтинги комментариям
comment1.like() # Рейтинг +1
comment2.like() # Рейтинг +1
comment3.like() # Рейтинг +1
comment4.like() # Рейтинг +1

# обновляем рейтинг автором
# (не очень понял, как правильно реализовать интерфейс метода.
# Можно сделать статическим и передавать либо username, либо объект Author.
# реализовал как функцию обновления рейтинга конкретного автора)

author1.update_rating()
author2.update_rating()

# Выводим данные автора с наивысшим рейтингом
# (тут не совсем разобрался, как вместо внешнего ключа подставить значение из другой таблицы,
# поэтому здесь и далее получил объект и вывел данные через print)

a1 = Author.objects.all().order_by('-rating')[0]
print(a1.id_user.username, a1.rating)

# Выводим данные статье с наивысшим рейтингом.
best_post = Post.objects.all().order_by('-rating')[0]
print(best_post.created, best_post.id_author.id_user, best_post.rating, best_post.header, best_post.preview())

# Выводим комментарии к лучшей статье (здесь просто вывел ссылку на User, как заменить значением - не разобрался)
Comment.objects.filter(id_post = best_post).values('created', 'id_user', 'rating', 'text')


