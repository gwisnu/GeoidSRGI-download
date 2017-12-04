# GeoidSRGI-download

# Pre-requisite
1. Python 3 :
C:\>python --version

2. PIP  :
C:\>pip --version

#Langkah-langkah
1. Buat python virtualenvironment
C:\>python -m venv geoid-dl
2. Masuk ke virtual env python
C:\>.\geoid-dl\Scripts\activate
3. Install library yang dibutuhkan
(geoid-dl)C:\>pip install requests
(geoid-dl)C:\>pip install beautifulsoup4
4. Jalankan script download_geoid.py (misalkan di simpan di C:\geoid-dl\Scripts)
(geoid-dl)C:\>python .\geoid-dl\Scripts\download_geoid.py
5. Selesai
Hasilnya akan berupa file CSV dengan nama geoid_indonesia_srgi.csv
Selanjutnya siap digunakan untuk interpolasi data geoid
