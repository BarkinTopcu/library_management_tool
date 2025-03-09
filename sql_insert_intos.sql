Select * FROM user;

INSERT INTO user(first_name,last_name,phone_number,email,membership_type,user_password)
VALUES
("Ali","Kara","99999999999","alikaradeneme@gmail.com","Normal","password123");

Select * FROM staff;
INSERT INTO staff(staff_name,staff_last_name,staff_email,staff_password)
VALUES
("Barkin","Topcu","barkinmail","admin123");

-- Authors
INSERT INTO author (author_name, author_last_name) VALUES
('Jane', 'Austen'),
('Stephen', 'King'),
('J.R.R.', 'Tolkien'),
('Paul', 'Theroux'),
('Edgar', 'Poe'),
('Yuval', 'Harari'),
('Isaac', 'Asimov'),
('Jules', 'Verne'),
('Mary', 'Shelley'),
('H.G.', 'Wells'),
('George', 'Orwell'),
('Mark', 'Twain'),
('Arthur', 'Doyle'),
('Bram', 'Stoker'),
('Leo', 'Tolstoy'),
('Homer', ''),
('Ernest', 'Hemingway'),
('Agatha', 'Christie'),
('Dan', 'Brown'),
('Gabriel', 'Marquez');

-- Books
INSERT INTO book (title, author_ID, year, category) VALUES
-- Romance
('Pride and Prejudice', 1, 1813, 'Romance'),
('Sense and Sensibility', 1, 1811, 'Romance'),
('Emma', 1, 1815, 'Romance'),

-- Horror
('The Shining', 2, 1977, 'Horror'),
('It', 2, 1986, 'Horror'),
('Carrie', 2, 1974, 'Horror'),
('Dracula', 14, 1897, 'Horror'),
('Frankenstein', 9, 1818, 'Horror'),

-- Fantasy
('The Hobbit', 3, 1937, 'Fantasy'),
('The Lord of the Rings', 3, 1954, 'Fantasy'),
('Harry Potter and the Sorcerer''s Stone', 3, 1997, 'Fantasy'),

-- Travel
('The Great Railway Bazaar', 4, 1975, 'Travel'),
('Dark Star Safari', 4, 2002, 'Travel'),

-- Short Story
('The Tell-Tale Heart', 5, 1843, 'Short Story'),
('The Black Cat', 5, 1843, 'Short Story'),
('The Lottery', 5, 1948, 'Short Story'),

-- History
('Sapiens', 6, 2011, 'History'),
('Homo Deus', 6, 2016, 'History'),
('Guns, Germs, and Steel', 6, 1997, 'History'),

-- Science Fiction
('Foundation', 7, 1951, 'Science Fiction'),
('I, Robot', 7, 1950, 'Science Fiction'),
('The War of the Worlds', 10, 1898, 'Science Fiction'),
('1984', 11, 1949, 'Science Fiction'),
('Brave New World', 11, 1932, 'Science Fiction'),

-- Adventure
('Around the World in 80 Days', 8, 1873, 'Adventure'),
('Twenty Thousand Leagues Under the Sea', 8, 1870, 'Adventure'),
('The Odyssey', 16, -700, 'Adventure'),
('The Old Man and the Sea', 17, 1952, 'Adventure'),
('Treasure Island', 18, 1883, 'Adventure');
