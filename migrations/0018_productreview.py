# Generated by Django 3.1.4 on 2022-04-22 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saler', '0017_wholesaleproductorders'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saler.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
