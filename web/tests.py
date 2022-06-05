import pytest
from pytest_django.asserts import assertTemplateUsed
from web.models import User , Profile
import datetime

def generate_user(username,password):
    return User.objects.create_user(username=username,password=password,first_name="fasd",last_name="awad",email="asdasfsdgsad@gmail.com")

@pytest.mark.test
@pytest.mark.django_db
def test_template_upload_anonymous(API):
    req = API.get("/upload/")
    print(req)
    assert 302 == req.status_code
    assert "/login?next=/upload/" == req.url

@pytest.mark.test
@pytest.mark.django_db
def test_template_upload_pro_user(API):
    user = generate_user(username="fadymalak",password="12345678a")
    profile = Profile.objects.get(user_id=user.id)
    profile.due_date = datetime.datetime.now() + datetime.timedelta(days=10)
    profile.save()
    API.login(username="fadymalak",password="12345678a")
    req = API.get("/upload/")
    print(req)
    assert 200 == req.status_code
    assertTemplateUsed(req,"upload.html")

@pytest.mark.test
@pytest.mark.django_db
def test_template_upload_free_user(API):
    user = generate_user(username="fadymalak",password="12345678a")
    API.login(username="fadymalak",password="12345678a")
    req = API.get("/upload/")
    print(req)
    assert 302 == req.status_code
    assert "/payment" == req.url
    
    
    
    
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
    user = generate_user(username="fadymalak",password="12345678a")
    API.login(username='fadymalak',password='12345678a')
    req = API.get("/login/")
    print(req)
    assert 302 == req.status_code
    assert "/" == req.url

@pytest.mark.test
@pytest.mark.django_db
def test_template_logout_anonymous_user(API):
    req = API.get("/logout/")
    assert req.status_code == 302
    

@pytest.mark.test
@pytest.mark.django_db
def test_template_lists_anonymous_user(API):
    req = API.get("/list/")
    assert 302 == req.status_code

@pytest.mark.test
@pytest.mark.django_db
def test_template_lists_user(API):
    user = generate_user(username="fadymalak",password="12345678a")
    API.login(username='fadymalak',password='12345678a')
    req = API.get("/list/")
    assert 200 == req.status_code
    assertTemplateUsed(req,"lists.html")

