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
</stylle>
""", unsafe_allow_html=True)
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

st.write("---")

st.subheader("✏ UPDATE SEAT")

pending2 = df[
    df["Status"] == "PENDING"
]

if not pending2.empty:

    seat_lama = st.selectbox(
        "Seat Lama",
        pending2["Seat"],
        key="update"
    )

    seat_baru = st.text_input(
        "Seat Baru"
    )

    if st.button("Update Seat"):

        booked = df["Seat"].tolist()

        if seat_baru in booked:

            st.error("Seat sudah dipakai!")

        else:

            df.loc[
                df["Seat"] == seat_lama,
                "Seat"
            ] = seat_baru

            df.to_csv(
                "data.csv",
                index=False
            )

            st.success(
                "Seat berhasil diupdate!"
            )

st.write("---")

st.subheader("🗑 DELETE PESANAN")

if not pending2.empty:

    delete_seat = st.selectbox(
        "Pilih Seat",
        pending2["Seat"],
        key="delete"
    )

    if st.button("Hapus Pesanan"):
            
        df = df[
        df["Seat"] != delete_seat
        ]

        df.to_csv("data.csv",
            index=False)

        st.success("Pesanan berhasil dihapus!")

metode = st.selectbox(
    "Metode Pembayaran",
    [
        "Debit",
        "Kredit",
        "QRIS"
    ]
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

# =========================
# E-TICKET
# =========================

kode_tiket = f"{seat}-{nama}"

eticket = f"""
========== E-TICKET ==========
TXT WORLD TOUR

Nama : {nama}
Seat : {seat}
Kategori : {kategori}

Metode Pembayaran : {metode}

Subtotal : Rp {harga:,}
Pajak : Rp {pajak:,}
Biaya Admin : Rp {admin:,}

TOTAL : Rp {total:,}

Status : PENDING

Kode Tiket :
{kode_tiket}

==============================
"""

st.download_button(
    label="🎫 Download E-Ticket",
    data=eticket,
    file_name=f"{kode_tiket}.txt",
    mime="text/plain"
)

if st.button("Konfirmasi Pesanan"):

    data_baru = pd.DataFrame([{
        "Nama":nama,
        "Seat":seat,
        "Kategori":kategori,
        "Subtotal":harga,
        "Pajak":pajak,
        "Admin":admin,
        "Total":total,
        "Metode":metode,
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
