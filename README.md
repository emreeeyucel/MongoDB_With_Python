# 🚀 MongoDB ve Python ile Veri Yönetimi Projesi 💻📊

   Bu projede, MongoDB ile veri ekleme, güncelleme, silme ve sorgulama işlemlerini detaylı bir şekilde ele alarak, NoSQL veritabanlarının temel prensiplerini öğrenmek ve bunları etkin bir şekilde uygulamak için güçlü bir altyapı sunar. Uygulamada, MongoDB'nin sağladığı esnek veri modeli, hızlı sorgulama mekanizmaları ve güçlü bağlantı özellikleri kullanılarak, verilerin yönetimi ve işlenmesi konularında kapsamlı bir deneyim kazandırılmaktadır. Python ile MongoDB arasındaki NoSQL bağlantıları, verilerin kolay entegrasyonu ve işlenmesi için örneklerle desteklenmiştir. Bu sayede, NoSQL mimarisine dayalı uygulamalar geliştirirken MongoDB'nin avantajlarını daha iyi anlamanıza ve bu altyapıyı projelerinizde verimli bir şekilde kullanmanıza olanak sağlanmaktadır.

## Kullanılan Teknolojiler:
- Python
- pymongo modülü
- MongoDB

## Projede Kullanılan Temel İşlemler:

1. **MongoDB Sunucusuna Bağlantı Kurma:**  
   MongoDB server’ına bağlanarak veritabanı ve collection oluşturuluyor.
   
2. **Tekli ve Çoklu Kayıt Ekleme:**  
   MongoDB’ye veri eklemek için `insert_one()` ve `insert_many()` metotları kullanılarak, hem tekil hem de birden fazla ürün kaydını veritabanına ekliyoruz.

3. **Veri Sorgulama:**  
   `find()` metodu ile verileri sorguluyoruz. Bu adımda, fiyatı 50.000’den büyük, belirli aralıklarda olan veya "Monster" gibi özel kelimeleri içeren ürünleri listelemek için regex ifadeleri kullanıyoruz.

4. **Veri Güncelleme:**  
   Belirli koşullara göre `update_one()` ve `update_many()` metotları ile ürünlerin fiyatlarını güncelliyoruz. Örneğin, belirli bir isme sahip ürünlerin fiyatlarını %10 artırmak veya tüm ürünlerin fiyatlarını azaltmak.

5. **Veri Silme ve Güncelleme:**  
   `update()` ve `delete_one()` gibi işlemlerle verileri silme veya güncelleme işlemleri gerçekleştirilmiştir.

6. **Sıralama:**  
   Verileri fiyat veya isim gibi belirli kriterlere göre sıralamak için `sort()` metodu kullanılmıştır.

## Öne Çıkan Sorgular ve İşlemler:

- **Aralığına Göre Filtreleme:**  
   MongoDB'nin `$gt`, `$lt`, `$gte` ve `$lte` gibi operatörleri ile veri aralıkları oluşturulup ürünler listeleniyor.

- **Regex ile İsim Arama:**  
   Ürün isimlerinde belirli kelimeleri aramak için regex ifadeleri kullanılarak "Monster" gibi ürünler filtreleniyor.

- **Veri Güncellemeleri:**  
   Kullanıcılar, belirli ürünlerin fiyatlarını toplu şekilde artırabilir ya da tüm ürünlerin fiyatlarını azaltabilirler.

- **Veri Gruplama ve Aggregation (Pipelining):**  
   MongoDB'nin aggregate() fonksiyonu ile daha karmaşık sorgular ve veri analizleri yapılabiliyor. Örneğin, tüm ürünlerin ortalama fiyatını hesaplamak için $group operatörü kullanılabilir. Ayrıca, sort(), $match, $limit gibi operatörler ile veriler daha ayrıntılı bir şekilde sıralanabilir ve filtrelenebilir. Bu özellik, kullanıcıların daha derinlemesine analiz yapabilmelerini sağlar.

- **Sıralama ve Sayfalama:**  
   sort() fonksiyonu ile fiyat, isim, tarih gibi parametrelere göre veriler sıralanabiliyor. Ayrıca, kullanıcılar skip() ve limit() metotları ile sayfalama yaparak, verilerin bir kısmını daha hızlı ve verimli bir şekilde çekebilirler.


