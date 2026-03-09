import streamlit as st
import random

# Konfigurasi Halaman
st.set_page_config(page_title="Generator GA Telkom-Bot", page_icon="🤖", layout="centered")

st.title("⚙️ Generator Parameter Algoritma Genetika")
st.markdown("Masukkan **5 digit terakhir NIM** Anda untuk mendapatkan data parameter Lembar Kerja Simulasi (Dry Run) Telkom-Bot.")

# Input NIM
nim_input = st.text_input("Masukkan NIM (Angka Saja):", max_chars=5, placeholder="Contoh: 12345")

# Tombol Eksekusi
if st.button("Generate Parameter LKS", type="primary"):
    if nim_input.isdigit():
        # Set seed berdasarkan NIM agar hasilnya selalu sama untuk anak tersebut
        random.seed(int(nim_input))
        
        st.success(f"✅ Data berhasil ditarik untuk NIM: **{nim_input}**")
        
        # --- BAGIAN A: POPULASI AWAL ---
        st.header("A. Populasi Awal (Generasi 0)")
        st.info("Ubah nilai integer (0-15) di bawah ini menjadi representasi Biner 4-bit di LKS Anda.")
        
        # Generate 6 kromosom awal
        for i in range(1, 7):
            genes = [random.randint(0, 15) for _ in range(5)]
            st.code(f"Kromosom {i}: {genes}", language="text")
            
        # --- BAGIAN B: PARAMETER GENERASI ---
        def show_params(gen_num):
            st.header(f"B. Parameter Siklus Generasi {gen_num}")
            
            # 1. Roulette Wheel
            roulette_vals = [round(random.uniform(0, 1), 3) for _ in range(4)]
            st.markdown(f"**1. Angka Acak Roulette Wheel (Pemilihan Induk):**")
            st.code(f"R1 = {roulette_vals[0]}  |  R2 = {roulette_vals[1]}  |  R3 = {roulette_vals[2]}  |  R4 = {roulette_vals[3]}", language="text")
            
            # 2. Crossover
            pts1 = sorted(random.sample(range(1, 20), 2))
            pts2 = sorted(random.sample(range(1, 20), 2))
            st.markdown(f"**2. Titik Potong 2-Point Crossover:**")
            st.markdown(f"- **Pasangan 1:** Potong setelah bit ke-{pts1[0]} dan bit ke-{pts1[1]}")
            st.markdown(f"- **Pasangan 2:** Potong setelah bit ke-{pts2[0]} dan bit ke-{pts2[1]}")
            
            # 3. Mutasi (Probabilitas 10%)
            mutation_prob = 0.10
            st.markdown(f"**3. Titik Mutasi Bit-Flip (Berdasarkan Probabilitas {int(mutation_prob*100)}% per bit):**")
            
            mut_text = ""
            for anak in range(1, 5):
                # Lempar dadu untuk tiap bit (1 sampai 20)
                flipped_bits = [bit for bit in range(1, 21) if random.random() < mutation_prob]
                
                if flipped_bits:
                    bit_str = ", ".join(map(str, flipped_bits))
                    mut_text += f"- **Anak {anak}:** Balik bit ke- **{bit_str}**\n"
                else:
                    mut_text += f"- **Anak {anak}:** Tidak ada mutasi (Aman)\n"
            
            st.markdown(mut_text)
            st.divider()

        # Tampilkan parameter untuk 2 generasi
        show_params(1)
        show_params(2)
        
        st.caption("⚠️ Ingat: Parameter di atas bersifat unik untuk NIM Anda. Jangan menyalin milik teman!")
        
    else:
        st.error("Harap masukkan format angka yang valid (Maksimal 5 digit)!")
