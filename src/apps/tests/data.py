from django.contrib.auth import get_user_model


class TestUser:
    ''' Class for storing test users credentials.  '''

    def __init__(self, username, email, password, is_superuser=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_superuser = is_superuser

    def create_in_db(self):
        if self.is_superuser:
            create_user_fun = get_user_model().objects.create_superuser
        else:
            create_user_fun = get_user_model().objects.create_user
        return create_user_fun(
            username=self.username, email=self.email, password=self.password
        )


USER1 = TestUser('john',  'john@gmail.com',  'johny_123')
USER2 = TestUser('alice', 'alice@gmail.com', 'alicia_123')
ADMIN = TestUser('admin', 'admin@gmail.com', 'adminn_123', is_superuser=True)
