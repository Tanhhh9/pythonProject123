#读取yaml文件
from yaml import safe_load


def yaml_data1(file=r'D:\Saas\4\pythonProject1\V_api\data\req.yaml'):
    f= open(file, mode="r",encoding='utf_8')
    data = f.read()
    data1 = safe_load(data)
    return data1