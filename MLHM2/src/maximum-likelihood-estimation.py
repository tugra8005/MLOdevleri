import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
import matplotlib.pyplot as plt
# Gözlemlenen Trafik Verisi (1 dakikada geçen araç sayısı)
traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9,
12, 11, 14, 10, 15])
def negative_log_likelihood(lam, data):
    """
    Poisson dağılımı için Negatif Log-Likelihood hesaplar.
    İpucu: log(k!) terimi optimizasyon sırasında sabit
    olduğu için ihmal edilebilir.
    """
    sn = len(data)
    # TODO: Log-likelihood formülünü (negatif olarak) buraya yazın
    # Ayrıca, np.sum ve np.log ile optimize implicit döngüler kullanılır.
    nll = sn * lam - np.sum(data) * np.log(lam)
    return nll
# Başlangıç tahmini
initial_guess = 1.0
# Optimizasyon: NLL'yi minimize etmek, Likelihood'u maximize etmektir.
result = opt.minimize(negative_log_likelihood, initial_guess, args=(traffic_data,), bounds=[(0.001, None)])
print(f"Sayısal Tahmin (MLE lambda): {result.x[0]}")
print(f"Analitik Tahmin (Ortalama): {np.mean(traffic_data)}")

max_traffic = np.max(traffic_data)
x_values = np.arange(0, max_traffic+5)

best_lambda = result.x[0]
# Poisson kütle fonksiyonu uygulanır bütün değerlere.
pmf_values = stats.poisson.pmf(x_values, best_lambda)
# Gerçek verinin histogramı oluşturulur.
plt.hist(traffic_data, bins=np.arange(min(traffic_data)-0.5, max_traffic+1.5, 1), density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Gerçek Veri (Histogram)') 
# Elde edilen eğri grafiğe çizilir.
plt.plot(x_values, pmf_values, label=f'Poisson PMF (λ={best_lambda:.2f})')
plt.xlabel('Bir Dakikada Geçen Araç Sayısı')
plt.ylabel('Olasılık')
plt.title('Bölüm 3: Trafik Verisi ve MLE Poisson Modeli Karşılaştırması')
plt.legend()

plt.show()
