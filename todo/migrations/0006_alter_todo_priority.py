# Generated by Django 4.2.2 on 2023-06-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1️⃣', 'One'), ('2️⃣', 'Two'), ('3️⃣', 'Three'), ('4️⃣', 'Four'), ('5️⃣', 'Five'), ('6️⃣', 'Six'), ('7️⃣', 'Seven'), ('8️⃣', 'Eight'), ('9️⃣', 'Nine'), ('🔟', 'Ten')], max_length=5),
        ),
    ]
