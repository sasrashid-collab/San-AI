import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- 1. ڕێکخستنی ژیری دەستکرد ---
# کلیلەکە لە فایلی .env دەخوێنێتەوە بۆ پاراستن
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- 2. ڕێکخستنی شێوازی لاپەڕە ---
st.set_page_config(page_title="San-AI", page_icon="🤖")
st.markdown("""
    <style>
    .stApp { background: #050a14; color: #00ffcc; }
    input { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. سیستەمی چوونەژوورەوە ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🛡️ San-AI Login")
    pwd = st.text_input("کۆدی 'san11' بنووسە بۆ دەسپێکردن:", type="password")
    if st.button("Unlock"):
        if pwd == "san11":
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("کۆدەکە هەڵەیە!")
else:
    # --- 4. بەشی سەرەکی پڕۆگرامەکە ---
    st.title("🚀 بەخێرهاتی San Shadman!")
    st.write("دۆخی سیستەم: **١٠٠٪ ئامادەیە** ✅")
    
    st.divider()
    
    query = st.text_input("چی لە San-AI دەپرسیت؟ (بۆ نموونە: باسی هەولێرم بۆ بکە)")
    
    if query:
        with st.spinner('خەریکە وەڵام دەدەمەوە...'):
            try:
                # لێرە داوا لە Gemini دەکەین وەڵام بداتەوە
                response = model.generate_content(f"وەک San-AI وەڵام بدەرەوە بە کوردی سۆرانی: {query}")
                st.success(f"🤖 San-AI: {response.text}")
            except Exception as e:
                st.error("کێشەیەک لە پەیوەندی دروست بوو. دڵنیابە کلیلەکە (API Key) ڕاستە.")

    st.sidebar.button("Log Out", on_click=lambda: st.session_state.update({"auth": False}))
