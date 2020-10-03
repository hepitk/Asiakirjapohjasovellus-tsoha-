CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE phrases (id SERIAL PRIMARY KEY, phrase TEXT);
CREATE TABLE documents (id SERIAL PRIMARY KEY, docuname TEXT);
CREATE TABLE phrases_in_documents (phrase_id INTEGER REFERENCES phrases, document_id INTEGER REFERENCES documents, PRIMARY KEY (phrase_id, document_id));