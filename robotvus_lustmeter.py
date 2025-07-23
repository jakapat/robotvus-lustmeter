import streamlit as st
import random

st.set_page_config(page_title="Self Assessment by Robotvus", layout="centered")
st.title("🤖 โรบอทวุส – แบบประเมินอารมณ์")

st.markdown("### 🧠 กรุณาประเมินตัวเองในแต่ละด้าน")

# Slider แบบหล่อ ๆ
mind = st.slider("🧘‍♂️ สภาพจิตใจตอนนี้", 0, 10, 5)
focus = st.slider("🎯 สมาธิของคุณ", 0, 10, 5)
tempt = st.slider("🔥 ความหวั่นไหวต่อสิ่งเย้ายวน", 0, 10, 5)

if st.button("✅ ประเมินเลย"):
    score = (mind + focus + (10 - tempt)) / 3
    st.subheader("📊 ผลการประเมินของคุณ")

    st.progress(score / 10)

    if score >= 8:
        st.success("คุณเพิ่งดอจ๊อง ✨")
        st.image("https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg", caption="เธอมองคุณด้วยความชื่นชม")
    elif score >= 5:
        st.warning("คุณเริ่มเงี้ยน 😅")
        st.image("https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg", caption="เธอมองคุณอย่างเป็นห่วง")
    else:
        st.error("อ๊าาาาส ชักต่อหวา... 🫠")
        st.image("https://images.pexels.com/photos/2100063/pexels-photo-2100063.jpeg", caption="ไอ๊จ้ะะะะ!! โรบอทวุสขอเตือน!")

    st.button("🧘‍♀️ เริ่มใหม่")