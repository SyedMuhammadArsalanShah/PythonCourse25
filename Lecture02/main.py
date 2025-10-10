import streamlit as st 

import pywhatkit as kit 
import pandas as pd

import time
import pyautogui

st.set_page_config("Whatsapp Automation System", page_icon="📱")
st.title("Whatsapp Automation")
st.write("Whatsapp sb ke liye")

merifileupload= st.file_uploader("Upload an Excel File ",type=["xlsx"])

portfolio=st.text_input("Enter a Portfolio",value="https://github.com/SyedMuhammadArsalanShah/")
message_data=st.text_area("Enter Your Detail Query ",value="Follow Me on  github ")

if merifileupload is not None:
    df=pd.read_excel(merifileupload)
    st.write("Contacts Upload Hogaye ")
    st.dataframe(df)
    if st.button("Send Message"):
        for a,row in df.iterrows():
            phonenumber=f"+{row["Phone"]}"
            message=f"{portfolio} {message_data}"
            try:
                kit.sendwhatmsg_instantly(phonenumber,message,wait_time=35)
                time.sleep(10)
                pyautogui.press("enter")
                st.write("message sent")
                time.sleep(10)
                pyautogui.press("enter")
            except Exception as e:
                st.write(e)