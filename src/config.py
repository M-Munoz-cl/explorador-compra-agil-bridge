from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

TICKET = os.getenv("TICKET")

if not TICKET:
    TICKET = st.secrets["TICKET"]

BASE_URL = "https://api2.mercadopublico.cl"

HEADERS = {'ticket': TICKET}