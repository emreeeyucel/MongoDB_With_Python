# pymongo modülünü MongoDB Server erişmek için kullanacağız.
from pymongo import MongoClient
from pprint import pprint
import re

# Connection String oluşturuyoruz. Bu connection string vasıtasıyla app ile server bağlantı kuracak.
conn = MongoClient('mongodb://localhost:27017/')

# server üzerinde bir veri tabanı yaratılım
db = conn['app_db']
# yukarı da yarattığımız veri tabanı içerisine bir collection açalım
collection = db['productc']


# region Tek Kayıt Ekleme.
product_name = input('Product Name: ')
price = input('Price: ')

product = {
    'name': product_name,
    'price': price
}
result = collection.insert_one(product)

print("Eklenen belgelerin ID'leri:", result.inserted_id)     # result.inserted_id  --> MongoDB'de bir belgeyi başarıyla ekledikten sonra döndürülen bir özelliktir. / Yeni eklenen belgenin _id'sini yazdırır
#endregion




#  region Çoklu Kayıt Ekleme

product_list = [
    {'_id': 1, 'name': 'Lenovo X1 Carbon', 'price': 84.999, 'country': 'USA', 'stock': 12, 'continent': 'North America'},
    {'_id': 2, 'name': 'MacBook Pro M3', 'price': 184.999, 'country': 'USA', 'stock': 8, 'continent': 'North America'},
    {'_id': 3, 'name': 'Asus Zen Book', 'price': 74.999, 'country': 'Taiwan', 'stock': 15, 'continent': 'Asia'},
    {'_id': 4, 'name': 'Monster Alba', 'price': 33.999, 'country': 'Turkey', 'stock': 20, 'continent': 'Europe'},
    {'_id': 5, 'name': 'Monster Tulpar', 'price': 64.999, 'country': 'Turkey', 'stock': 7, 'continent': 'Europe'},
    {'_id': 6, 'name': 'Monster Huma', 'price': None, 'country': 'Turkey', 'stock': 0, 'continent': 'Europe'},
    {'_id': 7, 'name': 'HP', 'price': '???', 'country': 'USA', 'stock': 5, 'continent': 'North America'},
    {'_id': 8, 'name': None, 'price': '???', 'country': 'Unknown', 'stock': 0, 'continent': 'Unknown'},
    {'_id': 9, 'name': '???', 'country': None, 'stock': 0, 'continent': 'Unknown'},
    {'_id': 10, 'price': '', 'country': 'Unknown', 'stock': 0, 'continent': 'Unknown'},
    {'_id': 11, 'price': '???', 'country': '???', 'stock': 0, 'continent': 'Unknown'},
    {'_id': 12, 'price': '', 'country': 'Unknown', 'stock': 0, 'continent': 'Unknown'},
    {'_id': 13, 'name': 'Dell XPS 13', 'price': 139.999, 'country': 'USA', 'stock': 10, 'continent': 'North America'},
    {'_id': 14, 'name': 'Acer Swift 5', 'price': 52.999, 'country': 'Taiwan', 'stock': 12, 'continent': 'Asia'},
    {'_id': 15, 'name': 'Samsung Galaxy Book', 'price': 47.999, 'country': 'South Korea', 'stock': 8, 'continent': 'Asia'},
    {'_id': 16, 'name': 'Huawei MateBook X', 'price': 89.999, 'country': 'China', 'stock': 6, 'continent': 'Asia'},
    {'_id': 17, 'name': 'Microsoft Surface Laptop', 'price': 125.999, 'country': 'USA', 'stock': 4, 'continent': 'North America'},
    {'_id': 18, 'name': 'Lenovo IdeaPad', 'price': 45.999, 'country': 'China', 'stock': 13, 'continent': 'Asia'},
    {'_id': 19, 'name': 'HP Pavilion', 'price': 55.999, 'country': 'USA', 'stock': 9, 'continent': 'North America'},
    {'_id': 20, 'name': 'Asus VivoBook', 'price': 39.999, 'country': 'Taiwan', 'stock': 18, 'continent': 'Asia'},
    {'_id': 21, 'name': 'LG Gram', 'price': 119.999, 'country': 'South Korea', 'stock': 3, 'continent': 'Asia'},
    {'_id': 22, 'name': 'Sony Vaio', 'price': 67.999, 'country': 'Japan', 'stock': 5, 'continent': 'Asia'},
    {'_id': 23, 'name': 'Apple MacBook Air', 'price': 129.999, 'country': 'USA', 'stock': 6, 'continent': 'North America'},
    {'_id': 24, 'name': 'Google Pixelbook', 'price': 99.999, 'country': 'USA', 'stock': 2, 'continent': 'North America'},
    {'_id': 25, 'name': 'Dell Inspiron', 'price': 53.999, 'country': 'USA', 'stock': 11, 'continent': 'North America'},
    {'_id': 26, 'name': 'Samsung Notebook 9', 'price': 79.999, 'country': 'South Korea', 'stock': 7, 'continent': 'Asia'},
    {'_id': 27, 'name': 'Razer Blade Stealth', 'price': 119.999, 'country': 'USA', 'stock': 4, 'continent': 'North America'}
]

