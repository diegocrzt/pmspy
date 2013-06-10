--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.9
-- Dumped by pg_dump version 9.1.9
-- Started on 2013-05-25 09:23:31 PYT

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 190 (class 3079 OID 11647)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2056 (class 0 OID 0)
-- Dependencies: 190
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 185 (class 1259 OID 50626)
-- Dependencies: 5
-- Name: atributo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE atributo (
    id integer NOT NULL,
    nombre character varying(20),
    "tipoDato" character varying(20),
    pertenece integer
);


ALTER TABLE public.atributo OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 50624)
-- Dependencies: 185 5
-- Name: atributo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE atributo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.atributo_id_seq OWNER TO postgres;

--
-- TOC entry 2057 (class 0 OID 0)
-- Dependencies: 184
-- Name: atributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE atributo_id_seq OWNED BY atributo.id;


--
-- TOC entry 167 (class 1259 OID 50485)
-- Dependencies: 5
-- Name: fase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE fase (
    id integer NOT NULL,
    nombre character varying(20),
    numero integer,
    "fechaInicio" timestamp without time zone,
    "fechaFin" timestamp without time zone,
    "fechaUltMod" timestamp without time zone,
    estado character varying(10),
    delproyecto integer
);


ALTER TABLE public.fase OWNER TO postgres;

--
-- TOC entry 166 (class 1259 OID 50483)
-- Dependencies: 167 5
-- Name: fase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE fase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fase_id_seq OWNER TO postgres;

--
-- TOC entry 2058 (class 0 OID 0)
-- Dependencies: 166
-- Name: fase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE fase_id_seq OWNED BY fase.id;


--
-- TOC entry 179 (class 1259 OID 50575)
-- Dependencies: 5
-- Name: item; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE item (
    id integer NOT NULL,
    tipo integer,
    etiqueta character varying(60),
    linea_id integer
);


ALTER TABLE public.item OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 50573)
-- Dependencies: 5 179
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO postgres;

--
-- TOC entry 2059 (class 0 OID 0)
-- Dependencies: 178
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE item_id_seq OWNED BY item.id;


--
-- TOC entry 171 (class 1259 OID 50511)
-- Dependencies: 5
-- Name: lineabase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE lineabase (
    id integer NOT NULL,
    creador_id integer,
    "fechaCreacion" timestamp without time zone,
    numero integer,
    comentario character varying(100),
    fase_id integer
);


ALTER TABLE public.lineabase OWNER TO postgres;

--
-- TOC entry 170 (class 1259 OID 50509)
-- Dependencies: 5 171
-- Name: lineabase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE lineabase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lineabase_id_seq OWNER TO postgres;

--
-- TOC entry 2060 (class 0 OID 0)
-- Dependencies: 170
-- Name: lineabase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE lineabase_id_seq OWNED BY lineabase.id;


--
-- TOC entry 165 (class 1259 OID 50468)
-- Dependencies: 5
-- Name: miembro; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE miembro (
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.miembro OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 50544)
-- Dependencies: 5
-- Name: peticion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE peticion (
    id integer NOT NULL,
    proyecto_id integer,
    item_id integer,
    comentario character varying(100),
    estado character varying(10),
    usuario_id integer
);


ALTER TABLE public.peticion OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 50542)
-- Dependencies: 174 5
-- Name: peticion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE peticion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.peticion_id_seq OWNER TO postgres;

--
-- TOC entry 2061 (class 0 OID 0)
-- Dependencies: 173
-- Name: peticion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE peticion_id_seq OWNED BY peticion.id;


--
-- TOC entry 164 (class 1259 OID 50455)
-- Dependencies: 5
-- Name: proyecto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proyecto (
    id integer NOT NULL,
    nombre character varying(20),
    "cantFase" integer,
    "fechaInicio" timestamp without time zone,
    "fechaFin" timestamp without time zone,
    "fechaUltMod" timestamp without time zone,
    delider integer,
    estado character varying(10)
);


ALTER TABLE public.proyecto OWNER TO postgres;

--
-- TOC entry 163 (class 1259 OID 50453)
-- Dependencies: 164 5
-- Name: proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyecto_id_seq OWNER TO postgres;

