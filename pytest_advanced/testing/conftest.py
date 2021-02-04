import pytest
import yaml

from pytest_advanced.calc.calc import Calculator

with open("data/calc_data.yaml") as f:
    load_data = yaml.safe_load(f)

add_case_data = load_data['add']['add_case_data']
add_case_id = load_data['add']['add_case_id']
sub_case_data = load_data['sub']['sub_case_data']
sub_case_id = load_data['sub']['sub_case_id']
mul_case_data = load_data['mul']['mul_case_data']
mul_case_id = load_data['mul']['mul_case_id']
div_case_data = load_data['div']['div_case_data']
div_case_id = load_data['div']['div_case_id']


@pytest.fixture(scope='module')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc


@pytest.fixture(params=add_case_data, ids=add_case_id)
def add_get_data(request):
    add_data = request.param
    print('开始计算')
    yield add_data
    print("结束计算")


@pytest.fixture(params=sub_case_data, ids=sub_case_id)
def sub_get_data(request):
    sub_data = request.param
    print('开始计算')
    yield sub_data
    print("结束计算")


@pytest.fixture(params=mul_case_data, ids=mul_case_id, scope='function')
def mul_get_data(request):
    mul_data = request.param
    print('开始计算')
    yield mul_data
    print("计算结束")


@pytest.fixture(params=div_case_data, ids=div_case_id)
def div_get_data(request):
    div_data = request.param
    print('开始计算')
    yield div_data
    print("结束计算")


