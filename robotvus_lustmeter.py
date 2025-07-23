import streamlit as st
import requests
import random
import os

# ✅ ใส่ API KEY ของคุณตรงนี้
PEXELS_API_KEY = "5Ez9UD4BxqpRHxvsnFOzhrXZp6Lf2UpFnrXIcYg9vQivxOKwABlIHnQ7"  # 🔁 แก้ตรงนี้
PEXELS_SEARCH_TERM = "sexy woman"
NUM_IMAGES = 15

st.set_page_config(page_title="Robotvus Lust Meter", layout="centered")
st.title("🤖 โรบอทวุส – เครื่องวัดระดับความเงี่ยน")

st.markdown("### 🎛️ ปรับระดับเพื่อประเมินตัวคุณเอง")

# 🎚️ Slider ให้ผู้ใช้ประเมิน
lust_level = st.slider("วันนี้คุณใจสั่นระดับไหน?", 1, 10, 5)

# 🔁 ดึงภาพสุ่มจาก Pexels API
def get_random_image():
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": PEXELS_SEARCH_TERM, "per_page": NUM_IMAGES}
    try:
        response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
        data = response.json()
        if "photos" in data and data["photos"]:
            return random.choice(data["photos"])["src"]["large"]
    except:
        return "https://placekitten.com/600/400"
    return "https://placekitten.com/600/400"

# 🧪 แสดงผลตามระดับ
if st.button("ประเมินเลย!"):
    st.subheader(f"ระดับความเงี่ยนของคุณคือ: {lust_level}/10")

    image_url = get_random_image()
    st.image(image_url, width=500)

    if lust_level <= 3:
        st.success("🟢 คุณยังนิ่ง! โรบอทวุสขอคารวะ")
    elif lust_level <= 6:
        st.warning("🟡 เริ่มใจเต้นเบาๆ... อย่าเปิด IG เลยนะ")
    elif lust_level <= 8:
        st.error("🔴 สั่นไหวแรงมาก! เตือนด้วยใจ")
    else:
        st.error("🚨 อันตราย! โรบอทวุสสั่งห้ามเปิด OnlyFans 🔒")
        st.markdown("## 🗣️ **ไอ๊จ้ะะะะะะ!!** 😤")

    st.button("ตั้งสติใหม่ 🙏")
