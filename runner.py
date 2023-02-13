from users.PremiumUser import PremiumUser
from users.FreeUser import FreeUser
from users.User import User

first = PremiumUser('Matt', 'matt@gmail.com','12345')
second = FreeUser('Mark', 'mark@gmail.com','23456')

post1 = "Hello World"
post2 = "Goodbye World"
post3 = "A third"
post4 = "A fourth"
first.create_post(post1)
print(User.all_posts)
second.create_post(post2)
print(User.all_posts)
second.create_post(post3)
second.create_post(post4)
print(User.all_posts)
