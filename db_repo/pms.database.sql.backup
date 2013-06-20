DROP TABLE IF EXISTS user_rol CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;
DROP TABLE IF EXISTS proyecto CASCADE;
DROP TABLE IF EXISTS rol CASCADE; -- relaciona fase
DROP TABLE IF EXISTS fase CASCADE;
DROP TABLE IF EXISTS lineabase CASCADE; -- relaciona usuario y fase
DROP TABLE IF EXISTS tipoitem CASCADE; --relaciona 
DROP TABLE IF EXISTS atributo CASCADE; --relaciona valordate, valorbool, valorint, valorstr
DROP TABLE IF EXISTS relacion CASCADE; --relaciona vitem
DROP TABLE IF EXISTS vitem CASCADE; --relaciona valordate, valorbool, valorint, valorstr
DROP TABLE IF EXISTS item CASCADE;
DROP TABLE IF EXISTS valorbool, valordate, valorint, valorstr CASCADE;
DROP TABLE IF EXISTS peticion CASCADE;
DROP TABLE IF EXISTS miembro; -- relaciona, proyecto, usuario
DROP TABLE IF EXISTS voto CASCADE; --relaciona peticion

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

-- Table: miembro

-- DROP TABLE miembro;

CREATE TABLE miembro
(
  proyecto_id integer NOT NULL,
  user_id integer NOT NULL,
  CONSTRAINT miembro_pkey PRIMARY KEY (proyecto_id , user_id ),
  CONSTRAINT miembro_proyecto_id_fkey FOREIGN KEY (proyecto_id)
      REFERENCES proyecto (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT miembro_user_id_fkey FOREIGN KEY (user_id)
      REFERENCES usuario (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE miembro
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
  
-- Table: rol

-- DROP TABLE rol;

CREATE TABLE rol
(
  id serial NOT NULL,
  fase_id integer,
  nombre character varying(30),
  "codigoTipo" integer,
  "codigoItem" integer,
  "codigoLB" integer,
  CONSTRAINT rol_pkey PRIMARY KEY (id ),
  CONSTRAINT rol_fase_id_fkey FOREIGN KEY (fase_id)
      REFERENCES fase (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE rol
  OWNER TO postgres;

-- Table: lineabase

-- DROP TABLE lineabase;

CREATE TABLE lineabase
(
  id serial NOT NULL,
  creador_id integer,
  "fechaCreacion" timestamp without time zone,
  numero integer,
  comentario character varying(100),
  fase_id integer,
  CONSTRAINT lineabase_pkey PRIMARY KEY (id ),
  CONSTRAINT lineabase_creador_id_fkey FOREIGN KEY (creador_id)
      REFERENCES usuario (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT lineabase_fase_id_fkey FOREIGN KEY (fase_id)
      REFERENCES fase (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE lineabase
  OWNER TO postgres;

-- Table: user_rol

-- DROP TABLE user_rol;

CREATE TABLE user_rol
(
  usuario_id integer NOT NULL,
  rol_id integer NOT NULL,
  CONSTRAINT user_rol_pkey PRIMARY KEY (usuario_id , rol_id ),
  CONSTRAINT user_rol_rol_id_fkey FOREIGN KEY (rol_id)
      REFERENCES rol (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT user_rol_usuario_id_fkey FOREIGN KEY (usuario_id)
      REFERENCES usuario (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE user_rol
  OWNER TO postgres;

-- Table: peticion

-- DROP TABLE peticion;

CREATE TABLE peticion
(
  id serial NOT NULL,
  proyecto_id integer,
  item_id integer,
  comentario character varying(100),
  estado character varying(10),
  usuario_id integer,
  CONSTRAINT peticion_pkey PRIMARY KEY (id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE peticion
  OWNER TO postgres;

-- Table: voto

-- DROP TABLE voto;

CREATE TABLE voto
(
  peticion_id integer NOT NULL,
  user_id integer NOT NULL,
  valor boolean,
  CONSTRAINT voto_pkey PRIMARY KEY (peticion_id , user_id ),
  CONSTRAINT voto_peticion_id_fkey FOREIGN KEY (peticion_id)
      REFERENCES peticion (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE voto
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
  linea_id integer,
  CONSTRAINT item_pkey PRIMARY KEY (id ),
  CONSTRAINT item_linea_id_fkey FOREIGN KEY (linea_id)
      REFERENCES lineabase (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
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
  
-- Table: relacion

-- DROP TABLE relacion;

CREATE TABLE relacion
(
  id serial NOT NULL,
  ante_id integer,
  post_id integer,
  tipo character varying(10),
  CONSTRAINT relacion_pkey PRIMARY KEY (id ),
  CONSTRAINT relacion_ante_id_fkey FOREIGN KEY (ante_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT relacion_post_id_fkey FOREIGN KEY (post_id)
      REFERENCES vitem (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE relacion
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
	VALUES ('Administrador','admin','7c4a8d09ca3762af61e59520943dc26494f8941b','true');
INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Martin Poletti','martin','54669547a225ff20cba8b75a4adca540eef25858','false');
INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Natalia Valdez','natalia','7c4a8d09ca3762af61e59520943dc26494f8941b','true');
INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Anna Dyst','anna','7c4a8d09ca3762af61e59520943dc26494f8941b','false');
INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Dan Tor','dan','7c4a8d09ca3762af61e59520943dc26494f8941b','false');
INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Thomas Dwin','tommy','7c4a8d09ca3762af61e59520943dc26494f8941b','false');

INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)
	VALUES ('Levithas', '3', '2013-05-20', '2014-05-20', null, 1, 'Pendiente');
INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)
	VALUES ('Reingenieria', '5', '2013-05-17', '2013-06-20', null, 3, 'Iniciado');
INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)--3
	VALUES ('Construcción', '2', '2013-05-17', '2013-06-20', null, 3, 'Iniciado');
INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)
	VALUES ('Celerity', '0', '2013-06-01', '2013-06-20', null, 1, 'Pendiente');
INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)
	VALUES ('Singularity', '0', '2013-06-01', '2013-06-20', null, 3, 'Pendiente');
INSERT INTO proyecto(nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado)
	VALUES ('Black Omen', '0', '2013-06-01', '2013-06-20', null, 1, 'Pendiente');

INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) -- Proyecto Reingeniería
	VALUES ('Análisis',1,'2013-05-17','2013-05-20',null,'Abierta',2);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Diseño Físico',2,'2013-05-21','2013-06-10',null,'Abierta',2);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Construcción',3,'2013-05-17','2013-05-10',null,'Abierta',2);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Pruebas',4,'2013-06-11','2013-06-20',null,'Abierta',2);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Implantación',5,'2013-06-11','2013-06-20',null,'Abierta',2);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) -- Proyecto Levithas
	VALUES ('Init',1,'2013-05-17','2013-05-20',null,'Abierta',1);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Dev',2,'2013-05-21','2013-06-10',null,'Abierta',1);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Dbg',3,'2013-05-17','2013-05-10',null,'Abierta',1);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) -- Proyecto Construcción
	VALUES ('Monofase',1,'2013-05-17','2013-05-10',null,'Abierta',3);
INSERT INTO fase (nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto)
	VALUES ('Bifase',2,'2013-06-17','2013-06-19',null,'Abierta',3);

INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") -- Fase Análisis
	VALUES (1, 'Desarrollador', 111, 0, 0);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") 
	VALUES (2, 'Tester', 101, 11111111, 11);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") 
	VALUES (3, 'Analista de Negocios', 0, 1000, 11);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") -- Fase Pruebas
	VALUES (4, 'Autorizante', 111, 0, 0);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") 
	VALUES (5, 'Arquitecto', 111, 11111111, 0);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") 
	VALUES (6, 'Tester', 0, 1000, 11);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") -- Fase Dev
	VALUES (7, 'Analista', 111, 0, 0);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") 
	VALUES (8, 'Desarrollador', 0, 11110111, 0);
INSERT INTO rol (fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") -- Fase Monofase
	VALUES (9, 'Full Control', 111, 11111111, 11);

INSERT INTO user_rol (usuario_id, rol_id) -- Fase Init
	VALUES (4, 1);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (5, 2);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (6, 3);
INSERT INTO user_rol (usuario_id, rol_id) -- Fase Dev
	VALUES (3, 4);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (5, 5);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (1, 6);
INSERT INTO user_rol (usuario_id, rol_id) -- Fase Dbg
	VALUES (2, 7);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (4, 8);
INSERT INTO user_rol (usuario_id, rol_id) 
	VALUES (3, 9);

INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (1, 'Libro', 'Representa un libro', 9);
INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (2, 'Lección', 'Representa una lección', 9);
INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (3, 'Capítulo', 'Representa una conclusión', 9);
INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (4, 'Relevamiento', 'Recoger datos', 1);
INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (5, 'Diseño', 'Representa una conclusión', 2);
INSERT INTO tipoitem (id, nombre, comentario, defase)
	VALUES (6, 'Aplicación', 'Representa la aplicación de conocimientos previos', 10);


INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (1,'Titulo','Cadena',1);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (2,'Autor','Cadena',1);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (3,'Leido','Booleano',2);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (4,'Leido','Booleano',3);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (5,'Entrevistado','Cadena',4);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (6,'Método Utilizado','Cadena',4);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (7,'Documento aprobado','Booleano',5);
INSERT INTO atributo(id, nombre, "tipoDato", pertenece)
	VALUES (8,'Verificable','Booleano',6);



INSERT INTO item(id, tipo, etiqueta, linea_id)
	VALUES (1, 1, 3-9-1, null);
INSERT INTO item(id, tipo, etiqueta, linea_id)
	VALUES (2, 6, 3-9-6, null);


INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (1,0,'Construcciones','Activo','false', 50, 5, 1);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (2,1,'Construcciones','Activo','false', 50, 5, 1);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (3,2,'Construcciones','Aprobado','true', 50, 5, 1);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (4,0,'Maqueta','Activo','false', 27, 9, 2);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (5,1,'Maqueta','Activo','false', 25, 10, 2);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
	VALUES (6,2,'Maqueta','Aprobado','true', 25, 10, 2);

INSERT INTO valorstr(atributo_id, item_id, valor)
	VALUES (1,1,'');
INSERT INTO valorstr(atributo_id, item_id, valor)
	VALUES (1,2,'Materiales');
INSERT Into valorstr(atributo_id, item_id, valor)
	VALUES (1,3,'Materiales');
INSERT INTO valorstr(atributo_id, item_id, valor)
	VALUES (2,1,'');
INSERT INTO valorstr(atributo_id, item_id, valor)
	VALUES (2,2,'Kurth Nixon');
INSERT Into valorstr(atributo_id, item_id, valor)
	VALUES (2,3,'Rigoberto Q. Zayas');
INSERT INTO valorbool(atributo_id, item_id, valor) -- booleano segunda fase
	VALUES (8,4,'false');
INSERT INTO valorbool(atributo_id, item_id, valor) -- booleano segunda fase
	VALUES (8,5,'false');
INSERT INTO valorbool(atributo_id, item_id, valor) -- booleano segunda fase
	VALUES (8,6,'true');
