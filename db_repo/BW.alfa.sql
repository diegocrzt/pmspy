--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: atributo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE atributo (
    id integer NOT NULL,
    nombre character varying(20),
    "tipoDato" character varying(20),
    pertenece integer
);


--
-- Name: atributo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE atributo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: atributo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE atributo_id_seq OWNED BY atributo.id;


--
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
-- Name: fase_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE fase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: fase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE fase_id_seq OWNED BY fase.id;


--
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
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE item_id_seq OWNED BY item.id;


--
-- Name: item_peticion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE item_peticion (
    peticion_id integer NOT NULL,
    item_id integer NOT NULL,
    actual boolean
);


--
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
-- Name: lineabase_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE lineabase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: lineabase_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE lineabase_id_seq OWNED BY lineabase.id;


--
-- Name: miembro; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE miembro (
    proyecto_id integer NOT NULL,
    user_id integer NOT NULL
);


--
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
-- Name: peticion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE peticion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: peticion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE peticion_id_seq OWNED BY peticion.id;


--
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
-- Name: proyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE proyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: proyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE proyecto_id_seq OWNED BY proyecto.id;


--
-- Name: relacion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE relacion (
    id integer NOT NULL,
    ante_id integer,
    post_id integer,
    tipo character varying(10)
);


--
-- Name: relacion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE relacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: relacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE relacion_id_seq OWNED BY relacion.id;


--
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
-- Name: rol_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rol_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rol_id_seq OWNED BY rol.id;


--
-- Name: tipoitem; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE tipoitem (
    id integer NOT NULL,
    nombre character varying(20),
    comentario character varying(100),
    defase integer
);


--
-- Name: tipoitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tipoitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tipoitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tipoitem_id_seq OWNED BY tipoitem.id;


--
-- Name: user_rol; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE user_rol (
    usuario_id integer NOT NULL,
    rol_id integer NOT NULL
);


--
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
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE usuario_id_seq OWNED BY usuario.id;


--
-- Name: valorbool; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorbool (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor boolean
);


--
-- Name: valordate; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valordate (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor timestamp without time zone
);


--
-- Name: valorfile; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorfile (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor bytea,
    nombre character varying(200)
);


--
-- Name: valorint; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorint (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor real
);


--
-- Name: valorstr; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE valorstr (
    atributo_id integer NOT NULL,
    item_id integer NOT NULL,
    valor character varying(200)
);


--
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
    usuario_modificador_id integer
);


--
-- Name: vitem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vitem_id_seq OWNED BY vitem.id;


