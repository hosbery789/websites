import streamlit as st 

import pyttsx3


def speak(sentence):

    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()
    


st.set_page_config(page_icon="C:/Users/Tonyr/Pictures/image_2024_05_12_152108972_Orw_icon.ico")

st.title("Personal Page ")
st.title("Only for me  ")
st.write("Some more")

st.image(r"C:\Users\Tonyr\Pictures\Jinwooo AI.jpeg", caption="personal" , use_column_width=True)


st.button("OK")


if st.button ('Connect' , key='Button_1') :

    speak("Ok GOt it")
    
    st.write("Button Clicked")

else:
    None





st.markdown("[Click for Quantum ](https://www.youTube.com)")



number = st.slider("pick A number ", 0, 200)
st.write("You Chose" ,  number)

audio_file = open(r"C:\Users\Tonyr\Videos\audio\『Sung Jin Woo』Solo Leveling ｜4k EDIT❗️(WEEKND - STAR BOY).mp3" , "rb" )

st.audio(audio_file.read() , format="Audio1.mp3")
