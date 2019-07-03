from .tenant_client import TenantClient
from tenant_schemas.test.cases import TenantTestCase
from vkadmin.models import User


class TestUtils(TenantTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'testpwd'
        self.name = 'test name'
        self.password_wrong = 'wrong password   '


    def create_super_user(self, name='test'):
        superuser = User.objects.create_superuser(
        user = name,
        email = name,
        password = self.password,
        name = self.name)
        superuser.save()
        return superuser

    def set_credentials(self, user):
        response = self.c.post('/vkadmin/api-token-auth', 
            data={'user': user.user, 'password': self.password})
        print(response)
        self.c.credentials(
            HTTP_AUTHORIZATION='BEARER {}'.format(response.json()['token']))
        return response

class AuthedUserTestCase(TestUtils):

    def setUp(self):
        self.c = TenantClient(self.tenant)
        self.user = self.create_super_user()
        response = self.set_credentials(self.user)

class AuthedSuperUserTestCase(TestUtils):


    def setUp(self):
        self.c = TenantClient(self.tenant)
        self.user = self.create_super_user()
        response = self.set_credentials(self.user)
