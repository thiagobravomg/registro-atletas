# Generated by Django 4.0.2 on 2022-02-10 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('equipe', models.CharField(max_length=200)),
                ('idade', models.IntegerField(default=0)),
                ('graduação', models.CharField(choices=[('branca', 'Faixa Branca'), ('azul', 'Faixa Azul'), ('roxa', 'Faixa Roxa'), ('marrom', 'Faixa Marrom'), ('preta', 'Faixa Preta')], max_length=200)),
                ('peso', models.IntegerField(default=0)),
                ('genero', models.CharField(choices=[('feminino', 'Feminino'), ('masculino', 'Masculino')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
