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
    defase integer,
    "fechaCreacion" timestamp without time zone,
    "fechaModificacion" timestamp without time zone,
    usuario_creador_id integer,
    usuario_modificador_id integer
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
    id integer NOT NULL,
    item_id integer,
    valor bytea,
    nombre character varying(200)
);


--
-- Name: valorfile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE valorfile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: valorfile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE valorfile_id_seq OWNED BY valorfile.id;


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

ALTER TABLE ONLY valorfile ALTER COLUMN id SET DEFAULT nextval('valorfile_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vitem ALTER COLUMN id SET DEFAULT nextval('vitem_id_seq'::regclass);


--
-- Data for Name: atributo; Type: TABLE DATA; Schema: public; Owner: -
--

COPY atributo (id, nombre, "tipoDato", pertenece) FROM stdin;
1	Revision	Fecha	1
2	Notas	Cadena	1
3	Genera Documento	Booleano	1
4	ID interno	Numerico	2
5	Descripcion	Cadena	2
6	Experimental	Booleano	2
7	Interno	Booleano	3
9	Descripcion	Cadena	3
10	Fabricable	Booleano	3
11	Revision	Fecha	3
12	Revision	Fecha	4
13	Nombre Clave	Cadena	4
14	Nuevo	Booleano	4
15	Version	Numerico	5
16	Nombre Clave	Cadena	5
17	Empotrado	Booleano	5
18	Novel	Booleano	5
19	Interno	Booleano	6
20	Notas	Cadena	6
21	Tiempo	Numerico	7
22	Notas	Cadena	7
23	Exito	Booleano	7
24	Notas	Cadena	8
25	ISA Compatible	Booleano	8
26	Tiempo	Numerico	9
27	Notas	Cadena	9
28	Mass. Manufacturing 	Booleano	9
29	radio	Numerico	10
30	relleno	Booleano	10
31	longitud	Numerico	12
32	nota	Cadena	12
33	lado X	Numerico	11
34	lado Y	Numerico	11
35	lado Z	Numerico	11
36	equilatero	Booleano	11
37	longitud	Numerico	13
38	punteada	Booleano	13
39	descripcion	Cadena	13
40	lado X	Numerico	14
41	lado Y	Numerico	14
43	descripcion	Cadena	14
44	revision	Fecha	14
45	lado	Numerico	15
46	revision	Fecha	15
47	radio A	Numerico	16
48	radio B	Numerico	16
49	notas	Cadena	16
50	trazos	Numerico	17
51	longitud X	Numerico	17
52	longitud Y	Numerico	17
53	punteada	Booleano	17
54	estable	Booleano	18
55	lado	Numerico	18
56	nota	Cadena	18
57	revision	Fecha	18
58	lado	Numerico	19
59	nota	Cadena	19
60	descripcion	Cadena	20
61	revision	Fecha	20
62	solido	Booleano	20
63	puntas	Numerico	21
64	punteada	Booleano	21
65	notas	Cadena	21
66	revision	Fecha	21
67	Autor	Cadena	23
68	Edicion	Numerico	23
69	Paginas	Numerico	24
70	Completo	Booleano	24
71	Fecha	Fecha	24
72	Monografia	Booleano	25
75	Completo	Booleano	25
76	Puntaje	Numerico	25
77	Materia	Cadena	26
78	Aprobado	Booleano	26
\.


--
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atributo_id_seq', 78, true);


--
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
3	Gama	3	2013-12-02 00:00:00	2014-02-01 00:00:00	2013-06-20 18:37:26.451821	Abierta	1
4	Delta	4	2014-02-02 00:00:00	2014-06-01 00:00:00	2013-06-20 18:53:49.51291	Abierta	1
1	Alfa	1	2013-06-01 00:00:00	2013-09-01 00:00:00	2013-06-20 17:55:53.436956	Abierta	1
7	Formas Avanzadas	3	2013-08-02 00:00:00	2013-09-01 00:00:00	2013-06-20 22:33:26.253698	Abierta	2
5	Formas Básicas	1	2013-06-01 00:00:00	2013-07-01 00:00:00	2013-06-20 22:21:54.08977	Abierta	2
6	Complicando Formas	2	2013-07-02 00:00:00	2013-08-01 00:00:00	2013-06-21 17:41:33.129279	Abierta	2
9	Rendir	2	2013-06-20 00:00:00	2013-07-01 00:00:00	2013-06-21 18:17:19.806841	Cerrada	3
2	Beta	2	2013-09-02 00:00:00	2013-12-01 00:00:00	2013-06-21 18:18:55.59743	Abierta	1
8	Estudiar	1	2013-06-21 17:52:08.760837	2013-07-06 17:52:08.760837	2013-06-21 18:15:16.153456	Cerrada	3
\.


--
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('fase_id_seq', 9, true);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item (id, tipo, etiqueta, "fechaCreacion", linea_id, usuario_creador_id) FROM stdin;
1	1	1-1-1	2013-06-20 17:36:50.405986	\N	1
7	1	1-1-19	2013-06-20 17:49:01.904475	1	1
2	1	1-1-4	2013-06-20 17:42:00.421074	1	1
3	1	1-1-6	2013-06-20 17:43:05.851946	2	1
4	2	1-1-9	2013-06-20 17:44:29.81556	2	1
5	2	1-1-11	2013-06-20 17:45:18.700759	2	1
6	2	1-1-13	2013-06-20 17:46:43.969808	2	1
8	3	1-2-1	2013-06-20 18:02:38.524235	3	1
9	3	1-2-4	2013-06-20 18:03:57.796369	4	1
10	3	1-2-8	2013-06-20 18:06:23.476064	4	1
11	4	1-2-11	2013-06-20 18:07:46.139315	4	1
13	3	1-2-16	2013-06-20 18:10:19.991607	4	1
14	5	1-3-1	2013-06-20 18:19:09.819748	5	1
15	5	1-3-4	2013-06-20 18:20:29.186812	5	1
16	5	1-3-7	2013-06-20 18:31:01.484868	6	1
17	6	1-3-10	2013-06-20 18:32:02.424953	6	1
18	6	1-3-12	2013-06-20 18:33:06.692516	6	1
19	9	1-4-1	2013-06-20 18:46:36.13507	\N	1
20	7	1-4-3	2013-06-20 18:48:09.372839	\N	1
21	9	1-4-5	2013-06-20 18:50:12.237212	\N	1
22	8	1-4-7	2013-06-20 18:51:56.670504	\N	1
33	14	2-6-1	2013-06-20 22:11:21.109807	\N	3
34	14	2-6-4	2013-06-20 22:12:56.593863	\N	3
35	15	2-6-7	2013-06-20 22:14:16.331761	\N	3
36	16	2-6-10	2013-06-20 22:15:04.641209	\N	3
37	17	2-6-14	2013-06-20 22:17:07.388567	\N	3
23	10	2-5-1	2013-06-20 21:51:39.60636	7	3
24	10	2-5-4	2013-06-20 21:52:16.799291	7	3
25	11	2-5-7	2013-06-20 21:52:56.522616	8	3
26	11	2-5-10	2013-06-20 21:53:32.753009	8	3
27	11	2-5-13	2013-06-20 21:54:15.026001	8	3
31	10	2-5-23	2013-06-20 22:03:28.583306	9	3
28	12	2-5-15	2013-06-20 21:55:13.504395	9	3
29	12	2-5-17	2013-06-20 21:55:52.013532	9	3
30	12	2-5-21	2013-06-20 22:02:39.81833	9	3
32	13	2-5-26	2013-06-20 22:04:44.634957	10	3
38	18	2-7-1	2013-06-20 22:26:45.814953	\N	1
39	19	2-7-3	2013-06-20 22:27:56.923618	\N	1
40	18	2-7-5	2013-06-20 22:28:41.341282	\N	1
41	20	2-7-7	2013-06-20 22:29:44.698716	\N	1
42	20	2-7-9	2013-06-20 22:30:36.686046	\N	1
43	20	2-7-11	2013-06-20 22:31:30.364325	\N	1
44	21	2-7-13	2013-06-20 22:32:36.81941	\N	1
45	23	3-8-1	2013-06-21 18:04:16.09045	11	3
46	23	3-8-4	2013-06-21 18:04:59.537703	12	3
47	24	3-8-7	2013-06-21 18:05:43.828379	12	3
48	23	3-8-10	2013-06-21 18:07:00.687042	13	3
49	26	3-9-1	2013-06-21 18:09:35.861741	14	3
50	25	3-9-5	2013-06-21 18:12:19.527835	15	3
51	26	3-9-8	2013-06-21 18:13:59.402721	15	3
12	4	1-2-14	2013-06-20 18:09:12.463724	16	1
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('item_id_seq', 51, true);


--
-- Data for Name: item_peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item_peticion (peticion_id, item_id, actual) FROM stdin;
1	74	t
1	96	t
1	85	t
\.


--
-- Data for Name: lineabase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lineabase (id, creador_id, "fechaCreacion", numero, comentario, fase_id, estado) FROM stdin;
1	1	2013-06-20 17:53:47.843473	1	Mejoras sobre las arquitecturas anteriores	1	Cerrada
2	1	2013-06-20 17:55:16.764845	2	Requisitos para el diseño completos	1	Cerrada
3	1	2013-06-20 18:12:26.040068	1	Extensiones para las versiones High Performance listas	2	Cerrada
4	1	2013-06-20 18:13:03.043264	2	Listo para Manufacturar	2	Cerrada
5	1	2013-06-20 18:35:42.099525	1	Versiones Especiales	3	Cerrada
6	1	2013-06-20 18:36:56.642727	2	Edición Regular Lista	3	Cerrada
7	3	2013-06-20 22:19:28.929864	1	LB1 Círculos	5	Cerrada
8	2	2013-06-20 22:20:17.896598	2	LB2 Triángulos	5	Cerrada
9	2	2013-06-20 22:21:05.294064	3	LB3 Cuadrados y un Círculo	5	Cerrada
10	2	2013-06-20 22:21:43.142788	4	LB5 Linea recta	5	Cerrada
11	3	2013-06-21 18:07:48.903639	1	Ya estudió Cálculo	8	Cerrada
12	3	2013-06-21 18:08:27.629569	2	Ya estudió Física	8	Cerrada
13	3	2013-06-21 18:08:45.542622	3	Ya sabe integrar	8	Cerrada
14	3	2013-06-21 18:16:03.666131	1	Pasó Cálculo	9	Cerrada
15	3	2013-06-21 18:16:37.264212	2	Firma en Física II	9	Cerrada
16	1	2013-06-20 18:18:40.369097	3	Tecnología Mobile lista	2	Cerrada
\.


--
-- Name: lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('lineabase_id_seq', 16, true);


--
-- Data for Name: miembro; Type: TABLE DATA; Schema: public; Owner: -
--

COPY miembro (proyecto_id, user_id) FROM stdin;
1	1
1	2
1	3
2	3
2	1
2	2
3	3
\.


--
-- Data for Name: peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY peticion (id, numero, proyecto_id, comentario, estado, usuario_id, "cantVotos", "cantItems", "costoT", "dificultadT", "fechaCreacion", "fechaEnvio", acciones) FROM stdin;
1	1	2	valores desactualizados	EnVotacion	1	2	3	72750	86	2013-06-20 22:35:03.267763	2013-06-20 22:35:13.013197	1
\.


--
-- Name: peticion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('peticion_id_seq', 1, true);


--
-- Data for Name: proyecto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY proyecto (id, nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado) FROM stdin;
1	BroadWell	4	2013-06-01 00:00:00	2014-06-01 00:00:00	\N	1	Iniciado
2	Geometría	3	2013-06-01 00:00:00	2013-09-01 00:00:00	\N	3	Iniciado
3	Semestre	2	2013-06-21 17:51:49.541762	2013-07-01 00:00:00	\N	3	Iniciado
\.


--
-- Name: proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('proyecto_id_seq', 3, true);


--
-- Data for Name: relacion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY relacion (id, ante_id, post_id, tipo) FROM stdin;
1	20	5	P-H
2	8	18	P-H
3	16	18	P-H
4	10	16	P-H
5	21	5	P-H
6	20	22	P-H
7	21	22	P-H
8	23	18	P-H
9	24	16	P-H
10	25	16	P-H
11	26	18	P-H
12	10	26	P-H
13	24	26	P-H
14	25	26	P-H
15	8	27	P-H
16	16	27	P-H
17	23	27	P-H
18	26	27	P-H
19	22	29	A-S
20	22	30	A-S
21	22	33	A-S
22	22	34	A-S
23	27	36	A-S
24	27	37	A-S
25	34	39	P-H
26	37	39	P-H
27	34	40	P-H
28	37	40	P-H
29	34	42	P-H
30	40	44	P-H
31	40	45	P-H
32	30	47	A-S
33	30	48	A-S
34	42	50	A-S
35	51	50	A-S
36	34	51	P-H
37	42	52	A-S
38	51	52	A-S
39	45	54	A-S
40	45	55	A-S
41	45	57	A-S
42	57	58	P-H
43	59	58	P-H
44	45	59	A-S
45	57	60	P-H
46	59	60	P-H
47	48	62	A-S
48	48	64	A-S
49	52	64	A-S
50	55	66	A-S
51	59	68	A-S
52	48	69	A-S
53	52	69	A-S
54	48	70	A-S
55	55	71	A-S
56	74	76	P-H
57	74	77	P-H
58	80	84	P-H
59	83	84	P-H
60	80	85	P-H
61	83	85	P-H
62	87	89	P-H
63	90	89	P-H
64	87	91	P-H
65	90	91	P-H
66	96	93	P-H
67	91	93	P-H
68	77	100	A-S
69	77	101	A-S
70	101	103	P-H
71	101	104	P-H
72	104	106	P-H
73	104	107	P-H
74	85	107	A-S
75	104	110	P-H
76	85	110	A-S
77	96	109	A-S
78	96	111	A-S
79	98	113	A-S
80	96	114	P-H
81	91	114	P-H
82	115	113	A-S
83	98	116	A-S
84	115	116	A-S
85	110	118	A-S
86	118	120	P-H
87	118	122	P-H
88	111	124	A-S
89	124	126	P-H
90	124	128	P-H
91	116	126	A-S
92	136	138	P-H
93	136	139	P-H
94	133	144	A-S
95	133	145	A-S
96	133	146	A-S
97	139	148	A-S
98	139	149	A-S
99	149	151	P-H
100	142	151	A-S
101	149	152	P-H
102	142	152	A-S
\.


--
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('relacion_id_seq', 102, true);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Jefe de Ingeniería	111	1000	1
2	1	Analista	0	11110111	0
3	2	Arquitecto HW	0	11110111	0
4	2	Jefe de Ingeniería	111	1000	1
5	3	Ingeniero	0	11110111	0
6	3	Jefe de Ingeniería	111	1000	1
7	4	Jefe de Ingeniería	111	11111111	1
8	5	Dibujante	0	11110111	0
9	5	Artista	111	1000	1
10	6	Diseñador	0	11110111	0
11	6	Artesano	111	1000	1
12	7	Escultor	0	11110111	0
13	7	Diseñador	111	1000	1
14	8	Estudiante	111	11111111	1
15	9	Estudiante	111	11111111	1
\.


--
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rol_id_seq', 15, true);


--
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY tipoitem (id, nombre, comentario, defase, "fechaCreacion", "fechaModificacion", usuario_creador_id, usuario_modificador_id) FROM stdin;
1	Análisis	Análisis de recursos y requisitos para la fabricación de microprocesadores	1	2013-06-20 17:27:30.755838	2013-06-20 17:27:30.755838	1	1
2	Requisitos	Requisitos a cumplir para el desarrollo de microprocesadores	1	2013-06-20 17:35:40.173451	2013-06-20 17:35:40.173451	1	1
3	Diseño Lógico	Diseño logico del ISA y la microarquitectura	2	2013-06-20 17:58:28.37556	2013-06-20 17:58:28.37556	1	1
4	Diseño Físico	Diseño del hardware del microprocesador	2	2013-06-20 17:59:59.708495	2013-06-20 17:59:59.708495	1	1
5	Microprocesador	Una obra maestra de la ingeniería	3	2013-06-20 18:16:38.245558	2013-06-20 18:16:38.245558	1	1
6	Documentación	Documentación de la pieza desarrollada	3	2013-06-20 18:18:00.588953	2013-06-20 18:18:00.588953	1	1
7	Prueba de Hardware	Pruebas sobre el hardware del componente	4	2013-06-20 18:40:29.415426	2013-06-20 18:40:29.415426	1	1
8	Homologación	Cumple con las normas y estándares propuestos	4	2013-06-20 18:42:46.825432	2013-06-20 18:42:46.825432	1	1
9	Rendimiento	Pruebas de rendimiento del nuevo microprocesador	4	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	1	1
10	Círculo	Conjunto de puntos equidistantes de un punto (centro)	5	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
11	Triángulo	Polígono cerrado de tres lados	5	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
12	Cuadrado	Polígono cerrado de cuatro lados iguales	5	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
13	Linea	Conjunto infinito de puntos que une dos puntos cualesquiera	5	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
14	Rectángulo	Un cuadrilatero con dos medias a y b	6	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
15	Pentágono	Poligono regular de cinco lados	6	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
16	Elipse	conjunto de puntos cuya suma de la distancia a dos puntos es constante	6	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
17	Cruz	Líneas que se cruzan	6	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
18	Hexágono	Polígono cerrado de seis lados	7	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
19	Octógono	Polígono cerrado de ocho lados	7	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
20	Amorfo	Figura Amorfa	7	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
21	Estrella	Estrella hecha con trazos	7	2013-06-20 18:43:39.53496	2013-06-20 18:43:39.53496	2	2
23	Libro	Un viejo volumen de textos arcanos	8	2013-06-21 17:58:50.527765	2013-06-21 17:58:50.527765	3	3
24	Cuaderno	Notas fugaces de un estudiante poco atento	8	2013-06-21 18:00:26.990259	2013-06-21 18:00:26.990259	3	3
25	TP	Trabajo Práctico	9	2013-06-21 18:01:41.752801	2013-06-21 18:01:41.752801	3	3
26	Examen	Prueba final en un arte o disciplina	9	2013-06-21 18:03:24.84732	2013-06-21 18:03:24.84732	3	3
\.


--
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipoitem_id_seq', 26, true);


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
1	1
3	1
1	2
2	2
1	3
2	3
1	4
3	4
1	5
2	5
3	6
1	6
1	7
2	7
3	7
1	8
3	8
3	9
2	9
1	10
3	10
3	11
2	11
3	13
2	13
1	12
3	12
3	14
3	15
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: -
--

COPY usuario (id, nombre, nombredeusuario, clave, "isAdmin") FROM stdin;
1	Administrador	admin	7c4a8d09ca3762af61e59520943dc26494f8941b	t
2	Martin Poletti	martin	54669547a225ff20cba8b75a4adca540eef25858	f
3	Natalia Valdez	natalia	2298625f2ba17912b286ad9afd8f089e460241b9	t
4	Dan Tor	dan	7c4a8d09ca3762af61e59520943dc26494f8941b	f
5	Anna Dyst	anna	7c4a8d09ca3762af61e59520943dc26494f8941b	f
6	Ryunosuke Asakura	ryu	7c4a8d09ca3762af61e59520943dc26494f8941b	f
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
3	2	t
3	3	t
3	4	f
3	5	t
3	6	f
3	7	f
3	8	t
6	9	f
6	10	f
6	11	f
6	12	f
6	13	f
6	14	f
6	15	f
6	16	f
6	17	t
6	18	t
3	19	f
3	20	t
3	21	t
3	22	t
3	23	t
6	24	f
6	25	f
6	26	f
6	27	t
7	28	f
10	28	f
7	29	t
10	29	f
7	30	t
10	30	f
7	31	f
10	31	f
7	32	t
10	32	t
7	33	t
10	33	t
7	34	t
10	34	t
7	35	f
10	35	f
7	36	t
10	36	f
7	37	t
10	37	f
14	38	f
14	39	t
14	40	t
14	41	f
14	42	t
7	43	f
10	43	f
7	44	f
10	44	f
7	45	f
10	45	f
17	46	f
18	46	f
17	47	f
18	47	t
17	48	f
18	48	t
17	49	f
18	49	f
17	50	t
18	50	f
14	51	t
17	52	t
18	52	f
17	53	f
18	53	f
17	54	f
18	54	f
17	55	f
18	55	f
19	56	f
19	57	f
19	58	f
19	59	f
19	60	f
28	61	f
28	62	t
23	63	f
23	64	t
28	65	f
28	66	t
25	67	f
25	68	t
23	69	t
28	70	t
28	71	t
30	72	f
30	73	t
30	74	t
30	75	f
30	76	f
30	77	f
36	78	f
36	79	f
36	80	f
36	81	f
36	82	f
36	83	f
36	84	f
36	85	f
30	94	f
30	95	t
30	96	t
38	97	f
38	98	f
53	112	f
53	113	t
38	115	f
53	116	t
54	117	f
54	118	t
54	121	f
54	122	f
62	123	f
62	124	f
62	125	f
62	126	f
62	127	f
62	128	t
64	129	f
64	130	t
70	137	f
70	138	f
70	139	f
78	143	f
78	144	t
78	145	t
78	146	t
72	147	f
75	147	f
72	148	t
75	148	t
72	149	t
75	149	t
78	150	f
78	151	t
78	152	t
\.


--
-- Data for Name: valordate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valordate (atributo_id, item_id, valor) FROM stdin;
1	1	\N
1	2	2013-06-02 00:00:00
1	3	\N
1	4	\N
1	5	2013-06-01 00:00:00
1	6	\N
1	7	2013-06-05 00:00:00
1	8	2013-06-05 00:00:00
1	19	\N
1	20	2013-06-02 00:00:00
1	21	\N
1	22	\N
1	23	\N
11	28	\N
11	29	2013-09-02 00:00:00
11	30	\N
11	31	\N
11	32	2013-09-06 00:00:00
11	33	2013-09-06 00:00:00
11	34	\N
11	35	\N
11	36	2013-09-07 00:00:00
11	37	\N
12	38	\N
12	39	2013-09-10 00:00:00
12	40	\N
12	41	\N
12	42	2013-09-20 00:00:00
11	43	\N
11	44	2013-09-27 00:00:00
11	45	\N
12	51	\N
44	99	\N
44	100	2013-07-05 00:00:00
44	101	\N
44	102	\N
44	103	2013-06-19 00:00:00
44	104	\N
46	105	\N
46	106	2013-07-20 00:00:00
46	107	\N
46	110	\N
57	117	\N
57	118	2013-08-10 00:00:00
57	121	\N
57	122	2013-08-10 00:00:00
61	123	\N
61	124	2013-08-11 00:00:00
61	125	\N
61	126	2013-08-12 00:00:00
61	127	\N
61	128	2013-08-13 00:00:00
66	129	\N
66	130	2013-08-25 00:00:00
71	137	\N
71	138	2013-06-19 00:00:00
71	139	\N
\.


--
-- Data for Name: valorfile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorfile (id, item_id, valor, nombre) FROM stdin;
\.


--
-- Name: valorfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('valorfile_id_seq', 1, false);


--
-- Data for Name: valorint; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorint (atributo_id, item_id, valor) FROM stdin;
4	9	0
4	10	1
4	11	0
4	12	2
4	13	0
4	14	3
4	15	2
4	16	2
4	17	3
4	18	3
4	24	1
4	25	1
4	26	2
4	27	3
15	46	0
15	47	1
15	48	1
15	49	0
15	50	3
15	52	3
15	53	0
15	54	1
15	55	1
26	61	0
26	62	5
21	63	0
21	64	5
26	65	0
26	66	3
21	69	5
26	70	5
26	71	3
29	72	0
29	73	1
29	74	1
29	75	0
29	76	2
29	77	2
33	78	0
34	78	0
35	78	0
33	79	5
34	79	5
35	79	2
33	80	5
34	80	5
35	80	2
33	81	0
34	81	0
35	81	0
33	82	5
34	82	4
35	82	3
33	83	5
34	83	4
35	83	3
33	84	0
34	84	0
35	84	0
33	85	0
34	85	0
35	85	0
31	86	0
31	87	3
31	88	0
31	89	3
31	90	3
31	91	3
31	92	0
31	93	4
29	94	0
29	95	3
29	96	3
37	97	0
37	98	7
40	99	0
41	99	0
40	100	2
41	100	4
40	101	2
41	101	4
40	102	0
41	102	0
40	103	5
41	103	6
40	104	5
41	104	6
45	105	0
45	106	5
45	107	5
47	108	0
48	108	0
47	109	7
48	109	5
45	110	5
47	111	7
48	111	5
50	112	0
51	112	0
52	112	0
50	113	2
51	113	4
52	113	4
31	114	4
37	115	7
50	116	2
51	116	4
52	116	4
55	117	0
55	118	4
58	119	0
58	120	4
55	121	0
55	122	7
63	129	0
63	130	5
68	131	0
68	132	2
68	133	2
68	134	0
68	135	4
68	136	4
69	137	0
69	138	20
69	139	20
68	140	0
68	141	2
68	142	2
76	147	0
76	148	95
76	149	95
\.


--
-- Data for Name: valorstr; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorstr (atributo_id, item_id, valor) FROM stdin;
2	1	
2	2	Análisis de las instalaciones industriales
2	3	Análisis de las instalaciones industriales
2	4	
2	5	Se proponen y analizan mejoras a las arquitecturas anteriores
2	6	
2	7	Análisis de la temperatura que generaría el procesador
2	8	Análisis de la temperatura que generaría el procesador
5	9	
5	10	Análisis y busqueda de suelos ricos en minerales (cuarzo)
5	11	
5	12	Obtención de obleas de cuarzo
5	13	
5	14	Prueba térmica sobre las obleas de cuarzo
5	15	Obtención de obleas de cuarzo
5	16	Obtención de obleas de cuarzo
5	17	Prueba térmica sobre las obleas de cuarzo
5	18	Prueba térmica sobre las obleas de cuarzo
2	19	
2	20	Análisis de las arquitecturas anteriores de microprocesadores
2	21	Análisis de las arquitecturas anteriores de microprocesadores
2	22	Se proponen y analizan mejoras a las arquitecturas anteriores
2	23	Análisis de la temperatura que generaría el procesador
5	24	Análisis y busqueda de suelos ricos en minerales (cuarzo)
5	25	Análisis y busqueda de suelos ricos en minerales (cuarzo)
5	26	Obtención de obleas de cuarzo
5	27	Prueba térmica sobre las obleas de cuarzo
9	28	
9	29	Extensiones agregadas a la arquitectura
9	30	Extensiones agregadas a la arquitectura
9	31	
9	32	Esquemático que describe los circutios en el integrado
9	33	Esquemático que describe los circutios en el integrado
9	34	Esquemático que describe los circutios en el integrado
9	35	
9	36	Especificación de la tolerancia y los límites del nuevo hardware
9	37	Especificación de la tolerancia y los límites del nuevo hardware
13	38	
13	39	BROADWELL
13	40	BROADWELL
13	41	
13	42	MOBILE
9	43	
9	44	Documenta y especifica el ISA del microprocesador
9	45	Documenta y especifica el ISA del microprocesador
16	46	
16	47	FULLWELL
16	48	FULLWELL
16	49	
16	50	SOURCEWELL
13	51	MOBILE
16	52	SOURCEWELL
16	53	
16	54	BROADWELL
16	55	BROADWELL
20	56	
20	57	Manual para implementadores y diseñadores de compiladores
20	58	
20	59	Manual para implementadores y diseñadores de compiladores
20	60	
27	61	
27	62	Operaciones en punto flotante para el microprocesador
22	63	
22	64	Prueba de los límites térmicos del encapsulado
27	65	
27	66	Pruebas de operaciones enteras, producto matriz vector para el microprocesador
24	67	
24	68	Implementación del ISA para el compilador gcc
22	69	Prueba de los límites térmicos del encapsulado
27	70	Operaciones en punto flotante para el microprocesador
27	71	Pruebas de operaciones enteras, producto matriz vector para el microprocesador
32	86	
32	87	Cuadrado Inicial
32	88	
32	89	Cuadrado número 2 
32	90	Cuadrado Inicial
32	91	Cuadrado número 2 
32	92	
32	93	El último cuadrado
39	97	
39	98	Una linea recta de
43	99	
43	100	rectángulo primal
43	101	rectángulo primal
43	102	
43	103	Rectángulo dual
43	104	Rectángulo dual
49	108	
49	109	Elipse Excéntrica
49	111	Elipse Excéntrica
32	114	El último cuadrado
39	115	Una linea recta de
56	117	
56	118	Héxagono primal
59	119	
59	120	Octógono final
56	121	
56	122	Héxagono inestable
60	123	
60	124	Figura Amorfa de primer nivel
60	125	
60	126	Figura Amorfa giratoria
60	127	
60	128	Sólido amorfo de revolución
65	129	
65	130	Pentagrama punteado
67	131	
67	132	Piskunov
67	133	Piskunov
67	134	
67	135	Sears
67	136	Sears
67	140	
67	141	Piskunov
67	142	Piskunov
77	143	
77	144	Cálculo I
77	145	Cálculo I
77	146	Cálculo I
77	150	
77	151	Física II
77	152	Física II
\.


--
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, "fechaModificacion", deitem, usuario_modificador_id) FROM stdin;
1	0	Instalaciones	Activo	f	14000	12	2013-06-20 17:36:50.405986	1	1
2	1	Instalaciones	Activo	f	14000	12	2013-06-20 17:37:15.228663	1	1
3	2	Instalaciones	Eliminado	t	14000	12	2013-06-20 17:39:31.973182	1	1
4	0	Mejoras	Activo	f	30000	10	2013-06-20 17:42:00.421074	2	1
6	0	Temperatura	Activo	f	10000	13	2013-06-20 17:43:05.851946	3	1
7	1	Temperatura	Activo	f	10000	13	2013-06-20 17:43:39.72127	3	1
9	0	Minerales	Activo	f	500000	10	2013-06-20 17:44:29.81556	4	1
11	0	Cuarzo	Activo	f	100000	15	2013-06-20 17:45:18.700759	5	1
13	0	Prueba Térmica	Activo	f	100000	19	2013-06-20 17:46:43.969808	6	1
12	1	Cuarzo	Activo	f	100000	15	2013-06-20 17:45:49.263322	5	1
15	2	Cuarzo	Activo	f	100000	15	2013-06-20 17:47:18.478895	5	1
14	1	Prueba Térmica	Activo	f	100000	19	2013-06-20 17:47:11.994942	6	1
17	2	Prueba Térmica	Activo	f	100000	19	2013-06-20 17:47:34.32786	6	1
19	0	Arq. Anteriores	Activo	f	13000	10	2013-06-20 17:49:01.904475	7	1
20	1	Arq. Anteriores	Activo	f	13000	10	2013-06-20 17:49:26.246358	7	1
5	1	Mejoras	Activo	f	30000	10	2013-06-20 17:42:27.009978	2	1
8	2	Temperatura	Activo	f	10000	13	2013-06-20 17:43:51.444928	3	1
10	1	Minerales	Activo	f	500000	10	2013-06-20 17:44:56.411065	4	1
24	2	Minerales	Activo	f	500000	10	2013-06-20 17:52:45.901596	4	1
16	3	Cuarzo	Activo	f	100000	15	2013-06-20 17:47:26.672209	5	1
18	3	Prueba Térmica	Activo	f	100000	19	2013-06-20 17:48:08.890503	6	1
21	2	Arq. Anteriores	Bloqueado	t	13000	10	2013-06-20 17:51:53.589317	7	1
22	2	Mejoras	Bloqueado	t	30000	10	2013-06-20 17:52:04.318766	2	1
23	3	Temperatura	Bloqueado	t	10000	13	2013-06-20 17:52:37.154051	3	1
25	3	Minerales	Bloqueado	t	500000	10	2013-06-20 17:53:00.20785	4	1
26	4	Cuarzo	Bloqueado	t	100000	15	2013-06-20 17:53:08.206306	5	1
27	4	Prueba Térmica	Bloqueado	t	100000	19	2013-06-20 17:53:20.128584	6	1
28	0	Extensiones	Activo	f	10000	3	2013-06-20 18:02:38.524235	8	1
29	1	Extensiones	Activo	f	10000	3	2013-06-20 18:03:08.287948	8	1
31	0	Esquemático	Activo	f	10000	5	2013-06-20 18:03:57.796369	9	1
32	1	Esquemático	Activo	f	10000	5	2013-06-20 18:04:46.291644	9	1
33	2	Esquemático	Activo	f	10000	5	2013-06-20 18:04:51.767846	9	1
35	0	Tolerancia y Límites	Activo	f	50000	7	2013-06-20 18:06:23.476064	10	1
36	1	Tolerancia y Límites	Activo	f	50000	7	2013-06-20 18:07:02.565662	10	1
38	0	Prototipo	Activo	f	75000	9	2013-06-20 18:07:46.139315	11	1
39	1	Prototipo	Activo	f	75000	9	2013-06-20 18:08:09.657044	11	1
41	0	Empotrado	Activo	f	15000	3	2013-06-20 18:09:12.463724	12	1
43	0	WhiteCard	Activo	f	20000	5	2013-06-20 18:10:19.991607	13	1
44	1	WhiteCard	Activo	f	20000	5	2013-06-20 18:11:01.279992	13	1
30	2	Extensiones	Bloqueado	t	10000	3	2013-06-20 18:03:31.314716	8	1
34	3	Esquemático	Bloqueado	t	10000	5	2013-06-20 18:05:36.105505	9	1
37	2	Tolerancia y Límites	Bloqueado	t	50000	7	2013-06-20 18:07:25.10511	10	1
40	2	Prototipo	Bloqueado	t	75000	9	2013-06-20 18:08:42.240532	11	1
45	2	WhiteCard	Bloqueado	t	20000	5	2013-06-20 18:11:42.333081	13	1
46	0	Extreme	Activo	f	100000	3	2013-06-20 18:19:09.819748	14	1
47	1	Extreme	Activo	f	100000	3	2013-06-20 18:19:31.218749	14	1
49	0	Mobile	Activo	f	75000	7	2013-06-20 18:20:29.186812	15	1
42	1	Empotrado	Activo	f	15000	3	2013-06-20 18:09:35.589538	12	1
50	1	Mobile	Activo	f	75000	7	2013-06-20 18:20:48.385835	15	1
53	0	Normal	Activo	f	50000	4	2013-06-20 18:31:01.484868	16	1
54	1	Normal	Activo	f	50000	4	2013-06-20 18:31:14.675961	16	1
56	0	Manua de Ref.	Activo	f	10000	3	2013-06-20 18:32:02.424953	17	1
57	1	Manua de Ref.	Activo	f	10000	3	2013-06-20 18:32:22.115822	17	1
58	0	Errata	Activo	f	5000	1	2013-06-20 18:33:06.692516	18	1
48	2	Extreme	Bloqueado	t	100000	3	2013-06-20 18:20:04.777671	14	1
52	2	Mobile	Bloqueado	t	75000	7	2013-06-20 18:30:25.72217	15	1
55	2	Normal	Bloqueado	t	50000	4	2013-06-20 18:31:43.234811	16	1
59	2	Manua de Ref.	Bloqueado	t	10000	3	2013-06-20 18:35:18.844707	17	1
60	1	Errata	Bloqueado	t	5000	1	2013-06-20 18:35:26.666884	18	1
61	0	Op. Punto flotante	Activo	f	10000	3	2013-06-20 18:46:36.13507	19	1
63	0	Barrera Térmica	Activo	f	30000	4	2013-06-20 18:48:09.372839	20	1
65	0	Op. Matriz Vector	Activo	f	10000	5	2013-06-20 18:50:12.237212	21	1
67	0	Compilador	Activo	f	50000	7	2013-06-20 18:51:56.670504	22	1
68	1	Compilador	Activo	t	50000	7	2013-06-20 18:52:57.455876	22	1
64	1	Barrera Térmica	Activo	f	30000	4	2013-06-20 18:49:03.995228	20	1
69	2	Barrera Térmica	Aprobado	t	30000	4	2013-06-20 18:53:24.476937	20	1
62	1	Op. Punto flotante	Activo	f	10000	3	2013-06-20 18:46:59.324532	19	1
70	2	Op. Punto flotante	Aprobado	t	10000	3	2013-06-20 18:53:39.873213	19	1
66	1	Op. Matriz Vector	Activo	f	10000	5	2013-06-20 18:51:33.196187	21	1
71	2	Op. Matriz Vector	Aprobado	t	10000	5	2013-06-20 18:53:49.131452	21	1
72	0	C1	Activo	f	1000	1	2013-06-20 21:51:39.60636	23	3
73	1	C1	Activo	f	1000	1	2013-06-20 21:51:49.284114	23	3
75	0	C2	Activo	f	1000	2	2013-06-20 21:52:16.799291	24	3
76	1	C2	Activo	f	1000	2	2013-06-20 21:52:22.816052	24	3
78	0	T1	Activo	f	1500	3	2013-06-20 21:52:56.522616	25	3
79	1	T1	Activo	f	1500	3	2013-06-20 21:53:09.907169	25	3
81	0	T2	Activo	f	1650	4	2013-06-20 21:53:32.753009	26	3
82	1	T2	Activo	f	1650	4	2013-06-20 21:53:43.090466	26	3
84	0	T3	Activo	f	1500	5	2013-06-20 21:54:15.026001	27	3
86	0	Q1	Activo	f	2000	2	2013-06-20 21:55:13.504395	28	3
88	0	Q2	Activo	f	2000	2	2013-06-20 21:55:52.013532	29	3
87	1	Q1	Activo	f	2000	2	2013-06-20 21:55:30.052163	28	3
89	1	Q2	Activo	f	2000	2	2013-06-20 21:59:45.230088	29	3
92	0	Q3	Activo	f	2000	2	2013-06-20 22:02:39.81833	30	3
94	0	C3	Activo	f	750	3	2013-06-20 22:03:28.583306	31	3
95	1	C3	Activo	f	750	3	2013-06-20 22:03:49.983897	31	3
97	0	L1	Activo	f	250	1	2013-06-20 22:04:44.634957	32	3
98	1	L1	Activo	f	250	1	2013-06-20 22:05:07.967524	32	3
74	2	C1	Bloqueado	t	1000	1	2013-06-20 21:51:57.863883	23	3
77	2	C2	Bloqueado	t	1000	2	2013-06-20 21:52:38.220282	24	3
80	2	T1	Bloqueado	t	1500	3	2013-06-20 21:53:16.961116	25	3
83	2	T2	Bloqueado	t	1650	4	2013-06-20 21:53:50.219905	26	3
85	1	T3	Bloqueado	t	1500	5	2013-06-20 21:54:45.005402	27	3
96	2	C3	Bloqueado	t	750	3	2013-06-20 22:03:58.948516	31	3
90	2	Q1	Bloqueado	t	2000	2	2013-06-20 22:01:54.180685	28	3
91	2	Q2	Bloqueado	t	2000	2	2013-06-20 22:02:04.420774	29	3
99	0	R1	Activo	f	2500	4	2013-06-20 22:11:21.109807	33	3
101	2	R1	Aprobado	t	2500	4	2013-06-20 22:12:31.503573	33	3
102	0	R2	Activo	f	2500	4	2013-06-20 22:12:56.593863	34	3
104	2	R2	Aprobado	t	2500	4	2013-06-20 22:13:36.686206	34	3
105	0	P1	Activo	f	5000	7	2013-06-20 22:14:16.331761	35	3
108	0	E1	Activo	f	2500	6	2013-06-20 22:15:04.641209	36	3
107	2	P1	Revision	f	5000	7	2013-06-20 22:14:49.011936	35	3
100	1	R1	Activo	f	2500	4	2013-06-20 22:11:45.906989	33	3
103	1	R2	Activo	f	2500	4	2013-06-20 22:13:17.535024	34	3
106	1	P1	Activo	f	5000	7	2013-06-20 22:14:32.668523	35	3
110	3	P1	Aprobado	t	5000	7	2013-06-20 22:16:23.981573	35	3
109	1	E1	Activo	f	2500	6	2013-06-20 22:15:28.678518	36	3
111	2	E1	Aprobado	t	2500	6	2013-06-20 22:16:44.133291	36	3
112	0	X1	Activo	f	1250	2	2013-06-20 22:17:07.388567	37	3
93	1	Q3	Activo	f	2000	2	2013-06-20 22:02:56.441996	30	3
113	1	X1	Activo	f	1250	2	2013-06-20 22:17:27.026093	37	3
116	2	X1	Aprobado	t	1250	2	2013-06-20 22:19:15.721253	37	3
114	2	Q3	Bloqueado	t	2000	2	2013-06-20 22:18:47.760786	30	3
115	2	L1	Bloqueado	t	250	1	2013-06-20 22:18:57.850142	32	3
117	0	H1	Activo	f	4500	6	2013-06-20 22:26:45.814953	38	1
118	1	H1	Activo	t	4500	6	2013-06-20 22:27:15.120765	38	1
119	0	O1	Activo	f	7000	9	2013-06-20 22:27:56.923618	39	1
120	1	O1	Activo	t	7000	9	2013-06-20 22:28:16.880583	39	1
121	0	H2	Activo	f	7500	9	2013-06-20 22:28:41.341282	40	1
122	1	H2	Activo	t	7500	9	2013-06-20 22:29:06.503349	40	1
123	0	A1	Activo	f	10000	9	2013-06-20 22:29:44.698716	41	1
124	1	A1	Activo	t	10000	9	2013-06-20 22:30:08.013095	41	1
125	0	A2	Activo	f	10000	9	2013-06-20 22:30:36.686046	42	1
126	1	A2	Activo	t	10000	9	2013-06-20 22:30:56.160752	42	1
127	0	A3	Activo	f	15000	10	2013-06-20 22:31:30.364325	43	1
128	1	A3	Activo	t	15000	10	2013-06-20 22:31:51.617826	43	1
129	0	S1	Activo	f	15000	10	2013-06-20 22:32:36.81941	44	1
130	1	S1	Activo	t	15000	10	2013-06-20 22:33:10.038023	44	1
131	0	Cálculo Infinitesima	Activo	f	35000	7	2013-06-21 18:04:16.09045	45	3
132	1	Cálculo Infinitesima	Activo	f	35000	7	2013-06-21 18:04:28.262483	45	3
134	0	Física	Activo	f	45000	5	2013-06-21 18:04:59.537703	46	3
135	1	Física	Activo	f	45000	5	2013-06-21 18:05:09.06256	46	3
137	0	Física II	Activo	f	2500	8	2013-06-21 18:05:43.828379	47	3
138	1	Física II	Activo	f	2500	8	2013-06-21 18:05:57.332014	47	3
140	0	Cálculo Integral	Activo	f	35000	9	2013-06-21 18:07:00.687042	48	3
141	1	Cálculo Integral	Activo	f	35000	9	2013-06-21 18:07:12.382311	48	3
133	2	Cálculo Infinitesima	Bloqueado	t	35000	7	2013-06-21 18:04:39.765972	45	3
136	2	Física	Bloqueado	t	45000	5	2013-06-21 18:05:16.755639	46	3
139	2	Física II	Bloqueado	t	2500	8	2013-06-21 18:06:18.225172	47	3
142	2	Cálculo Integral	Bloqueado	t	35000	9	2013-06-21 18:07:21.016267	48	3
143	0	Final 1	Activo	f	4500	9	2013-06-21 18:09:35.861741	49	3
144	1	Final 1	Activo	f	4500	9	2013-06-21 18:09:44.827203	49	3
145	2	Final 1	Aprobado	f	4500	9	2013-06-21 18:11:07.287767	49	3
147	0	Electromagnetismo	Activo	f	2450	6	2013-06-21 18:12:19.527835	50	3
148	1	Electromagnetismo	Activo	f	2450	6	2013-06-21 18:12:32.311323	50	3
150	0	Recuperatorio	Activo	f	2450	9	2013-06-21 18:13:59.402721	51	3
151	1	Recuperatorio	Activo	f	2450	9	2013-06-21 18:14:33.655884	51	3
146	3	Final 1	Bloqueado	t	4500	9	2013-06-21 18:11:15.228308	49	3
149	2	Electromagnetismo	Bloqueado	t	2450	6	2013-06-21 18:13:36.7113	50	3
152	2	Recuperatorio	Bloqueado	t	2450	9	2013-06-21 18:15:01.235348	51	3
51	2	Empotrado	Bloqueado	t	15000	3	2013-06-20 18:30:10.85877	12	1
\.


--
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('vitem_id_seq', 152, true);


--
-- Data for Name: voto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY voto (peticion_id, user_id, valor) FROM stdin;
1	1	t
1	2	f
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
    ADD CONSTRAINT valorfile_pkey PRIMARY KEY (id);


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
-- Name: tipoitem_usuario_creador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_usuario_creador_id_fkey FOREIGN KEY (usuario_creador_id) REFERENCES usuario(id);


--
-- Name: tipoitem_usuario_modificador_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipoitem
    ADD CONSTRAINT tipoitem_usuario_modificador_id_fkey FOREIGN KEY (usuario_modificador_id) REFERENCES usuario(id);


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
-- Name: valorfile_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY valorfile
    ADD CONSTRAINT valorfile_item_id_fkey FOREIGN KEY (item_id) REFERENCES item(id);


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

