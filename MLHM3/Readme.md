#### 1. Makine Öğrenmesi ve Matris Manipülasyonu, Özdeğerler, Özvektörler [1]  [2]

- **Matris Manipülasyonu**: Matris manipülasyonu için yapılabilen işlemler belirlidir ve bazıları sadece kısıtlı sayıda matrise uygulanabilir. Bunlar toplama ve çıkartma, çarpma –birkaç tane türevi vardır, kullanımdan kullanıma değişebilir-, tersini alma, determinant, transpozesini almak, faktörizasyon ve birkaç tane daha işlem vardır. Matris manipülasyonları lineer dönüşümlerdir.

- **Özdeğerler**: Bir matrisin spesifik bir `özvektör` ile çarpımı sonucu oluşan `özvektörün` skaler katsayısıdır.

- **Özvektörler**: Bir matris ile çarpıldığında yine kendisinin bir katsayı ile çarpılmış halini üreten vektörlerdir.

Genel olarak üç şey için kullanılırlar:
- **Principal Component Analysis(PCA/Temel bileşen analizi)**: PCA ile veri setinin kovaryans matrisinin `özvektörleri` hesaplanır ve değeri düşük olanlar yok sayılır.
- **Bilgisayarlı Görü**: Yüz tanımada her yüz piksel piksel karşılaştırılmak yerine `eigenface` değerleri hesaplanır ve sadece o değerler kontrol edilir.
- **Spektral Kümeleme**: Karmaşık ve doğrusal olmayan veri kümeleri, benzerlik matrislerinin `özdeğerleri`kullanılarak kümelenir.

Her birinin ortak yanı ***veriyi basitleştirip içerisindeki trendleri fazla işlem yapmadan ortaya çıkarmaktır.*** `Brute force` yöntemlerden çok daha az maliyetli yaklaşımlar sunar.

#### 2. NumPy `linalg.eig` Fonksiyonunun İncelenmesi [3]

**Dokümantasyon Özeti:**
`numpy.linalg.eig(a)` fonksiyonu, parametre olarak karesel bir `a` matrisi alır ve geriye iki farklı yapı döndürür: `w` ve `v`.
* **`w` (Özdeğerler):** Matrisin hesaplanan özdeğerlerini içeren 1 boyutlu bir dizidir. Bu değerler büyüklüklerine göre sıralı olmak zorunda değildir.
* **`v` (Özvektörler):** Özdeğerlere karşılık gelen, normalize edilmiş özvektörleri barındıran 2 boyutlu matristir. Matris manipülasyonlarında en çok dikkat edilmesi gereken kritik detay şudur: Özvektörler satırlarda değil, **sütunlarda** dizilidir. Yani `w[i]` konumundaki bir özdeğere karşılık gelen özvektör, `v` matrisinin `i` indeksli sütunudur (`v[:, i]`).

**Kaynak Kod ve Arka Plan İşlemleri:**
NumPy'ın GitHub deposundaki `linalg` kaynak kodları incelendiğinde, Python'ın bu ağır lineer cebir işlemlerini kendi başına yapmadığı görülür. Python yorumlanan bir dil olduğu için bu tarz nümerik analizlerde yavaş kalır.

Bu nedenle `eig` fonksiyonu; matris boyutlarını, veri tiplerini ve bellek düzenini kontrol ettikten sonra asıl matematiksel yükü C ve Fortran ile yazılmış, endüstri standardı olan **LAPACK** kütüphanesine devreder. Standart karesel matrisler için arka planda LAPACK'ın `_geev` rutini çağrılır. İşlem çok yüksek bir hızda tamamlandıktan sonra, sonuçlar C belleğinden tekrar Python'ın okuyabileceği NumPy dizilerine dönüştürülerek kullanıcıya döndürülür.

#### 3. El Yapımı Özvektör ile Özdeğer Hesabı ve NumPy Kütüphanesiyle Karşılaştırılması 

Kendi yazdığım özdeğer ve özvektör bulma algoritmasında kuvvet iterasyonu yöntemini kullandım. Örnek olarak [ [4.0 1.0], [2.0 3.0] ] matrisini kullandım.

Benim ürettiğim değerler:
	- Dominant Özdeğer: 5.0000
	- Dominant Özvektör: [0.70710678 0.70710678]
NumPy'ın ürettiği değerler:
	- Dominant Özdeğer: 5.0000
	- Dominant Özvektör: [0.70710678 0.70710678]

Görüldüğü üzere kullanılan ondalıklı sayısında aynılar. Kalanının aynılık garantisi yoktur. Kuvvet iterasyonu aşırı isabetli bir yaklaşımdır ama yine de yaklaşımdır.



[1] _G. Strang, Linear Algebra and Its Applications_
[2] https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D
[3] https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html