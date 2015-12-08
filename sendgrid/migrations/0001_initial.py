# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255)),
                ('data_type', models.IntegerField(default=0, verbose_name='Data Type', choices=[(0, 'Unknown'), (1, 'Boolean'), (2, 'Integer'), (3, 'Float'), (4, 'Complex'), (5, 'String')])),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Argument',
                'verbose_name_plural': 'Arguments',
            },
        ),
        migrations.CreateModel(
            name='BounceReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BounceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ClickUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.CharField(null=True, editable=False, max_length=36, blank=True, help_text=b'UUID', unique=True)),
                ('from_email', models.CharField(help_text=b"Sender's e-mail", max_length=254)),
                ('to_email', models.CharField(help_text=b"Primiary recipient's e-mail", max_length=254)),
                ('category', models.CharField(help_text=b'Primary SendGrid category', max_length=150, null=True, blank=True)),
                ('response', models.IntegerField(help_text=b'Response received from SendGrid after sending', null=True, blank=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Email Message',
                'verbose_name_plural': 'Email Messages',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueArgument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('argument', models.ForeignKey(to='sendgrid.Argument')),
            ],
            options={
                'verbose_name': 'Unique Argument',
                'verbose_name_plural': 'Unique Arguments',
            },
        ),
        migrations.CreateModel(
            name='BounceEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sendgrid.Event')),
                ('status', models.CharField(max_length=16)),
                ('bounce_reason', models.ForeignKey(to='sendgrid.BounceReason', null=True)),
                ('bounce_type', models.ForeignKey(to='sendgrid.BounceType', null=True)),
            ],
            options={
                'verbose_name': 'Bounce Event',
                'verbose_name_plural': 'Bounce Events',
            },
            bases=('sendgrid.event',),
        ),
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sendgrid.Event')),
                ('click_url', models.ForeignKey(to='sendgrid.ClickUrl')),
            ],
            options={
                'verbose_name': 'Click Event',
                'verbose_name_plural': 'Click Events',
            },
            bases=('sendgrid.event',),
        ),
        migrations.CreateModel(
            name='DeferredEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sendgrid.Event')),
                ('response', models.TextField()),
                ('attempt', models.IntegerField()),
            ],
            bases=('sendgrid.event',),
        ),
        migrations.CreateModel(
            name='DeliverredEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sendgrid.Event')),
                ('response', models.TextField()),
            ],
            bases=('sendgrid.event',),
        ),
        migrations.CreateModel(
            name='DroppedEvent',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sendgrid.Event')),
                ('reason', models.CharField(max_length=255)),
            ],
            bases=('sendgrid.event',),
        ),
        migrations.CreateModel(
            name='EmailMessageAttachmentsData',
            fields=[
                ('email_message', models.OneToOneField(related_name='attachments', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Attachments', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Attachment Data',
                'verbose_name_plural': 'Email Message Attachments Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageBccData',
            fields=[
                ('email_message', models.OneToOneField(related_name='bcc', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Blind Carbon Copies', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Bcc Data',
                'verbose_name_plural': 'Email Message Bcc Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageBodyData',
            fields=[
                ('email_message', models.OneToOneField(related_name='body', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Body', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Body Data',
                'verbose_name_plural': 'Email Message Body Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageCcData',
            fields=[
                ('email_message', models.OneToOneField(related_name='cc', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Carbon Copies', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Cc Data',
                'verbose_name_plural': 'Email Message Cc Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageExtraHeadersData',
            fields=[
                ('email_message', models.OneToOneField(related_name='extra_headers', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Extra Headers', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Extra Headers Data',
                'verbose_name_plural': 'Email Message Extra Headers Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageSendGridHeadersData',
            fields=[
                ('email_message', models.OneToOneField(related_name='sendgrid_headers', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='SendGrid Headers', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message SendGrid Headers Data',
                'verbose_name_plural': 'Email Message SendGrid Headers Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageSubjectData',
            fields=[
                ('email_message', models.OneToOneField(related_name='subject', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='Subject', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message Subject Data',
                'verbose_name_plural': 'Email Message Subject Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageToData',
            fields=[
                ('email_message', models.OneToOneField(related_name='to', primary_key=True, serialize=False, to='sendgrid.EmailMessage')),
                ('data', models.TextField(verbose_name='To', editable=False)),
            ],
            options={
                'verbose_name': 'Email Message To Data',
                'verbose_name_plural': 'Email Message To Data',
            },
        ),
        migrations.AddField(
            model_name='uniqueargument',
            name='email_message',
            field=models.ForeignKey(to='sendgrid.EmailMessage'),
        ),
        migrations.AddField(
            model_name='event',
            name='email_message',
            field=models.ForeignKey(to='sendgrid.EmailMessage'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='sendgrid.EventType'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='arguments',
            field=models.ManyToManyField(to='sendgrid.Argument', through='sendgrid.UniqueArgument'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='categories',
            field=models.ManyToManyField(to='sendgrid.Category'),
        ),
    ]
