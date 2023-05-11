
import streamlit as st







# 设置网页名称
from tools import GBK2312, str_cou
from request2 import this_chole

st.set_page_config(page_title='V链开放接口')




# 设置网页标题
st.header('开放接口调用')


# 侧边栏
add_selectbox = st.sidebar.selectbox('工具',('开放接口调用','文字方面', '计算汉字数量'))
if "开放接口调用"in add_selectbox:
    # 设置网页子标题
    st.subheader('开放接口调用')
    this_chole()
elif "文字方面"in add_selectbox:
    st.subheader('随机生成汉字')
    inp=st.text_input("请输入生成数量")
    te1=GBK2312(int(inp))
    st.text(te1)
    if te1 !="":
        inp = st.text_input("计算汉字数量")
        te1 = str_cou(inp)
        st.text(te1)