result = collection.insert_many(product_list)
print(result)
print(result.acknowledged)      # Eğer bu işlem başarılı bir şekilde gerçekleştiyse True, Başarılı bir şekilde gerçekleşmediyse False döner.

# insert_many() -->  MongoDB'ye birden fazla belge eklemek için kullanılır, eklenecek belgelerin bir liste içinde belirtilmesi gerekir.Listelerin içini ise set olarak oluşturmak zorundayız.
# insert_one() -->   MongoDB'ye sadece tek bir belge eklemek için kullanılır.

#endregion




# region Kayıtları Ekrana Getirme
veriler = collection.find()

for item in veriler:
    print(item)

#endregion




# region Fiyatı 50.000'den büyük olan ürünleri Listeleme.

my_filter = {
    'price': {'$gt': 50.000}
}

veriler = collection.find(my_filter)

for item in veriler:
    print(item)


# $lt: Küçüktür (less than)
# $gt: Büyüktür (greater than)
# $lte: Küçük eşittir (less than or equal to)
# $gte: Büyük eşittir (greater than or equal to)
# $eq: Eşittir (equal to)
# $ne: Eşit değildir (not equal to)
# $in: Belirtilen değerler kümesinde bulunur (in array) - $in operatörünü kullanırken değerler listesini [ ] içinde belirtiriz.$in operatöründe belirtilen değerlerden herhangi birini sağlaması yeterlidir.
# $nin: Belirtilen değerler kümesinde bulunmaz (not in array)
# $and:  iki veya daha fazla koşulu aynı anda sağlaması gereken belgeleri bulmak için kullanılır..

# endregion




# region Fiyatı 80.000'e eşit ve daha az olan ürünleri Listeleme

my_filter = {
    'price': {
        '$lte': 80.000
    }
}
veriler = collection.find(my_filter)

for item in veriler:
    print(item)

# endregion




# region Fiyatı 20.000 ile 100.000 Arasında Olan Ürünler Listeleme.

queery = {'$and': [{'price': {'$gte': 20.000}}, {'price': {'$lte': 100.000}}]}

for item in collection.find(queery):
    print(item)
# endregion




# region Ürün İsminde  "Monster" Geçen ve Fiyatı 50.000'den Büyük olan Ürünleri Listeleme (regex formülü)

queery = {
    '$and': [
        {'price': {'$gt': 50.000}},
        {'name': {'$regex': 'Monster', '$options': 'i'}}
    ]
}
for item in collection.find(queery):
    print(item)

# '$options': 'i' ifadesi, regex ifadesinin büyük-küçük harf duyarlılığını devre dışı bırakır.


# "Monster" geçmeyen belgeleri bulmak için sorgu ;
my_query = {
    '$and': [
        {'price': {'$lt': 50.000}},
        {'name': {'$not': {'$regex': 'Monster', '$options': 'i'}}}
    ]
}
# endregion




