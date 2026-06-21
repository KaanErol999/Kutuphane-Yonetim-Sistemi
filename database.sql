-- Kütüphane Yönetim Sistemi Veritabanı Şeması (database.sql)

-- 1. Üyeler Tablosu (Members)
CREATE TABLE IF NOT EXISTS Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    join_date DATE DEFAULT CURRENT_DATE
);

-- 2. Kitaplar Tablosu (Books)
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    is_available BOOLEAN DEFAULT 1
);

-- 3. Ödünç Alma Tablosu (Loans) - İlişkisel ve Yabancı Anahtarlı (Foreign Keys)
CREATE TABLE IF NOT EXISTS Loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    loan_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Örnek Verilerin Eklenmesi (INSERT INTO)
INSERT INTO Members (first_name, last_name, email) VALUES 
('Ali', 'Yılmaz', 'ali.yilmaz@email.com'),
('Ayşe', 'Kaya', 'ayse.kaya@email.com'),
('Mehmet', 'Demir', 'mehmet.demir@email.com');

INSERT INTO Books (title, author, is_available) VALUES 
('Suç ve Ceza', 'Fyodor Dostoyevski', 1),
('1984', 'George Orwell', 1),
('Simyacı', 'Paulo Coelho', 1),
('Nutuk', 'Mustafa Kemal Atatürk', 1);
