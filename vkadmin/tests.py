from django.test import TestCase, Client
import django

from .models import User

# Create your tests here.




class UsersTestCase(TestCase):
    
    user = 'test'
    email = 'test@test.com'
    password = 'testpwd'
    name = 'test name'
    password_wrong = 'wrong'

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
        client = Client()
        response = client.post('/vkadmin/token', {'user': self.user, 'password': self.password}, format='json')
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
        client = Client()
        response = client.post('/vkadmin/token', {'user': self.user, 'password': self.password_wrong}, format='json')
        print(response.data)
        self.assertNotEqual(response.status_code, 200)
        response_expect_keys = ['access', 'refresh']
        for key in response_expect_keys:
            self.assertFalse(key in response.data)