# region Fiyatı 20.000 ile 100.000 arasında olan Monster ürünlerini fiyatlar artan olarak listele.

filter = {
    '$and': [{'price': {'$gte': 20.000}}, {'price': {'$lte': 100.000}}, {'name': {'$regex': 'monster', '$options': 'i'}}]
}

for item in collection.find(filter).sort('price', 1):
    print(item)
# endregion




# region Fiyatı 33.999, 64.999, 50.000 olan ürünlerin listele
        # $in Operatörü: $in, bir alanın belirtilen bir dizi değerden herhangi birine eşit olup olmadığını kontrol eder

query = {'price': {'$in': [33.999, 64.999, 50.000]}}
for item in collection.find(query):
    print(item)
# endregion




# region Fiyatı 33.999, 64.999, 50.000 olan Monster Alba'nın ürünlerini listele
query = {'$and': [{'price': {'$in': [33.999, 64.999, 50.000]}}, {'name': {'$regex': 'Alba', '$options': 'i'}}]}

for item in collection.find(query):
    print(item)
# endregion




# region Price alanı boş olan, string olan ve None olan değerleri bulma.

filters = {'price': ''}
querys = {'price': None}
my_filters = {'price': {"$exists": False}}

for filter in collection.find(filters):
    print(filter)

for query in collection.find(querys):
    print(query)

for my_filter in collection.find(my_filters):
    print(my_filter)

# Mevcut olmayan alanları bulma ==> {"price": {"$exists": False}}
# Boş string değerleri bulma ==> {"price": ""}
# None değerleri bulma ==> {"price": None}
# endregion




# region Update

# Path 1
result = collection.update_one(
    filter={'name': {'$regex': 'Monster'}},
    update={
        '$set': {
            'name': 'Del Vega',
            'price': 69.000
        }
    }
)
print(f'{result.modified_count} adet kayıt güncellendi')

#  $set operatörü, MongoDB'de belgelerdeki belirli alanları güncellemek veya yeni alanlar eklemek için kullanılır. updateOne, updateMany veya findOneAndUpdate gibi yöntemlerle birlikte kullanılır.

# Path 2
filter = {'name': {'$regex': 'Monster', '$options': 'i'}}
set_value = {'$set': {'name': 'Apple', 'price': 99.999}}
collection.update_one(filter, set_value)

# Not ==>  Sadece 'name': 'Del Vega' yapılsaydı name değişir, price aynı kalıcaktı.
# update_one şartı sağlayan ilk ürünü günceller, update_many ise tüm monster olanları günceller.
# endregion




# region İsminde Apple Geçenlerin Fiyatını %10 arttır. Artışını Güncelleme

collection.update_many(
    {"name": {"$regex": "Apple", "$options": "i"}},
    {"$mul": {"price": 1.10}}
)

# $mul --> MongoDB'de bir güncelleme operatörüdür ve bir sayısal alanın mevcut değerini belirtilen bir sayı ile çarpmak için kullanılır.

# endregion




# region Tüm Ürünlerin Fiyatını Azaltma:
collection.update_many(
    {},
    {"$mul": {"price": 0.95}}
)
# endregion




# region Ürünleri Artan Fiyata Göre Sıralama
for item in collection.find().sort("price", 1):
    print(item)

# endregion




# region Ürünleri İsimlerine Göre(Z-A) Sıralama
for item in collection.find().sort("name", -1):
    print(item)
# endregion




# region Fiyat Alanı sayısal olmayan (int ve float) tüm alanları Listeleyelim.
query = {'price': {'$not': {'$type': ['int', 'double']}}}               # int ve float (double) olmayanlar

for item in collection.find(query):
    print(item)
# endregion




# region İsim alanı string olmayan tüm belgeleri bulalım.

query = {'name': {'$not': {'$type': 'string'}}}

for item in collection.find(query):
    print(item)
