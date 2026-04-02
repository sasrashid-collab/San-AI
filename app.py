import streamlit as st
import requests

# --- Settings ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"

st.set_page_config(page_title="San-AI Ultimate", page_icon="🤖")

# --- UI Styling ---
st.markdown("""<style> .stApp { background: #050a14; color: #00ffcc; } </style>""", unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🛡️ San-AI Login")
    pwd = st.text_input("Code:", type="password")
    if st.button("Unlock"):
        if pwd.lower().strip() == SECRET_CODE:
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Access Denied.")
else:
    st.title(f"🚀 Welcome, Boss San")
    tab1, tab2 = st.tabs(["🧠 Brain", "🎨 Art Studio"])

    with tab1:
        query = st.text_input("Ask anything:", key="q_brain")
        if query:
            st.info("Searching...")
            # ڕاستکردنەوەی لینکی گەڕان
            search_url = f"https://duckduckgo.com{query.replace(' ', '+')}&format=json"
            try:
                res = requests.get(search_url).json()
                ans = res.get("AbstractText", "I found some info, but try asking about a specific thing like 'The Moon' or 'Robots'!")
                if not ans:
                    ans = "I'm still learning about this topic. Ask me something else!"
                st.success(ans)
                # خوێندنەوەی وەڵامەکە بە دەنگ
                audio_url = f"https://google.com{ans[:200].replace(' ', '%20')}&tl=en&client=tw-ob"
                st.audio(audio_url)
            except:
                st.error("Connection error. Check your internet!")

    with tab2:
        prompt = st.text_input("Describe your art (English):", key="p_art")
        if st.button("Create Image"):
            if prompt:
                st.info("San-AI is painting...")
                # بەکارهێنانی سێرڤەرێکی جێگیر بۆ وێنە
                clean_p = prompt.replace(' ', '%20')
                img_url = f"https://pollinations.ai{clean_p}?width=800&height=800&nologo=true&seed=55"
                st.image(img_url, caption=f"Result for {OFFICIAL_OWNER}")
            else:
                st.warning("Please type something!")
