import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["数字档案",
                                              "动物图鉴",
                                              "简易danking播放器",
                                              "音乐播放器",
                                              "南宁美食数据",
                                              "🔞个人简历生成表"])

with tab1:
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
    

with tab2:
    st.set_page_config(page_title='动物园', page_icon='ggbond')

    images = [
    {
            'url':'https://attach.veryapex.com/2023/07/jjb.jpg',
            'parm':'ggbond'
    },
    {
            'url':'https://ts2.tc.mm.bing.net/th/id/OIP-C.dLPSAF_r4whoYNty63L_PgHaEo?cb=12ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
            'parm':'ggbond'
    },
    {
            'url':'https://huyaimg.msstatic.com/avatar/1022/d0/d2676d2993e82a01dd88b75738edf9_180_135.jpg?1703059207',
            'parm':'Danking'
    }
    ]
    if 'ind' not in st.session_state:
            st.session_state['ind']=0

    def nextImg():
            st.session_state['ind'] =(st.session_state['ind'] + 1)% len(images)

    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

    c1,c2 = st.columns(2)

    with c1:
            st.button('上一张', on_click=nextImg,use_container_width=True)

    with c2:
            st.button('下一张', on_click=nextImg,use_container_width=True)
            
with tab3:
    st.title("📺︎简易danking播放器")

    st.set_page_config(page_title='视频', page_icon='📺︎')

    video_url = [
        {
       'url':'https://upos-sz-estghw.bilivideo.com/upgcxcode/73/18/32384681873/32384681873-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&gen=playurlv3&deadline=1761303356&mid=0&uipk=5&oi=2672555743&os=estghw&og=hw&trid=cb7e064860274d17aaa41986b8a5073h&nbs=1&upsig=66171c5af2c1f5bf3313ae55a4ce8c9e&uparams=e,platform,gen,deadline,mid,uipk,oi,os,og,trid,nbs&bvc=vod&nettype=0&bw=329593&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
       'title':'danking',
       'number':'1'
       },
        {
       'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/32/16/1503841632/1503841632-1-192.mp4?e=ig8euxZM2rNcNbNgnWdVhwdlhbNHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&uipk=5&platform=html5&oi=1782024106&nbs=1&trid=efa9da65cdf04612871efecb2cec25eh&deadline=1761303280&mid=0&gen=playurlv3&os=estgcos&upsig=6f58a9ce873193a162dae190a4aeb997&uparams=e,og,uipk,platform,oi,nbs,trid,deadline,mid,gen,os&bvc=vod&nettype=0&bw=1843750&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
       'title':'乌兰巴托',
       'number':'2'
       },
        {
       'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/19/77/28647557719/28647557719-1-192.mp4?e=ig8euxZM2rNcNbNVnWdVhwdlhbdHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=1782024106&os=estgcos&trid=9e12356f2f814775b1a288d92adbe0fh&nbs=1&uipk=5&platform=html5&mid=0&gen=playurlv3&og=cos&deadline=1761303429&upsig=cffe660fa75b1febe6cd6f713390befe&uparams=e,oi,os,trid,nbs,uipk,platform,mid,gen,og,deadline&bvc=vod&nettype=0&bw=1677456&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
       'title':'“我会装作不在乎 直到真正不在乎”',
       'number':'3'
               }
    ]

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    st.title(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['number']+'集')
    st.video(video_url[st.session_state['ind']]['url'])

    c1,c2,c3 = st.columns(3)

    def play(arg):

             st.session_state['ind']=int(arg)

    for i in range(len(video_url)):
        st.button('第' + str(i+1) + '集',use_container_width=True,on_click=play,args=([i]))

with tab4:
    st.title("🎧️简易音乐播放器")

    st.text("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

    images = [
            {
                'url':'https://music.163.com/song/media/outer/url?id=2526625.mp3',
                'author':'歌手：Deep Side',
                'photo':'https://p1.music.126.net/dUSiZ5ASRpWgaq9OTMtoDw==/860917604602698.jpg?param=250y250',
                'name':'booty music'
            },
            {
                'url':'https://music.163.com/song/media/outer/url?id=1842728629.mp3',
                'author':'歌手：郑润泽',
                'photo':'https://p1.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=250y250',
                'name':'如果呢'
            },
            {
                'url':'https://music.163.com/song/media/outer/url?id=18638059.mp3',
                'author':'歌手：Justin Bieber',
                'photo':'https://p1.music.126.net/w-KG9LFj7Z2F9bjtlHG3JA==/109951165476414199.jpg?param=250y250',
                'name':'One Time'
            }
    ]
    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)
    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)


    b1,b2=st.columns([1,2])
    with b1:
    
       st.image(images[st.session_state['ind']]['photo'],caption=images[st.session_state['ind']]['name'])

    with b2:
       st.title(images[st.session_state['ind']]['name'])
       st.header(images[st.session_state['ind']]['author'])
    
       c1,c2 = st.columns(2)

       with c1:
    
        st.button('上一首',on_click=lastImg,use_container_width=True)
        
       with c2:
           
        st.button('下一首',on_click=nextImg,use_container_width=True)

    st.audio(images[st.session_state['ind']]['url'])

with tab5:
    import pandas as pd
    import numpy as np

    restaurants_data = {
        "餐厅":['牛天宝','大福食堂','破烂泡泡','大山自助烤肉','苏格拉岛自助'],
        "类型":["自助餐", "中餐", "自助餐", "自助餐", "自助餐"],
        "评分":[4.6, 4.8, 4.7, 4.7, 4.5],
        "人均消费(元)": [70, 50,60,80, 90],
    }    
    data = {
        "latitude":[22.832202,22.814752,22.816595,22.813986,22.813919],
        "longitude":[108.286485,108.320848,108.321551,108.321535,108.321484]
    }
    df = pd.DataFrame(data)
    st.map(df)

    import streamlit as st
    import pandas as pd

    data = {    
        '牛天宝':[200, 150, 180,180,120,130,150,120, 160,123,150, 200],
        '大福食堂':[120, 160, 123,150,200,190,160,160,150,180,180,200],
        '破烂泡泡':[110, 100, 160,190,160,160,150, 180,180,160,170,180],
        '大山自助烤肉':[150, 200, 230,200,190,180,180,200,180,160,170,160],
        '苏格拉岛自助':[120,240, 143,150, 200, 230,200,190,180,180,200,170],
    }
    df = pd.DataFrame(data)

    index = pd.Series(['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'], name='月份')

    df.index = index

    st.dataframe(df)
    st.table(df)

    st.line_chart(df)
 
    st.bar_chart(df)

    map_data = {
         "latitude":[22.832202,22.814752,22.816595,22.813986,22.813919],
        "longitude":[108.286485,108.320848,108.321551,108.321535,108.321484]
    }

    st.map(pd.DataFrame(map_data))


    import streamlit as st
    import pandas as pd

    crowd_data = pd.DataFrame({
        "时间":['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
        "牛天宝":[30,95,50,70,40,85,60,25,85,65,35,90],
        "大福食堂":[65,35,90,65,40,80,50,45,75,55,66,84],
        "破烂泡泡":[34,57,89,12,45,78,23,67,90,56,82,39],
        "大山自助烤肉":[47,83,19,62,95,31,76,24,58,13,69,40],
        "苏格拉岛自助":[28,91,55,17,74,36,80,42,66,35,59,88]
    })

    st.line_chart(crowd_data.set_index('时间'))

with tab6:
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