# endregion





# region Ürün Sayısını Hesaplama
print(collection.count_documents({}))
# endregion





# region Kaç Adet Monster Bulunmaktadır.
query = {'name': {'$regex': 'monster', '$options': 'i'}}
print(collection.count_documents(query))
# endregion




# region Fiyatı ??? eşit olanları olanları listeleyelim.Ayrıca Sadece isim bilgisi ve fiyat değeri ile ekrana gelsin.

query = {'price': {'$eq': '???'}}

for item in collection.find(query, {'name': 1, 'price': 1, '_id': 0}):
    print(item)
# endregion




# region Price Alanı Boş olan ürünlerin Değerini 1 olarak güncelle
result = collection.update_many(
    filter={'price': {'$exists': False}},          # 'price' alanı olmayanları filtrele
    update={
        '$set': {
            'price': 1
        }
    }
)
# endregion




# region Fiyatların Toplamını Bulma ($sum)
pipeline = [
    {"$match": {"price": {"$type": ["int", "double"]}}},
    {"$group": {"_id": None, "toplam_fiyat": {"$sum": "$price"}}}
]

result = collection.aggregate(pipeline)
for r in result:
    print(f"Toplam Fiyat: {r['toplam_fiyat']}")
# endregion




# region Fiyatların Ortalamasını Bulma ($avg)
pipeline = [
    {"$group": {"_id": None, "ortalama_fiyat": {"$avg": "$price"}}}
]

result = collection.aggregate(pipeline)
for r in result:
    print(f"Ortalama Fiyat: {r['ortalama_fiyat']}")

# endregion

# region  Fiyatların ortalamasını ve Toplamını Bulma

pipeline = [
    {'$match': {'price': {'$type': ['int', 'double']}}},
    {'$group': {'_id': None, 'Ortamala Fiyat Bilgisi': {'$avg': '$price'}, 'Toplam Fiyat': {'$sum': '$price'}}},

]

result = collection.aggregate(pipeline)
for item in result:
    pprint(item)
# endregion




# region İsimlerinde "Monster" Geçen Ürünlerin Fiyatlarını Toplama

pipeline = [
    {'$match': {'name': {'$regex': 'monster', '$options': 'i'},                 # "Monster" kelimesini içeren ürünleri bul
                'price': {'$type': ['int', 'double']}}},
    {'$group': {'_id': None, 'Toplam Fiyat': {'$sum': '$price'}, 'Ortalama Fiyat': {'$avg': '$price'}
                }}
]

result = collection.aggregate(pipeline)

for item in result:
    print(item)
    print(f"Toplam Fiyat (Monster Ürünler): {item['Toplam Fiyat']}")
    print(f"Ortalama Fiyat (Monster Ürünler): {item['Ortalama Fiyat']}")
# endregion




# region Şehirlere göre toplam stok miktarlarını bulma
pipeline = [
    {'$match': {'stock': {'$type': 'int'}}},
    {'$group': {
        '_id': '$country',
        'Toplam Stok': {'$sum': '$stock'}
    }}
]

result = collection.aggregate(pipeline)
for item in result:
    print(item)
# endregion




# region USA göre toplam stok miktarlarını bulma
pipeline = [
    {'$match': {
        'stock': {'$type': 'int'},
        'country': {'$eq': 'USA'}
    }},
    {'$group': {
        '_id': '$country',
        'Toplam Stok': {'$sum': '$stock'}
    }}
]

result = collection.aggregate(pipeline)
for item in result:
    print(item)
# endregion




# region Stokları olmayan ürünlere statülerini ekle
query = {'stock': {'$eq': 0}}
update = {'$set': {'status': 'PASSIVE'}}

result = collection.update_many(query, update)
print(result.modified_count)
# endregion




# region Stokları olan ürünlere statülerini ekleyelim.

query = {'stock': {'$gte': 1}}
update = {'$set': {'status': 'ACTIVE'}}

result = collection.update_many(query, update)
print(result.modified_count)
# endregion