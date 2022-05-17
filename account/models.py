from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    """Класс пользователя блога"""

    send_message = models.BooleanField(default=True,
                                       verbose_name='Получать сообщения на электронную почту о новых постах')
    image = models.ImageField(upload_to="media", default='python.jpeg')

