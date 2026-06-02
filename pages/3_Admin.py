import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>

.stApp{
    background-color:#1e1e1e;
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.title("👨‍💼 ADMIN PANEL")

password = st.text_input(
    "Password Admin",
    type="password"
)
if password == "":
    st.warning("Masukkan Password Admin")
    
elif password == "Kaawai14":

    df = pd.read_csv("data.csv")

    st.subheader("📋 DATA PESANAN")

    st.dataframe(df)

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
    st.warning("❌ Password admin salah!")
