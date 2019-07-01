# django packages
import django

# third-party packages
from tenant_schemas.test.cases import TenantTestCase
# from tenant_schemas.test.client import TenantClient
from .tenant_client import TenantClient

# own packeages
from .models import User

# Create your tests here.




class UsersTestCase(TenantTestCase):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init class')
        self.user = 'test'
        self.email = 'test@test.com'
        self.password = 'testpwd'
        self.name = 'test name'
        print('init')

    def setUp(self):
        #django.setup()
        print('ok')
		self.c = TenantClient(self.tenant)
        # print(self.c)


    def test_create_superuser(self):
        django.setup()
        superuser = User.objects.create_superuser(
        user = self.user,
        email = self.email,
        password = self.password,
        name = self.name)
        superuser.save()
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_active, True)
"""
    def test_authenticate_success(self):
        '''
            we authenticate with a user and right password
         
        '''
        self.test_create_superuser()
        response = self.c.post('/vkadmin/token', {'user': self.user, 'password': self.password}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        response_expect_keys = ['access', 'refresh']
        for key in response_expect_keys:
            self.assertTrue(key in response.data)
    

    def test_authenticate_fail(self):
        '''
            we authenticate with a wrong password
        '''
        self.test_create_superuser()
        response = self.c.post('/vkadmin/token', {'user': self.user, 'password': self.password_wrong}, format='json')
        print(response.data)
        self.assertNotEqual(response.status_code, 200)
        response_expect_keys = ['access', 'refresh']
        for key in response_expect_keys:
            self.assertFalse(key in response.data)

"""