import streamlit as st
import random

st.set_page_config(page_title="Self Test by Robotvus", layout="centered")
st.title("🤖 โรบอทวุส – แบบประเมินอารมณ์")

q1 = st.radio("1. วันนี้คุณรู้สึกยังไง?", ["สงบ", "เฉยๆ", "หวิวๆ", "ใจสั่น 😳"])
q2 = st.radio("2. เวลาเจอสาวใน TikTok", ["เลื่อนผ่าน", "แอบดูนิดๆ", "ดูจนลืมเวลา"])
q3 = st.radio("3. คุณคิดว่าคุณ...", ["ควบคุมตัวเองได้", "ลังเล", "หลุดไปแล้ว 🫣"])

if st.button("ประเมินเลย"):
    score = sum([
        ["สงบ", "เฉยๆ", "หวิวๆ", "ใจสั่น 😳"].index(q1),
        ["เลื่อนผ่าน", "แอบดูนิดๆ", "ดูจนลืมเวลา"].index(q2),
        ["ควบคุมตัวเองได้", "ลังเล", "หลุดไปแล้ว 🫣"].index(q3)
    ])

    st.subheader("🤖 โรบอทวุสประเมินว่า...")

    if score <= 2:
        st.success("คุณคือ พระอาทิตย์แห่งสติ ☀️")
        st.image("https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg", caption="เธอชื่นชมคุณจากแดนสงบ")
    elif score <= 4:
        st.warning("คุณคือ นักเหม่อผู้ไม่แน่ใจ 🌀")
        st.image("https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg", caption="เธอกำลังถามว่า... คิดถึงใครอยู่เหรอ?")
    else:
        st.error("คุณคือ เจ้าชายไฟราคะ 🔥")
        st.image("https://images.pexels.com/photos/2100063/pexels-photo-2100063.jpeg", caption="โรบอทวุส: ไอ๊จ้ะะะะ!! ใจเย็นลูกพี่!")

    st.button("ตั้งสติใหม่ 🙏")