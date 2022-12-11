# Generated by Django 4.1.3 on 2022-12-10 21:18

from django.db import migrations, models
import iiitdrive.models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdrive', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(help_text='only IIITD emails', max_length=50, unique=True, validators=[iiitdrive.models.AllowlistEmailValidator(allowlist=['iiitd.ac.in'])], verbose_name='Email address'),
        ),
    ]