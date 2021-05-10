import streamlit as st
import os

# layout setting
st.set_page_config(page_title="namazu-tabular",page_icon=None,layout='wide',initial_sidebar_state="collapsed")
hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {
                            
                            visibility: hidden;
                            
                            }
                        footer:after {
                            content:'Made for my mother'; 
                            visibility: visible;
                            display: block;
                            position: relative;
                            #background-color: red;
                            padding: 5px;
                            top: 2px;
                        }
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

from file_downloader import get_binary_file_downloader_html

st.markdown("<h1 style='text-align: center;'>Sounds concatenator</h1>", unsafe_allow_html=True)
st.empty()

st.markdown("## Import first audio file")
first = st.file_uploader("first sound", type=['mp3','m4a'], key='a', accept_multiple_files=False)
st.markdown("## Import second audio file")
second = st.file_uploader("second sound", type=['mp3','m4a'], key='b', accept_multiple_files=False)

from pydub import AudioSegment

if (first and second):
    # 音声ファイルの読み込み
    sound1 = AudioSegment.from_file(first)
    sound2 = AudioSegment.from_file(second)

    # 連結
    sound = sound1 + sound2

    # 保存
    sound.export("output.mp3", format="mp3")
    st.markdown("Your audio file is ready for download")         
    st.markdown(get_binary_file_downloader_html("output.mp3", 'the sound file'), unsafe_allow_html=True)
    os.remove("output.mp3")