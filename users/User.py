
class User:
    all_posts = {}

    def __init__(self, name, email, dl_number):
        self.name = name
        self.email = email
        self.dl = dl_number
        self.posts = []
        self.all_posts[name] = self.posts

    def create_post(self, post):
        self.posts.append(post)
        self.all_posts[self.name]= self.posts

    def delete_post(self, index):
        self.posts.pop(index)
        self.all_posts[self.name]= self.posts
        