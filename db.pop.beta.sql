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
11	revision	Fecha	3
12	clave	Cadena	3
13	Interno	Booleano	4
14	revision	Fecha	4
15	descripcion	Cadena	4
16	fabricable	Booleano	4
17	nuevo	Booleano	3
18	Version	Numerico	5
19	Nombre Clave	Cadena	5
20	Revision	Fecha	5
21	Empotrable	Booleano	5
22	Novel	Booleano	5
23	Interno	Booleano	6
24	Notas	Cadena	6
25	tiempo	Numerico	7
26	Notas	Cadena	7
27	Exito	Booleano	7
28	Notas	Cadena	8
30	ISA Compatible	Booleano	8
31	Tiempo	Numerico	9
32	Notas	Cadena	9
33	Mass. Prod. ready	Booleano	9
\.


--
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atributo_id_seq', 33, true);


--
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
1	alfa	1	2013-06-01 00:00:00	2013-09-01 00:00:00	2013-06-18 16:06:56.717407	Abierta	1
2	beta	2	2013-09-02 00:00:00	2013-12-01 00:00:00	2013-06-18 17:28:11.23471	Abierta	1
3	gama	3	2013-12-02 00:00:00	2014-03-01 00:00:00	2013-06-18 17:28:59.816383	Abierta	1
4	delta	4	2014-03-02 00:00:00	2014-06-01 00:00:00	2013-06-18 17:29:28.762774	Abierta	1
\.


--
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('fase_id_seq', 4, true);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item (id, tipo, etiqueta, "fechaCreacion", linea_id, usuario_creador_id) FROM stdin;
2	1	1-1-4	2013-06-18 13:32:31.321181	\N	1
7	2	1-1-15	2013-06-18 13:39:24.550494	\N	1
18	6	1-3-9	2013-06-18 14:58:16.373748	\N	1
4	1	1-1-9	2013-06-18 13:35:10.758247	1	1
5	2	1-1-11	2013-06-18 13:36:47.560435	1	1
6	1	1-1-13	2013-06-18 13:37:59.290193	2	1
1	1	1-1-1	2013-06-18 13:31:33.264764	2	1
3	2	1-1-7	2013-06-18 13:33:58.974538	2	1
9	4	1-2-3	2013-06-18 14:03:26.833141	4	1
13	4	1-2-11	2013-06-18 14:35:20.978521	4	1
8	4	1-2-1	2013-06-18 14:01:53.581885	5	1
11	3	1-2-7	2013-06-18 14:06:12.883895	6	1
12	3	1-2-9	2013-06-18 14:34:29.031991	6	1
10	4	1-2-5	2013-06-18 14:05:03.725902	6	1
14	5	1-3-1	2013-06-18 14:52:30.295589	7	1
16	5	1-3-5	2013-06-18 14:55:31.995324	7	1
15	5	1-3-3	2013-06-18 14:54:01.967011	8	1
17	6	1-3-7	2013-06-18 14:57:24.301069	8	1
19	7	1-4-1	2013-06-18 15:12:21.145149	9	1
20	8	1-4-3	2013-06-18 15:13:13.483027	9	1
21	9	1-4-5	2013-06-18 15:14:30.947849	9	1
22	9	1-4-7	2013-06-18 15:17:55.669804	9	1
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('item_id_seq', 22, true);


--
-- Data for Name: item_peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item_peticion (peticion_id, item_id, actual) FROM stdin;
1	50	t
\.


--
-- Data for Name: lineabase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lineabase (id, creador_id, "fechaCreacion", numero, comentario, fase_id, estado) FROM stdin;
1	1	2013-06-18 16:00:35.398446	1	Optimizado a partir de experiencias anteriores	1	Cerrada
2	1	2013-06-18 16:02:15.856979	2	Cuarzo y su límite conocidos y aprobados	1	Cerrada
4	1	2013-06-18 16:15:41.303258	1	Bases de Diseño establecidas	2	Cerrada
5	1	2013-06-18 17:24:54.621068	2	Listo el whitecard	2	Cerrada
6	1	2013-06-18 17:27:52.035738	3	ready for manufacturing	2	Cerrada
7	1	2013-06-18 17:28:20.031951	1	Modelos especiales	3	Cerrada
8	1	2013-06-18 17:28:43.730294	2	Mainstream Target Ready	3	Cerrada
9	1	2013-06-18 17:29:11.061239	1	Aprobado	4	Cerrada
\.


