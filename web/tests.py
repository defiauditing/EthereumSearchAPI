import pytest
from pytest_django.asserts import assertTemplateUsed
from web.models import User

def generate_user():
    return User.objects.create_user(username="testuser",password="12345678a",first_name="fasd",last_name="awad",email="asdasfsdgsad@gmail.com")

@pytest.mark.test
@pytest.mark.django_db
def test_template_upload(API):
    req = API.get("/upload/")
    assertTemplateUsed(req,"upload.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_register(API):
    req = API.get("/register/")
    assert req.status_code == 200
    assertTemplateUsed(req,"register.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_login_anonymous(API):
    req = API.get("/login/")
    assertTemplateUsed(req,"login.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_login_already_logged(API):
    user = generate_user()
    API.force_authenticate(user)
    req = API.get("/login/")
    assertTemplateUsed(req,"nindex.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_logout(API):
    req = API.get("/logout/")
    assert req.status_code == 200
    assertTemplateUsed(req,"login.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_lists(API):
    req = API.get("/list/")
    assertTemplateUsed(req,"lists.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_details(API):
    req = API.get("/details/")
    assertTemplateUsed(req,"files.html")