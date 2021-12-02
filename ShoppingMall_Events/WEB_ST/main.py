import streamlit as st 
import requests
from PIL import Image
import io
import webbrowser


def open_web(url: str) :  # 페이지 열기 

    webbrowser.open(url, new=1)

url = ' https://gg6hx0.deta.dev/'

res = requests.get(url)

lists = res.json()

option_candi = lists['쇼핑몰 리스트']

options = st.sidebar.selectbox(
    '어떤 사이트의 이벤트를 보시겠습니까?',
    option_candi
)

option = options

st.title(f'{option} 이벤트 페이지')


image_url_lists = lists[option]['image_url']
detail_url_lists = lists[option]['detail_url']


for idx in range(0,len(image_url_lists),3) :

    col1, col2, col3 = st.columns(3)

    try:
        with col1:
            with st.form(f"form{idx}") : 

                first_url = image_url_lists[idx]
                first_image = Image.open(io.BytesIO(requests.get(first_url).content))
                st.image(first_image)
                submit = st.form_submit_button("이동")
                if submit :
                    webbrowser.open(detail_url_lists[idx])
            

        with col2:
            with st.form(f"form{idx+1}") : 
                second_url = image_url_lists[idx+1]
                second_image = Image.open(io.BytesIO(requests.get(second_url).content))
                st.image(second_image,use_column_width='auto')
                submit = st.form_submit_button("이동")
                if submit :
                    webbrowser.open(detail_url_lists[idx+1])

            

        with col3:
            with st.form(f"form{idx+2}") : 
                third_url = image_url_lists[idx+2]
                third_image = Image.open(io.BytesIO(requests.get(third_url).content))
                st.image(third_image,use_column_width='auto')
                submit = st.form_submit_button("이동")
                if submit :
                    webbrowser.open(detail_url_lists[idx+2])

            

    except: 
        print("존재하지 않는 데이터")

    


