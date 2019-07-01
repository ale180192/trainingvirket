from .models import Client


'''

tenant1 = Client(
    domain_url='localhost',
    schema_name='public',
    on_trial=True
)
tenant2 = Client(
    domain_url='demo.localhost',
    schema_name='demo',
    on_trial=True
)
'''
tenant3 = Client(
    domain_url='demo2.localhost',
    schema_name='demo2',
    on_trial=True
)
'''
tenant1.save()
tenant2.save()
'''
tenant3.save()
