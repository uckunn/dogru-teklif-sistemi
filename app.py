import streamlit as st
from fpdf import FPDF

# --- Uygulama Başlığı ---
st.set_page_config(page_title="Doğru Mühendislik Teklif")
st.title("Doğru Mühendislik Teklif")

# --- Malzeme Ekleme Alanı ---
with st.form("malzeme_formu"):
    malzeme_adi = st.text_input("Malzeme İsmi")
    adet = st.number_input("Adet", min_value=1, step=1)
    ekle = st.form_submit_button("Listeye Ekle")

# --- Oturum Yönetimi (Listeyi Hafızada Tutmak İçin) ---
if 'liste' not in st.session_state:
    st.session_state.liste = []

if ekle and malzeme_adi:
    st.session_state.liste.append({"İsim": malzeme_adi, "Adet": adet})

# --- Liste Görünümü ---
if st.session_state.liste:
    st.write("### Seçilen Malzemeler")
    for i, item in enumerate(st.session_state.liste):
        st.write(f"{i+1}. **{item['İsim']}** - {item['Adet']} adet")
    
    if st.button("Listeyi Temizle"):
        st.session_state.liste = []
        st.rerun()

# --- Müşteri Bilgileri ve PDF ---
st.write("---")
musteri = st.text_input("Müşteri Adı / Unvanı")
kdv_durumu = st.radio("KDV Durumu:", ["KDV Hariç", "KDV Dahil"])

def teklif_uret():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "DOGRU MUHENDISLIK TEKLIF", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Musteri: {musteri}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Malzeme Listesi:", ln=True)
    pdf.set_font("Arial", '', 12)
    for item in st.session_state.liste:
        pdf.cell(0, 10, f"- {item['İsim']} ({item['Adet']} adet)", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, f"Not: Bu teklifteki fiyatlar {kdv_durumu}'dir.", ln=True)
    return pdf.output(dest='S').encode('latin-1', 'replace')

if st.button("Teklif PDF Oluştur"):
    if musteri and st.session_state.liste:
        pdf_data = teklif_uret()
        st.download_button("Dosyayı İndir", data=pdf_data, file_name=f"Teklif_{musteri}.pdf", mime="application/pdf")
        st.success("PDF hazır!")
    else:
        st.error("Lütfen müşteri adını girin ve listeye en az bir malzeme ekleyin.")
