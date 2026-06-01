import streamlit as st
import pandas as pd
import time
import random

st.set_page_config(layout="wide")

# =========================
# STYLE
# =========================

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
    color:#111111;
}

/* LABEL INPUT */
label{
    color:#111111 !important;
    font-weight:bold !important;
}

/* TEXT */
p, span, div{
    color:#111111 !important;
}

/* TITLE */
h1, h2, h3, h4{
    color:#111111 !important;
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

def generate_booking_id(df):

    while True:

        booking_id = "BK" + str(
            random.randint(1000, 9999)
        )

        if booking_id not in df["BookingID"].astype(str).tolist():

            return booking_id

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
    df = pd.read_csv("data.csv")

    if seat in df["Seat"].tolist():

        st.error("Seat sudah dibooking!")

        st.stop()

    if nama == "":
        st.warning("Nama wajib diisi!")

    else:

        cek = df[
            (df["Nama"] == nama) &
            (df["Seat"] == seat)
        ]
        booking_id = generate_booking_id(df)

        if not cek.empty:
            st.error("Pesanan sudah ada!")

        else:
            data_baru = pd.DataFrame([{
            "BookingID": booking_id,
            "Nama": nama,
            "Seat": seat,
            "Kategori": kategori,
            "Subtotal": harga,
            "Pajak": pajak,
            "Admin": admin,
            "Total": total,
            "Metode": metode,
            "Saldo": 0,
            "SisaSaldo": 0,
            "Status": "PENDING"
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
            f"Pesanan berhasil dibuat!\n\nID Booking: {booking_id}"
            )
            time.sleep(1)
            st.rerun()

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

    st.dataframe(
        pesanan_user[
            [
                "BookingID",
                "Nama",
                "Seat",
                "Kategori",
                "Total",
                "Status"
            ]
        ]
    )
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

        st.subheader("✏ UPDATE PESANAN")

        seat_lama = st.selectbox(
            "Pilih Seat Lama",
            pending["Seat"]
        )

        kategori_baru = st.selectbox(
            "Kategori Baru",
            list(harga_tiket.keys())
        )

        seat_baru_tersedia = [
            s for s in seat_data[kategori_baru]
            if s not in booked
        ]

        seat_baru = st.selectbox(
            "Seat Baru",
            seat_baru_tersedia
        )

        if st.button("Update Pesanan"):

            harga_baru = harga_tiket[kategori_baru]

            pajak_baru = harga_baru * 0.10

            total_baru = harga_baru + pajak_baru + admin

            idx = df[
                df["Seat"] == seat_lama
            ].index

            df.loc[idx, "Kategori"] = kategori_baru
            df.loc[idx, "Seat"] = seat_baru
            df.loc[idx, "Subtotal"] = harga_baru
            df.loc[idx, "Pajak"] = pajak_baru
            df.loc[idx, "Total"] = total_baru

            df.to_csv(
                "data.csv",
                index=False
            )

            st.success(
                "Pesanan berhasil diupdate!"
            )
            time.sleep(1)
            st.rerun()

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
            time.sleep(1)
            st.rerun()

        # =====================
        # BAYAR
        # =====================

       st.subheader("💳 BAYAR SEKARANG")

        pilih_bayar = st.selectbox(
            "Pilih Seat",
            pending["Seat"],
            key="bayar"
        )
        
        total_bayar = int(
            df.loc[
                df["Seat"] == pilih_bayar,
                "Total"
            ].values[0]
        )
        
        st.info(
            f"Total Pembayaran : Rp {total_bayar:,}"
        )
        
        metode_bayar = st.selectbox(
            "Metode Pembayaran",
            ["Debit", "Kredit", "QRIS"],
            key="metode_bayar"
        )
        
        saldo = st.number_input(
            "Masukkan Saldo",
            min_value=0,
            key="saldo"
        )
        
        sisa_saldo = 0
        
        if saldo >= total_bayar:
        
            sisa_saldo = saldo - total_bayar
        
            st.success(
                f"Sisa Saldo : Rp {sisa_saldo:,}"
            )
        
        else:
        
            st.warning(
                "Saldo tidak cukup. Silakan pilih metode lain atau isi saldo lebih besar."
            )
        
        if st.button("Bayar"):
        
            if saldo < total_bayar:
        
                st.error(
                    "Pembayaran gagal karena saldo tidak cukup."
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
                    "Metode"
                ] = metode_bayar
        
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
        
                time.sleep(1)
        
                st.rerun()

# =========================
# E-TICKET
# =========================

st.write("---")

st.subheader("🎫 E-TICKET")

booking_id_cari = st.text_input(
    "Masukkan Booking ID"
)

if booking_id_cari != "":

    df = pd.read_csv("data.csv")

    tiket = df[
        (df["BookingID"] == booking_id_cari)
        &
        (df["Status"] == "PAID")
    ]

    if not tiket.empty:

        row = tiket.iloc[0]

        st.markdown(f"""
        ## TXT WORLD TOUR
        ### ACT : LOVESICK

        👤 Nama :
        {row['Nama']}

        🆔 Booking ID :
        {row['BookingID']}

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
        st.warning("Booking ID tidak ditemukan atau tiket belum dibayar")