--
-- Name: voto; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE voto (
    peticion_id integer NOT NULL,
    user_id integer NOT NULL,
    valor boolean
);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY atributo ALTER COLUMN id SET DEFAULT nextval('atributo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY fase ALTER COLUMN id SET DEFAULT nextval('fase_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY item ALTER COLUMN id SET DEFAULT nextval('item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase ALTER COLUMN id SET DEFAULT nextval('lineabase_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion ALTER COLUMN id SET DEFAULT nextval('peticion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY proyecto ALTER COLUMN id SET DEFAULT nextval('proyecto_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion ALTER COLUMN id SET DEFAULT nextval('relacion_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rol ALTER COLUMN id SET DEFAULT nextval('rol_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem ALTER COLUMN id SET DEFAULT nextval('tipoitem_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY usuario ALTER COLUMN id SET DEFAULT nextval('usuario_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem ALTER COLUMN id SET DEFAULT nextval('vitem_id_seq'::regclass);


--
-- Data for Name: atributo; Type: TABLE DATA; Schema: public; Owner: -
--

COPY atributo (id, nombre, "tipoDato", pertenece) FROM stdin;
2	Notas	Cadena	1
3	Genera Documento	Booleano	1
4	Revision	Fecha	1
6	Id Interno	Numerico	2
7	Descripcion	Cadena	2
8	Experimental	Booleano	2
\.


--
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atributo_id_seq', 8, true);


--
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
2	beta	2	2013-09-02 00:00:00	2013-12-01 00:00:00	\N	Abierta	1
3	gama	3	2013-12-02 00:00:00	2014-03-01 00:00:00	\N	Abierta	1
4	delta	4	2014-03-02 00:00:00	2014-06-01 00:00:00	\N	Abierta	1
1	alfa	1	2013-06-01 00:00:00	2013-09-01 00:00:00	2013-06-18 13:40:41.721343	Abierta	1
\.


--
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('fase_id_seq', 4, true);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item (id, tipo, etiqueta, "fechaCreacion", linea_id, usuario_creador_id) FROM stdin;
1	1	1-1-1	2013-06-18 13:31:33.264764	\N	1
2	1	1-1-4	2013-06-18 13:32:31.321181	\N	1
3	2	1-1-7	2013-06-18 13:33:58.974538	\N	1
4	1	1-1-9	2013-06-18 13:35:10.758247	\N	1
5	2	1-1-11	2013-06-18 13:36:47.560435	\N	1
6	1	1-1-13	2013-06-18 13:37:59.290193	\N	1
7	2	1-1-15	2013-06-18 13:39:24.550494	\N	1
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('item_id_seq', 7, true);


--
-- Data for Name: item_peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item_peticion (peticion_id, item_id, actual) FROM stdin;
\.


--
-- Data for Name: lineabase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lineabase (id, creador_id, "fechaCreacion", numero, comentario, fase_id, estado) FROM stdin;
\.


--
-- Name: lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('lineabase_id_seq', 1, false);


--
-- Data for Name: miembro; Type: TABLE DATA; Schema: public; Owner: -
--

COPY miembro (proyecto_id, user_id) FROM stdin;
1	1
\.


--
-- Data for Name: peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY peticion (id, numero, proyecto_id, comentario, estado, usuario_id, "cantVotos", "cantItems", "costoT", "dificultadT", "fechaCreacion", "fechaEnvio", acciones) FROM stdin;
\.


--
-- Name: peticion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('peticion_id_seq', 1, false);


--
-- Data for Name: proyecto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY proyecto (id, nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado) FROM stdin;
1	BroadWell	4	2013-06-01 00:00:00	2014-06-01 00:00:00	\N	1	Iniciado
\.


--
-- Name: proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('proyecto_id_seq', 1, true);


--
-- Data for Name: relacion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY relacion (id, ante_id, post_id, tipo) FROM stdin;
1	3	8	P-H
2	10	8	P-H
3	12	14	P-H
4	8	16	P-H
5	14	16	P-H
\.


--
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('relacion_id_seq', 5, true);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Jefe de Area	111	11111111	1
\.


--
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rol_id_seq', 1, true);


--
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY tipoitem (id, nombre, comentario, defase) FROM stdin;
1	Análisis	Actividades de análisis para la fabricación de procesadores	1
2	Requisito	Actividad pre requisito en el proceso de fabricación de procesadores	1
\.


--
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipoitem_id_seq', 2, true);


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
1	1
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: -
--

COPY usuario (id, nombre, nombredeusuario, clave, "isAdmin") FROM stdin;
1	Administrador	admin	7c4a8d09ca3762af61e59520943dc26494f8941b	t
2	Natalia Valdez	natalia	fb7f46ec329a5e0f6fdfabfcccec30545fbe6d3f	t
3	Martín Poletti	martin	54669547a225ff20cba8b75a4adca540eef25858	f
4	Dan Tor	dan	7c4a8d09ca3762af61e59520943dc26494f8941b	t
5	Eva Almada	eva	7c4a8d09ca3762af61e59520943dc26494f8941b	f
6	Ryunosuke Asakura	ryu	7c4a8d09ca3762af61e59520943dc26494f8941b	f
7	Anna Dyst	anna	7c4a8d09ca3762af61e59520943dc26494f8941b	f
\.


--
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('usuario_id_seq', 7, true);


--
-- Data for Name: valorbool; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorbool (atributo_id, item_id, valor) FROM stdin;
3	1	f
3	2	f
3	3	f
3	4	f
3	5	t
3	6	t
8	7	f
8	8	f
3	9	f
3	10	t
8	11	f
8	12	t
3	13	f
3	14	t
8	15	f
8	16	f
\.


--
-- Data for Name: valordate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valordate (atributo_id, item_id, valor) FROM stdin;
4	1	\N
4	2	2013-06-05 00:00:00
4	3	2013-06-06 00:00:00
4	4	\N
4	5	2013-06-02 00:00:00
4	6	\N
4	9	\N
4	10	2013-06-10 00:00:00
4	13	\N
4	14	\N
\.


--
-- Data for Name: valorfile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorfile (atributo_id, item_id, valor, nombre) FROM stdin;
\.


--
-- Data for Name: valorint; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorint (atributo_id, item_id, valor) FROM stdin;
6	7	0
6	8	1
6	11	0
6	12	2
6	15	0
6	16	4
\.


--
-- Data for Name: valorstr; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorstr (atributo_id, item_id, valor) FROM stdin;
2	1	
2	2	Análisis de suelos en busca de minerales (cuarzo)
2	3	Análisis de suelos en busca de minerales (cuarzo)
2	4	
2	5	Análisis de las instalaciones de la fabrica
2	6	Análisis de las instalaciones de la fabrica
7	7	
7	8	Obtención de obleas de cuarzo para microprocesadores
2	9	
2	10	Análisis de las arquitecturas anteriores a BroadWell
7	11	
7	12	Mejoras a la nueva arquitectura
2	13	
2	14	Análisis de tempertura de la nueva aquitectura
7	15	
7	16	Prueba Térmica sobre el nuevo diseño térmico
\.


--
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, "fechaModificacion", deitem, usuario_modificador_id) FROM stdin;
1	0	Minerales	Activo	f	250000	30	2013-06-18 13:31:33.264764	1	1
2	1	Minerales	Activo	f	250000	30	2013-06-18 13:31:53.059921	1	1
3	2	Minerales	Activo	t	250000	30	2013-06-18 13:32:04.71778	1	1
4	0	Instalaciones	Activo	f	30000	10	2013-06-18 13:32:31.321181	2	1
5	1	Instalaciones	Activo	f	30000	10	2013-06-18 13:33:34.582212	2	1
6	2	Instalaciones	Eliminado	t	30000	10	2013-06-18 13:33:43.050457	2	1
7	0	Quarzo	Activo	f	500000	25	2013-06-18 13:33:58.974538	3	1
8	1	Quarzo	Activo	t	500000	25	2013-06-18 13:34:26.650533	3	1
9	0	Arq. anteriores	Activo	f	15000	9	2013-06-18 13:35:10.758247	4	1
10	1	Arq. anteriores	Activo	t	15000	9	2013-06-18 13:35:34.596879	4	1
11	0	Mejoras	Activo	f	60000	12	2013-06-18 13:36:47.560435	5	1
12	1	Mejoras	Activo	t	60000	12	2013-06-18 13:37:07.044416	5	1
13	0	Temperatura	Activo	f	5000	10	2013-06-18 13:37:59.290193	6	1
14	1	Temperatura	Activo	t	5000	10	2013-06-18 13:38:21.061465	6	1
15	0	Prueba Térmica	Activo	f	50000	10	2013-06-18 13:39:24.550494	7	1
16	1	Prueba Térmica	Activo	t	50000	10	2013-06-18 13:39:58.357826	7	1
\.


--
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('vitem_id_seq', 16, true);


--
-- Data for Name: voto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY voto (peticion_id, user_id, valor) FROM stdin;
\.


--
-- Name: atributo_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pkey PRIMARY KEY (id);


--
-- Name: fase_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_pkey PRIMARY KEY (id);


--
-- Name: item_etiqueta_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_etiqueta_key UNIQUE (etiqueta);


--
-- Name: item_peticion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY item_peticion
    ADD CONSTRAINT item_peticion_pkey PRIMARY KEY (peticion_id, item_id);


--
-- Name: item_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: lineabase_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_pkey PRIMARY KEY (id);


--
-- Name: miembro_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_pkey PRIMARY KEY (proyecto_id, user_id);


--
-- Name: peticion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_pkey PRIMARY KEY (id);


--
-- Name: proyecto_nombre_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_nombre_key UNIQUE (nombre);


--
-- Name: proyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_pkey PRIMARY KEY (id);


--
-- Name: relacion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_pkey PRIMARY KEY (id);


--
-- Name: rol_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (id);


--
-- Name: tipoitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_pkey PRIMARY KEY (id);


--
-- Name: user_rol_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_pkey PRIMARY KEY (usuario_id, rol_id);


--
-- Name: usuario_nombredeusuario_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_nombredeusuario_key UNIQUE (nombredeusuario);


--
-- Name: usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- Name: valorbool_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_pkey PRIMARY KEY (atributo_id, item_id);


--
-- Name: valordate_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_pkey PRIMARY KEY (atributo_id, item_id);


--
-- Name: valorfile_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorfile
    ADD CONSTRAINT valorfile_pkey PRIMARY KEY (atributo_id, item_id);


--
-- Name: valorint_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_pkey PRIMARY KEY (atributo_id, item_id);


--
-- Name: valorstr_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_pkey PRIMARY KEY (atributo_id, item_id);


--
-- Name: vitem_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_pkey PRIMARY KEY (id);


--
-- Name: voto_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_pkey PRIMARY KEY (peticion_id, user_id);


--
-- Name: atributo_pertenece_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY atributo
    ADD CONSTRAINT atributo_pertenece_fkey FOREIGN KEY (pertenece) REFERENCES tipoitem(id);


--
-- Name: fase_delproyecto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fase
    ADD CONSTRAINT fase_delproyecto_fkey FOREIGN KEY (delproyecto) REFERENCES proyecto(id);


--
-- Name: item_linea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_linea_id_fkey FOREIGN KEY (linea_id) REFERENCES lineabase(id);


--
-- Name: item_peticion_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item_peticion
    ADD CONSTRAINT item_peticion_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: item_peticion_peticion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item_peticion
    ADD CONSTRAINT item_peticion_peticion_id_fkey FOREIGN KEY (peticion_id) REFERENCES peticion(id);


--
-- Name: item_tipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_tipo_fkey FOREIGN KEY (tipo) REFERENCES tipoitem(id);


--
-- Name: item_usuario_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_usuario_creador_id_fkey FOREIGN KEY (usuario_creador_id) REFERENCES usuario(id);


--
-- Name: lineabase_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_creador_id_fkey FOREIGN KEY (creador_id) REFERENCES usuario(id);


--
-- Name: lineabase_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lineabase
    ADD CONSTRAINT lineabase_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- Name: miembro_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto(id);


--
-- Name: miembro_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY miembro
    ADD CONSTRAINT miembro_user_id_fkey FOREIGN KEY (user_id) REFERENCES usuario(id);


--
-- Name: peticion_proyecto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_proyecto_id_fkey FOREIGN KEY (proyecto_id) REFERENCES proyecto(id);


--
-- Name: peticion_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY peticion
    ADD CONSTRAINT peticion_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuario(id);


--
-- Name: proyecto_delider_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY proyecto
    ADD CONSTRAINT proyecto_delider_fkey FOREIGN KEY (delider) REFERENCES usuario(id);


--
-- Name: relacion_ante_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_ante_id_fkey FOREIGN KEY (ante_id) REFERENCES vitem(id);


--
-- Name: relacion_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY relacion
    ADD CONSTRAINT relacion_post_id_fkey FOREIGN KEY (post_id) REFERENCES vitem(id);


--
-- Name: rol_fase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY rol
    ADD CONSTRAINT rol_fase_id_fkey FOREIGN KEY (fase_id) REFERENCES fase(id);


--
-- Name: tipoitem_defase_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_defase_fkey FOREIGN KEY (defase) REFERENCES fase(id);


--
-- Name: user_rol_rol_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_rol_id_fkey FOREIGN KEY (rol_id) REFERENCES rol(id);


--
-- Name: user_rol_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY user_rol
    ADD CONSTRAINT user_rol_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES usuario(id);


--
-- Name: valorbool_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- Name: valorbool_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorbool
    ADD CONSTRAINT valorbool_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: valordate_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- Name: valordate_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valordate
    ADD CONSTRAINT valordate_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: valorfile_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorfile
    ADD CONSTRAINT valorfile_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- Name: valorfile_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorfile
    ADD CONSTRAINT valorfile_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: valorint_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- Name: valorint_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorint
    ADD CONSTRAINT valorint_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: valorstr_atributo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_atributo_id_fkey FOREIGN KEY (atributo_id) REFERENCES atributo(id);


--
-- Name: valorstr_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorstr
    ADD CONSTRAINT valorstr_item_id_fkey FOREIGN KEY (item_id) REFERENCES vitem(id);


--
-- Name: vitem_deitem_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_deitem_fkey FOREIGN KEY (deitem) REFERENCES item(id);


--
-- Name: vitem_usuario_modificador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem
    ADD CONSTRAINT vitem_usuario_modificador_id_fkey FOREIGN KEY (usuario_modificador_id) REFERENCES usuario(id);


--
-- Name: voto_peticion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_peticion_id_fkey FOREIGN KEY (peticion_id) REFERENCES peticion(id);


--
-- Name: voto_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY voto
    ADD CONSTRAINT voto_user_id_fkey FOREIGN KEY (user_id) REFERENCES usuario(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--
