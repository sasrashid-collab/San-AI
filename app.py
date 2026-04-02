import streamlit as st

# --- San-AI Master Configuration ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"  # دڵنیابە بە بچووکی دەینووسیت

# Page Settings
st.set_page_config(page_title="San-AI Official", page_icon="🚀", layout="centered")

# Professional Cyber Design (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #00d4ff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput input {
        background-color: #1a1a1a;
        color: #00ff41;
        border: 2px solid #00d4ff;
        border-radius: 10px;
    }
    .owner-text {
        text-align: center;
        font-size: 12px;
        color: #888;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State for Authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- 1. Login Screen ---
if not st.session_state['authenticated']:
    st.image("https://icons8.com", width=100)
    st.title("🛡️ San-AI System Lock")
    st.write(f"System Reserved for: **{OFFICIAL_OWNER}**")
    
    password_input = st.text_input("Enter your Secret Code / کۆدی نهێنی:", type="password")
    
    if st.button("Unlock San-AI"):
        if password_input.lower().strip() == SECRET_CODE:
            st.session_state['authenticated'] = True
            st.balloons() # ئاهەنگی سەرکەوتن
            st.rerun()
        else:
            st.error("❌ Access Denied. Please check your code.")

# --- 2. Main Interface (After Login) ---
else:
    st.title(f"🚀 {OFFICIAL_OWNER}'s San-AI")
    st.markdown(f"**Status:** `Online & Secure` ✅")
    
    st.divider()
    
    # Interaction Box
    user_input = st.text_input("What is your command today, Boss San?", placeholder="Type here...")
    
    if user_input:
        cmd = user_input.lower()
        if "hello" in cmd or "سڵاو" in cmd:
            st.info("San-AI: Welcome back, San! I'm ready to build something epic with you.")
        elif "who are you" in cmd or "تۆ کێیت" in cmd:
            st.success(f"I am San-AI, the most advanced assistant created for {OFFICIAL_OWNER}.")
        elif "creator" in cmd or "developer" in cmd:
            st.write("This AI system was developed by **Shadman** and is owned by **San Shadman**.")
        else:
            st.write("🤖 San-AI: That sounds like a great idea. Let's research how to do it!")

    # Sidebar for logout and info
    st.sidebar.title("System Menu")
    st.sidebar.write(f"Owner: {OFFICIAL_OWNER}")
    if st.sidebar.button("Log Out / قوفڵکردنەوە"):
        st.session_state['authenticated'] = False
        st.rerun()

st.markdown(f'<div class="owner-text">© 2024 San-AI Ecosystem | Private Property of {OFFICIAL_OWNER}</div>', unsafe_allow_html=True)
