import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🎟 BOOKING TIKET")

df = pd.read_csv("data.csv")

harga_tiket = {
    "VIP":3000000,
    "BLUE":2500000,
    "PINK":1500000
}

seat_data = {
    "VIP": [f"A{i}" for i in range(1,11)],
    "BLUE": [f"B{i}" for i in range(1,11)],
    "PINK": [f"C{i}" for i in range(1,11)]
}

nama = st.text_input("Nama")

kategori = st.selectbox(
    "Kategori",
    list(harga_tiket.keys())
)

booked = df["Seat"].tolist()

seat_tersedia = [
    seat
    for seat in seat_data[kategori]
    if seat not in booked
]

seat = st.selectbox(
    "Pilih Seat",
    seat_tersedia
)

harga = harga_tiket[kategori]

pajak = harga * 0.10

admin = 5000

total = harga + pajak + admin

st.write("### 🧾 DETAIL PEMBAYARAN")

st.write(f"Harga Tiket : Rp {harga:,}")
st.write(f"Pajak 10% : Rp {pajak:,}")
st.write(f"Biaya Admin : Rp {admin:,}")

st.success(f"TOTAL : Rp {total:,}")

if st.button("Konfirmasi Pesanan"):

    data_baru = pd.DataFrame([{
        "Nama":nama,
        "Seat":seat,
        "Kategori":kategori,
        "Subtotal":harga,
        "Pajak":pajak,
        "Admin":admin,
        "Total":total,
        "Status":"PENDING"
    }])

    df = pd.concat(
        [df,data_baru],
        ignore_index=True
    )

    df.to_csv(
        "data.csv",
        index=False
    )

    st.success("Pesanan berhasil dibuat!")
