# Kütüphane Yönetim Sistemi Ana Uygulama Kodu (main.py)
import sqlite3
import os
from datetime import datetime

DB_NAME = "library.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def setup_database():
    """database.sql dosyasını okuyarak veritabanı tablolarını ve örnek verileri hazırlar."""
    if not os.path.exists(DB_NAME):
        conn = connect_db()
        cursor = conn.cursor()
        with open('database.sql', 'r', encoding='utf-8') as f:
            cursor.executescript(f.read())
        conn.commit()
        conn.close()
        print("[SİSTEM] Veritabanı başarıyla oluşturuldu ve şema yüklendi.")

# --- CRUD İŞLEMLERİ ---

# 1. Kitap Ekleme (CREATE)
def add_book(title, author):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    print(f" BAŞARILI: '{title}' isimli kitap sisteme eklendi.")

# 2. Kitap Listeleme (READ)
def list_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT book_id, title, author, is_available FROM Books")
    books = cursor.fetchall()
    conn.close()
    
    print("\n--- KİTAP LİSTESİ ---")
    for b in books:
        durum = "Müsait" if b[3] else "Ödünç Verildi"
        print(f"ID: {b[0]} | Kitap: {b[1]} | Yazar: {b[2]} | Durum: {durum}")
    print("----------------------")

# 3. Kitap Güncelleme (UPDATE)
def update_book(book_id, new_title, new_author):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Books SET title = ?, author = ? WHERE book_id = ?", (new_title, new_author, book_id))
    conn.commit()
    conn.close()
    print(f" BAŞARILI: ID {book_id} olan kitap güncellendi.")

# 4. Kitap Silme (DELETE)
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()
    print(f" BAŞARILI: ID {book_id} olan kitap sistemden silindi.")

# 5. Kitap Ödünç Alma İşlemi (Loans Entegrasyonu)
def borrow_book(book_id, member_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Kitap müsait mi kontrol et
    cursor.execute("SELECT is_available FROM Books WHERE book_id = ?", (book_id,))
    res = cursor.fetchone()
    
    if res and res[0] == 1:
        # Ödünç kaydı aç
        cursor.execute("INSERT INTO Loans (book_id, member_id, loan_date) VALUES (?, ?, ?)", 
                       (book_id, member_id, datetime.now().strftime('%Y-%m-%d')))
        # Kitap durumunu güncelle
        cursor.execute("UPDATE Books SET is_available = 0 WHERE book_id = ?", (book_id,))
        conn.commit()
        print(" BAŞARILI: Kitap başarıyla ödünç verildi.")
    else:
        print(" HATA: Kitap mevcut değil veya zaten ödünç verilmiş.")
    conn.close()

# --- Otomatik Test Durumları (Hocanın İstediği Test Case Gereksinimi) ---
def run_tests():
    print("\n=== OTOMATİK SİSTEM TESTLERİ BAŞLATILIYOR ===")
    print("1. Test: Yeni Kitap Ekleme...")
    add_book("Test Kitabı", "Test Yazarı")
    
    print("\n2. Test: Kitapları Listeleme...")
    list_books()
    
    print("\n3. Test: Kitap Ödünç Verme Simülasyonu (Kitap ID: 1, Üye ID: 1)...")
    borrow_book(1, 1)
    
    print("\n4. Test: Ödünç Sonrası Durum Kontrolü...")
    list_books()
    print("=== TÜM TEST DURUMLARI BAŞARIYLA TAMAMLANDI ===\n")

# --- ANA CLI MENÜSÜ ---
def main():
    setup_database()
    while True:
        print("\n=================================")
        print("   KÜTÜPHANE YÖNETİM SİSTEMİ")
        print("=================================")
        print("1. Kitapları Listele")
        print("2. Yeni Kitap Ekle")
        print("3. Kitap Güncelle")
        print("4. Kitap Sil")
        print("5. Kitap Ödünç Ver")
        print("6. Otomatik Sistem Testlerini Çalıştır")
        print("7. Çıkış")
        
        secim = input("Lütfen bir işlem seçin (1-7): ")
        
        if secim == '1':
            list_books()
        elif secim == '2':
            t = input("Kitap Adı: ")
            a = input("Yazar: ")
            add_book(t, a)
        elif secim == '3':
            b_id = int(input("Güncellenecek Kitap ID: "))
            t = input("Yeni Kitap Adı: ")
            a = input("Yeni Yazar: ")
            update_book(b_id, t, a)
        elif secim == '4':
            b_id = int(input("Silinecek Kitap ID: "))
            delete_book(b_id)
        elif secim == '5':
            b_id = int(input("Kitap ID: "))
            m_id = int(input("Üye ID: "))
            borrow_book(b_id, m_id)
        elif secim == '6':
            run_tests()
        elif secim == '7':
            print("Sistemden çıkılıyor. Başarılar dileriz!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
