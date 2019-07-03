# django packages
import django

# third-party packages
from rest_framework import status

# own packeages
from .models import User
from products.models import Product
from libs.test.utlis import AuthedSuperUserTestCase, TestUtils
# Create your tests here.






class UsersTestCase(AuthedSuperUserTestCase):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def test_create_superuser(self):
        superuser = self.create_super_user(name='test1')
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_active, True)

    def test_authenticate_success(self):
        '''
            we authenticate with a user and right password
         
        '''
        self.create_super_user(name='test1')
        response = self.c.post('/vkadmin/api-token-auth', {'user': 'test1', 'password': self.password}, format='json')
        self.assertEqual(response.status_code, 200)
        response_expect_keys = ['token']
        for key in response_expect_keys:
            self.assertTrue(key in response.data)
    

    def test_authenticate_fail(self):
        '''
            we authenticate with a wrong password
        '''

        self.test_create_superuser()
        response = self.c.post('/vkadmin/api-token-auth', {'user': self.username, 'password': self.password_wrong}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class ProductsTestCase(AuthedSuperUserTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {
            'name': 'record number ',
            'description': 'description value',
            'pricce': 55.69
        }

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

