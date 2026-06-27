import streamlit as st
import pandas as pd

# 1. ऐप की सेटिंग (ब्लॉग की तरह वाइड या सेंटर्ड)
st.set_page_config(page_title="Navyuvak Banjara Sewa Samiti", layout="wide")

# 2. ब्लॉग थीम CSS (डार्क ब्लू हेडर, फॉन्ट, और कार्ड डिज़ाइन)
st.markdown("""
    <style>
    /* पूरे पेज का बैकग्राउंड */
    .stApp {
        background-color: #f3f4f6;
        font-family: Arial, sans-serif;
    }
    
    /* ब्लॉग स्टाइल हेडर */
    .blog-header {
        background-color: #0f172a;
        color: white;
        padding: 20px;
        text-align: center;
        border-radius: 0px 0px 10px 10px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* संकल्प संदेश */
    .sankalp-banner {
        background-color: #10b981;
        color: white;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    
    /* मूविंग (Marquee) मीटिंग नोटिस */
    .moving-notice {
        background-color: #fee2e2;
        color: #dc2626;
        padding: 10px;
        font-weight: bold;
        border-radius: 5px;
        margin-bottom: 20px;
        border-left: 5px solid #dc2626;
    }
    
    /* ब्लॉग स्टाइल पोस्ट कार्ड */
    .post-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-top: 4px solid #2563eb;
    }
    
    /* कस्टम बटन */
    .stButton>button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 8px 20px !important;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ब्लॉग हेडर सेक्शन ---
st.markdown("""
    <div class="blog-header">
        <h1 style="color: white; margin: 0;">नवयुवक बंजारा सेवा समिति</h1>
        <p style="color: #38bdf8; margin: 5px 0 0 0;">मुख्य पृष्ठ | हमारे संकल्प | फंड का विवरण | मीटिंग सूचना</p>
    </div>
    """, unsafe_allow_html=True)

# --- संकल्प बैनर ---
st.markdown('<div class="sankalp-banner">✨ संकल्प: दुःख में भोजन | बेटी को आशीर्वाद</div>', unsafe_allow_html=True)

# --- मूविंग (Marquee) मीटिंग शेड्यूल ---
# यह आपके ब्लॉग की तरह लगातार चलती हुई सूचना दिखाएगा
st.markdown("""
    <div class="moving-notice">
        <marquee behavior="scroll" direction="left" scrollamount="5">
            📢 आगामी मासिक बैठक की आवश्यक सूचना: स्थान - श्री राजकुमार मुणावत निवास (जयपुर), दिनांक - 02-07-2026, समय - शाम 4:00 बजे। कृपया सभी सदस्य समय पर पधारें!
        </marquee>
    </div>
    """, unsafe_allow_html=True)

# दो कॉलम लेआउट (मुख्य सामग्री और फॉर्म के लिए)
col_main, col_side = st.columns([2, 1])

with col_main:
    # --- हमारे संकलन सेक्शन ---
    st.markdown('<div class="post-card"><h3>📚 समिति के मुख्य ऐतिहासिक कदम</h3><hr>', unsafe_allow_html=True)
    
    st.info("📌 **कदम 1:** दुःख की घड़ी में संबल (भोजन व्यवस्था) - जयपुर के किसी भी बंजारा समाज बंधु के घर मृत्यु होने पर समिति द्वारा भोजन की व्यवस्था की जाती है।")
    st.warning("📌 **कदम 2:** बेटी को आशीर्वाद (कन्यादान राशि) - समाज की बेटियों की शादी के अवसर पर समिति की तरफ से सहयोग राशि प्रदान की जाती है।")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- फंड का विवरण (मंथ वाइज लिस्ट और टेबल) ---
    st.markdown('<div class="post-card"><h3>💰 समिति फंड का मासिक लाइव हिसाब (पूर्ण पारदर्शिता)</h3><hr>', unsafe_allow_html=True)
    
    # फंड का क्विक समरी मैट्रिक्स
    m1, m2, m3 = st.columns(3)
    m1.metric("पिछली जमा राशि", "₹ 0.00")
    m2.metric("चालू माह की कुल जमा", "₹ 8,200.00")
    m3.metric("कुल सुरक्षित फंड राशि", "₹ 7,840.00", "- ₹ 360.00 (खर्च)")
    
    st.write("📊 **पदम मासिक बैठक - आय एवं व्यय का पूर्ण विवरण:**")
    
    # डमी फंड डेटा टेबल
    fund_data = pd.DataFrame({
        "क्र.सं.": [1, 2, 3, 4],
        "दिनांक/माह": ["04/06/2026", "04/06/2026", "04/06/2026", "04/06/2026"],
        "नाम": ["नरेंद्र जी मूणावत", "कैलाश जी मुणावत", "सुरेश जी भुख्या", "राजेंद्र जी विसलावत"],
        "गोत्र": ["मूणावत", "मूणावत", "भुख्या", "विसलावत"],
        "प्राप्त राशि (In)": [500, 500, 500, 500],
        "विवरण": ["मासिक सदस्यता सहयोग", "मासिक सदस्यता सहयोग", "मासिक सदस्यता सहयोग", "मासिक सदस्यता सहयोग"]
    })
    st.dataframe(fund_data, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    # --- आगामी बैठक का विवरण ---
    st.markdown('<div class="post-card"><h3>🗓️ आगामी बैठक</h3><hr>', unsafe_allow_html=True)
    st.write("**स्थान:** श्री राजकुमार मुणावत निवास")
    st.write("**समय:** शाम 4:00 बजे")
    if st.button("🗺️ लोकेशन मैप खोलें"):
        st.caption("गूगल मैप रूट सक्रिय...")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- सदस्यता फॉर्म ---
    st.markdown('<div class="post-card"><h3>📝 डिजिटल सदस्यता फॉर्म</h3><hr>', unsafe_allow_html=True)
    with st.form("member_form_blog"):
        name = st.text_input("पूरा नाम")
        gotra = st.selectbox("गोत्र", ["मूणावत", "गोरामा", "विसलावत", "भुख्या", "अन्य"])
        phone = st.text_input("मोबाइल नंबर")
        submitted = st.form_submit_button("सदस्यता सबमिट करें")
        if submitted:
            st.success(f"पंजीकरण सफल: {name}")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- मीटिंग मैसेज/व्हाट्सएप एक्शन पैनल ---
    st.markdown('<div class="post-card"><h3>💬 त्वरित संपर्क / मीटिंग संदेश</h3><hr>', unsafe_allow_html=True)
    st.write("यहाँ क्लिक करके सीधे बैठक की सूचना साझा करें या नए लोगों को जोड़ें:")
    msg = st.text_input("संदेश टाइप करें", placeholder="मीटिंग में आने का समय...")
    if st.button("🟢 WhatsApp पर ग्रुप में भेजें"):
        st.success("संदेश ग्रुप ब्रॉडकास्ट के लिए तैयार है!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- ब्लॉग स्टाइल फुटर ---
st.markdown("""
    <div style="background-color: #0f172a; color: white; text-align: center; padding: 15px; margin-top: 30px; border-radius: 5px 5px 0 0;">
        © 2026 Navyuvak Banjara Sewa Samiti | All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
