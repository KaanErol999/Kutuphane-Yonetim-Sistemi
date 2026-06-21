# Kütüphane Yönetim Sistemi - İş Yeri Uygulaması (IYU 228) Projesi

## Projenin Genel Özeti
Bu proje, Ostim Teknik Üniversitesi İş Yeri Uygulaması Dersi (IYU 228) Faz-2 ve Faz-3 gereksinimleri doğrultusunda geliştirilmiş ilişkisel tabanlı bir **Kütüphane Yönetim Sistemi** uygulamasıdır. Proje; kitap, üye ve ödünç alma kayıtlarının eklenmesi, listelenmesi, güncellenmesi ve silinmesi (CRUD) süreçlerini komut satırı arayüzü (CLI) üzerinden dinamik bir şekilde yönetir. Verilerin tamamı ilişkisel model prensiplerine uygun olarak bir SQL veritabanında (SQLite) tutulmaktadır.

## Çalıştırma Talimatları ve Bağımlılıklar
- **Gerekli Bağımlılıklar:** Proje, Python dilinin dahili standart kütüphanesi olan `sqlite3` modülü ile geliştirilmiştir. Herhangi bir harici kütüphane kurulumuna (`pip install`) ihtiyaç duymaz. Bilgisayarınızda Python 3.x sürümünün kurulu olması çalışması için yeterlidir.
- **Çalıştırma Adımları:**
  1. Bu repodaki dosyaları bilgisayarınıza indirin veya klonlayın.
  2. Terminal (Komut İstemi) uygulamasını açarak proje klasörünün dizinine geçiş yapın.
  3. `python main.py` komutunu çalıştırarak sistemi başlatın.
  4. Açılan etkileşimli CLI menüsü üzerinden tüm fonksiyonları test edebilir, dilerseniz "6" numaralı seçeneği seçerek otomatik entegrasyon test senaryolarını izleyebilirsiniz.

## Proje Süreci ve İzlenen Adımlar
1. **Veritabanı Modelleme:** Projenin başında ilk olarak ilişkisel veritabanı mimarisi kurgulanmış; `Books`, `Members` ve `Loans` tabloları arasındaki mantıksal bağlar (Foreign Key) belirlenerek `database.sql` dosyası oluşturulmuştur.
2. **Backend ve CRUD Entegrasyonu:** Python üzerinde `sqlite3` bağlantı motoru kurularak SQL scriptlerinin otomatik çalıştırılması ve veri manipülasyon fonksiyonları kodlanmıştır.
3. **Kullanıcı Arayüzü ve Test Senaryoları:** Kullanıcının sistemle etkileşime girmesini sağlayan CLI menüsü ve hocanın yönergelerinde belirttiği sistem işlevsellik test durumları (test cases) entegre edilmiştir.
4. **Sürüm Kontrolü:** Projenin her aşaması Git aracı ile yerelde izlenmiş ve anlamlı commit geçmişi oluşturularak GitHub'a push edilmiştir.

## Proje Sürecinde Zorlanılan Kısımlar
Proje sürecinde beni en çok zorlayan kısım, ilişkisel bütünlüğün korunması aşaması olmuştur. Bir üye kitap ödünç aldığında hem `Loans` tablosuna yeni bir kayıt atılması hem de `Books` tablosundaki ilgili kitabın `is_available` (müsaitlik) bayrağının eş zamanlı olarak `0` yapılması gerekiyordu. Bu iki işlemi veri tabanında eşzamanlı, güvenli ve tutarlı bir mantık örgüsüyle işletmek ve SQL yabancı anahtar (Foreign Key) kısıtlamalarını SQLite üzerinde aktif kılmak algoritma tasarımı açısından öğretici bir zorluk oluşturmuştur.

## Proje Sonunda Edinilen Kazanımlar
Bu çalışma sayesinde okulda teorik olarak gördüğüm ilişkisel veritabanı (SQL) mimarisini, popüler bir programlama dili olan Python ile canlı bir senaryoda birleştirmeyi pratik ettim. Yazılım yaşam döngüsünde dökümantasyonun (`README`) ve sürüm kontrol sistemlerinin (`Git/GitHub`) önemini, düzenli commit atmanın projeyi nasıl izlenebilir kıldığını yaşayarak deneyimledim.

## Seçilen Teknolojilerin Projedeki Rolü
- **Python:** Projenin ana omurgasını oluşturur. İş mantığını (business logic) yönetir, kullanıcıdan girdileri alır ve veri tabanına parametrik güvenli istekler gönderir.
- **SQL (SQLite):** Kütüphanedeki verilerin yapılandırılmış, tutarlı ve ilişkisel bir modelde kalıcı olarak saklanmasını sağlar.
- **GitHub:** Projenin versiyon geçmişini korur, geliştirme aşamalarını şeffaf bir şekilde belgeler ve kodun bulut üzerinde güvenle teslim edilmesine zemin hazırlar.
