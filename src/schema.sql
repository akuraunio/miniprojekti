CREATE TABLE citations (
  id SERIAL PRIMARY KEY, 
  title TEXT NOT NULL,
  authors TEXT,
  year INT,
  isbn TEXT,
  publisher TEXT,
  type TEXT
)