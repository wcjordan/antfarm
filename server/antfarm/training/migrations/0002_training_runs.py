# Generated by Django 3.0.5 on 2020-04-07 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingEpisodeModel',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('iteration', models.IntegerField()),
                ('total_reward', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRunModel',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingStepModel',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('iteration', models.IntegerField()),
                ('state', models.TextField()),
                ('reward', models.FloatField()),
                ('is_done', models.BooleanField()),
                ('episode',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='step_set',
                                   to='training.TrainingEpisodeModel')),
            ],
            options={
                'unique_together': {('episode', 'iteration')},
            },
        ),
        migrations.DeleteModel(name='EpisodeModel',),
        migrations.AddField(
            model_name='trainingepisodemodel',
            name='training_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='episode_set',
                                    to='training.TrainingRunModel'),
        ),
        migrations.AlterUniqueTogether(
            name='trainingepisodemodel',
            unique_together={('training_run', 'iteration')},
        ),
    ]