--
-- TOC entry 2062 (class 0 OID 0)
-- Dependencies: 163
-- Name: proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE proyecto_id_seq OWNED BY proyecto.id;


--
-- TOC entry 183 (class 1259 OID 50608)
-- Dependencies: 5
-- Name: relacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE relacion (
    id integer NOT NULL,
    ante_id integer,
    post_id integer,
    tipo character varying(10)
);


ALTER TABLE public.relacion OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 50606)
-- Dependencies: 5 183
-- Name: relacion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE relacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relacion_id_seq OWNER TO postgres;

--
-- TOC entry 2063 (class 0 OID 0)
-- Dependencies: 182
-- Name: relacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE relacion_id_seq OWNED BY relacion.id;


--
-- TOC entry 169 (class 1259 OID 50498)
-- Dependencies: 5
-- Name: rol; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE rol (
    id integer NOT NULL,
    fase_id integer,
    nombre character varying(30),
    "codigoTipo" integer,
    "codigoItem" integer,
    "codigoLB" integer
);


ALTER TABLE public.rol OWNER TO postgres;

--
-- TOC entry 168 (class 1259 OID 50496)
-- Dependencies: 5 169
-- Name: rol_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE rol_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rol_id_seq OWNER TO postgres;

--
-- TOC entry 2064 (class 0 OID 0)
-- Dependencies: 168
-- Name: rol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE rol_id_seq OWNED BY rol.id;


--
-- TOC entry 177 (class 1259 OID 50562)
-- Dependencies: 5
-- Name: tipoitem; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tipoitem (
    id integer NOT NULL,
    nombre character varying(20),
    comentario character varying(100),
    defase integer
);


ALTER TABLE public.tipoitem OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 50560)
-- Dependencies: 5 177
-- Name: tipoitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE tipoitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipoitem_id_seq OWNER TO postgres;

--
-- TOC entry 2065 (class 0 OID 0)
-- Dependencies: 176
-- Name: tipoitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE tipoitem_id_seq OWNED BY tipoitem.id;


--
-- TOC entry 172 (class 1259 OID 50527)
-- Dependencies: 5
-- Name: user_rol; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE user_rol (
    usuario_id integer NOT NULL,
    rol_id integer NOT NULL
);


ALTER TABLE public.user_rol OWNER TO postgres;

--
-- TOC entry 162 (class 1259 OID 50445)
-- Dependencies: 5
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE usuario (
    id integer NOT NULL,
    nombre character varying(20),
    nombredeusuario character varying(20),
    clave character varying(41),
    "isAdmin" boolean
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 161 (class 1259 OID 50443)
-- Dependencies: 5 162
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuario_id_seq OWNER TO postgres;

--
-- TOC entry 2066 (class 0 OID 0)
-- Dependencies: 161
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE usuario_id_seq OWNED BY usuario.id;


--
-- TOC entry 186 (class 1259 OID 50637)
-- Dependencies: 5
-- Name: valorbool; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE valorbool (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor boolean
);


ALTER TABLE public.valorbool OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 50652)
-- Dependencies: 5
-- Name: valordate; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE valordate (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor timestamp without time zone
);


ALTER TABLE public.valordate OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 50667)
-- Dependencies: 5
-- Name: valorint; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE valorint (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor real
);


ALTER TABLE public.valorint OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 50682)
-- Dependencies: 5
-- Name: valorstr; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE valorstr (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor character varying(200)
);


ALTER TABLE public.valorstr OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 50595)
-- Dependencies: 5
-- Name: vitem; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vitem (
    id integer NOT NULL,
    version integer,
    nombre character varying(20),
    estado character varying(20),
    actual boolean,
    costo integer,
    dificultad integer,
    deitem integer
);


ALTER TABLE public.vitem OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 50593)
-- Dependencies: 181 5
-- Name: vitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE vitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vitem_id_seq OWNER TO postgres;

--
-- TOC entry 2067 (class 0 OID 0)
-- Dependencies: 180
-- Name: vitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE vitem_id_seq OWNED BY vitem.id;


--
-- TOC entry 175 (class 1259 OID 50550)
-- Dependencies: 5
-- Name: voto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE voto (
    peticion_id integer NOT NULL,
    user_id integer NOT NULL,
    valor boolean
);
<<<<<<< HEAD
=======
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
        VALUES ('Construcción', '1', '2013-05-17', '2013-06-20', null, 3, 'Iniciado');
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
>>>>>>> branch 'master' of https://syncrhonous@code.google.com/p/pmspy/


