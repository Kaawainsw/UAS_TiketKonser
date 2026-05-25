import streamlit as st

st.set_page_config(
    page_title="TXT Concert Ticket",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #000000,
        #5c0000,
        #f5f0e6
    );
    color:white;
}

/* TITLE */
.title{
    text-align:center;
    font-size:65px;
    font-weight:bold;
    margin-top:30px;
    color:#f5f0e6;
}

.subtitle{
    text-align:center;
    font-size:28px;
    color:#ffb3b3;
    margin-bottom:40px;
}

/* BOX */
.box{
    background-color:rgba(255,255,255,0.1);
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
}

/* SONG */
.song{
    padding:10px;
    border-bottom:1px solid rgba(255,255,255,0.2);
    font-size:18px;
}

/* CONTACT */
.contact{
    font-size:18px;
    line-height:2;
}

/* BUTTON */
.stButton>button{
    width:100%;
    background-color:#8b0000;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown("""
<div class="title">
TXT WORLD TOUR
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
ACT : LOVESICK
</div>
""", unsafe_allow_html=True)

# =========================
# DESKRIPSI
# =========================

st.markdown("""
<div class="box">

### 🎤 Tentang Konser

Tomorrow X Together World Tour
ACT : LOVESICK merupakan konser
global TXT dengan konsep emotional,
dark, dan youthful.

Konser ini menampilkan berbagai
lagu populer TXT dengan visual
dan performance spektakuler.

</div>
""", unsafe_allow_html=True)

# =========================
# SETLIST
# =========================

st.markdown("""
<div class="box">

### 🎶 SETLIST

<div class="song">0X1=LOVESONG</div>
<div class="song">LO$ER=LO♡ER</div>
<div class="song">Blue Hour</div>
<div class="song">Sugar Rush Ride</div>
<div class="song">Deja Vu</div>
<div class="song">Anti-Romantic</div>
<div class="song">Opening Sequence</div>
<div class="song">Farewell, Neverland</div>
<div class="song">Chasing That Feeling</div>
<div class="song">Magic</div>

</div>
""", unsafe_allow_html=True)

# =========================
# INFORMASI
# =========================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="box">

    ### 📍 INFORMASI KONSER

    📅 Tanggal :
    25 Agustus 2026

    🕖 Waktu :
    19.00 WIB

    📌 Lokasi :
    ICE BSD Hall 5

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="box contact">

    ### ☎ CONTACT ADMIN

    📧 Email :
    txtticket@gmail.com

    📱 WhatsApp :
    0812-3456-7890

    📷 Instagram :
    @txtticket.id

    </div>
    """, unsafe_allow_html=True)

# =========================
# BOOKING INFO
# =========================

st.write("---")

st.info(
    "Gunakan menu di sidebar untuk melihat seat konser dan melakukan booking tiket 🎟"
)

# =========================
# FOOTER
# =========================

st.write("---")

st.caption(
    "TXT Concert Ticket System © 2026"
)
