import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TXT Concert",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* BACKGROUND */
.stApp{
    background: linear-gradient(
        135deg,
        #dcecf7,
        #f8f4ef,
        #ffe4e1
    );
}

/* TITLE */
h1,h2,h3,h4{
    color:#111111 !important;
}

/* LABEL */
label{
    color:#111111 !important;
    font-weight:bold !important;
}

/* INPUT */
input{
    color:#111111 !important;
    background:white !important;
}

/* SELECTBOX */
.stSelectbox div[data-baseweb="select"]{
    background:white !important;
    color:#111111 !important;
    border-radius:10px;
}

/* BUTTON */
.stButton>button{
    background-color:#8b0000;
    color:white !important;
    border:none;
    border-radius:12px;
    padding:10px 20px;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#b22222;
}

/* BOX SEAT */
.seat-box{
    text-align:center;
    padding:20px;
    border-radius:15px;
    font-weight:bold;
    margin-bottom:10px;
    font-size:20px;
}

/* AVAILABLE */
.available{
    background:#7fffd4;
    color:black;
}

/* BOOKED */
.booked{
    background:#ff4d4d;
    color:white;
}

/* STAGE */
.stage{
    background:black;
    color:white;
    text-align:center;
    padding:30px;
    border-radius:20px;
    font-size:40px;
    font-weight:bold;
    margin-bottom:50px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATA CSV
# =========================

df = pd.read_csv("data.csv")

# =========================
# TITLE
# =========================

st.title("🎤 TXT WORLD TOUR")
st.header("ACT : LOVESICK")

st.write("## 🎵 SONG LIST")
st.write("""
- 0X1=LOVESONG  
- Anti Romantic  
- Blue Hour  
- Sugar Rush Ride  
- Deja Vu  
- LO$ER=LO♡ER  
""")

st.write("📞 Contact Admin : 0812-XXXX-XXXX")

st.write("---")

# =========================
# STAGE
# =========================

st.markdown("""
<div class="stage">
STAGE
</div>
""", unsafe_allow_html=True)

# =========================
# SEAT DATA
# =========================

seat_data = {
    "VIP":[f"A{i}" for i in range(1,11)],
    "BLUE":[f"B{i}" for i in range(1,11)],
    "PINK":[f"C{i}" for i in range(1,11)]
}

# =========================
# BOOKED
# =========================

booked = df["Seat"].tolist()

# =========================
# VIP
# =========================

st.subheader("VIP")

cols = st.columns(5)

for i, seat in enumerate(seat_data["VIP"]):

    if seat in booked:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box booked">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box available">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# BLUE
# =========================

st.subheader("BLUE")

cols = st.columns(5)

for i, seat in enumerate(seat_data["BLUE"]):

    if seat in booked:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box booked">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box available">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# PINK
# =========================

st.subheader("PINK")

cols = st.columns(5)

for i, seat in enumerate(seat_data["PINK"]):

    if seat in booked:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box booked">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        cols[i % 5].markdown(
            f"""
            <div class="seat-box available">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# PRICE LIST
# =========================

st.write("---")

st.header("💰 PRICE LIST")

col1, col2, col3 = st.columns(3)

col1.success("""
VIP

Rp 3.000.000
""")

col2.info("""
BLUE

Rp 2.500.000
""")

col3.error("""
PINK

Rp 1.500.000
""")

# =========================
# INFO
# =========================

st.write("---")

st.write("🟩 Available Seat")
st.write("🟥 Booked Seat")
