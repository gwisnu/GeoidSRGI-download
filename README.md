# GeoidSRGI-download
Berikut adalah scrupt untuk mendownload data geoid di website SRGI Badan Informasi Geospasial. selanjutnya data semua titik sampling sampling geoid Indonesia tersebut diinterpolasi untuk mengenerate Geoid Indonesia dalam format raster dengan bantuan software GIS lain (ArcGIS Dektop, QGIS, dsb) <br/>
# Pre-requisite
1. Python 3 :<br/>
C:\>python --version

2. PIP  :<br/>
C:\>pip --version

#Langkah-langkah
1. Buat python virtualenvironment<br/>
C:\>python -m venv geoid-dl
2. Masuk ke virtual env python<br/>
C:\>.\geoid-dl\Scripts\activate
3. Install library yang dibutuhkan<br/>
(geoid-dl)C:\>pip install requests<br/>
(geoid-dl)C:\>pip install beautifulsoup4<br/>
4. Jalankan script download_geoid.py <br/>(misalkan di simpan di C:\geoid-dl\Scripts)<br/>
(geoid-dl)C:\>python .\geoid-dl\Scripts\download_geoid.py
5. Selesai<br/>
Hasilnya akan berupa file CSV dengan nama geoid_indonesia_srgi.csv. Selanjutnya siap digunakan untuk interpolasi data geoid
