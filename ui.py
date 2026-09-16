import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource  #cache - fast access, temp storage => most freq accessed
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter Youtube Video Link") # str
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)