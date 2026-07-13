from yougileApi import yougileAPI
from faker import Faker
from config import config


api = yougileAPI()
fake = Faker()

# # Расскоментировать, если нет токена
# def test_create_token():
#     api.get_token()


def test_create_project():
    project_name = fake.company()
    resp = api.create_project(project_name, token=config.TOKEN)
    # Проверяем, что пришел код 201
    assert resp.status_code == 201

    id = resp.json()["id"]
    # Удаляем созданное
    api.update_project(id, "123", deleted=True, token=config.TOKEN)


def test_create_project_fail_token():
    project_name = fake.company()
    resp = api.create_project(project_name, token=123)
    assert resp.status_code == 401


def test_change_project_title():
    project_name = fake.company()
    resp = api.create_project(project_name, token=config.TOKEN)
    id = resp.json()["id"]
    new_name = fake.company()
    upd_resp = api.update_project(id, new_name, token=config.TOKEN).json()

    # проверяем, что id в ответе тот же
    assert upd_resp["id"] == id
    new_title = api.get_project_by_id(id, token=config.TOKEN)["title"]

    # проверяем, что тайтл изменился на заданный
    assert new_title == new_name

    # Удаляем созданное
    api.update_project(id, "123", deleted=True, token=config.TOKEN)


def test_change_project_wrong_id():
    project_name = fake.company()
    resp = api.create_project(project_name, token=config.TOKEN)
    id = resp.json()["id"]
    upd_resp = api.update_project(1, "123", token=config.TOKEN)
    # проверяем, что апдейт id=1 вернет нам 404
    assert upd_resp.status_code == 404

    # Удаляем созданное
    api.update_project(id, "123", deleted=True, token=config.TOKEN)


def test_get_project():
    project_name = fake.company()
    resp = api.create_project(project_name, token=config.TOKEN)

    id = resp.json()["id"]
    resp_by_id = api.get_project_by_id(id, token=config.TOKEN)
    title = resp_by_id["title"]

    # Проверяем что название созданного проекта совпадает с заданным
    assert project_name == title

    # Удаляем созданное
    api.update_project(id, "123", deleted=True, token=config.TOKEN)


def test_get_project_wrong_id():
    # проверяем, что запрос id=1 вернет нам 404
    resp_by_id = api.get_project_by_id(1, token=config.TOKEN)
    assert resp_by_id["statusCode"] == 404

# # Расскоментировать, если нет токена
# def test_delete_token():
#     api.delete_token(config.TOKEN)
