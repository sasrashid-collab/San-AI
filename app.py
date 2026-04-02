import streamlit as st
import requests

# --- Settings ---
OFFICIAL_OWNER = "San Shadman"
SECRET_CODE = "san11"

st.set_page_config(page_title="San-AI V1", page_icon="🤖")

# --- Authentication ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔒 San-AI Login")
    pwd = st.text_input("Enter Code:", type="password")
    if st.button("Unlock"):
        if pwd.lower().strip() == SECRET_CODE:
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Wrong Code!")
else:
    st.title(f"🚀 Welcome, Boss San")
    
    # Simple Search (The Brain)
    query = st.text_input("Ask San-AI (English):", placeholder="e.g. Earth, Lion, Erbil")
    
    if query:
        st.info("Searching...")
        # بەکارهێنانی سادەترین لینکی ویکیپیدیا
        url = f"https://wikipedia.org{query.replace(' ', '_')}"
        try:
            res = requests.get(url).json()
            if "extract" in res:
                answer = res["extract"]
                st.success(answer)
                # دەنگ بۆ خوێندنەوەی وەڵامەکە
                audio_url = f"https://google.com{answer[:200].replace(' ', '%20')}&tl=en&client=tw-ob"
                st.audio(audio_url)
            else:
                st.warning("I couldn't find that. Try a simpler word!")
        except:
            st.error("Internet connection problem!")

    st.divider()
    # Simple Image (The Art)
    img_prompt = st.text_input("Describe a photo to draw:")
    if st.button("Draw It"):
        if img_prompt:
            img_url = f"https://pollinations.ai{img_prompt.replace(' ', '%20')}?width=500&height=500&nologo=true"
            st.image(img_url)
