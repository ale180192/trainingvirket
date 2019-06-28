from .models import Client




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

tenant1.save()
tenant2.save()