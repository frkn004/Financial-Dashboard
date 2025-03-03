import streamlit as st
from utils.data_loader import load_data

def main():
    st.set_page_config(
        page_title="Aiva Financial",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("💰 Finansal Dashboard")

if __name__ == "__main__":
    main()
