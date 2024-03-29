# Generated by Django 4.2.7 on 2023-11-06 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pathology_Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='test_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pathology_Test_Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parameter', models.TextField()),
                ('expected_result', models.CharField(max_length=100)),
                ('result_unit', models.CharField(max_length=100)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pathology_test')),
            ],
        ),
        migrations.AddField(
            model_name='pathology_test',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.test_category'),
        ),
    ]
