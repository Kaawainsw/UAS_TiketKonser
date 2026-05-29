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

/* VIP */
.available{
    background:#7fffd4;
    color:black;
}

/* BLUE */
.blue{
    background:#87cefa;
    color:black;
}

/* PINK */
.pink{
    background:#ffb6c1;
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
# BOOKED SEAT
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
            <div class="seat-box blue">
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
            <div class="seat-box pink">
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

col1.markdown("""
<div style="
background:#7fffd4;
padding:20px;
border-radius:15px;
text-align:center;
font-weight:bold;
font-size:20px;
color:black;
">
VIP<br>
Rp 3.000.000
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div style="
background:#87cefa;
padding:20px;
border-radius:15px;
text-align:center;
font-weight:bold;
font-size:20px;
color:black;
">
BLUE<br>
Rp 2.500.000
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div style="
background:#ffb6c1;
padding:20px;
border-radius:15px;
text-align:center;
font-weight:bold;
font-size:20px;
color:black;
">
PINK<br>
Rp 1.500.000
</div>
""", unsafe_allow_html=True)

# =========================
# INFO
# =========================

st.write("---")

st.write("🟩 VIP Available")
st.write("🟦 BLUE Available")
st.write("🩷 PINK Available")
st.write("🟥 Booked Seat")
