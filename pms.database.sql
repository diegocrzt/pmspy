DROP TABLE IF EXISTS usuario CASCADE;
DROP TABLE IF EXISTS proyecto CASCADE;
DROP TABLE IF EXISTS fase CASCADE;
DROP TABLE IF EXISTS tipoitem CASCADE; --relaciona atributo
DROP TABLE IF EXISTS atributo CASCADE; --relaciona valordate, valorbool, valorint, valorstr
DROP TABLE IF EXISTS vitem CASCADE; --relaciona valordate, valorbool, valorint, valorstr
DROP TABLE IF EXISTS item CASCADE;
DROP TABLE IF EXISTS valorbool, valordate, valorint, valorstr CASCADE;

-- Table: usuario

-- DROP TABLE usuario;

CREATE TABLE usuario
(
  id serial NOT NULL,
  nombre character varying(20),
  nombredeusuario character varying(20),
  clave character varying(41),
  "isAdmin" boolean,
  CONSTRAINT usuario_pkey PRIMARY KEY (id ),
  CONSTRAINT usuario_nombredeusuario_key UNIQUE (nombredeusuario )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE usuario
  OWNER TO postgres;

-- Table: proyecto

-- DROP TABLE proyecto;

CREATE TABLE proyecto
(
  id serial NOT NULL,
  nombre character varying(20),
  "cantFase" integer,
  "fechaInicio" timestamp without time zone,
  "fechaFin" timestamp without time zone,
  "fechaUltMod" timestamp without time zone,
  delider integer,
  estado character varying(10),
  CONSTRAINT proyecto_pkey PRIMARY KEY (id ),
  CONSTRAINT proyecto_delider_fkey FOREIGN KEY (delider)
      REFERENCES usuario (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT proyecto_nombre_key UNIQUE (nombre )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE proyecto
  OWNER TO postgres;

-- Table: fase

-- DROP TABLE fase;

CREATE TABLE fase
(
  id serial NOT NULL,
  nombre character varying(20),
  numero integer,
  "fechaInicio" timestamp without time zone,
  "fechaFin" timestamp without time zone,
  "fechaUltMod" timestamp without time zone,
  estado character varying(10),
  delproyecto integer,
  CONSTRAINT fase_pkey PRIMARY KEY (id ),
  CONSTRAINT fase_delproyecto_fkey FOREIGN KEY (delproyecto)
      REFERENCES proyecto (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE fase
  OWNER TO postgres;

-- Table: tipoitem

-- DROP TABLE tipoitem;

CREATE TABLE tipoitem
(
  id serial NOT NULL,
  nombre character varying(20),
  comentario character varying(100),
  defase integer,
  CONSTRAINT tipoitem_pkey PRIMARY KEY (id ),
  CONSTRAINT tipoitem_defase_fkey FOREIGN KEY (defase)
      REFERENCES fase (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipoitem
  OWNER TO postgres;

-- Table: item

-- DROP TABLE item;

CREATE TABLE item
(
  id serial NOT NULL,
  tipo integer,
  etiqueta character varying(60),
  CONSTRAINT item_pkey PRIMARY KEY (id ),
  CONSTRAINT item_tipo_fkey FOREIGN KEY (tipo)
      REFERENCES tipoitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT item_etiqueta_key UNIQUE (etiqueta )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE item
  OWNER TO postgres;

-- Table: vitem

-- DROP TABLE vitem;

CREATE TABLE vitem
(
  id serial NOT NULL,
  version integer,
  nombre character varying(20),
  estado character varying(20),
  actual boolean,
  costo integer,
  dificultad integer,
  deitem integer,
  CONSTRAINT vitem_pkey PRIMARY KEY (id ),
  CONSTRAINT vitem_deitem_fkey FOREIGN KEY (deitem)
      REFERENCES item (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE vitem
  OWNER TO postgres;

-- Table: atributo

-- DROP TABLE atributo;

CREATE TABLE atributo
(
  id serial NOT NULL,
  nombre character varying(20),
  "tipoDato" character varying(20),
  pertenece integer,
  CONSTRAINT atributo_pkey PRIMARY KEY (id ),
  CONSTRAINT atributo_pertenece_fkey FOREIGN KEY (pertenece)
      REFERENCES tipoitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE atributo
  OWNER TO postgres;

-- Table: valorbool

-- DROP TABLE valorbool;

CREATE TABLE valorbool
(
  atributo_id integer NOT NULL,
  item_id integer NOT NULL,
  valor boolean,
  CONSTRAINT valorbool_pkey PRIMARY KEY (atributo_id , item_id ),
  CONSTRAINT valorbool_atributo_id_fkey FOREIGN KEY (atributo_id)
      REFERENCES atributo (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT valorbool_item_id_fkey FOREIGN KEY (item_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE valorbool
  OWNER TO postgres;

-- Table: valordate

-- DROP TABLE valordate;

CREATE TABLE valordate
(
  atributo_id integer NOT NULL,
  item_id integer NOT NULL,
  valor timestamp without time zone,
  CONSTRAINT valordate_pkey PRIMARY KEY (atributo_id , item_id ),
  CONSTRAINT valordate_atributo_id_fkey FOREIGN KEY (atributo_id)
      REFERENCES atributo (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT valordate_item_id_fkey FOREIGN KEY (item_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE valordate
  OWNER TO postgres;

-- Table: valorint

-- DROP TABLE valorint;

CREATE TABLE valorint
(
  atributo_id integer NOT NULL,
  item_id integer NOT NULL,
  valor real,
  CONSTRAINT valorint_pkey PRIMARY KEY (atributo_id , item_id ),
  CONSTRAINT valorint_atributo_id_fkey FOREIGN KEY (atributo_id)
      REFERENCES atributo (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT valorint_item_id_fkey FOREIGN KEY (item_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE valorint
  OWNER TO postgres;

-- Table: valorstr

-- DROP TABLE valorstr;

CREATE TABLE valorstr
(
  atributo_id integer NOT NULL,
  item_id integer NOT NULL,
  valor character varying(200),
  CONSTRAINT valorstr_pkey PRIMARY KEY (atributo_id , item_id ),
  CONSTRAINT valorstr_atributo_id_fkey FOREIGN KEY (atributo_id)
      REFERENCES atributo (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT valorstr_item_id_fkey FOREIGN KEY (item_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE valorstr
  OWNER TO postgres;

INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
VALUES ('Administrador','admin','7c4a8d09ca3762af61e59520943dc26494f8941b','true')