--
-- Name: lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('lineabase_id_seq', 9, true);


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
1	1	1	El nombre está mal escrito	EnVotacion	1	0	1	673200	121	2013-06-18 17:09:56.134459	2013-06-18 17:10:03.047224	1
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
3	12	14	P-H
4	8	16	P-H
5	14	16	P-H
6	18	24	P-H
7	20	24	P-H
8	24	22	P-H
9	34	46	A-S
10	32	46	A-S
11	32	44	A-S
12	34	44	A-S
14	30	40	A-S
15	36	42	A-S
16	26	30	A-S
17	22	32	A-S
18	28	34	A-S
19	16	20	A-S
20	48	14	P-H
21	49	8	P-H
22	50	16	P-H
23	3	50	P-H
24	49	50	P-H
25	51	16	P-H
26	12	51	P-H
27	48	51	P-H
28	14	52	P-H
29	14	52	P-H
30	52	14	P-H
31	52	14	P-H
32	52	14	P-H
33	53	14	P-H
34	53	14	P-H
35	53	14	P-H
36	14	53	P-H
37	14	53	P-H
38	54	20	A-S
39	8	54	P-H
40	14	54	P-H
41	50	54	P-H
42	51	54	P-H
43	55	24	P-H
44	16	55	A-S
45	54	55	A-S
46	48	28	A-S
47	56	34	A-S
48	48	56	A-S
49	58	46	A-S
51	28	58	A-S
52	56	58	A-S
53	48	57	A-S
54	48	59	A-S
55	59	26	P-H
56	55	26	P-H
57	59	24	P-H
58	60	22	P-H
59	18	60	P-H
60	20	60	P-H
61	55	60	P-H
62	59	60	P-H
63	61	30	A-S
64	59	61	P-H
65	55	61	P-H
66	62	32	A-S
67	24	62	P-H
68	60	62	P-H
69	63	46	A-S
70	63	44	A-S
71	22	63	A-S
72	62	63	A-S
73	64	40	A-S
74	26	64	A-S
75	61	64	A-S
76	62	36	A-S
77	36	38	P-H
78	65	42	A-S
79	65	38	P-H
80	62	65	A-S
81	36	66	P-H
82	65	66	P-H
83	58	40	A-S
84	30	67	A-S
85	64	67	A-S
86	58	67	A-S
87	36	68	A-S
88	65	68	A-S
89	32	69	A-S
90	34	69	A-S
91	63	69	A-S
92	34	70	A-S
93	32	70	A-S
94	58	70	A-S
95	63	70	A-S
\.


--
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('relacion_id_seq', 95, true);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Jefe de Area	111	11111111	1
2	2	Jefe de Area	111	11111111	1
3	3	Jefe de Area	111	11111111	1
4	4	Jefe de Area	111	11111111	1
\.


--
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rol_id_seq', 4, true);


--
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY tipoitem (id, nombre, comentario, defase) FROM stdin;
1	Análisis	Actividades de análisis para la fabricación de procesadores	1
2	Requisito	Actividad pre requisito en el proceso de fabricación de procesadores	1
3	Diseño Físico	Diseño del hardware del microprocesador	2
4	Diseño Lógico	Descripción lógica de la arqutiectura	2
5	Microprocesador	Producto finalmente manufacturado	3
6	Documento	Documentación de lo manufacturado	3
7	Pruebas Hardware	Pruebas físicas sobre el hardware	4
8	Homologación	Se verifica que la documentación describa apropiadamente el ISA	4
9	Rendimiento	Se evalua el rendimiento del nuevo ISA	4
\.