<<<<<<< HEAD
ALTER TABLE public.voto OWNER TO postgres;

--
-- TOC entry 1952 (class 2604 OID 50629)
-- Dependencies: 185 184 185
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY atributo ALTER COLUMN id SET DEFAULT nextval('atributo_id_seq'::regclass);
=======
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
>>>>>>> branch 'master' of https://syncrhonous@code.google.com/p/pmspy/


--
-- TOC entry 1944 (class 2604 OID 50488)
-- Dependencies: 167 166 167
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

<<<<<<< HEAD
ALTER TABLE ONLY fase ALTER COLUMN id SET DEFAULT nextval('fase_id_seq'::regclass);
=======
INSERT INTO item(id, tipo, etiqueta, linea_id)
        VALUES (1, 1, 3-9-1, null);
>>>>>>> branch 'master' of https://syncrhonous@code.google.com/p/pmspy/


<<<<<<< HEAD
--
-- TOC entry 1949 (class 2604 OID 50578)
-- Dependencies: 179 178 179
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item ALTER COLUMN id SET DEFAULT nextval('item_id_seq'::regclass);
=======
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
        VALUES (1,0,'Construcciones','Activo','false', 50, 5, 1);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
        VALUES (1,1,'Construcciones','Activo','false', 50, 5, 1);
INSERT INTO  vitem(id, version, nombre, estado, actual, costo, dificultad, deitem)
        VALUES (1,2,'Construcciones','Aprobado','true', 50, 5, 1);
>>>>>>> branch 'master' of https://syncrhonous@code.google.com/p/pmspy/


<<<<<<< HEAD
--
-- TOC entry 1946 (class 2604 OID 50514)
-- Dependencies: 171 170 171
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY lineabase ALTER COLUMN id SET DEFAULT nextval('lineabase_id_seq'::regclass);


--
-- TOC entry 1947 (class 2604 OID 50547)
-- Dependencies: 173 174 174
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY peticion ALTER COLUMN id SET DEFAULT nextval('peticion_id_seq'::regclass);


--
-- TOC entry 1943 (class 2604 OID 50458)
-- Dependencies: 164 163 164
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto ALTER COLUMN id SET DEFAULT nextval('proyecto_id_seq'::regclass);


--
-- TOC entry 1951 (class 2604 OID 50611)
-- Dependencies: 182 183 183
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY relacion ALTER COLUMN id SET DEFAULT nextval('relacion_id_seq'::regclass);


--
-- TOC entry 1945 (class 2604 OID 50501)
-- Dependencies: 169 168 169
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rol ALTER COLUMN id SET DEFAULT nextval('rol_id_seq'::regclass);


--
-- TOC entry 1948 (class 2604 OID 50565)
-- Dependencies: 176 177 177
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tipoitem ALTER COLUMN id SET DEFAULT nextval('tipoitem_id_seq'::regclass);


--
-- TOC entry 1942 (class 2604 OID 50448)
-- Dependencies: 161 162 162
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY usuario ALTER COLUMN id SET DEFAULT nextval('usuario_id_seq'::regclass);


--
-- TOC entry 1950 (class 2604 OID 50598)
-- Dependencies: 180 181 181
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vitem ALTER COLUMN id SET DEFAULT nextval('vitem_id_seq'::regclass);


--
-- TOC entry 2044 (class 0 OID 50626)
-- Dependencies: 185 2049
-- Data for Name: atributo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY atributo (id, nombre, "tipoDato", pertenece) FROM stdin;
1	Titulo	Cadena	1
2	Autor	Cadena	1
3	Leido	Booleano	2
4	Leido	Booleano	3
5	Entrevistado	Cadena	4
6	Método Utilizado	Cadena	4
7	Documento aprobado	Booleano	5
8	Verificable	Booleano	6
\.


--
-- TOC entry 2068 (class 0 OID 0)
-- Dependencies: 184
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('atributo_id_seq', 1, false);


