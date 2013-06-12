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

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.9
-- Dumped by pg_dump version 9.1.9
-- Started on 2013-06-12 16:49:26 PYT

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 190 (class 3079 OID 11647)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2033 (class 0 OID 0)
-- Dependencies: 190
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 180 (class 1259 OID 60700)
-- Dependencies: 5
-- Name: atributo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE atributo (
    id integer NOT NULL,
    nombre character varying(20),
    "tipoDato" character varying(20),
    pertenece integer
);


--
-- TOC entry 179 (class 1259 OID 60698)
-- Dependencies: 180 5
-- Name: atributo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE atributo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2034 (class 0 OID 0)
-- Dependencies: 179
-- Name: atributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE atributo_id_seq OWNED BY atributo.id;


--
-- TOC entry 169 (class 1259 OID 60603)
-- Dependencies: 5
-- Name: fase; Type: TABLE; Schema: public; Owner: -; Tablespace: 
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


--
-- TOC entry 168 (class 1259 OID 60601)
-- Dependencies: 5 169
-- Name: fase_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE fase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2035 (class 0 OID 0)
-- Dependencies: 168
-- Name: fase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE fase_id_seq OWNED BY fase.id;


--
-- TOC entry 178 (class 1259 OID 60675)
-- Dependencies: 5
-- Name: item; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE item (
    id integer NOT NULL,
    tipo integer,
    etiqueta character varying(60),
    "fechaCreacion" timestamp without time zone,
    linea_id integer,
    usuario_creador_id integer
);


--
-- TOC entry 177 (class 1259 OID 60673)
-- Dependencies: 5 178
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2036 (class 0 OID 0)
-- Dependencies: 177
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE item_id_seq OWNED BY item.id;


--
-- TOC entry 175 (class 1259 OID 60642)
-- Dependencies: 5
-- Name: lineabase; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE lineabase (
    id integer NOT NULL,
    creador_id integer,
    "fechaCreacion" timestamp without time zone,
    numero integer,
    comentario character varying(100),
    fase_id integer,
    estado character varying(15)
);


--
-- TOC entry 174 (class 1259 OID 60640)
-- Dependencies: 175 5
-- Name: lineabase_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE lineabase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2037 (class 0 OID 0)
-- Dependencies: 174
-- Name: lineabase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE lineabase_id_seq OWNED BY lineabase.id;


