import streamlit as st

st.title("🐉学生 谭玮奎 - 数字档案")
st.header("🥪基础信息")
st.markdown('##### 学生ID:23031310121')
st.markdown(" ##### 注册时间：:green[2025/10/10 08:00]|精神状态:✋😭✋")
st.markdown(" ##### 当前教室：:blue[实训楼204]|安全等级:普通")
st.header("🔱技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言", value="88%", delta="6%")
c2.metric(label="pythin", value="76%", delta="6%")
c3.metric(label="java", value=None, delta="0", delta_color="off")
import pandas as pd
data = {
    '日期':['2025/10/11','2025/10/12','2025/10/15'],
    '任务':['学生数字档案','课程管理系统','数据图表系统'],
    '状态':['✅完成','🕣进行中','❎未完成'],
}
index = pd.Series(['0', '1', '2'])
df = pd.DataFrame(data, index=index)
st.subheader('🔞任务日志')
st.dataframe(df)
st.subheader('🔞最新代码成果')
# 创建要显示的Python代码块的内容
python_code = '''def hello():
    print("st.title("🐉学生 谭玮奎 - 数字档案")
st.header("🥪基础信息")
st.markdown('##### 学生ID:23031310121')
st.markdown(" ##### 注册时间：:green[2025/10/10 08:00]|精神状态:✋😭✋")
st.markdown(" ##### 当前教室：:blue[实训楼204]|安全等级:普通")
st.header("🔱技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言", value="88%", delta="6%")
c2.metric(label="pythin", value="76%", delta="6%")
c3.metric(label="java", value=None, delta="0", delta_color="off")
import pandas as pd
data = {
    '日期':['2025/10/11','2025/10/12','2025/10/15'],
    '任务':['学生数字档案','课程管理系统','数据图表系统'],
    '状态':['✅完成','🕣进行中','❎未完成'],
}
index = pd.Series(['0', '1', '2'])
df = pd.DataFrame(data, index=index)
st.subheader('🔞任务日志')
st.dataframe(df)")
'''
st.code(python_code, line_numbers=True)
st.markdown('***')
st.markdown(" ##### :green[>>SYSTEM MESSAGE] 下一个任务目标已解锁...")
