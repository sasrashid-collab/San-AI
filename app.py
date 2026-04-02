import streamlit as st
import requests

# --- 1. User Database (دەتوانی هاوڕێکانی لێرە زیاد بکەیت) ---
USERS = {
    "san": "san11",
    "shadman": "1234",
    "guest": "0000"
}

st.set_page_config(page_title="San-AI Ecosystem", page_icon="🤖", layout="centered")

# --- 2. Hide Everything (Manage App & Streamlit Menu) ---
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

if not st.session_state['user']:
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
    # --- Main Interface ---
    current_user = st.session_state['user'].capitalize()
    st.title(f"🚀 Welcome, {current_user}")
    
    tab1, tab2 = st.tabs(["🧠 Smart Brain", "🎨 Art Studio"])

    with tab1:
        st.subheader("Search & Learn")
        query = st.text_input("Ask a question:", key="brain_input")
        if query:
            st.info(f"Searching for {current_user}...")
            # (Search Logic remains the same)
            res = requests.get(f"https://duckduckgo.com{query}&format=json").json()
            st.success(res.get("AbstractText", "I'm searching... try again!"))

    with tab2:
        st.subheader("AI Art Studio")
        img_prompt = st.text_input("Describe your art:", key="art_input")
        if st.button("Generate Image"):
            img_url = f"https://pollinations.ai{img_prompt.replace(' ', '%20')}?nologo=true"
            st.image(img_url, caption=f"Created for {current_user}")

    # Sidebar Logout
    if st.sidebar.button("Log Out"):
        st.session_state['user'] = None
        st.rerun()

st.sidebar.write(f"Active User: {current_user}")
