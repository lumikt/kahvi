DROP TABLE IF EXISTS reference CASCADE;
DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS ref_authors CASCADE;

CREATE TABLE reference (id SERIAL PRIMARY KEY,
                         address TEXT,
                         annote TEXT,
                         author TEXT[],
                         booktitle TEXT,
                         chapter INTEGER,
                         crossfer TEXT,
                         doi TEXT,
                         edition TEXT,
                         editor TEXT,
                         email TEXT,
                         howpublished TEXT,
                         institution TEXT,
                         journal TEXT,
                         month TEXT,
                         note TEXT,
                         number INTEGER,
                         organization TEXT,
                         pages TEXT,
                         publisher TEXT,
                         ref_type TEXT,
                         school TEXT,
                         series TEXT,
                         title TEXT,
                         type TEXT,
                         volume INTEGER,
                         year INTEGER);

CREATE TABLE authors (id SERIAL PRIMARY KEY,
                      name TEXT);

CREATE TABLE ref_authors (ref_id INTEGER REFERENCES reference,
                          author_id INTEGER REFERENCES authors);

                         