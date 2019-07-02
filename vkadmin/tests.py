# django packages
import django

# third-party packages
from tenant_schemas.test.cases import TenantTestCase
# from tenant_schemas.test.client import TenantClient
from .tenant_client import TenantClient
from rest_framework import status
# own packeages
from .models import User
from products.models import Product
# Create your tests here.




#TODO: Delete superfluous code
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
        self.c = TenantClient(self.tenant)

    def _create_super_user(self):
        superuser = User.objects.create_superuser(
        user = self.user,
        email = self.email,
        password = self.password,
        name = self.name)
        superuser.save()
        return superuser

    def test_create_superuser(self):
        superuser = self._create_super_user()
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_active, True)

    def test_authenticate_success(self):
        '''
            we authenticate with a user and right password
         
        '''
        self._create_super_user()
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
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

class ProductsTestCase(TenantTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {
            'name': 'record number ',
            'description': 'description value',
            'pricce': 55.69
        }

    def setUp(self):
        self.c = TenantClient(self.tenant)

    def _insert_records(self, num_records=2):
        data_list = []
        for index in range(num_records):
            self.data['name'] = '{name}{number}'.format_map({'name': self.data['name'], 'number': index} )
            data_list.append(Product(**self.data))
        Product.objects.bulk_create(data_list)

    def test_insert(self):
        response = self.c.post('/products', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all(self):
        num_records = 2
        self._insert_records(num_records=num_records)
        response = self.c.get('/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(len(response.data['data']), num_records)

    def test_update(self):
        self._insert_records(num_records=5)
       
        data_update = {
            'name': 'name update test',
            'description': 'new description'
        }
        response = self.c.patch('/products/1', data=data_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