--
-- TOC entry 2026 (class 0 OID 50485)
-- Dependencies: 167 2049
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
1	Análisis	1	2013-05-17 00:00:00	2013-05-20 00:00:00	\N	Abierta	2
2	Diseño Físico	2	2013-05-21 00:00:00	2013-06-10 00:00:00	\N	Abierta	2
3	Construcción	3	2013-05-17 00:00:00	2013-05-10 00:00:00	\N	Abierta	2
4	Pruebas	4	2013-06-11 00:00:00	2013-06-20 00:00:00	\N	Abierta	2
5	Implantación	5	2013-06-11 00:00:00	2013-06-20 00:00:00	\N	Abierta	2
6	Init	1	2013-05-17 00:00:00	2013-05-20 00:00:00	\N	Abierta	1
7	Dev	2	2013-05-21 00:00:00	2013-06-10 00:00:00	\N	Abierta	1
8	Dbg	3	2013-05-17 00:00:00	2013-05-10 00:00:00	\N	Abierta	1
9	Monofase	1	2013-05-17 00:00:00	2013-05-10 00:00:00	\N	Abierta	3
10	Bifase	2	2013-06-17 00:00:00	2013-06-19 00:00:00	\N	Abierta	3
\.


--
-- TOC entry 2069 (class 0 OID 0)
-- Dependencies: 166
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('fase_id_seq', 10, true);


--
-- TOC entry 2038 (class 0 OID 50575)
-- Dependencies: 179 2049
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY item (id, tipo, etiqueta, linea_id) FROM stdin;
1	1	-7	\N
2	6	-12	\N
\.


--
-- TOC entry 2070 (class 0 OID 0)
-- Dependencies: 178
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('item_id_seq', 1, true);


--
-- TOC entry 2030 (class 0 OID 50511)
-- Dependencies: 171 2049
-- Data for Name: lineabase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY lineabase (id, creador_id, "fechaCreacion", numero, comentario, fase_id) FROM stdin;
\.


--
-- TOC entry 2071 (class 0 OID 0)
-- Dependencies: 170
-- Name: lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('lineabase_id_seq', 1, false);


--
-- TOC entry 2024 (class 0 OID 50468)
-- Dependencies: 165 2049
-- Data for Name: miembro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY miembro (proyecto_id, user_id) FROM stdin;
\.


--
-- TOC entry 2033 (class 0 OID 50544)
-- Dependencies: 174 2049
-- Data for Name: peticion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY peticion (id, proyecto_id, item_id, comentario, estado, usuario_id) FROM stdin;
\.


--
-- TOC entry 2072 (class 0 OID 0)
-- Dependencies: 173
-- Name: peticion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('peticion_id_seq', 1, false);


--
-- TOC entry 2023 (class 0 OID 50455)
-- Dependencies: 164 2049
-- Data for Name: proyecto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyecto (id, nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado) FROM stdin;
1	Levithas	3	2013-05-20 00:00:00	2014-05-20 00:00:00	\N	1	Pendiente
2	Reingenieria	5	2013-05-17 00:00:00	2013-06-20 00:00:00	\N	3	Iniciado
3	Construcción	2	2013-05-17 00:00:00	2013-06-20 00:00:00	\N	3	Iniciado
4	Celerity	0	2013-06-01 00:00:00	2013-06-20 00:00:00	\N	1	Pendiente
5	Singularity	0	2013-06-01 00:00:00	2013-06-20 00:00:00	\N	3	Pendiente
6	Black Omen	0	2013-06-01 00:00:00	2013-06-20 00:00:00	\N	1	Pendiente
\.


--
-- TOC entry 2073 (class 0 OID 0)
-- Dependencies: 163
-- Name: proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyecto_id_seq', 6, true);


--
-- TOC entry 2042 (class 0 OID 50608)
-- Dependencies: 183 2049
-- Data for Name: relacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY relacion (id, ante_id, post_id, tipo) FROM stdin;
1	3	6	A-S
\.


--
-- TOC entry 2074 (class 0 OID 0)
-- Dependencies: 182
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('relacion_id_seq', 1, true);


--
-- TOC entry 2028 (class 0 OID 50498)
-- Dependencies: 169 2049
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Desarrollador	111	0	0
2	2	Tester	101	11111111	11
3	3	Analista de Negocios	0	1000	11
4	4	Autorizante	111	0	0
5	5	Arquitecto	111	11111111	0
6	6	Tester	0	1000	11
7	7	Analista	111	0	0
8	8	Desarrollador	0	11110111	0
9	9	phase operator	111	11111111	11
10	10	phase controller	111	11111111	11
\.


