# Generated by Django 2.0.5 on 2018-06-01 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctorant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationaliter', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=10)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=100)),
                ('addresse', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
                ('nom_prenom_mere', models.CharField(max_length=50)),
                ('nom_pere', models.CharField(max_length=50)),
                ('accepted', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitulerPostGrade', models.CharField(max_length=100)),
                ('intitulerSujet', models.CharField(max_length=100)),
                ('diplomeGraduation', models.CharField(max_length=250)),
                ('nomEncadreur', models.CharField(max_length=100)),
                ('gradeEncadreur', models.CharField(max_length=100)),
                ('nomCoEncadreur', models.CharField(max_length=100)),
                ('gradeCoEncadreur', models.CharField(max_length=100)),
                ('dateInscription', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('doctorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscriptions', to='Administration.Doctorant')),
            ],
            options={
                'ordering': ['intitulerPostGrade'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('niveau', models.CharField(max_length=10)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Recourt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=2550)),
                ('accepted', models.BooleanField(default=False)),
                ('doctorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recours', to='Administration.Doctorant')),
            ],
            options={
                'ordering': ['sujet'],
            },
        ),
        migrations.CreateModel(
            name='Reinscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitulerPostGrade', models.CharField(max_length=100)),
                ('intitulerSujet', models.CharField(max_length=100)),
                ('diplomeGraduation', models.CharField(max_length=250)),
                ('nomEncadreur', models.CharField(max_length=100)),
                ('gradeEncadreur', models.CharField(max_length=100)),
                ('nomCoEncadreur', models.CharField(max_length=100)),
                ('gradeCoEncadreur', models.CharField(max_length=100)),
                ('dateReinscription', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('doctorant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reinscriptions', to='Administration.Doctorant')),
            ],
            options={
                'ordering': ['intitulerPostGrade'],
            },
        ),
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['titre'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='recourt',
            unique_together={('doctorant', 'sujet')},
        ),
    ]
