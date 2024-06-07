import pytest


@pytest.fixture()
def test_user(django_user_model):
    return django_user_model.objects.create_user(
        email='john@watson.com', password='123456Ab?', name='John Watson', date_of_birth='1994-07-19'
    )


@pytest.fixture()
def test_superuser(django_user_model):
    return django_user_model.objects.create_superuser(
        email='john@watson.com', password='123456Ab?', name='John Watson', date_of_birth='1994-07-19'
    )
