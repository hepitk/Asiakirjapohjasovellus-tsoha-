CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE phrases (id SERIAL PRIMARY KEY, phrase TEXT, document_id INTEGER REFERENCES documents);
CREATE TABLE documents (id SERIAL PRIMARY KEY, docuname TEXT);