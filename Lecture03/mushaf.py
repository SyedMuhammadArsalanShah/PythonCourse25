import streamlit as st 
import requests


st.set_page_config(page_title="MushafWebAPP", page_icon="📖")
st.title("Mushaf Lecture ")
st.sidebar.title("Controls")
st.sidebar.write("Select Surah And Search Ayah")


surahlist=requests.get("http://api.alquran.cloud/v1/surah").json()["data"]
surah_names=[f"{s["number"]} . {s["englishName"]} . {s["name"]}" for s in surahlist]
selected_surah_name=st.sidebar.selectbox("Choose Surah", surah_names)
selected_surah_num=int(selected_surah_name.split(".")[0])
# st.write(selected_surah_num)

search_keyword=st.sidebar.text_input("Search Arabic Ayah")
show_translation= st.sidebar.checkbox("Show Translation")
show_Recitation= st.sidebar.checkbox("Show Recitation")
choice_tr= st.sidebar.selectbox("Choose Translation",["en.sahih","ur.maududi","ur.jalandhry"])


recitation_url=f"http://api.alquran.cloud/v1/surah/{selected_surah_num}/ar.abdurrahmaansudais"
rec_response=requests.get(recitation_url).json()
arabic_ayah=rec_response["data"]["ayahs"]

if show_translation:
    recitation_url_tr=f"http://api.alquran.cloud/v1/surah/{selected_surah_num}/{choice_tr}"
    rec_response_tr=requests.get(recitation_url_tr).json()
    tr_ayah=rec_response_tr["data"]["ayahs"]
else:
    tr_ayah=[None]*len(arabic_ayah)




if search_keyword.strip():
    filter_Ar=[]
    filter_Tr=[]
    for i, ayah in enumerate(arabic_ayah):
        if search_keyword in ayah["text"]:
            filter_Ar.append(ayah)
            filter_Tr.append(tr_ayah[i])
    arabic_ayah=filter_Ar
    tr_ayah=filter_Tr


st.subheader(selected_surah_name)
for i , ayah in enumerate(arabic_ayah):
    st.markdown(f"**{ayah['numberInSurah']}**-{ayah["text"]}")
    if show_Recitation:
        if 'audio' in ayah and ayah["audio"]:
            st.audio(ayah['audio'],format="audio/mp3")
    if show_translation and tr_ayah[i]:
        st.info(tr_ayah[i]["text"])

st.html("<p></p>")
st.balloons()
st.snow()
st.markdown("---")
st.markdown("Developed BY SMASB")
