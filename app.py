import streamlit as st
import requests

# --- Configuration & Security ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"

# Page Setup for Mobile App Feel
st.set_page_config(page_title="San-AI Ultimate", page_icon="🤖", layout="centered")

# --- Professional Cyber Design (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020111, #050a14);
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .stButton>button {
        background-color: #00d4ff;
        color: black;
        border-radius: 15px;
        font-weight: bold;
        border: none;
    }
    .stTextInput input {
        background-color: #1a1a1a;
        color: #00ff41;
        border: 1px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Authentication Logic ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.title("🛡️ San-AI System Lock")
    st.write(f"Authorized User: **{OFFICIAL_OWNER}**")
    
    password_input = st.text_input("Enter Secret Code / کۆدی نهێنی:", type="password")
    
    if st.button("Unlock System"):
        if password_input.lower().strip() == SECRET_CODE:
            st.session_state['authenticated'] = True
            st.balloons()
            st.rerun()
        else:
            st.error("❌ Access Denied. Try again.")

# --- Main App Interface (After Login) ---
else:
    st.title(f"🚀 San-AI Ultimate v3.0")
    st.markdown(f"**Welcome, Boss {OFFICIAL_OWNER}**")
    
    # Tabs for different AI Powers
    tab1, tab2 = st.tabs(["🧠 Smart Brain", "🎨 Art Studio"])

    # --- TAB 1: Internet Search & Learning ---
    with tab1:
        st.subheader("Search & Learn Anything")
        query = st.text_input("Ask a question (English or Kurdish):", placeholder="e.g. How do rockets work?")
        
        if query:
            st.write("🔍 San-AI is exploring the web...")
            # Free Search API (DuckDuckGo)
            search_url = f"https://duckduckgo.com{query}&format=json"
            try:
                response = requests.get(search_url).json()
                answer = response.get("AbstractText", "I found some info, but I need to study it more! Try a more specific question.")
                if not answer:
                    answer = "I'm still learning about this. Let's ask again later!"
                st.success(f"Result: {answer}")
            except:
                st.error("📡 Connection lost. Please check your internet.")

    # --- TAB 2: AI Image Generation ---
    with tab2:
        st.subheader("AI Image Generator")
        st.write("Turn your English words into Art!")
        img_prompt = st.text_input("Describe your image:", placeholder="e.g. A futuristic city in Erbil with flying cars")
        
        if st.button("Generate Magic Image"):
            if img_prompt:
                st.info("🎨 San-AI is painting... please wait.")
                # High-quality Free AI Image API
                image_url = f"https://pollinations.ai{img_prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
                st.image(image_url, caption=f"Created by San-AI for {OFFICIAL_OWNER}", use_column_width=True)
            else:
                st.warning("Please describe what you want to see!")

    # Sidebar for logout and info
    st.sidebar.title("⚙️ System Control")
    st.sidebar.write(f"User: {OFFICIAL_OWNER}")
    st.sidebar.write("Evolution: Phase 11.0")
    st.sidebar.write("Year: 2026")
    
    if st.sidebar.button("Log Out"):
        st.session_state['authenticated'] = False
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.write(f"© 2026 San-AI Ecosystem")
