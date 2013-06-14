--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: pms; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON DATABASE pms IS '"dev"';


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
1	explicación	Cadena	1
2	Planificado	Booleano	1
3	Fecha de Análisis	Fecha	1
4	Explicación	Cadena	2
5	Genera Documentación	Booleano	2
6	Nombre Clave	Cadena	3
7	Páginas	Numerico	3
8	Componente Activo	Booleano	4
9	Experimental	Booleano	4
10	Nombre Clave	Cadena	4
11	Experimental	Booleano	5
12	Duración del proceso	Numerico	5
13	Notas Finales	Cadena	5
14	Descripción	Cadena	6
15	Duración	Numerico	6
16	Exitoso	Booleano	6
\.


--
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atributo_id_seq', 16, true);


--
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
2	beta	2	2013-08-02 00:00:00	2013-11-01 00:00:00	2013-06-13 11:36:00.288595	Abierta	1
3	gama	3	2013-11-02 00:00:00	2014-02-01 00:00:00	2013-06-13 11:39:17.823924	Abierta	1
4	delta	4	2014-02-02 00:00:00	2014-06-01 00:00:00	2013-06-13 11:41:43.249159	Abierta	1
1	alfa	1	2013-06-13 10:17:50.626447	2013-08-01 00:00:00	2013-06-13 15:45:59.181756	Abierta	1
\.


--
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('fase_id_seq', 4, true);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item (id, tipo, etiqueta, "fechaCreacion", linea_id, usuario_creador_id) FROM stdin;
1	1	1-1-1	2013-06-13 15:45:58.98332	\N	\N
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('item_id_seq', 1, true);


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
1	4
1	5
1	9
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
1	BroadWell	4	2013-06-13 10:13:18.009162	2014-06-01 00:00:00	\N	4	Iniciado
\.


--
-- Name: proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('proyecto_id_seq', 1, true);


--
-- Data for Name: relacion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY relacion (id, ante_id, post_id, tipo) FROM stdin;
\.


--
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('relacion_id_seq', 1, false);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Jefe de Ingeniería	111	1000	1
2	1	Analista	0	11110111	0
5	3	Ingeniero	0	11110111	0
3	2	Arquitecto	111	1000	1
6	2	Técnico	0	11110111	0
7	4	Depurador	0	11110111	0
8	4	Jefe de Ingeniería	111	1000	1
4	3	Jefe de Ingeniería	111	1000	1
\.


--
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rol_id_seq', 8, true);


--
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY tipoitem (id, nombre, comentario, defase) FROM stdin;
2	Requisito	Requisito Concretos para las fases posteriores del proyecto	1
1	Análisis	Estudio detallado de resquisitos y recursos	1
3	Arquitectura Lógica	Describe la lógica de los microprocesardores	2
4	Arquitectura Física	Describe los detalles del hardware que ha de ser implementado	2
5	Componente	Componente Fabricado en la fase gama	3
6	Prueba	Pruebas finales realizadas al microprocesador	4
\.


--
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipoitem_id_seq', 6, true);


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
4	1
5	2
6	2
4	3
9	3
4	4
9	4
9	5
4	5
9	6
5	7
6	7
4	8
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: -
--

COPY usuario (id, nombre, nombredeusuario, clave, "isAdmin") FROM stdin;
1	Administrador	admin	7c4a8d09ca3762af61e59520943dc26494f8941b	t
2	Natalia Valdez	natalia	2298625f2ba17912b286ad9afd8f089e460241b9	t
3	Martin Poletti	martin	54669547a225ff20cba8b75a4adca540eef25858	f
4	Thomas Dwyn	tom	7c4a8d09ca3762af61e59520943dc26494f8941b	t
5	Anna Dyst	anna	7c4a8d09ca3762af61e59520943dc26494f8941b	f
6	Dan Tor	dan	7c4a8d09ca3762af61e59520943dc26494f8941b	f
7	Celia Rivas	crivas	7c4a8d09ca3762af61e59520943dc26494f8941b	f
8	Bruno Díaz	bdiaz	7c4a8d09ca3762af61e59520943dc26494f8941b	t
9	Ryunosuke Asakura	ryu	7c4a8d09ca3762af61e59520943dc26494f8941b	f
10	Xiao Lang	xiao	7c4a8d09ca3762af61e59520943dc26494f8941b	f
11	Ronaldo Riveiros	ronaldo	7c4a8d09ca3762af61e59520943dc26494f8941b	f
12	Eva Soler	eva	7c4a8d09ca3762af61e59520943dc26494f8941b	t
\.


--
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('usuario_id_seq', 12, true);


--
-- Data for Name: valorbool; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorbool (atributo_id, item_id, valor) FROM stdin;
2	1	f
\.


--
-- Data for Name: valordate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valordate (atributo_id, item_id, valor) FROM stdin;
3	1	\N
\.


--
-- Data for Name: valorint; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorint (atributo_id, item_id, valor) FROM stdin;
\.


--
-- Data for Name: valorstr; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorstr (atributo_id, item_id, valor) FROM stdin;
1	1	
\.


--
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, "fechaModificacion", deitem, usuario_modificador_id) FROM stdin;
1	0	Minerales	Activo	t	500000	30	2013-06-13 15:45:58.98332	1	6
\.


--
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('vitem_id_seq', 1, true);


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

