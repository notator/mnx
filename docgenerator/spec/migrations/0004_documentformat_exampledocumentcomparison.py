# Generated by Django 3.1.5 on 2021-02-02 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0003_datatypeoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'document_formats',
            },
        ),
        migrations.CreateModel(
            name='ExampleDocumentComparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preamble', models.TextField(blank=True)),
                ('document', models.TextField()),
                ('doc_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spec.documentformat')),
                ('example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spec.exampledocument')),
            ],
            options={
                'db_table': 'example_comparisons',
            },
        ),
    ]
