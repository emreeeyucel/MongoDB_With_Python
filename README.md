# 🚀 MongoDB ve Python ile Veri Yönetimi Projesi 💻📊

Bu projede, MongoDB ve Python kullanarak temel CRUD (Create, Read, Update, Delete) işlemlerinin nasıl yapılacağını adım adım gösterdim. Bu uygulama, MongoDB ile veri ekleme, güncelleme, silme ve sorgulama işlemleri üzerinde durarak veri tabanı yönetimi hakkında temel bilgi edinmenizi sağlayacak.

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

- **Fiyat Aralığına Göre Filtreleme:**  
   MongoDB'nin `$gt`, `$lt`, `$gte` ve `$lte` gibi operatörleri ile fiyat aralıkları oluşturulup ürünler listeleniyor.

- **Regex ile İsim Arama:**  
   Ürün isimlerinde belirli kelimeleri aramak için regex ifadeleri kullanılarak "Monster" gibi ürünler filtreleniyor.

- **Veri Güncellemeleri:**  
   Kullanıcılar, belirli ürünlerin fiyatlarını toplu şekilde artırabilir ya da tüm ürünlerin fiyatlarını azaltabilirler.

## Projeyi GitHub’dan İnceleyebilirsiniz.

