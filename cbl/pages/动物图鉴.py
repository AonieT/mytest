import streamlit as st

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