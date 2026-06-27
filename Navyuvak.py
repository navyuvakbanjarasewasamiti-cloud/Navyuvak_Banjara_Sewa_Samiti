import streamlit as st
import pandas as pd

# 1. ऐप की सेटिंग
st.set_page_config(page_title="Navyuvak Banjara Sewa Samiti", layout="centered")

# 2. कस्टम CSS (ऐप को सुंदर बनाने के लिए)
st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .stButton>button {width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white;}
    </style>
    """, unsafe_allow_html=True)

# 3. हेडलाइन और "हमारे कदम" स्लाइडर (डमी डेटा)
st.title("📍 Navyuvak Banjara Sewa Samiti")
st.success("✨ संकल्प: दुःख में भोजन | बेटी को आशीर्वाद")

# 4. गुरुवार बैठक का लाइव सेक्शन (Dynamic)
st.subheader("🗓️ आगामी गुरुवार बैठक (02-07-2026)")
col1, col2 = st.columns(2)
with col1:
    st.write("**स्थान:** श्री राजकुमार मुणावत निवास")
    st.write("**समय:** शाम 4:00 बजे")
with col2:
    if st.button("🗺️ लोकेशन (Map)"):
        st.write("गूगल मैप लिंक खोलें...")

st.divider()

# 5. सदस्य पंजीकरण (जो आप मांग रहे थे)
st.subheader("📝 समाज डिजिटल सदस्यता फॉर्म")
with st.form("member_form"):
    name = st.text_input("पूरा नाम")
    gotra = st.selectbox("गोत्र", ["मूणावत", "गोरामा", "विसलावत", "भुख्या", "अन्य"])
    phone = st.text_input("मोबाइल नंबर")
    submitted = st.form_submit_button("सदस्य बनें")
    
    if submitted:
        # यहाँ डेटा गूगल शीट या CSV में सेव होगा
        st.success(f"धन्यवाद {name}! जानकारी समिति को भेज दी गई है।")

# 6. पदाधिकारी व्हाट्सएप सूचना बटन
st.subheader("📢 पदाधिकारी सूचना पैनल")
msg = st.text_input("सूचना टाइप करें:")
if st.button("🟢 WhatsApp पर सभी को भेजें"):
    st.info(f"भेजा जा रहा है: {msg}")
  
