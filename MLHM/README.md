# YZM212 Makine Öğrenmesi - Lab 1: HMM ile İzole Kelime Tanıma Sistemi

Bu proje, YZM212 Makine Öğrenmesi dersi I. Laboratuvar değerlendirmesi kapsamında geliştirilmiş bir Gizli Markov Modeli (HMM) tabanlı kelime tanıma simülasyonudur.

## Problem Tanımı
Konuşma tanımada kelimeleri oluşturan fonemlerin "Gizli Durumlar" (Hidden States) ve ses frekans karakteristiklerinin "Gözlemler" (Observations) olarak modellendiği bir sistem tasarlanmıştır. Amaç, dışarıdan gelen bilinmeyen bir ses dizisinin (örn. `[High, Low]`), önceden tanımlanmış "EV" ve "OKUL" HMM modellerinden hangisine ait olduğunu log-olabilirlik (Log-Likelihood) skorlarını karşılaştırarak bulmaktır.

## Veri
Model parametreleri (Başlangıç, Geçiş ve Emisyon olasılıkları) sentetik olarak tanımlanmış ve projede esneklik sağlaması adına `.csv` formatında `data/` dizininde saklanmıştır.
* **EV Modeli:** 2 bileşenli (e, v fonemleri) model.
* **OKUL Modeli:** 4 bileşenli (O, K, U, L fonemleri) model.

## Yöntem
Proje iki ana aşamadan oluşmaktadır:
1. **Teorik (Viterbi Algoritması):** "EV" kelimesi için verilen `[High, Low]` gözlem dizisinin en olası fonem dizilimi (e -> v) matematiksel olarak adımlarla hesaplanmıştır. (Detaylar `report/cozum_anahtari.pdf` dosyasındadır).
2. **Uygulama (Python & hmmlearn):** Python ortamında `hmmlearn` kütüphanesi (güncel sürümdeki `CategoricalHMM` modülü) kullanılarak modeller oluşturulmuş ve verilen test verileri `.score()` metodu ile karşılaştırılarak sınıflandırma yapılmıştır.

## Sonuçlar
Sistem, `src/recognizer.py` dosyası üzerinden çalıştırıldığında test dizilerini başarıyla dekode etmekte ve her iki model için hesaplanan Log-Likelihood skorlarını ekrana yazdırmaktadır. Daha yüksek skor veren model, sistemin tahmini olarak kabul edilmektedir. Manuel olarak hesaplanan Viterbi olasılıkları ile Python kütüphanesinin ürettiği log olasılık değerleri birbiriyle eşleşmiştir.

## Yorum ve Tartışma
Ses verisindeki çevresel gürültünün emisyon olasılıklarını nasıl etkilediği ve gerçek dünya senaryolarında binlerce kelime için HMM yerine neden Derin Öğrenme (Deep Learning) mimarilerinin tercih edildiğine dair detaylı analiz rapor dosyasında sunulmuştur.

## Kurulum ve Çalıştırma
```bash
# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Modeli çalıştırın
python src/recognizer.py