--
-- TOC entry 167 (class 1259 OID 60586)
-- Dependencies: 5
-- Name: miembro; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE miembro (
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 166 (class 1259 OID 60570)
-- Dependencies: 5
-- Name: peticion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE peticion (
    id integer NOT NULL,
    numero integer,
    proyecto_id integer,
    comentario character varying(100),
    estado character varying(15),
    usuario_id integer,
    "cantVotos" integer,
    "cantItems" integer,
    "costoT" integer,
    "dificultadT" integer,
    "fechaCreacion" timestamp without time zone,
    "fechaEnvio" timestamp without time zone,
    acciones integer
);


--
-- TOC entry 165 (class 1259 OID 60568)
-- Dependencies: 5 166
-- Name: peticion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE peticion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2038 (class 0 OID 0)
-- Dependencies: 165
-- Name: peticion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE peticion_id_seq OWNED BY peticion.id;


--
-- TOC entry 164 (class 1259 OID 60555)
-- Dependencies: 5
-- Name: proyecto; Type: TABLE; Schema: public; Owner: -; Tablespace: 
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


--
-- TOC entry 163 (class 1259 OID 60553)
-- Dependencies: 164 5
-- Name: proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2039 (class 0 OID 0)
-- Dependencies: 163
-- Name: proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE proyecto_id_seq OWNED BY proyecto.id;


--
-- TOC entry 189 (class 1259 OID 60811)
-- Dependencies: 5
-- Name: relacion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE relacion (
    id integer NOT NULL,
    ante_id integer,
    post_id integer,
    tipo character varying(10)
);


--
-- TOC entry 188 (class 1259 OID 60809)
-- Dependencies: 189 5
-- Name: relacion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE relacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2040 (class 0 OID 0)
-- Dependencies: 188
-- Name: relacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE relacion_id_seq OWNED BY relacion.id;


--
-- TOC entry 173 (class 1259 OID 60629)
-- Dependencies: 5
-- Name: rol; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE rol (
    id integer NOT NULL,
    fase_id integer,
    nombre character varying(30),
    "codigoTipo" integer,
    "codigoItem" integer,
    "codigoLB" integer
);


--
-- TOC entry 172 (class 1259 OID 60627)
-- Dependencies: 173 5
-- Name: rol_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rol_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2041 (class 0 OID 0)
-- Dependencies: 172
-- Name: rol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rol_id_seq OWNED BY rol.id;


--
-- TOC entry 171 (class 1259 OID 60616)
-- Dependencies: 5
-- Name: tipoitem; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE tipoitem (
    id integer NOT NULL,
    nombre character varying(20),
    comentario character varying(100),
    defase integer
);


--
-- TOC entry 170 (class 1259 OID 60614)
-- Dependencies: 5 171
-- Name: tipoitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tipoitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2042 (class 0 OID 0)
-- Dependencies: 170
-- Name: tipoitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tipoitem_id_seq OWNED BY tipoitem.id;


--
-- TOC entry 181 (class 1259 OID 60711)
-- Dependencies: 5
-- Name: user_rol; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE user_rol (
    usuario_id integer NOT NULL,
    rol_id integer NOT NULL
);


--
-- TOC entry 162 (class 1259 OID 60545)
-- Dependencies: 5
-- Name: usuario; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE usuario (
    id integer NOT NULL,
    nombre character varying(20),
    nombredeusuario character varying(20),
    clave character varying(41),
    "isAdmin" boolean
);


--
-- TOC entry 161 (class 1259 OID 60543)
-- Dependencies: 5 162
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2043 (class 0 OID 0)
-- Dependencies: 161
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE usuario_id_seq OWNED BY usuario.id;


--
-- TOC entry 185 (class 1259 OID 60764)
-- Dependencies: 5
-- Name: valorbool; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorbool (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor boolean
);


--
-- TOC entry 184 (class 1259 OID 60749)
-- Dependencies: 5
-- Name: valordate; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valordate (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor timestamp without time zone
);


--
-- TOC entry 186 (class 1259 OID 60779)
-- Dependencies: 5
-- Name: valorint; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorint (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor real
);


--
-- TOC entry 187 (class 1259 OID 60794)
-- Dependencies: 5
-- Name: valorstr; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorstr (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor character varying(200)
);


--
-- TOC entry 183 (class 1259 OID 60728)
-- Dependencies: 5
-- Name: vitem; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE vitem (
    id integer NOT NULL,
    version integer,
    nombre character varying(20),
    estado character varying(20),
    actual boolean,
    costo integer,
    dificultad integer,
    "fechaModificacion" timestamp without time zone,
    deitem integer,
    peticion_id integer,
    usuario_modificador_id integer
);


--
-- TOC entry 182 (class 1259 OID 60726)
-- Dependencies: 183 5
-- Name: vitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2044 (class 0 OID 0)
-- Dependencies: 182
-- Name: vitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vitem_id_seq OWNED BY vitem.id;


--
-- TOC entry 176 (class 1259 OID 60658)
-- Dependencies: 5
-- Name: voto; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE voto (
    peticion_id integer NOT NULL,
    user_id integer NOT NULL,
    valor boolean
);


--
-- TOC entry 1950 (class 2604 OID 60703)
-- Dependencies: 180 179 180
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY atributo ALTER COLUMN id SET DEFAULT nextval('atributo_id_seq'::regclass);


--
-- TOC entry 1945 (class 2604 OID 60606)
-- Dependencies: 169 168 169
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY fase ALTER COLUMN id SET DEFAULT nextval('fase_id_seq'::regclass);


--
-- TOC entry 1949 (class 2604 OID 60678)
-- Dependencies: 178 177 178
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY item ALTER COLUMN id SET DEFAULT nextval('item_id_seq'::regclass);


--
-- TOC entry 1948 (class 2604 OID 60645)
-- Dependencies: 174 175 175
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase ALTER COLUMN id SET DEFAULT nextval('lineabase_id_seq'::regclass);


--
-- TOC entry 1944 (class 2604 OID 60573)
-- Dependencies: 165 166 166
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion ALTER COLUMN id SET DEFAULT nextval('peticion_id_seq'::regclass);


--
-- TOC entry 1943 (class 2604 OID 60558)
-- Dependencies: 163 164 164
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY proyecto ALTER COLUMN id SET DEFAULT nextval('proyecto_id_seq'::regclass);


--
-- TOC entry 1952 (class 2604 OID 60814)
-- Dependencies: 188 189 189
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion ALTER COLUMN id SET DEFAULT nextval('relacion_id_seq'::regclass);


--
-- TOC entry 1947 (class 2604 OID 60632)
-- Dependencies: 173 172 173
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rol ALTER COLUMN id SET DEFAULT nextval('rol_id_seq'::regclass);


--
-- TOC entry 1946 (class 2604 OID 60619)
-- Dependencies: 171 170 171
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem ALTER COLUMN id SET DEFAULT nextval('tipoitem_id_seq'::regclass);


--
-- TOC entry 1942 (class 2604 OID 60548)
-- Dependencies: 161 162 162
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY usuario ALTER COLUMN id SET DEFAULT nextval('usuario_id_seq'::regclass);


--
-- TOC entry 1951 (class 2604 OID 60731)
-- Dependencies: 182 183 183
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem ALTER COLUMN id SET DEFAULT nextval('vitem_id_seq'::regclass);


--
-- TOC entry 1980 (class 2606 OID 60705)
-- Dependencies: 180 180 2027
-- Name: atributo_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pkey PRIMARY KEY (id);


--
-- TOC entry 1966 (class 2606 OID 60608)
-- Dependencies: 169 169 2027
-- Name: fase_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_pkey PRIMARY KEY (id);


--
-- TOC entry 1976 (class 2606 OID 60682)
-- Dependencies: 178 178 2027
-- Name: item_etiqueta_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_etiqueta_key UNIQUE (etiqueta);


--
-- TOC entry 1978 (class 2606 OID 60680)
-- Dependencies: 178 178 2027
-- Name: item_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- TOC entry 1972 (class 2606 OID 60647)
-- Dependencies: 175 175 2027
-- Name: lineabase_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_pkey PRIMARY KEY (id);


--
-- TOC entry 1964 (class 2606 OID 60590)
-- Dependencies: 167 167 167 2027
-- Name: miembro_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_pkey PRIMARY KEY (proyecto_id, user_id);


--
-- TOC entry 1962 (class 2606 OID 60575)
-- Dependencies: 166 166 2027
-- Name: peticion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_pkey PRIMARY KEY (id);


--
-- TOC entry 1958 (class 2606 OID 60562)
-- Dependencies: 164 164 2027
-- Name: proyecto_nombre_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_nombre_key UNIQUE (nombre);


--
-- TOC entry 1960 (class 2606 OID 60560)
-- Dependencies: 164 164 2027
-- Name: proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_pkey PRIMARY KEY (id);


--
-- TOC entry 1994 (class 2606 OID 60816)
-- Dependencies: 189 189 2027
-- Name: relacion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_pkey PRIMARY KEY (id);


--
-- TOC entry 1970 (class 2606 OID 60634)
-- Dependencies: 173 173 2027
-- Name: rol_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (id);


--
-- TOC entry 1968 (class 2606 OID 60621)
-- Dependencies: 171 171 2027
-- Name: tipoitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_pkey PRIMARY KEY (id);


--
-- TOC entry 1982 (class 2606 OID 60715)
-- Dependencies: 181 181 181 2027
-- Name: user_rol_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_pkey PRIMARY KEY (usuario_id, rol_id);


--
-- TOC entry 1954 (class 2606 OID 60552)
-- Dependencies: 162 162 2027
-- Name: usuario_nombredeusuario_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_nombredeusuario_key UNIQUE (nombredeusuario);


--
-- TOC entry 1956 (class 2606 OID 60550)
-- Dependencies: 162 162 2027
-- Name: usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- TOC entry 1988 (class 2606 OID 60768)
-- Dependencies: 185 185 185 2027
-- Name: valorbool_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1986 (class 2606 OID 60753)
-- Dependencies: 184 184 184 2027
-- Name: valordate_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1990 (class 2606 OID 60783)
-- Dependencies: 186 186 186 2027
-- Name: valorint_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1992 (class 2606 OID 60798)
-- Dependencies: 187 187 187 2027
-- Name: valorstr_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_pkey PRIMARY KEY (atributo_id, item_id);


--
-- TOC entry 1984 (class 2606 OID 60733)
-- Dependencies: 183 183 2027
-- Name: vitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_pkey PRIMARY KEY (id);


--
-- TOC entry 1974 (class 2606 OID 60662)
-- Dependencies: 176 176 176 2027
-- Name: voto_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_pkey PRIMARY KEY (peticion_id, user_id);


--
-- TOC entry 2010 (class 2606 OID 60706)
-- Dependencies: 171 180 1967 2027
-- Name: atributo_pertenece_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pertenece_fkey FOREIGN KEY (pertenece) REFERENCES tipoitem(id);


--
-- TOC entry 2000 (class 2606 OID 60609)
-- Dependencies: 169 1959 164 2027
-- Name: fase_delproyecto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_delproyecto_fkey FOREIGN KEY (delproyecto) REFERENCES proyecto(id);


--
-- TOC entry 2008 (class 2606 OID 60688)
-- Dependencies: 178 175 1971 2027
-- Name: item_linea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_linea_id_fkey FOREIGN KEY (linea_id) REFERENCES lineabase(id);


--
-- TOC entry 2007 (class 2606 OID 60683)
-- Dependencies: 178 1967 171 2027
-- Name: item_tipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_tipo_fkey FOREIGN KEY (tipo) REFERENCES tipoitem(id);


--
-- TOC entry 2009 (class 2606 OID 60693)
-- Dependencies: 178 1955 162 2027
-- Name: item_usuario_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_usuario_creador_id_fkey FOREIGN KEY (usuario_creador_id) REFERENCES usuario(id);


--
-- TOC entry 2003 (class 2606 OID 60648)
-- Dependencies: 175 1955 162 2027
-- Name: lineabase_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_creador_id_fkey FOREIGN KEY (creador_id) REFERENCES usuario(id);


--
-- TOC entry 2004 (class 2606 OID 60653)
-- Dependencies: 169 1965 175 2027
-- Name: lineabase_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- TOC entry 1998 (class 2606 OID 60591)
-- Dependencies: 167 1959 164 2027
-- Name: miembro_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto(id);


--
-- TOC entry 1999 (class 2606 OID 60596)
-- Dependencies: 162 167 1955 2027
-- Name: miembro_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_user_id_fkey FOREIGN KEY (user_id) REFERENCES usuario(id);


--
-- TOC entry 1996 (class 2606 OID 60576)
-- Dependencies: 166 164 1959 2027
-- Name: peticion_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto(id);


--
-- TOC entry 1997 (class 2606 OID 60581)
-- Dependencies: 162 166 1955 2027
-- Name: peticion_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuario(id);


--
-- TOC entry 1995 (class 2606 OID 60563)
-- Dependencies: 1955 164 162 2027
-- Name: proyecto_delider_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_delider_fkey FOREIGN KEY (delider) REFERENCES usuario(id);


--
-- TOC entry 2024 (class 2606 OID 60817)
-- Dependencies: 183 1983 189 2027
-- Name: relacion_ante_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_ante_id_fkey FOREIGN KEY (ante_id) REFERENCES vitem(id);


--
-- TOC entry 2025 (class 2606 OID 60822)
-- Dependencies: 1983 189 183 2027
-- Name: relacion_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_post_id_fkey FOREIGN KEY (post_id) REFERENCES vitem(id);


--
-- TOC entry 2002 (class 2606 OID 60635)
-- Dependencies: 173 1965 169 2027
-- Name: rol_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- TOC entry 2001 (class 2606 OID 60622)
-- Dependencies: 169 1965 171 2027
-- Name: tipoitem_defase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_defase_fkey FOREIGN KEY (defase) REFERENCES fase(id);


--
-- TOC entry 2012 (class 2606 OID 60721)
-- Dependencies: 1969 181 173 2027
-- Name: user_rol_rol_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_rol_id_fkey FOREIGN KEY (rol_id) REFERENCES rol(id);


--
-- TOC entry 2011 (class 2606 OID 60716)
-- Dependencies: 162 181 1955 2027
-- Name: user_rol_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuario(id);


--
-- TOC entry 2018 (class 2606 OID 60769)
-- Dependencies: 1979 185 180 2027
-- Name: valorbool_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2019 (class 2606 OID 60774)
-- Dependencies: 185 1983 183 2027
-- Name: valorbool_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2016 (class 2606 OID 60754)
-- Dependencies: 180 1979 184 2027
-- Name: valordate_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2017 (class 2606 OID 60759)
-- Dependencies: 183 1983 184 2027
-- Name: valordate_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2020 (class 2606 OID 60784)
-- Dependencies: 180 1979 186 2027
-- Name: valorint_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2021 (class 2606 OID 60789)
-- Dependencies: 1983 186 183 2027
-- Name: valorint_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2022 (class 2606 OID 60799)
-- Dependencies: 180 1979 187 2027
-- Name: valorstr_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- TOC entry 2023 (class 2606 OID 60804)
-- Dependencies: 1983 183 187 2027
-- Name: valorstr_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- TOC entry 2013 (class 2606 OID 60734)
-- Dependencies: 1977 178 183 2027
-- Name: vitem_deitem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_deitem_fkey FOREIGN KEY (deitem) REFERENCES item(id);


--
-- TOC entry 2014 (class 2606 OID 60739)
-- Dependencies: 1961 166 183 2027
-- Name: vitem_peticion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_peticion_id_fkey FOREIGN KEY (peticion_id) REFERENCES peticion(id);


--
-- TOC entry 2015 (class 2606 OID 60744)
-- Dependencies: 1955 183 162 2027
-- Name: vitem_usuario_modificador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_usuario_modificador_id_fkey FOREIGN KEY (usuario_modificador_id) REFERENCES usuario(id);


--
-- TOC entry 2005 (class 2606 OID 60663)
-- Dependencies: 1961 166 176 2027
-- Name: voto_peticion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_peticion_id_fkey FOREIGN KEY (peticion_id) REFERENCES peticion(id);


--
-- TOC entry 2006 (class 2606 OID 60668)
-- Dependencies: 176 162 1955 2027
-- Name: voto_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_user_id_fkey FOREIGN KEY (user_id) REFERENCES usuario(id);


--
-- TOC entry 2032 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2013-06-12 16:49:27 PYT

--
-- PostgreSQL database dump complete
--

INSERT INTO usuario (nombre, nombredeusuario, clave, "isAdmin") 
	VALUES ('Administrador','admin','7c4a8d09ca3762af61e59520943dc26494f8941b','true');