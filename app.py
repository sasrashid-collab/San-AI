import streamlit as st

# --- Core Settings ---
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
            st.error("Access Denied.")
else:
    st.title(f"🚀 Welcome, Boss San")
    tab1, tab2 = st.tabs(["🧠 Smart Brain", "🎨 Art Studio"])

    with tab1:
        st.subheader("San-AI Knowledge")
        query = st.text_input("Ask San anything:", key="q_internal")
        if query:
            q = query.lower()
            # وەڵامی ناوخۆیی بۆ ئەوەی هەرگیز تووشی Connection Error نەبێت
            if "hello" in q or "سڵاو" in q:
                ans = "Hello Boss San! I am your AI, ready to help you build the future."
            elif "who are you" in q or "تۆ کێیت" in q:
                ans = f"I am San-AI, the personal assistant of {OFFICIAL_OWNER}."
            elif "ai" in q:
                ans = "AI stands for Artificial Intelligence. It helps humans solve big problems!"
            elif "space" in q:
                ans = "Space is vast and contains stars, planets, and galaxies. It's infinite!"
            else:
                ans = "That's a great question! I am saving this to research and tell you more tomorrow."
            
            st.success(ans)
            # بەشی دەنگەکەمان لاداوە چونکە ئەویش ئینتەرنێتی دەوێت و کێشە دروست دەکات
            st.info("Note: Internal Mode is active for maximum speed.")

    with tab2:
        st.subheader("Art Gallery")
        st.write("To see images, ensure you have a strong internet connection.")
        prompt = st.text_input("Describe your art (English):", key="p_art")
        if st.button("Generate Image"):
            if prompt:
                # بەکارهێنانی لینکی سادە کە کەمترین کێشە دروست دەکات
                img_url = f"https://pollinations.ai{prompt.replace(' ', '%20')}?width=500&height=500&nologo=true"
                st.image(img_url, caption="San-AI Creation")
            else:
                st.warning("Please type something!")

    if st.sidebar.button("Log Out"):
        st.session_state['auth'] = False
        st.rerun()
