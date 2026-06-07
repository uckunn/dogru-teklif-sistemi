import streamlit as st

# Uygulama Başlığı
st.title("Doğru Mühendislik Teklif Sistemi")
st.write("Teklif detaylarını aşağıya girin:")

# Kullanıcıdan veri alma alanları
birim_fiyat = st.number_input("Birim Fiyat (TL)", min_value=0.0, format="%.2f")
miktar = st.number_input("Miktar", min_value=0)
kdv_orani = st.selectbox("KDV Oranı", [0, 10, 20])

# Hesaplama butonu
if st.button("Teklifi Hesapla"):
    ara_toplam = birim_fiyat * miktar
    kdv_tutari = ara_toplam * (kdv_orani / 100)
    genel_toplam = ara_toplam + kdv_tutari
    
    st.success(f"Ara Toplam: {ara_toplam:,.2f} TL")
    st.info(f"KDV ({kdv_orani}%): {kdv_tutari:,.2f} TL")
    st.write(f"### Genel Toplam: {genel_toplam:,.2f} TL")