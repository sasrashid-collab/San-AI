import streamlit as st
import requests

# --- Configuration ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"

st.set_page_config(page_title="San-AI Ultimate", page_icon="🤖", layout="centered")

# --- UI Styling ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050a14 0%, #000000 100%); color: #00e5ff; }
    #MainMenu, footer, header {visibility: hidden;}
    .stButton>button { background-color: #00d4ff; color: black; border-radius: 15px; width: 100%; font-weight: bold; }
    .stTextInput input { background-color: #0a192f; color: #00ffcc; border: 1px solid #00e5ff; }
    </style>
    """, unsafe_allow_html=True)

# --- Authentication Logic ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🛡️ San-AI Secure Login")
    pwd = st.text_input("Enter Secret Code:", type="password")
    if st.button("Unlock System"):
        if pwd.lower().strip() == SECRET_CODE:
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Access Denied.")
else:
    st.title(f"🚀 San-AI: Welcome Boss {OFFICIAL_OWNER}")
    
    # Defining Tabs Clearly to avoid NameError
    tab1, tab2 = st.tabs(["🧠 Smart Brain", "🎨 Art Studio"])

    with tab1:
        st.subheader("Search & Learn")
        query = st.text_input("Ask San-AI anything:", key="q1")
        if query:
            st.info("🔍 Searching...")
            res = requests.get(f"https://duckduckgo.com{query}&format=json").json()
            answer = res.get("AbstractText", "I'm still learning this topic!")
            st.success(answer)
            # Text to Speech
            audio_url = f"https://google.com{answer[:200].replace(' ', '%20')}&tl=en&client=tw-ob"
            st.audio(audio_url)

        with tab2:
        st.subheader("🎨 Imagine & Create")
        img_prompt = st.text_input("Describe your art (in English):", key="p1")
        if st.button("Generate Magic Image"):
            if img_prompt:
                st.info("🎨 San-AI is painting... please wait.")
                # بەکارهێنانی مۆدێلی Flux کە زۆر بەهێزە بۆ نووسین و ناو
                clean_prompt = img_prompt.replace(' ', '%20')
                # زیادکردنی &model=flux بۆ ئەوەی وێنەی نایاب دروست بکات
                image_url = f"https://pollinations.ai{clean_prompt}?width=1024&height=1024&model=flux&nologo=true&seed=123"
                st.image(image_url, caption=f"Created for {OFFICIAL_OWNER}", use_container_width=True)
            else:
                st.warning("Please type a description!")


    # Sidebar
    if st.sidebar.button("Log Out"):
        st.session_state['auth'] = False
        st.rerun()
    st.sidebar.write(f"Owner: {OFFICIAL_OWNER}")
    st.sidebar.write("© 2026 San-AI Ecosystem")
