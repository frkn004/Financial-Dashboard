import streamlit as st
from utils.data_loader import load_data
from utils.helpers import format_currency

def main():
    st.set_page_config(
        page_title="Aiva Financial",
        page_icon="💰",
        layout="wide"
    )

    if 'data' not in st.session_state:
        st.session_state.data = None

    st.title("Aiva Financial Dashboard")

    # Dosya yükleme
    uploaded_file = st.file_uploader("CSV Dosyası Yükle", type=['csv'])
    if uploaded_file:
        st.session_state.data = load_data(uploaded_file)

    if st.session_state.data is not None:
        st.success("Veri başarıyla yüklendi!")

if __name__ == "__main__":
    main()
