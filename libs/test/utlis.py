from .tenant_client import TenantClient
from vkadmin.models import User


class TestUtils(TenantClient):

    def __init__(self, *args, **kwargs):
        print(super())
        super().__init__(*args, **kwargs)
        self.user = 'test'
        self.email = 'test@test.com'
        self.password = 'testpwd'
        self.name = 'test name'
        self.password_wrong = 'wrong password   '


    def create_super_user(self):
        superuser = User.objects.create_superuser(
        user = self.user,
        email = self.email,
        password = self.password,
        name = self.name)
        superuser.save()
        return superuser

    def set_credentials(self, user):
        response = self.c.post(self.api_uri+'auth/', 
            data={'user': user.user, 'password': self.password})
        self.c.credentials(
            HTTP_AUTHORIZATION='BEARER {}'.format(response.json()['data']['token']))
        return response

class AuthedUserTestCase(TestUtils):

    def setUp(self):
        self.c = TenantClient(self.tenant)
        self.user = self.create_super_user()
        response = self.set_credentials(self.user)

class AuthedSuperUserTestCase(TestUtils):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(super())

    def setUp(self):
        print('setUp')
        self.c = TenantClient(super().tenant)
        self.user = self.create_super_user()
        response = self.set_credentials(self.user)
        self