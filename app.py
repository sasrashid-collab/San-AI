import streamlit as st

# --- San-AI Security & Identity ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "San11"

st.set_page_config(page_title="San-AI", page_icon="🚀")

# Fixing the error: changed 'stdio' to 'html'
st.markdown("""
    <style>
    .stApp { background-color: #050a14; color: #00ff41; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.title("🛡️ San-AI System Lock")
    password = st.text_input("Enter Secret Code:", type="password")
    if st.button("Unlock System"):
        if password == SECRET_CODE:
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("Access Denied.")
else:
    st.title(f"🚀 San-AI v1.1")
    st.write(f"Authenticated: **{OFFICIAL_OWNER}**")
    
    user_input = st.text_input("Command San-AI:")
    if user_input:
        st.write("System processing... Building the future with San!")

    if st.sidebar.button("Log Out"):
        st.session_state['authenticated'] = False
        st.rerun()
