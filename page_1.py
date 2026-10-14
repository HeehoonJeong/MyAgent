import streamlit as st
from dotenv import load_dotenv # 환경파일 불러오기위한 함수 환경파일엔 개인정보들 유출되면 안되는 것들이 담겨있음
#모델 객체 생성
from langchain.chat_models import init_chat_model
# 도구 생성
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_tavily import TavilySearch



load_dotenv()
model = init_chat_model('gpt-5.4-mini')

tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)


@tool
def get_weather(location : str) -> str:
    '''특정 지역의 날씨 정보 조회 도구'''
    return f'{location}의 날씨는 -5도에 미세먼지는 매우 나쁨'


agent = create_agent(model, tools=[get_weather])

st.title('1페이지 입니다.')
if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input('무엇이든 물어보세요')


if prompt:
    response = model.invoke(
        {'messages' : [{'role' : 'user', 'content' : prompt}]}
    )
    st.session_state.messages.append({'role' : 'user', 'content': prompt})
    st.session_state.messages.append({'role' : 'ai', 'content': response.content})

for message in st.session_state.messages :
    with st.chat_message(message['role']):
        st.write(message['content'])
