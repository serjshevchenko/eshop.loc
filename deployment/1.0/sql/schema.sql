CREATE SEQUENCE content_id_seq;
CREATE SEQUENCE news_id_seq;

CREATE TABLE content (
  id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('content_id_seq'),
  url VARCHAR(100) NOT NULL,
  text TEXT NOT NULL,
  CONSTRAINT url_unique UNIQUE(url)
);

CREATE TABLE news (
    id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('news_id_seq'),
    name VARCHAR (250) NOT NULL,
    text TEXT NOT NULL
);