--
-- TOC entry 2075 (class 0 OID 0)
-- Dependencies: 168
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('rol_id_seq', 10, true);


--
-- TOC entry 2036 (class 0 OID 50562)
-- Dependencies: 177 2049
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tipoitem (id, nombre, comentario, defase) FROM stdin;
1	Libro	Representa un libro	9
2	Lección	Representa una lección	9
3	Capítulo	Representa una conclusión	9
4	Relevamiento	Recoger datos	1
5	Diseño	Representa una conclusión	2
6	Aplicación	Representa la aplicación de conocimientos previos	10
\.


--
-- TOC entry 2076 (class 0 OID 0)
-- Dependencies: 176
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tipoitem_id_seq', 1, false);


--
-- TOC entry 2031 (class 0 OID 50527)
-- Dependencies: 172 2049
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
4	1
5	2
6	3
3	4
5	5
1	6
2	7
4	8
3	9
3	10
\.


--
-- TOC entry 2021 (class 0 OID 50445)
-- Dependencies: 162 2049
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY usuario (id, nombre, nombredeusuario, clave, "isAdmin") FROM stdin;
1	Administrador	admin	7c4a8d09ca3762af61e59520943dc26494f8941b	t
2	Martin Poletti	martin	54669547a225ff20cba8b75a4adca540eef25858	f
3	Natalia Valdez	natalia	7c4a8d09ca3762af61e59520943dc26494f8941b	t
4	Anna Dyst	anna	7c4a8d09ca3762af61e59520943dc26494f8941b	f
5	Dan Tor	dan	7c4a8d09ca3762af61e59520943dc26494f8941b	f
6	Thomas Dwin	tommy	7c4a8d09ca3762af61e59520943dc26494f8941b	f
\.


--
-- TOC entry 2077 (class 0 OID 0)
-- Dependencies: 161
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('usuario_id_seq', 6, true);


--
-- TOC entry 2045 (class 0 OID 50637)
-- Dependencies: 186 2049
-- Data for Name: valorbool; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY valorbool (atributo_id, item_id, valor) FROM stdin;
8	4	f
8	5	f
8	6	t
\.


--
-- TOC entry 2046 (class 0 OID 50652)
-- Dependencies: 187 2049
-- Data for Name: valordate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY valordate (atributo_id, item_id, valor) FROM stdin;
\.


--
-- TOC entry 2047 (class 0 OID 50667)
-- Dependencies: 188 2049
-- Data for Name: valorint; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY valorint (atributo_id, item_id, valor) FROM stdin;
\.


--
-- TOC entry 2048 (class 0 OID 50682)
-- Dependencies: 189 2049
-- Data for Name: valorstr; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY valorstr (atributo_id, item_id, valor) FROM stdin;
1	1	
1	2	Materiales
1	3	Materiales
2	1	
2	2	Kurth Nixon
2	3	Rigoberto Q. Zayas
\.


--
-- TOC entry 2040 (class 0 OID 50595)
-- Dependencies: 181 2049
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, deitem) FROM stdin;
1	0	Construcciones	Activo	f	50	5	1
2	1	Construcciones	Activo	f	50	5	1
3	2	Construcciones	Aprobado	t	50	5	1
4	0	Maqueta	Activo	f	27	9	2
5	1	Maqueta	Activo	f	25	10	2
6	2	Maqueta	Aprobado	t	25	10	2
\.


--
-- TOC entry 2078 (class 0 OID 0)
-- Dependencies: 180
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('vitem_id_seq', 1, false);


--
-- TOC entry 2034 (class 0 OID 50550)
-- Dependencies: 175 2049
-- Data for Name: voto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY voto (peticion_id, user_id, valor) FROM stdin;
\.


--
-- TOC entry 1986 (class 2606 OID 50631)
-- Dependencies: 185 185 2050
-- Name: atributo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pkey PRIMARY KEY (id);


--
-- TOC entry 1964 (class 2606 OID 50490)
-- Dependencies: 167 167 2050
-- Name: fase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_pkey PRIMARY KEY (id);


