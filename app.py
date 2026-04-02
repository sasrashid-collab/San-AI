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
    st.title(f"🚀 Welcome, Boss San")
    tab1, tab2 = st.tabs(["🧠 Brain", "🎨 Art Studio"])

    with tab1:
        query = st.text_input("Ask anything:", key="q_brain")
        if query:
            st.info("Searching the world for you...")
            # Using DuckDuckGo for real facts
            res = requests.get(f"https://duckduckgo.com{query}&format=json").json()
            ans = res.get("AbstractText", "I found some info but I need to study more. Try asking about a planet or a famous person!")
            st.success(ans)
            st.audio(f"https://google.com{ans[:200].replace(' ', '%20')}&tl=en&client=tw-ob")

    with tab2:
        prompt = st.text_input("Describe your art (English):", key="p_art")
        if st.button("Create Image"):
            if prompt:
                st.info("San-AI is looking for the best image...")
                # We use a backup stable server for the image
                img_url = f"https://pollinations.ai{prompt.replace(' ', '%20')}?width=800&height=800&seed=99"
                st.image(img_url, caption=f"Result for {OFFICIAL_OWNER}")
                st.write("If you only see a cloud, try to describe something else like 'a futuristic car'!")
