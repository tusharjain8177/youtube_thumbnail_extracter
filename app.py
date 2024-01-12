import streamlit as st 
import main


st.title("Download Thumbnail of any Youtube Video")

Video_url=st.text_input("Enter Video url here")
if Video_url:
    thumbnail_url = main.get_thumbnail(Video_url)
    st.image(thumbnail_url)
    if st.button("Download"):
        main.download_thumbnail(Video_url)
        
    