--
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipoitem_id_seq', 9, true);


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
1	1
1	2
1	3
1	4
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
13	17	f
16	17	f
13	18	f
16	18	t
13	19	f
16	19	f
13	20	t
16	20	f
13	21	f
16	21	f
13	22	f
16	22	f
17	23	f
17	24	t
17	25	f
17	26	f
13	27	f
16	27	f
13	28	t
16	28	f
21	29	f
22	29	f
21	30	t
22	30	f
21	31	f
22	31	f
21	32	f
22	32	f
21	33	f
22	33	f
21	34	f
22	34	t
23	35	f
23	36	f
23	37	f
23	38	t
27	39	f
27	40	f
30	41	f
30	42	t
33	43	f
33	44	t
33	45	f
33	46	t
3	47	t
8	48	t
3	49	f
8	50	f
3	51	t
3	52	t
3	53	t
8	54	f
13	55	t
16	55	f
13	56	t
16	56	f
13	57	f
16	57	f
21	58	f
22	58	t
13	59	f
16	59	f
17	60	t
17	61	f
13	62	f
16	62	f
21	63	f
22	63	f
21	64	t
22	64	f
23	65	f
23	66	t
27	67	f
30	68	t
33	69	t
33	70	t
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
14	17	\N
14	18	2013-09-12 00:00:00
14	19	\N
14	20	2013-09-02 00:00:00
14	21	\N
14	22	2013-09-25 00:00:00
11	23	\N
11	24	2013-10-01 00:00:00
11	25	\N
11	26	2013-11-02 00:00:00
14	27	\N
14	28	\N
20	29	\N
20	30	2014-01-01 00:00:00
20	31	\N
20	32	2014-01-01 00:00:00
20	33	\N
20	34	2014-01-01 00:00:00
4	47	\N
4	49	\N
4	51	\N
4	52	\N
4	53	\N
14	55	\N
14	56	\N
14	57	\N
20	58	\N
14	59	\N
11	60	\N
11	61	\N
14	62	\N
20	63	\N
20	64	\N
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
18	29	0
18	30	1
18	31	0
18	32	1
18	33	0
18	34	1
25	39	0
25	40	4
31	43	0
31	44	5
31	45	0
31	46	4
6	48	2
6	50	1
6	54	4
18	58	1
18	63	1
18	64	1
25	67	4
31	69	5
31	70	4
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
15	17	
15	18	Esquemático del nuevo procesador
15	19	
15	20	Describe los límites y la tolerancia a fallos de los componentes
15	21	
15	22	Información de la arquitectura para implementadores finales
12	23	
12	24	BROADWELL ZERO
12	25	
12	26	LITTLEWELL
15	27	
15	28	Extensiones implementables sobre la arquitectura
19	29	
19	30	M-Edition
19	31	
19	32	BroadWell
19	33	
19	34	X-treme Edition
24	35	
24	36	Manual de referencia para implementadores
24	37	
24	38	Detalla las posibles fallas de una arquitectura
26	39	
26	40	Se prueba el límite térmico del integrado antes de fundirse
28	41	
28	42	Se implementa en un compilador el ISA de la nueva arquitectura
32	43	
32	44	Se prueba el microprocesador en operaciones matriz vector
32	45	
32	46	Operaciones en punto flotante
2	47	Análisis de las arquitecturas anteriores a BroadWell
7	48	Mejoras a la nueva arquitectura
2	49	Análisis de suelos en busca de minerales (cuarzo)
7	50	Obtención de obleas de cuarzo para microprocesadores
2	51	Análisis de tempertura de la nueva aquitectura
2	52	Análisis de tempertura de la nueva aquitectura
2	53	Análisis de tempertura de la nueva aquitectura
7	54	Prueba Térmica sobre el nuevo diseño térmico
15	55	Describe los límites y la tolerancia a fallos de los componentes
15	56	Extensiones implementables sobre la arquitectura
15	57	
19	58	X-treme Edition
15	59	
12	60	BROADWELL ZERO
12	61	LITTLEWELL
15	62	Información de la arquitectura para implementadores finales
19	63	BroadWell
19	64	M-Edition
24	65	Manual de referencia para implementadores
24	66	Detalla las posibles fallas de una arquitectura
26	67	Se prueba el límite térmico del integrado antes de fundirse
28	68	Se implementa en un compilador el ISA de la nueva arquitectura
32	69	Se prueba el microprocesador en operaciones matriz vector
32	70	Operaciones en punto flotante
\.


