import pytest
# from rest_framework.test import APIClient
from django.test.client import Client 


import random
# def run_sql(sql):
    # conn = sqlite3.connect(database='test.sqlite',check_same_thread=False)
    # cur = conn.cursor()
    # cur.execute(sql)
    # conn.close()
# 
# TODO if i uncomment this function it will Use settings_test default
#now it use in-memory sqlite
# @pytest.fixture(scope='session')
# def django_db_setup():
    # '''Custom database configuration for Test'''
# 
    # yield
#     for connection in connections.all():
#         connection.close()
# # 
    # run_sql("select 'delete from ' || name from sqlite_master where type = 'table';")



def pytest_runtest_setup(item):
    print(f"Hook Anounce", item)


@pytest.fixture
def API():
    return Client()
