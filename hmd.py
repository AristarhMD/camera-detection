import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detection")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        dt = datetime.now()


        cv2.putText(img=frame, text=dt.strftime("%A"), org=(50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=dt.strftime("%H:%M:%S"), org=(50, 100), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
