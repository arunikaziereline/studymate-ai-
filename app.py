import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(page_title="StudyMate AI", page_icon="📘", layout="centered")

# Inisialisasi Riwayat Obrolan
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di **StudyMate AI** 🎓. Aku asisten belajar virtualmu. Kamu mau mendiskusikan materi kuliah apa hari ini? (Sains, Logika, Sejarah, atau mau latihan kuis pendek?)"}
    ]

# Header Aplikasi
st.title("📘 StudyMate AI")
st.caption("Asisten Pintar Pendamping Belajar & Persiapan Ujian Mahasiswa")

# Menampilkan Riwayat Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Logika Respons Chatbot Sederhana (Mockup Simulation)
def dapatkan_respons_studymate(prompt):
    prompt_lower = prompt.lower()
    
    if "kuis" in prompt_lower or "latihan" in prompt_lower:
        return "✨ **Mode Kuis Aktif!** ✨\n\n**Pertanyaan:** Manakah di bawah ini yang merupakan komponen utama dari sebuah argumen logis?\n\nA. Premis dan Kesimpulan\nB. Kalimat Tanya\nC. Opini Pribadi\n\n*Ketik jawabanmu (A, B, atau C) untuk memeriksa!*"
    
    elif prompt_lower.strip() == "a" or prompt_lower.strip() == "a.":
        return "✅ **Betul sekali!** Premis dan kesimpulan adalah struktur dasar pembentuk argumen yang valid dalam ilmu logika. Keren!"
        
    elif "rumus" in prompt_lower or "fourier" in prompt_lower or "matematika" in prompt_lower:
        return "Materi yang menarik! Sebagai contoh, jika kita membahas **Deret Fourier** (pengurai fungsi periodik), rumus dasarnya diwakili oleh:\n\n$$f(x) = \\frac{a_0}{2} + \\sum_{n=1}^{\\infty} \\left( a_n \\cos(nx) + b_n \\sin(nx) \\right)$$\n\nApakah kamu ingin mencoba contoh soal atau diskusi teori lainnya?"
        
    elif "sejarah" in prompt_lower or "social" in prompt_lower or "humaniora" in prompt_lower:
        return "Siap! Di bidang Sejarah atau Humaniora, aku bisa membantumu merangkum garis waktu peristiwa penting atau menganalisis dampak sosial dari sebuah era. Topik spesifik apa yang sedang kamu baca?"
        
    else:
        return f"Pertanyaan yang bagus tentang '{prompt}'. Sebagai StudyMate, aku menyarankan kita membagi topik ini menjadi beberapa bagian: konsep dasar, teori utama, dan contoh kasus. Mau mulai dari konsep dasarnya dulu?"

# Input dari Pengguna
if user_input := st.chat_input("Tanyakan materi kuliah, rumus, atau ketik 'Mulai Kuis'..."):
    # Tampilkan chat pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Generate respons simulasi
    respons = dapatkan_respons_studymate(user_input)
    st.session_state.messages.append({"role": "assistant", "content": respons})
    with st.chat_message("assistant"):
        st.markdown(respons)
