import pytest


@pytest.mark.django_db
def test_create_user(test_user, django_user_model):
    assert test_user.email == 'john@watson.com'
    assert test_user.name == 'John Watson'
    assert test_user.date_of_birth == '1994-07-19'
    assert len(test_user.identifier) == 8
    assert test_user.username is None
    assert test_user.first_name is None
    assert test_user.last_name is None
    assert test_user.USERNAME_FIELD == 'email'
    assert not test_user.is_staff
    assert not test_user.is_superuser
    assert test_user.is_active


@pytest.mark.django_db
def test_create_superuser(test_superuser):
    assert test_superuser.email == 'john@watson.com'
    assert test_superuser.name == 'John Watson'
    assert test_superuser.date_of_birth == '1994-07-19'
    assert len(test_superuser.identifier) == 8
    assert test_superuser.username is None
    assert test_superuser.first_name is None
    assert test_superuser.last_name is None
    assert test_superuser.USERNAME_FIELD == 'email'
    assert test_superuser.is_staff
    assert test_superuser.is_superuser
    assert test_superuser.is_active
