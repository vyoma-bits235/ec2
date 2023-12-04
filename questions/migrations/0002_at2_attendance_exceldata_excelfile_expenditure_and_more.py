# Generated by Django 4.2.7 on 2023-12-04 22:03

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AT2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='0', max_length=20)),
                ('Dinner', models.CharField(default='0', max_length=20)),
                ('breakfast', models.CharField(default='0', max_length=20)),
                ('lunch', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=250, null=True)),
                ('Dinner', models.CharField(default='0', max_length=20)),
                ('breakfast', models.CharField(default='0', max_length=20)),
                ('lunch', models.CharField(default='0', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('exp', models.CharField(default='0', max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Image23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='myimage')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='.', max_length=255)),
                ('item1', models.CharField(default='.', max_length=255)),
                ('item2', models.CharField(default='.', max_length=255)),
                ('item3', models.CharField(default='.', max_length=255)),
                ('item4', models.CharField(default='.', max_length=255)),
                ('item5', models.CharField(default='.', max_length=255)),
                ('item6', models.CharField(default='.', max_length=255)),
                ('item7', models.CharField(default='.', max_length=255)),
                ('item8', models.CharField(default='.', max_length=255)),
                ('item9', models.CharField(default='.', max_length=255)),
                ('item10', models.CharField(default='.', max_length=255)),
                ('item11', models.CharField(default='.', max_length=255)),
                ('item12', models.CharField(default='.', max_length=255)),
                ('item13', models.CharField(default='.', max_length=255)),
                ('item14', models.CharField(default='.', max_length=255)),
                ('item15', models.CharField(default='.', max_length=255)),
                ('item16', models.CharField(default='.', max_length=255)),
                ('item17', models.CharField(default='.', max_length=255)),
                ('item18', models.CharField(default='.', max_length=255)),
                ('item19', models.CharField(default='.', max_length=255)),
                ('item20', models.CharField(default='.', max_length=255)),
                ('item21', models.CharField(default='.', max_length=255)),
                ('item22', models.CharField(default='.', max_length=255)),
                ('item23', models.CharField(default='.', max_length=255)),
                ('item24', models.CharField(default='.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=350)),
                ('breakfast', models.CharField(max_length=350)),
                ('dinner', models.CharField(max_length=350)),
                ('lunch', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('item', models.CharField(max_length=255)),
                ('total_rating', models.IntegerField(default=0)),
                ('number_of_ratings', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('image', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='.', max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=90)),
                ('rating', models.IntegerField(default='0')),
                ('person', models.IntegerField(default='0')),
                ('avg', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='image23',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.menuitem'),
        ),
    ]
