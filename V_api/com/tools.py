import random
#随机生成汉字
from yaml import safe_load
import streamlit as st

from request1 import RE_data


def GBK2312(num):
    a=''
    for i in range(0,num):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        str = bytes.fromhex(val).decode('gb2312')
        a=a+str
    return a
#计算汉字数量
def str_cou(str):
    a=len(str)
    return a

def requ_do(key,str):
    title = st.text_area('输入参数', ' ')
    title_str = title.replace(title[-1], f',{key}')
    if st.button('运行'):

        cl1, cl2 = st.columns([3, 1.5])
        with cl1:
            st.text("返回结果：")
            st.json(RE_data(title_str, f"{str}").req()["text"])
        with cl2:
            st.metric("响应时间", f"{RE_data(title_str, f'{str}').req()['date']}ms")
