
--------------------------------------------------------------------------------------------
----            Populate the basebase to run the test class                             ----
--------------------------------------------------------------------------------------------   

CREATE TABLE person
(
  id integer NOT NULL,
  name character varying(200) NOT NULL,
  birth_date date,
  CONSTRAINT pk PRIMARY KEY (id, name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE person
  OWNER TO postgres;


INSERT INTO person(id, name, birth_date) VALUES (1, 'João', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (2, 'José', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (3, 'Maria', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (4, 'Paulo', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (5, 'Beth', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (6, 'Pedro', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (7, 'Clark Kent', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (8, 'Vitoria', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (9, 'Beto', '01/01/1990');
INSERT INTO person(id, name, birth_date) VALUES (10, 'Ana', '01/01/1990');
