import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# =========================
# STYLE
# =========================

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

# =========================
# TITLE
# =========================

st.title("🎟 BOOKING TICKET")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data.csv")

# =========================
# HARGA
# =========================

harga_tiket = {
    "VIP":3000000,
    "BLUE":2500000,
    "PINK":1500000
}

# =========================
# SEAT
# =========================

seat_data = {
    "VIP":[f"A{i}" for i in range(1,11)],
    "BLUE":[f"B{i}" for i in range(1,11)],
    "PINK":[f"C{i}" for i in range(1,11)]
}

# =========================
# FORM BOOKING
# =========================

nama = st.text_input("Nama")

kategori = st.selectbox(
    "Kategori",
    list(harga_tiket.keys())
)

booked = df[
    df["Status"] == "PAID"
]["Seat"].tolist()

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

# =========================
# PERHITUNGAN
# =========================

harga = harga_tiket[kategori]

pajak = harga * 0.10

admin = 5000

total = harga + pajak + admin

# =========================
# DETAIL
# =========================

st.write("### 🧾 DETAIL PEMBAYARAN")

st.write(f"Harga Tiket : Rp {harga:,}")
st.write(f"Pajak 10% : Rp {pajak:,}")
st.write(f"Biaya Admin : Rp {admin:,}")

st.success(f"TOTAL : Rp {total:,}")

# =========================
# KONFIRMASI PESANAN
# =========================

if st.button("Konfirmasi Pesanan"):

    if nama == "":
        st.warning("Nama wajib diisi!")

    else:

        cek = df[
            (df["Nama"] == nama) &
            (df["Seat"] == seat)
        ]

        if not cek.empty:
            st.error("Pesanan sudah ada!")

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
                "Saldo":0,
                "SisaSaldo":0,
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

# =========================
# PESANAN SAYA
# =========================

st.write("---")

st.subheader("📋 PESANAN SAYA")

if nama != "":

    df = pd.read_csv("data.csv")

    pesanan_user = df[
        df["Nama"] == nama
    ]

    st.dataframe(pesanan_user)

    # =====================
    # PENDING
    # =====================

    pending = pesanan_user[
        pesanan_user["Status"] == "PENDING"
    ]

    if not pending.empty:

        # =====================
        # UPDATE
        # =====================

        st.subheader("✏ UPDATE SEAT")

        seat_lama = st.selectbox(
            "Seat Lama",
            pending["Seat"]
        )

        kategori_lama = df.loc[
            df["Seat"] == seat_lama,
            "Kategori"
        ].values[0]

        seat_kategori = [
            s for s in seat_data[kategori_lama]
            if s not in booked
        ]

        seat_baru = st.selectbox(
            "Seat Baru",
            seat_kategori
        )

        if st.button("Update Seat"):

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

        # =====================
        # DELETE
        # =====================

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

        # =====================
        # BAYAR
        # =====================

        st.subheader("💳 BAYAR SEKARANG")

        pilih_bayar = st.selectbox(
            "Pilih Seat",
            pending["Seat"],
            key="bayar"
        )

        total_bayar = int(df.loc[
            df["Seat"] == pilih_bayar,
            "Total"
        ].values[0])

        st.info(
            f"Total Pembayaran : Rp {total_bayar:,}"
        )

        saldo = st.number_input(
            "Masukkan Saldo",
            min_value=0,
            key="saldo"
        )

        if saldo >= total_bayar:

            sisa_saldo = saldo - total_bayar

            st.success(
                f"Sisa Saldo : Rp {sisa_saldo:,}"
            )

        if st.button("Bayar"):

            if saldo < total_bayar:

                st.error(
                    "Saldo tidak cukup!"
                )

            else:

                df.loc[
                    df["Seat"] == pilih_bayar,
                    "Saldo"
                ] = saldo

                df.loc[
                    df["Seat"] == pilih_bayar,
                    "SisaSaldo"
                ] = sisa_saldo

                df.loc[
                    df["Seat"] == pilih_bayar,
                    "Status"
                ] = "PAID"

                df.to_csv(
                    "data.csv",
                    index=False
                )

                st.success(
                    "Pembayaran berhasil!"
                )

# =========================
# E-TICKET
# =========================

st.write("---")

st.subheader("🎫 E-TICKET")

if nama != "":

    df = pd.read_csv("data.csv")

    pesanan_user = df[
        df["Nama"] == nama
    ]

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
