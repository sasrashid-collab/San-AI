import streamlit as st

# --- 1. Basic Settings ---
st.set_page_config(page_title="San-AI", page_icon="🤖")

# --- 2. Clean UI ---
st.markdown("""<style> .stApp { background: #050a14; color: #00ffcc; } </style>""", unsafe_allow_html=True)

# --- 3. Simple Login ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🛡️ San-AI Login")
    pwd = st.text_input("Enter 'san11' to start:", type="password")
    if st.button("Unlock"):
        if pwd == "san11":
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Wrong Code!")
else:
    # --- 4. Main App (Pure Logic, No Internet Required) ---
    st.title("🚀 Welcome, San Shadman!")
    st.write("System Status: **100% Operational** ✅")
    
    st.divider()
    
    query = st.text_input("Ask San-AI (Try: Hello, Space, Erbil):")
    
    if query:
        q = query.lower().strip()
        # وەڵامی ناوخۆیی جێگیر
        if "hello" in q or "سڵاو" in q:
            st.success("🤖 San-AI: Hello Boss San! I am your AI friend.")
        elif "erbil" in q or "هەولێر" in q:
            st.success("🤖 San-AI: Erbil is the heart of Kurdistan. It has a great Citadel!")
        elif "space" in q or "فەزا" in q:
            st.success("🤖 San-AI: Space is huge! It has stars and planets like Mars.")
        elif "san" in q:
            st.success("🤖 San-AI: San Shadman is a tech genius and the owner of this AI!")
        else:
            st.info("🤖 San-AI: I am learning about this. I will tell you more tomorrow!")

    st.sidebar.button("Log Out", on_click=lambda: st.session_state.update({"auth": False}))
