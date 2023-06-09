from django.db import models
from django.contrib.auth.models import User






class ToDo(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo")
    title = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=status_choices)
    priority = models.CharField(max_length=2, choices=priority_choices)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "ToDo"

