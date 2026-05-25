import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>

.stApp{
    background-color:#fff8ee;
}

.box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

st.title("🎟 BOOKING TICKET")

df = pd.read_csv("data.csv")

harga_tiket = {
    "VIP":3000000,
    "BLUE":2500000,
    "PINK":1500000
}

seat_data = {
    "VIP":[f"A{i}" for i in range(1,11)],
    "BLUE":[f"B{i}" for i in range(1,11)],
    "PINK":[f"C{i}" for i in range(1,11)]
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

saldo = st.number_input(
    "Masukkan Saldo",
    min_value=0
)

kembalian = saldo - total

st.write("### 🧾 DETAIL PEMBAYARAN")

st.write(f"Harga Tiket : Rp {harga:,}")
st.write(f"Pajak 10% : Rp {pajak:,}")
st.write(f"Biaya Admin : Rp {admin:,}")

st.success(f"TOTAL : Rp {total:,}")

if saldo > 0:

    if saldo < total:
        st.error("Saldo tidak cukup!")

    else:
        st.success(
            f"Kembalian : Rp {kembalian:,.0f}"
        )

if st.button("Konfirmasi Pesanan"):

    if nama == "":
        st.warning("Nama wajib diisi!")

    elif saldo < total:
        st.error("Saldo tidak cukup!")

    else:

        data_baru = pd.DataFrame([{
            "Nama":nama,
            "Seat":seat,
            "Kategori":kategori,
            "Subtotal":harga,
            "Pajak":pajak,
            "Admin":admin,
            "Total":total,
            "Metode":metode,
            "Saldo":saldo,
            "Kembalian":kembalian,
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

        st.success(
            "Pesanan berhasil dibuat!"
        )

st.write("---")

st.subheader("📋 PESANAN SAYA")

if nama != "":

    pesanan_user = df[
        df["Nama"] == nama
    ]

    st.dataframe(pesanan_user)

    pending = pesanan_user[
        pesanan_user["Status"] == "PENDING"
    ]

    if not pending.empty:

        st.subheader("✏ UPDATE SEAT")

        seat_lama = st.selectbox(
            "Seat Lama",
            pending["Seat"]
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

        st.subheader("🗑 BATALKAN PESANAN")

        hapus = st.selectbox(
            "Pilih Seat",
            pending["Seat"],
            key="hapus"
        )

        if st.button("Batalkan"):

            df = df[
                df["Seat"] != hapus
            ]

            df.to_csv(
                "data.csv",
                index=False
            )

            st.success(
                "Pesanan berhasil dibatalkan"
            )

st.write("---")

st.subheader("🎫 E-TICKET")

if nama != "":

    paid = pesanan_user[
        pesanan_user["Status"] == "PAID"
    ]

    if not paid.empty:

        for i, row in paid.iterrows():

            st.markdown(f"""
            ## TXT WORLD TOUR
            ### ACT : LOVESICK

            👤 Nama :
            {row['Nama']}

            💺 Seat :
            {row['Seat']}

            🎟 Kategori :
            {row['Kategori']}

            💳 Metode :
            {row['Metode']}

            💰 Total :
            Rp {row['Total']:,.0f}

            ✅ STATUS :
            {row['Status']}
            """)

    else:
        st.warning(
            "E-Ticket belum tersedia"
        )
