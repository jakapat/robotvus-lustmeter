import streamlit as st
import requests
import random
import os

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "5Ez9UD4BxqpRHxvsnFOzhrXZp6Lf2UpFnrXIcYg9vQivxOKwABlIHnQ7")  # ใช้ ENV หรือเว้นว่างไว้
PEXELS_SEARCH_TERM = "beautiful woman"
NUM_IMAGES = 10

st.set_page_config(page_title="🤖 Lust Meter", layout="centered")
st.audio("https://www.bensound.com/bensound-music/bensound-sunny.mp3", loop=True)

st.markdown("""
    <h1 style='text-align: center; color: #fca311;'>🤖 โรบอทวุสวัดระดับความเงี่ยน</h1>
    <p style='text-align: center; color: #6c757d;'>ระบบประเมินอารมณ์ขำๆ พร้อมช่วยให้คุณตั้งสติกลับมา 🤖</p>
""", unsafe_allow_html=True)

def get_random_image():
    if not PEXELS_API_KEY:
        return "https://placekitten.com/400/300"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": PEXELS_SEARCH_TERM, "per_page": NUM_IMAGES}
    try:
        response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
        data = response.json()
        return random.choice(data["photos"])["src"]["medium"]
    except:
        return "https://placekitten.com/400/300"

if st.button("วัดระดับความเงี่ยน 🧪"):
    level = random.randint(1, 10)
    st.subheader(f"ระดับความเงี่ยนของคุณคือ: {level}/10")
    img_url = get_random_image()
    st.image(img_url, width=400)

    if level <= 3:
        st.success("🟢 สงบ สติอยู่ครบ")
    elif level <= 6:
        st.warning("🟡 เริ่มหวั่นไหว... ไปล้างหน้า!")
    elif level <= 8:
        st.error("🔴 โรบอทวุสแนะนำให้เบรก")
    else:
        st.error("🚨 ระบบเตือน: ระดับเกินพิกัด! ไอ๊จ้ะะะะ!!")
    st.button("ตั้งสติใหม่ 🙏")