--
-- TOC entry 1978 (class 2606 OID 50582)
-- Dependencies: 179 179 2050
-- Name: item_etiqueta_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_etiqueta_key UNIQUE (etiqueta);


--
-- TOC entry 1980 (class 2606 OID 50580)
-- Dependencies: 179 179 2050
-- Name: item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- TOC entry 1968 (class 2606 OID 50516)
-- Dependencies: 171 171 2050
-- Name: lineabase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_pkey PRIMARY KEY (id);


--
-- TOC entry 1962 (class 2606 OID 50472)
-- Dependencies: 165 165 165 2050
-- Name: miembro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_pkey PRIMARY KEY (proyecto_id, user_id);


--
-- TOC entry 1972 (class 2606 OID 50549)
-- Dependencies: 174 174 2050
-- Name: peticion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_pkey PRIMARY KEY (id);


--
-- TOC entry 1958 (class 2606 OID 50462)
-- Dependencies: 164 164 2050
-- Name: proyecto_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_nombre_key UNIQUE (nombre);


--
-- TOC entry 1960 (class 2606 OID 50460)
-- Dependencies: 164 164 2050
-- Name: proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_pkey PRIMARY KEY (id);


--
-- TOC entry 1984 (class 2606 OID 50613)
-- Dependencies: 183 183 2050
-- Name: relacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_pkey PRIMARY KEY (id);


--
-- TOC entry 1966 (class 2606 OID 50503)
-- Dependencies: 169 169 2050
-- Name: rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (id);


--
-- TOC entry 1976 (class 2606 OID 50567)
-- Dependencies: 177 177 2050
-- Name: tipoitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_pkey PRIMARY KEY (id);


--
-- TOC entry 1970 (class 2606 OID 50531)
-- Dependencies: 172 172 172 2050
-- Name: user_rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_pkey PRIMARY KEY (usuario_id, rol_id);


--
-- TOC entry 1954 (class 2606 OID 50452)
-- Dependencies: 162 162 2050
-- Name: usuario_nombredeusuario_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_nombredeusuario_key UNIQUE (nombredeusuario);


--
-- TOC entry 1956 (class 2606 OID 50450)
-- Dependencies: 162 162 2050
-- Name: usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- TOC entry 1988 (class 2606 OID 50641)
-- Dependencies: 186 186 186 2050
-- Name: valorbool_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1990 (class 2606 OID 50656)
-- Dependencies: 187 187 187 2050
-- Name: valordate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1992 (class 2606 OID 50671)
-- Dependencies: 188 188 188 2050
-- Name: valorint_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1994 (class 2606 OID 50686)
-- Dependencies: 189 189 189 2050
-- Name: valorstr_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1982 (class 2606 OID 50600)
-- Dependencies: 181 181 2050
-- Name: vitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_pkey PRIMARY KEY (id);


--
-- TOC entry 1974 (class 2606 OID 50554)
-- Dependencies: 175 175 175 2050
-- Name: voto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_pkey PRIMARY KEY (peticion_id, user_id);


--
-- TOC entry 2011 (class 2606 OID 50632)
-- Dependencies: 1975 185 177 2050
-- Name: atributo_pertenece_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pertenece_fkey FOREIGN KEY (pertenece) REFERENCES tipoitem(id);


--
-- TOC entry 1998 (class 2606 OID 50491)
-- Dependencies: 1959 167 164 2050
-- Name: fase_delproyecto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_delproyecto_fkey FOREIGN KEY (delproyecto) REFERENCES proyecto(id);


--
-- TOC entry 2006 (class 2606 OID 50583)
-- Dependencies: 179 171 1967 2050
-- Name: item_linea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_linea_id_fkey FOREIGN KEY (linea_id) REFERENCES lineabase(id);


--
-- TOC entry 2007 (class 2606 OID 50588)
-- Dependencies: 179 1975 177 2050
-- Name: item_tipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_tipo_fkey FOREIGN KEY (tipo) REFERENCES tipoitem(id);


--
-- TOC entry 2000 (class 2606 OID 50517)
-- Dependencies: 1955 162 171 2050
-- Name: lineabase_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_creador_id_fkey FOREIGN KEY (creador_id) REFERENCES usuario(id);