--
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, "fechaModificacion", deitem, usuario_modificador_id) FROM stdin;
1	0	Minerales	Activo	f	250000	30	2013-06-18 13:31:33.264764	1	1
2	1	Minerales	Activo	f	250000	30	2013-06-18 13:31:53.059921	1	1
4	0	Instalaciones	Activo	f	30000	10	2013-06-18 13:32:31.321181	2	1
5	1	Instalaciones	Activo	f	30000	10	2013-06-18 13:33:34.582212	2	1
6	2	Instalaciones	Eliminado	t	30000	10	2013-06-18 13:33:43.050457	2	1
7	0	Quarzo	Activo	f	500000	25	2013-06-18 13:33:58.974538	3	1
9	0	Arq. anteriores	Activo	f	15000	9	2013-06-18 13:35:10.758247	4	1
11	0	Mejoras	Activo	f	60000	12	2013-06-18 13:36:47.560435	5	1
13	0	Temperatura	Activo	f	5000	10	2013-06-18 13:37:59.290193	6	1
15	0	Prueba Térmica	Activo	f	50000	10	2013-06-18 13:39:24.550494	7	1
17	0	Esquemático	Activo	f	15000	25	2013-06-18 14:01:53.581885	8	1
19	0	Tolerancia y Límite	Activo	f	10000	5	2013-06-18 14:03:26.833141	9	1
21	0	WhiteCard	Activo	f	5000	15	2013-06-18 14:05:03.725902	10	1
23	0	Prototipo	Activo	f	35000	4	2013-06-18 14:06:12.883895	11	1
25	0	Empotrado	Activo	f	15000	10	2013-06-18 14:34:29.031991	12	1
27	0	Extensiones	Activo	f	15000	5	2013-06-18 14:35:20.978521	13	1
29	0	Mobile	Activo	f	15000	10	2013-06-18 14:52:30.295589	14	1
31	0	Normal	Activo	f	10000	5	2013-06-18 14:54:01.967011	15	1
33	0	Extreme	Activo	f	25000	15	2013-06-18 14:55:31.995324	16	1
35	0	Manua de Referencia	Activo	f	1000	1	2013-06-18 14:57:24.301069	17	1
37	0	Errata	Activo	f	1200	2	2013-06-18 14:58:16.373748	18	1
39	0	Barrera Térmica	Activo	f	15000	9	2013-06-18 15:12:21.145149	19	1
41	0	Compilador	Activo	f	10000	12	2013-06-18 15:13:13.483027	20	1
43	0	Op. Matriz Vector	Activo	f	5000	10	2013-06-18 15:14:30.947849	21	1
45	0	Punto Flotante	Activo	f	1000	3	2013-06-18 15:17:55.669804	22	1
10	1	Arq. anteriores	Activo	f	15000	9	2013-06-18 13:35:34.596879	4	1
12	1	Mejoras	Activo	f	60000	12	2013-06-18 13:37:07.044416	5	1
3	2	Minerales	Activo	f	250000	30	2013-06-18 13:32:04.71778	1	1
8	1	Quarzo	Activo	f	500000	25	2013-06-18 13:34:26.650533	3	1
14	1	Temperatura	Activo	f	5000	10	2013-06-18 13:38:21.061465	6	1
51	2	Temperatura	Aprobado	f	5000	10	2013-06-18 15:59:53.507513	6	1
52	3	Temperatura	Activo	f	5000	10	2013-06-18 16:00:05.885807	6	1
47	2	Arq. anteriores	Bloqueado	t	15000	9	2013-06-18 15:59:15.80414	4	1
48	2	Mejoras	Bloqueado	t	60000	12	2013-06-18 15:59:22.616938	5	1
53	4	Temperatura	Bloqueado	t	5000	10	2013-06-18 16:00:25.944638	6	1
49	3	Minerales	Bloqueado	t	250000	30	2013-06-18 15:59:30.432138	1	1
50	2	Quarzo	Bloqueado	t	500000	25	2013-06-18 15:59:41.407924	3	1
16	1	Prueba Térmica	Activo	f	50000	10	2013-06-18 13:39:58.357826	7	1
54	2	Prueba Térmica	Aprobado	t	50000	10	2013-06-18 16:06:56.569205	7	1
20	1	Tolerancia y Límite	Activo	f	10000	5	2013-06-18 14:03:56.312471	9	1
28	1	Extensiones	Activo	f	15000	5	2013-06-18 14:35:50.031558	13	1
18	1	Esquemático	Activo	f	15000	25	2013-06-18 14:02:25.469043	8	1
55	2	Tolerancia y Límite	Bloqueado	t	10000	5	2013-06-18 16:07:08.974733	9	1
56	2	Extensiones	Bloqueado	t	15000	5	2013-06-18 16:11:18.449712	13	1
34	1	Extreme	Activo	f	25000	15	2013-06-18 14:55:48.704906	16	1
57	2	Esquemático	Activo	f	15000	25	2013-06-18 16:12:01.05961	8	1
24	1	Prototipo	Activo	f	35000	4	2013-06-18 14:06:48.2071	11	1
26	1	Empotrado	Activo	f	15000	10	2013-06-18 14:35:02.819793	12	1
22	1	WhiteCard	Activo	f	5000	15	2013-06-18 14:05:37.116868	10	1
32	1	Normal	Activo	f	10000	5	2013-06-18 14:54:22.344471	15	1
30	1	Mobile	Activo	f	15000	10	2013-06-18 14:53:18.825863	14	1
36	1	Manua de Referencia	Activo	f	1000	1	2013-06-18 14:57:47.499628	17	1
38	1	Errata	Activo	f	1200	2	2013-06-18 14:58:37.365263	18	1
66	2	Errata	Aprobado	t	1200	2	2013-06-18 17:05:16.16897	18	1
40	1	Barrera Térmica	Activo	f	15000	9	2013-06-18 15:12:42.749792	19	1
42	1	Compilador	Activo	f	10000	12	2013-06-18 15:13:31.351332	20	1
44	1	Op. Matriz Vector	Activo	f	5000	10	2013-06-18 15:14:52.560199	21	1
46	1	Punto Flotante	Activo	f	1000	3	2013-06-18 15:18:20.045911	22	1
59	3	Esquemático	Bloqueado	t	15000	25	2013-06-18 16:58:08.707788	8	1
60	2	Prototipo	Bloqueado	t	35000	4	2013-06-18 17:01:34.822645	11	1
61	2	Empotrado	Bloqueado	t	15000	10	2013-06-18 17:02:41.299055	12	1
62	2	WhiteCard	Bloqueado	t	5000	15	2013-06-18 17:02:59.190605	10	1
64	2	Mobile	Bloqueado	t	15000	10	2013-06-18 17:04:25.195462	14	1
58	2	Extreme	Bloqueado	t	25000	15	2013-06-18 16:18:10.64415	16	1
63	2	Normal	Bloqueado	t	10000	5	2013-06-18 17:04:19.383484	15	1
65	2	Manua de Referencia	Bloqueado	t	1000	1	2013-06-18 17:05:10.633255	17	1
67	2	Barrera Térmica	Bloqueado	t	15000	9	2013-06-18 17:07:26.664383	19	1
68	2	Compilador	Bloqueado	t	10000	12	2013-06-18 17:07:32.386032	20	1
69	2	Op. Matriz Vector	Bloqueado	t	5000	10	2013-06-18 17:07:37.954485	21	1
70	2	Punto Flotante	Bloqueado	t	1000	3	2013-06-18 17:07:44.841431	22	1
\.


--
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('vitem_id_seq', 70, true);


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

