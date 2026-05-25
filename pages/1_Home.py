import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #8b0000,
        #fff8ee
    );
}

.stage{
    background-color:black;
    color:white;
    text-align:center;
    padding:20px;
    border-radius:15px;
    font-size:35px;
    font-weight:bold;
    margin-bottom:30px;
}

.seat{
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-weight:bold;
    margin:5px;
    color:black;
}

.vip{
    background:#8ef0c1;
}

.blue{
    background:#7fc8ff;
}

.pink{
    background:#ffb3c7;
}

.booked{
    background:red;
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.title("🎤 TXT WORLD TOUR")

st.markdown("""
<div class="stage">
STAGE
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("data.csv")

booked = df["Seat"].tolist()

seat_data = {
    "VIP": [f"A{i}" for i in range(1,11)],
    "BLUE": [f"B{i}" for i in range(1,11)],
    "PINK": [f"C{i}" for i in range(1,11)]
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
