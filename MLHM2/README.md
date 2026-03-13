# YZM212 - Makine Öğrenmesi 2. Laboratuvar Ödevi
**MLE ile Akıllı Şehir Planlaması**

Bu repository, bir caddedeki trafik yoğunluğunu Poisson Dağılımı ve Maximum Likelihood Estimation kullanarak modelleyen laboratuvar ödevinin kodlarını ve sonuçlarını içermektedir.

## Bölüm 1: Teorik Türetme (Analitik Çözüm)
Bu bölümde, trafik verilerinin Poisson dağılımına uyduğu varsayılarak Log-Likelihood fonksiyonu matematiksel olarak türetilmiştir. Fonksiyonun türevi alınıp sıfıra eşitlenerek, en iyi parametre tahmininin aslında veri setinin aritmetik ortalamasına eşit olduğu analitik olarak kanıtlanmıştır. İlgili matematiksel ispatlar rapor dosyasında sunulmuştur.

## Bölüm 2: Python ile Sayısal (Numerical) MLE
Analitik çözümü doğrulamak amacıyla, Python'da `scipy.optimize.minimize` kütüphanesi kullanılarak Negatif Log-Likelihood (NLL) minimizasyonu yapılmıştır. 
* Verilen 14 dakikalık trafik verisi kullanılmıştır.
* **Sayısal Tahmin (MLE lambda):** 12.14
* **Analitik Tahmin (Ortalama):** 12.14
Sayısal optimizasyon algoritması, teorik kanıtımızla birebir aynı sonucu bulmuştur.

## Bölüm 3: Model Karşılaştırma ve Görselleştirme
Report klasöründe, raporun içerisinde bulunuyor.

## Bölüm 4: Gerçek Hayat Senaryosu - "Outlier" Analizi
Report klasöründe, raporun içerisinde bulunuyor.
