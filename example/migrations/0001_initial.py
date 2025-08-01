# Generated by Django 4.2.2 on 2023-06-26 11:48

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exposicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('nombre_exposicion', models.CharField(max_length=255)),
                ('lugar', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('curaduria', models.CharField(max_length=150, blank=True, null=True)),
                ('tipo',
                 models.CharField(choices=[('Colectiva', 'Colectiva'), ('Individual', 'Individual')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PremioDistincion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.CharField(max_length=9)),
                ('distincion', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=100)),
            ]
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('anio', models.PositiveIntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('dimension', models.CharField(max_length=100,blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('anio', models.PositiveIntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('dimension', models.CharField(max_length=100, blank=True, null=True)),
                ('coleccion', models.CharField(max_length=200, blank=True, null=True)),
                ('serie', models.ForeignKey(
                    related_name='trabajos',
                    null=True,
                    blank=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='example.Serie'
                )),
            ],
        ),
        migrations.CreateModel(
            name='AcercaDe',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('acerca', models.TextField()),
                ('otros_proyectos', models.TextField()),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Información CV',
                'verbose_name_plural': 'Información CV',
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='statement/')),
            ],
        ),
    ]