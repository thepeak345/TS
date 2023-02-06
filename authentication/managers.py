from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def _create_user(self, email, firstname, lastname, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not firstname:
            raise ValueError("Вы не ввели имя")
        if not lastname:
            raise ValueError("Вы не ввели фамилию")
        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, firstname, lastname, password):
        return self._create_user(email, firstname, lastname, password)

    def create_superuser(self, email, firstname, lastname, password):
        return self._create_user(email, firstname, lastname, password, is_staff=True, is_superuser=True)