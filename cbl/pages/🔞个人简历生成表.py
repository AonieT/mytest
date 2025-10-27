import streamlit as st

st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
st.title('🔞个人简历生成表')
st.text('使用Seamlit创建您的个性化简历')
c1, c2, = st.columns(2)
with c1:
    st.header('个人信息表单')
    st.markdown('***')
    name = st.text_input('姓名', autocomplete='name')
    position = st.text_input('职位', autocomplete='position')
    phone = st.text_input('电话', autocomplete='phone')
    postbox = st.text_input('邮箱', autocomplete='postbox')
    from datetime import datetime, timedelta
    date = st.date_input("出生日期", value=None)
    st.text('性别')
    genden = st.radio(
        '你的性别是什么？',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden'
)
    def my_format_func(option):
        return f'{option}'
    city = st.selectbox('学历', ['小学', '初中', '高中','中专','大学','大专','研究生','硕士','博士'], format_func=my_format_func, index=2)
    language = st.selectbox('语言能力', ['英语', '汉语', '西班牙语','阿拉伯语','法语','葡萄牙语','俄语','德语','日语','韩语'], format_func=my_format_func, index=2)
    def my_format_func(option):
        return f'{option}'
    options_1 = st.multiselect(
        '技能（可多选）',
        ['Java', 'HTML/CSS', '机器学习', 'PYthon', 'C语言'],
        format_func=my_format_func,
        )
    year = st.slider('工作经验（年）', 0, 40)
    money = st.slider(
        '期望薪资范围（元）',
        0, 20000, (0, 0))
    jj=st.text_area(label='个人简介', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
    w1 = st.time_input("每日最佳联系时间段")
    photo = st.file_uploader("上传你的照片")
    if photo is not None: 
        bytes_data=photo.getvalue()

with c2:
    st.header('简历实时预览')
    st.markdown('***')
    b1, b2, = st.columns([1,1])
    with b1:
        st.image(bytes_data)
        st.write('职位: ',position)
        st.write('电话',phone)
        st.write('邮箱',postbox)
        st.write('出生日期',date)
    with b2:
        st.write('性别: ',genden)
        st.write('学历: ',city)
        st.write('工作经验: ',year)
        st.write('期望薪资: ',money)
        st.write('最佳联系时间: ',w1)
        st.write('语言能力: ',language)
    st.markdown('***')
    st.write('个人简介: ',jj)
    st.markdown('***')
    
    
