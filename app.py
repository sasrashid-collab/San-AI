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
        query = st.text_input("Ask anything (English):", key="q_brain")
        if query:
            st.info("🔍 Searching Knowledge Base...")
            # بەکارهێنانی ویکیپیدیا بۆ گەڕانی جێگیر و بێ کێشە
            wiki_url = f"https://wikipedia.org{query.replace(' ', '_')}"
            try:
                res = requests.get(wiki_url).json()
                if "extract" in res:
                    ans = res["extract"]
                    st.success(ans)
                    # Text to Speech
                    audio_url = f"https://google.com{ans[:200].replace(' ', '%20')}&tl=en&client=tw-ob"
                    st.audio(audio_url)
                else:
                    st.warning("🤔 I couldn't find an exact answer. Try asking about a planet, animal, or city!")
            except:
                st.error("📡 System Error: Please try again in a moment.")

    with tab2:
        prompt = st.text_input("Describe your art (English):", key="p_art")
        if st.button("Create Image"):
            if prompt:
                st.info("🎨 San-AI is painting...")
                img_url = f"https://pollinations.ai{prompt.replace(' ', '%20')}?width=800&height=800&nologo=true&seed=77"
                st.image(img_url, caption=f"Result for {OFFICIAL_OWNER}")
            else:
                st.warning("Please type something!")
