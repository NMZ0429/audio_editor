import streamlit as st
import os

# layout setting
st.set_page_config(page_title="Made by Namazur",page_icon=None,layout='wide',initial_sidebar_state="collapsed")
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

st.markdown("## Import first audio files")
st.markdown("### Upload files in order such that the files are concatenated in that way. If you upload two files A first then B, resultant audio file plays A then B.\n\n You can drag and drop file one by one or multiple files at once.")
audio_files = st.file_uploader("", type=['mp3','m4a'], key='a', accept_multiple_files=True)
st.empty()

num_files = len(audio_files)
confirmed = st.button('Start')

from pydub import AudioSegment

if (num_files > 0) and confirmed: 
    # 音声ファイルの読み込み
    combined_sound = AudioSegment.empty()
    for i in audio_files:
        sound_i = AudioSegment.from_file(i)
        combined_sound += sound_i

    # 保存
    combined_sound.export("output.mp3", format="mp3")

    # ダウンロードリンク生成
    st.markdown("Your audio file is ready for download")         
    st.markdown(get_binary_file_downloader_html("output.mp3", 'the sound file'), unsafe_allow_html=True)
    
    # ファイル消去
    os.remove("output.mp3")