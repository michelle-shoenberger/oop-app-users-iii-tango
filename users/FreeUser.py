from users.User import User

class FreeUser(User):
    def __init__(self, name, email, dl_number):
        super().__init__(name, email, dl_number)
        self.number_posts = 0

    def create_post(self, post):
        if self.number_posts < 2:
            self.number_posts += 1
            return super().create_post(post)
        print("No more posts permitted")