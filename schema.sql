-- Drop existing tables if they exist
DROP TABLE IF EXISTS article CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS inproceedings CASCADE;
DROP TABLE IF EXISTS reference CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS ref_tags CASCADE;

-- Create the reference table
CREATE TABLE reference (
    id SERIAL PRIMARY KEY,
    citation_key TEXT UNIQUE NOT NULL,
    type TEXT NOT NULL
);

-- Create the article table
CREATE TABLE article (
    id SERIAL PRIMARY KEY,
    citation_key TEXT NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    journal TEXT NOT NULL,
    year INT NOT NULL,
    volume TEXT,
    number TEXT,
    pages TEXT,
    month TEXT,
    note TEXT,
    doi TEXT,
    issn TEXT,
    zblnumber TEXT,
    eprint TEXT,
    CONSTRAINT fk_reference
        FOREIGN KEY (citation_key)
        REFERENCES reference (citation_key)
        ON DELETE CASCADE
);
-- Create the book table
CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    citation_key TEXT NOT NULL,
    author TEXT NOT NULL,
    editor TEXT,
    title TEXT NOT NULL,
    publisher TEXT NOT NULL,
    year INT NOT NULL,
    volume TEXT,
    number TEXT,
    pages TEXT,
    month TEXT,
    note TEXT,
    doi TEXT,
    issn TEXT,
    isbn TEXT,
    CONSTRAINT fk_reference 
        FOREIGN KEY (citation_key)
        REFERENCES reference (citation_key)
        ON DELETE CASCADE
);

-- Create the inproceedings table
CREATE TABLE inproceedings (
    id SERIAL PRIMARY KEY,
    citation_key TEXT NOT NULL,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    booktitle TEXT NOT NULL,
    year INT NOT NULL,
    editor TEXT,
    volume TEXT,
    number TEXT,
    series TEXT,
    pages TEXT,
    address TEXT,
    month TEXT,
    organization TEXT,
    publisher TEXT,
    CONSTRAINT fk_reference
        FOREIGN KEY (citation_key)
        REFERENCES reference (citation_key)
        ON DELETE CASCADE
);

-- Create the tags table
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the ref_tags table, which links tags to references
CREATE TABLE ref_tags (
    ref_id INTEGER REFERENCES reference,
    tag_id INTEGER REFERENCES tags
);