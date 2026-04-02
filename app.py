import streamlit as st
import requests

# --- 1. User Database (دەتوانی هاوڕێکانی لێرە زیاد بکەیت) ---
USERS = {
    "san": "san11",
    "shadman": "1234",
    "guest": "0000"
}

st.set_page_config(page_title="San-AI Ecosystem", page_icon="🤖", layout="centered")

# --- 2. Professional UI & Hide Streamlit Elements ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    .stApp { background: linear-gradient(135deg, #020111, #050a14); color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Authentication Logic ---
if 'user' not in st.session_state:
    st.session_state['user'] = None

# --- 4. Main App Flow ---
if st.session_state['user'] is None:
    st.title("🛡️ San-AI Network Login")
    user_id = st.text_input("Username (ناو):").lower().strip()
    user_pwd = st.text_input("Password (پاسۆرد):", type="password")
    
    if st.button("Connect to San-AI"):
        if user_id in USERS and USERS[user_id] == user_pwd:
            st.session_state['user'] = user_id
            st.rerun()
        else:
            st.error("Invalid User or Password.")
else:
    # Get the active user name properly
    active_user = st.session_state['user'].capitalize()
    
    st.title(f"🚀 Welcome, {active_user}")
    
    tab1, tab2 = st.tabs(["🧠 Smart Brain", "🎨 Art Studio"])

    with tab1:
        st.subheader("Search & Learn")
        query = st.text_input("Ask a question:", key="brain_input")
        if query:
            st.info(f"Searching for {active_user}...")
            try:
                res = requests.get(f"https://duckduckgo.com{query}&format=json").json()
                answer = res.get("AbstractText", "I'm searching... try again with a clearer topic!")
                st.success(answer if answer else "I'm still learning about this!")
            except:
                st.error("Connection error.")

    with tab2:
        st.subheader("AI Art Studio")
        img_prompt = st.text_input("Describe your art (English):", key="art_input")
        if st.button("Generate Image"):
            if img_prompt:
                img_url = f"https://pollinations.ai{img_prompt.replace(' ', '%20')}?nologo=true"
                st.image(img_url, caption=f"Created for {active_user}")
            else:
                st.warning("Please describe what to draw.")

    # Sidebar UI
    st.sidebar.title("⚙️ System Control")
    st.sidebar.write(f"Active User: **{active_user}**")
    st.sidebar.write("Evolution: Phase 11.0")
    
    if st.sidebar.button("Log Out"):
        st.session_state['user'] = None
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.write("© 2026 San-AI Ecosystem")
