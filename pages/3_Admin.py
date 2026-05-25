import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("👨‍💼 ADMIN PANEL")

password = st.text_input(
    "Password Admin",
    type="password"
)

if password == "admin123":

    df = pd.read_csv("data.csv")

    st.subheader("📋 DATA PESANAN")

    st.dataframe(df)

    st.write("---")

    st.subheader("✅ ACC PEMBAYARAN")

    pending = df[
        df["Status"] == "PENDING"
    ]

    if not pending.empty:

        pilih = st.selectbox(
            "Pilih Seat",
            pending["Seat"]
        )

        if st.button("ACC Pembayaran"):

            df.loc[
                df["Seat"] == pilih,
                "Status"
            ] = "PAID"

            df.to_csv(
                "data.csv",
                index=False
            )

            st.success(
                "Pembayaran berhasil di ACC"
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

            df.to_csv(
                "data.csv",
                index=False
            )

            st.success(
                "Pesanan berhasil dihapus!"
            )

    st.write("---")

    st.subheader("💰 TOTAL PEMASUKAN")

    paid = df[
        df["Status"] == "PAID"
    ]

    total = paid["Total"].sum()

    st.success(
        f"Rp {int(total):,}"
    )

else:

    st.warning(
        "Masukkan password admin"
    )
