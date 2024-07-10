import streamlit as st
from openai import OpenAI



# OpenAI API 키 설정
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

# Streamlit 앱 설정
st.title("학생들을 위한 GPT 챗봇")
st.write("안녕하세요! 저는 GPT 기반 챗봇입니다. 무엇이든 물어보세요.")

# 채팅 히스토리 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:", key="user_input")

if st.button("전송"):
    if user_input:

        # GPT-4 API 호출
        response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that provides feedback based on given criteria."},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.1,
                    max_tokens=200
                )
        
        # 응답 표시
        answer = response.choices[0].message.content.strip()
        st.write(f"GPT-4o의 응답: {answer}")

        # 메시지 히스토리에 추가
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": answer})


# 채팅 히스토리 표시
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div style='text-align: right; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin: 10px 0;'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #E1E1E1; padding: 10px; border-radius: 10px; margin: 10px 0;'>{message['content']}</div>", unsafe_allow_html=True)
