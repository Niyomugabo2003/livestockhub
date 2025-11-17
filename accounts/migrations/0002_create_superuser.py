# accounts/migrations/0002_create_superuser.py
from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    
    # Check if superuser already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com', 
            password='admin123',
            user_type='admin',
            phone_number='+250123456789',
            address='Admin Address',
            city='Kigali'
        )
        print("✅ Superuser created: username=admin, password=admin123")
    else:
        print("✅ Superuser already exists")

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]