import streamlit as st

from bokeh.plotting import figure

from tools import requ_do
from request1 import RE_data

def this_chole():
    str_key_id = '"secretId":"e3Byb2plY3RJZD1YTS0xMTAyLCBvcmdJZD1KRy0xMTAyfQ==","secretKey":"YzI4YWY3NDUxMjRkMjMxNGZkMGUyOWJiYWU5NjQ5OGMxMDc1NDVhNTY1OGEzOWFkYzJhOThjODkwMjliODlmNA=="}'

    # 下拉
    chole = st.selectbox("请选择平台", ["直接输入参数", "云采", "权益"])
    chole1 = st.selectbox("请选择接口", ["平台商品池接口", "查询商品详情", "查询平台商品库存","查询平台商品价格","查询平台供应商","查询分类列表"])
    if "不需要密钥" in chole:
        pass
    elif "云采" in chole:
        if "平台商品池接口"in chole1:
            requ_do(key=str_key_id,str="平台商品池接口")
        elif "查询商品详情"in chole1:
            requ_do(key=str_key_id,str="查询商品详情")
        elif "查询平台商品库存"in chole1:
            requ_do(key=str_key_id,str="查询平台商品库存")
        elif "查询平台商品价格"in chole1:
            requ_do(key=str_key_id,str="查询平台商品价格")
        elif "查询平台供应商"in chole1:
            requ_do(key=str_key_id,str="查询平台供应商")
        elif "查询分类列表"in chole1:
            requ_do(key=str_key_id,str="查询分类列表")
        else:
            pass





    else:
        str_key_id = "null"