# django packages
import django

# third-party packages
from tenant_schemas.test.cases import TenantTestCase
# from tenant_schemas.test.client import TenantClient
from .tenant_client import TenantClient
from rest_framework import status
# own packeages
from .models import User

# Create your tests here.





class VkTestCase(TenantTestCase):
    '''
        class that autehnticate to user for it have user
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = 'test'
        self.email = 'test@test.com'
        self.password = 'testpwd'
        self.name = 'test name'
        self.password_wrong = 'wrong password   '
    
    def setUp(self):
        django.setup()
        self.c = TenantClient(self.tenant)

     


class UsersTestCase(TenantTestCase):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = 'test'
        self.email = 'test@test.com'
        self.password = 'testpwd'
        self.name = 'test name'
        self.password_wrong = 'wrong password   '

    def setUp(self):
        django.setup()
        self.c = TenantClient(self.tenant)


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

    def test_authenticate_success(self):
        '''
            we authenticate with a user and right password
         
        '''
        self.test_create_superuser()
        response = self.c.post('/vkadmin/token', {'user': self.user, 'password': self.password}, format='json')
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
        self.assertNotEqual(response.status_code, 200)
        response_expect_keys = ['access', 'refresh']
        for key in response_expect_keys:
            self.assertFalse(key in response.data)


class ProductsTestCase(TenantTestCase):


    def setUp(self):
        django.setup()
        self.c = TenantClient(self.tenant)


    def test_insert(self):
        data = {
            'name': 'name value',
            'description': 'description value',
            'pricce': 55.69
        }
        response = self.c.post('/products', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all(self):
        self.test_insert()
        self.test_insert()
        response = self.c.get('/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(len(response.data['data']), 2)

    def test_update(self):
        data_update = {
            'name': 'name update test',
            'description': 'new description'
        }
        self.test_insert()
        response = self.c.patch('/products/1', data=data_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