--
-- TOC entry 2001 (class 2606 OID 50522)
-- Dependencies: 171 167 1963 2050
-- Name: lineabase_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- TOC entry 1996 (class 2606 OID 50473)
-- Dependencies: 164 165 1959 2050
-- Name: miembro_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto(id);


--
-- TOC entry 1997 (class 2606 OID 50478)
-- Dependencies: 1955 162 165 2050
-- Name: miembro_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_user_id_fkey FOREIGN KEY (user_id) REFERENCES usuario(id);


--
-- TOC entry 1995 (class 2606 OID 50463)
-- Dependencies: 162 1955 164 2050
-- Name: proyecto_delider_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_delider_fkey FOREIGN KEY (delider) REFERENCES usuario(id);


--
-- TOC entry 2009 (class 2606 OID 50614)
-- Dependencies: 183 1981 181 2050
-- Name: relacion_ante_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_ante_id_fkey FOREIGN KEY (ante_id) REFERENCES vitem(id);


--
-- TOC entry 2010 (class 2606 OID 50619)
-- Dependencies: 181 1981 183 2050
-- Name: relacion_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_post_id_fkey FOREIGN KEY (post_id) REFERENCES vitem(id);


--
-- TOC entry 1999 (class 2606 OID 50504)
-- Dependencies: 167 169 1963 2050
-- Name: rol_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- TOC entry 2005 (class 2606 OID 50568)
-- Dependencies: 167 177 1963 2050
-- Name: tipoitem_defase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_defase_fkey FOREIGN KEY (defase) REFERENCES fase(id);


--
-- TOC entry 2002 (class 2606 OID 50532)
-- Dependencies: 1965 169 172 2050
-- Name: user_rol_rol_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_rol_id_fkey FOREIGN KEY (rol_id) REFERENCES rol(id);


--
-- TOC entry 2003 (class 2606 OID 50537)
-- Dependencies: 172 162 1955 2050
-- Name: user_rol_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuario(id);


--
-- TOC entry 2012 (class 2606 OID 50642)
-- Dependencies: 186 1985 185 2050
-- Name: valorbool_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2013 (class 2606 OID 50647)
-- Dependencies: 1981 181 186 2050
-- Name: valorbool_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2014 (class 2606 OID 50657)
-- Dependencies: 185 1985 187 2050
-- Name: valordate_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2015 (class 2606 OID 50662)
-- Dependencies: 181 1981 187 2050
-- Name: valordate_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2016 (class 2606 OID 50672)
-- Dependencies: 185 1985 188 2050
-- Name: valorint_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2017 (class 2606 OID 50677)
-- Dependencies: 1981 188 181 2050
-- Name: valorint_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2018 (class 2606 OID 50687)
-- Dependencies: 189 1985 185 2050
-- Name: valorstr_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2019 (class 2606 OID 50692)
-- Dependencies: 1981 181 189 2050
-- Name: valorstr_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2008 (class 2606 OID 50601)
-- Dependencies: 1979 181 179 2050
-- Name: vitem_deitem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_deitem_fkey FOREIGN KEY (deitem) REFERENCES item(id);


--
-- TOC entry 2004 (class 2606 OID 50555)
-- Dependencies: 1971 175 174 2050
-- Name: voto_peticion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_peticion_id_fkey FOREIGN KEY (peticion_id) REFERENCES peticion(id);


--
-- TOC entry 2055 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2013-05-25 09:23:31 PYT

--
-- PostgreSQL database dump complete
--

=======
INSERT INTO valorstr(atributo_id, item_id, valor)
        VALUES (1,0,'');
INSERT INTO valorstr(atributo_id, item_id, valor)
        VALUES (1,1,'Materiales');
INSERT Into valorstr(atributo_id, item_id, valor)
        VALUES (1,2,'Materiales');
INSERT INTO valorstr(atributo_id, item_id, valor)
        VALUES (2,0,'');
INSERT INTO valorstr(atributo_id, item_id, valor)
        VALUES (2,1,'Kurth Nixon');
INSERT Into valorstr(atributo_id, item_id, valor)
        VALUES (2,2,'Rigoberto Q. Zayas');
>>>>>>> branch 'master' of https://syncrhonous@code.google.com/p/pmspy/
