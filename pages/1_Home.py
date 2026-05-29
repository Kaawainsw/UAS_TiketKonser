import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
.stApp{
    background: linear-gradient(
        135deg,
        #fff8ee,
        #ffe4e1,
        #f5f0e6
    );
}

/* SEMUA TEXT */
html, body, [class*="css"]{
    color:#111111 !important;
    font-weight:500;
}

/* LABEL */
label{
    color:#111111 !important;
    font-weight:bold !important;
}

/* TITLE */
h1, h2, h3, h4{
    color:#111111 !important;
}

/* TEXT */
p, span, div{
    color:#111111 !important;
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
    color:white !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background-color:#fff0f5;
}

/* INFO BOX */
.stAlert{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

st.title("🎫 SEAT CONCERT")

st.markdown("""
<div class="stage">
STAGE
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("data.csv")

booked = df["Seat"].tolist()

seat_data = {
    "VIP":[f"A{i}" for i in range(1,11)],
    "BLUE":[f"B{i}" for i in range(1,11)],
    "PINK":[f"C{i}" for i in range(1,11)]
}

for kategori, seats in seat_data.items():

    st.subheader(kategori)

    cols = st.columns(5)

    for i, seat in enumerate(seats):

        if seat in booked:
            warna = "booked"

        elif kategori == "VIP":
            warna = "vip"

        elif kategori == "BLUE":
            warna = "blue"

        else:
            warna = "pink"

        cols[i % 5].markdown(
            f"""
            <div class="seat {warna}">
            {seat}
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("---")

st.subheader("💰 PRICE LIST")

col1,col2,col3 = st.columns(3)

with col1:
    st.success("VIP : Rp 3.000.000")

with col2:
    st.info("BLUE : Rp 2.500.000")

with col3:
    st.error("PINK : Rp 1.500.000")
