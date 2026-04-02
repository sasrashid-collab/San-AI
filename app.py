import streamlit as st

# --- Security Configuration ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "San11"  # ئەمە پاسۆردە نهێنییەکەیە (دەتوانیت بیگۆڕیت)

st.set_page_config(page_title="San-AI Security", page_icon="🔐")

# Custom CSS for Cyber-Security look
st.markdown("""
    <style>
    .stApp { background-color: #050a14; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .stTextInput input { background-color: #1a1a1a; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_stdio=True)

# Session State to keep the app unlocked once the password is correct
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.title("🛡️ San-AI System Lock")
    st.subheader("Identification Required")
    
    password = st.text_input("Enter Secret Code / کۆدی نهێنی بنووسە:", type="password")
    
    if st.button("Unlock System"):
        if password == SECRET_CODE:
            st.session_state['authenticated'] = True
            st.success(f"Access Granted. Welcome, Boss {OFFICIAL_OWNER}!")
            st.rerun()
        else:
            st.error("Access Denied. Wrong Code.")
else:
    # --- Main App Interface (After Unlock) ---
    st.title(f"🚀 San-AI v1.1 Online")
    st.markdown(f"**Verified User:** `{OFFICIAL_OWNER}`")
    
    st.divider()
    
    user_input = st.text_input("Command San-AI / فەرمانی نوێ بدە:")
    
    if user_input:
        cmd = user_input.lower()
        if "who are you" in cmd or "تۆ کێیت" in cmd:
            st.write(f"I am **San-AI**, the private assistant of **{OFFICIAL_OWNER}**.")
        elif "hello" in cmd or "سڵاو" in cmd:
            st.info(f"System active and ready for your next project, San!")
        else:
            st.write("Processing... I am learning from your commands!")

    if st.sidebar.button("Log Out / قوفڵکردنەوە"):
        st.session_state['authenticated'] = False
        st.rerun()
