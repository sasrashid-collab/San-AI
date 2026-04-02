import streamlit as st

# --- Core Settings ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"

st.set_page_config(page_title="San-AI V1", page_icon="🤖")

# --- UI Styling ---
st.markdown("""<style> .stApp { background: #050a14; color: #00ffcc; } </style>""", unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔒 San-AI System")
    pwd = st.text_input("Security Code:", type="password")
    if st.button("Unlock"):
        if pwd.lower().strip() == SECRET_CODE:
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Wrong Code!")
else:
    st.title(f"🚀 Welcome, Boss San Shadman")
    st.write("System Status: **Online & Secure** ✅")

    # The Internal Brain (No Internet needed)
    query = st.text_input("Ask San-AI (Try: Space, Robots, Erbil, or Hello):")
    
    if query:
        q = query.lower().strip()
        
        # وەڵامە ئامادەکراوەکان بۆ ئەوەی هەرگیز Error نەدات
        responses = {
            "hello": "Hello Boss San! I am your AI friend. How are you today?",
            "erbil": "Erbil is a beautiful city in Kurdistan. It has a very old Citadel (Qalat).",
            "space": "Space is amazing! It has millions of stars and planets like Mars and Jupiter.",
            "robots": "Robots are machines built to help humans. Some are very smart like me!",
            "ai": "AI means Artificial Intelligence. It's like a brain for computers.",
            "san": "San Shadman is the genius owner and boss of this AI system!"
        }
        
        if q in responses:
            st.success(f"🤖 San-AI: {responses[q]}")
        else:
            st.info("🤖 San-AI: That's a great question! I'm adding this to my memory to tell you more about it tomorrow.")

    st.divider()
    st.write("🎨 **Art Gallery**")
    st.write("Imagine a cool robot in your head! Art generation will be active soon.")
    
    if st.sidebar.button("Log Out"):
        st.session_state['auth'] = False
        st.rerun()

st.sidebar.write(f"Owner: {OFFICIAL_OWNER}")
