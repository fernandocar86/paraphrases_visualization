import streamlit as st


st.set_page_config(
    page_title="Parafraseador",
    page_icon="🗪",
    layout="wide"
)


# This hides streamlit's info
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Name of the web app
st.title('Parafraseador')

# File uploader
uploaded_file = st.file_uploader("Suba su texto en un archivo .TXT para visualizarlo", type=["txt"])


if uploaded_file is not None:
    # once uploaded, the text of the file is shown below line by line
    text = uploaded_file.getvalue().decode("utf-8")
    lines = text.splitlines()
    for line in lines:
        st.markdown(f'<a href="https://google.com">{line}</a>', unsafe_allow_html=True)

    
