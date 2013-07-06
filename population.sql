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
-- Name: lb_ver; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE lb_ver (
    lb_id integer NOT NULL,
    ver_id integer NOT NULL
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
2	Genera Documento	Booleano	1
3	Revision	Fecha	1
4	ID interno	Numerico	2
5	Descripcion	Cadena	2
6	Experimental	Booleano	2
7	Interno	Booleano	3
8	Revision	Fecha	3
9	Descripcion	Cadena	3
12	Revision	Fecha	4
15	Clave	Cadena	4
16	Nuevo	Booleano	4
10	Fabricable	Booleano	3
1	Notas	Cadena	1
17	Nombre clave	Cadena	5
18	Revision	Fecha	5
19	Empotrado	Booleano	5
20	Novel	Booleano	5
21	Interno	Booleano	6
22	Notas	Cadena	6
23	Notas	Cadena	7
24	ISA compatible	Booleano	7
25	Tiempo	Numerico	8
26	Notas	Cadena	8
27	Exito	Booleano	8
28	Tiempo	Numerico	9
29	Notas	Cadena	9
30	Mass ready	Booleano	9
31	Radio	Numerico	10
32	Relleno	Booleano	10
33	X	Numerico	11
34	Y	Numerico	11
35	Z	Numerico	11
36	Equilatero	Booleano	11
37	Lado	Numerico	12
38	Nota	Cadena	12
39	Longitud	Numerico	13
40	Punteada	Booleano	13
41	Descripcion	Cadena	13
42	Descripcion	Cadena	14
43	X	Numerico	14
44	Y	Numerico	14
45	Lado	Numerico	15
46	Revision	Fecha	15
47	RA	Numerico	16
48	RB	Numerico	16
49	Notas	Cadena	16
50	X	Numerico	17
51	Y	Numerico	17
52	Punteada	Booleano	17
53	Estable	Booleano	18
54	Lado	Numerico	18
55	Nota	Cadena	18
56	Revision	Fecha	18
57	Lado	Numerico	19
58	Nota	Cadena	19
59	Descripcion	Cadena	20
60	Revision	Fecha	20
61	Solido	Booleano	20
62	Puntas	Numerico	21
63	Punteada	Booleano	21
64	Notas	Cadena	21
65	Revision	Fecha	21
66	Paginas	Numerico	22
67	Autor	Cadena	22
68	Fecha	Fecha	23
69	Completo	Booleano	23
70	Monografia	Booleano	24
71	Completo	Booleano	24
72	Materia	Cadena	25
73	Aprobado	Booleano	25
\.


--
-- Name: atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('atributo_id_seq', 73, true);


--
-- Data for Name: fase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY fase (id, nombre, numero, "fechaInicio", "fechaFin", "fechaUltMod", estado, delproyecto) FROM stdin;
3	Gama	3	2013-12-02 00:00:00	2014-03-01 00:00:00	2013-07-05 13:27:15.608814	Abierta	1
8	Estudiar	1	2013-08-01 00:00:00	2013-08-15 00:00:00	2013-07-05 15:36:27.829606	Cerrada	3
2	Beta	2	2013-09-02 00:00:00	2013-12-01 00:00:00	2013-07-05 13:17:10.837039	Abierta	1
9	Rendir	2	2013-08-16 00:00:00	2013-09-01 00:00:00	2013-07-05 15:40:41.957931	Abierta	3
7	GrandGeometry	3	2013-08-02 00:00:00	2013-09-01 00:00:00	2013-07-05 15:24:19.510757	Abierta	2
1	Alfa	1	2013-06-01 00:00:00	2013-09-01 00:00:00	2013-07-05 12:22:54.77703	Abierta	1
6	Complicando Formas	2	2013-07-02 00:00:00	2013-08-01 00:00:00	2013-07-05 14:20:58.045586	Cerrada	2
5	Formas Basicas	1	2013-06-01 00:00:00	2013-07-01 00:00:00	2013-07-05 14:08:36.566858	Cerrada	2
4	Delta	4	2014-03-02 00:00:00	2014-06-01 00:00:00	2013-07-05 23:44:45.261539	Abierta	1
\.


--
-- Name: fase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('fase_id_seq', 9, true);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item (id, tipo, etiqueta, "fechaCreacion", linea_id, usuario_creador_id) FROM stdin;
7	1	1-1-20	2013-07-05 10:02:22.618785	\N	2
1	1	1-1-1	2013-07-04 22:00:04.308328	2	2
2	1	1-1-2	2013-07-04 22:00:24.883391	2	2
3	1	1-1-7	2013-07-04 22:03:18.754222	4	2
4	2	1-1-11	2013-07-04 22:05:47.856005	4	2
5	2	1-1-14	2013-07-05 09:59:17.016962	4	2
6	2	1-1-17	2013-07-05 10:00:08.301692	4	2
8	3	1-2-1	2013-07-05 12:57:33.98838	5	2
9	3	1-2-4	2013-07-05 13:00:29.39333	6	2
10	3	1-2-7	2013-07-05 13:09:21.794007	6	2
12	4	1-2-13	2013-07-05 13:11:40.548171	6	2
11	4	1-2-10	2013-07-05 13:10:42.384573	6	2
13	3	1-2-16	2013-07-05 13:12:49.384376	6	2
14	5	1-3-1	2013-07-05 13:20:53.728145	7	2
15	5	1-3-4	2013-07-05 13:21:37.616806	7	2
16	5	1-3-7	2013-07-05 13:22:30.632315	8	2
17	6	1-3-10	2013-07-05 13:23:49.302305	8	2
18	6	1-3-13	2013-07-05 13:24:41.222259	8	2
19	9	1-4-1	2013-07-05 13:31:11.050432	\N	2
20	8	1-4-4	2013-07-05 13:32:23.287148	\N	2
21	7	1-4-8	2013-07-05 13:34:19.897199	\N	2
22	9	1-4-12	2013-07-05 13:35:44.607363	\N	2
23	10	2-5-1	2013-07-05 13:48:18.240736	9	3
24	10	2-5-4	2013-07-05 13:52:31.871646	9	3
25	11	2-5-7	2013-07-05 13:53:03.749773	10	3
26	11	2-5-10	2013-07-05 13:53:46.728944	10	3
27	11	2-5-13	2013-07-05 13:54:21.315959	10	3
29	10	2-5-19	2013-07-05 13:56:31.854397	11	3
28	12	2-5-16	2013-07-05 13:55:22.864941	11	3
30	12	2-5-22	2013-07-05 13:57:32.119984	11	3
31	12	2-5-25	2013-07-05 14:01:25.487166	11	3
32	13	2-5-29	2013-07-05 14:05:47.166599	12	3
33	14	2-6-1	2013-07-05 14:13:42.237696	13	3
34	14	2-6-4	2013-07-05 14:14:24.27631	13	3
35	15	2-6-7	2013-07-05 14:15:20.351715	13	3
36	16	2-6-10	2013-07-05 14:16:31.91073	14	3
37	17	2-6-13	2013-07-05 14:18:34.297967	15	3
38	18	2-7-1	2013-07-05 15:16:42.462378	16	3
40	18	2-7-7	2013-07-05 15:18:12.666601	16	3
39	19	2-7-4	2013-07-05 15:17:29.799642	16	3
41	20	2-7-10	2013-07-05 15:19:11.855038	17	3
42	20	2-7-13	2013-07-05 15:20:00.103931	17	3
43	20	2-7-16	2013-07-05 15:21:02.57153	17	3
44	21	2-7-19	2013-07-05 15:21:59.648496	18	3
45	22	3-8-1	2013-07-05 15:31:46.327095	19	4
46	22	3-8-4	2013-07-05 15:32:29.146505	20	4
47	22	3-8-7	2013-07-05 15:32:57.828194	21	4
48	23	3-8-10	2013-07-05 15:33:39.985293	21	4
49	24	3-9-1	2013-07-05 15:37:59.932601	\N	4
50	25	3-9-3	2013-07-05 15:38:19.296975	\N	4
51	24	3-9-7	2013-07-05 15:39:14.923822	\N	4
52	25	3-9-10	2013-07-05 15:40:10.917323	\N	4
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('item_id_seq', 52, true);


--
-- Data for Name: item_peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY item_peticion (peticion_id, item_id, actual) FROM stdin;
1	25	f
2	24	f
2	26	f
2	44	f
\.


--
-- Data for Name: lb_ver; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lb_ver (lb_id, ver_id) FROM stdin;
3	10
3	13
3	16
3	19
\.


--
-- Data for Name: lineabase; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lineabase (id, creador_id, "fechaCreacion", numero, comentario, fase_id, estado) FROM stdin;
2	2	2013-07-05 10:04:09.422009	1	Experiencias anteriores, aplicadas en la nueva arquitectura	1	Cerrada
3	2	2013-07-05 10:05:36.966278	2	Requerimientos completos	1	Quebrada
4	2	2013-07-05 12:22:26.75339	3	Requerimientos revisados y completos	1	Cerrada
5	2	2013-07-05 13:15:33.726857	1	Extensiones Listas	2	Cerrada
6	2	2013-07-05 13:15:49.916433	2	Prototipos y documentacion lista	2	Cerrada
7	2	2013-07-05 13:26:09.768802	1	Versiones Especiales Ready For Mass production	3	Cerrada
8	2	2013-07-05 13:26:40.106739	2	Versiones mainstream y documentos	3	Cerrada
9	3	2013-07-05 14:06:39.735136	1	Circulos listos	5	Cerrada
10	3	2013-07-05 14:06:59.006015	2	Triangulos listos	5	Cerrada
11	3	2013-07-05 14:07:22.798512	3	Cuadrados listos (circulo incluido)	5	Cerrada
12	3	2013-07-05 14:08:01.25102	4	Linea Lista	5	Cerrada
13	3	2013-07-05 14:19:14.38115	1	Rectangulo y Pentagono	6	Cerrada
14	3	2013-07-05 14:20:21.572329	2	Ovalo	6	Cerrada
15	3	2013-07-05 14:20:34.20645	3	Crux	6	Cerrada
16	3	2013-07-05 15:23:15.744411	1	Geometria Completa	7	Cerrada
17	3	2013-07-05 15:23:45.631684	2	Amorfos completos	7	Cerrada
18	3	2013-07-05 15:24:07.459255	3	Masterpiece	7	Cerrada
19	4	2013-07-05 15:34:51.830196	1	Ya estudio calculo I	8	Cerrada
20	4	2013-07-05 15:35:08.164854	2	Ya sabe Integrar	8	Cerrada
21	4	2013-07-05 15:35:35.042032	3	Ya estudio y termino su trabajo practico para fisica II	8	Cerrada
\.


--
-- Name: lineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('lineabase_id_seq', 21, true);


--
-- Data for Name: miembro; Type: TABLE DATA; Schema: public; Owner: -
--

COPY miembro (proyecto_id, user_id) FROM stdin;
2	3
3	4
3	2
3	3
1	2
1	3
1	4
\.


--
-- Data for Name: peticion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY peticion (id, numero, proyecto_id, comentario, estado, usuario_id, "cantVotos", "cantItems", "costoT", "dificultadT", "fechaCreacion", "fechaEnvio", acciones) FROM stdin;
1	1	1	Cuarzo depende de minerales	Terminada	2	3	1	250000	13	2013-07-05 12:20:10.724179	2013-07-05 12:20:21.137821	100
2	2	1	Cambiar los costos	Rechazada	2	1	3	1032000	67	2013-07-05 23:38:07.428813	2013-07-05 23:38:27.356253	1
\.


--
-- Name: peticion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('peticion_id_seq', 2, true);


--
-- Data for Name: proyecto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY proyecto (id, nombre, "cantFase", "fechaInicio", "fechaFin", "fechaUltMod", delider, estado) FROM stdin;
2	Geometria	3	2013-06-01 00:00:00	2013-09-01 00:00:00	2013-07-05 15:24:19.529124	3	Iniciado
3	Semestre	2	2013-07-01 00:00:00	2013-08-01 00:00:00	2013-07-05 15:40:41.976195	4	Iniciado
1	BroadWell	4	2013-06-01 00:00:00	2014-06-01 00:00:00	2013-07-05 23:44:45.332319	2	Iniciado
\.


--
-- Name: proyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('proyecto_id_seq', 3, true);


--
-- Data for Name: relacion; Type: TABLE DATA; Schema: public; Owner: -
--

COPY relacion (id, ante_id, post_id, tipo) FROM stdin;
1	3	4	P-H
2	5	4	P-H
3	3	6	P-H
4	5	6	P-H
5	16	18	P-H
6	10	18	P-H
7	16	19	P-H
8	10	19	P-H
9	23	18	P-H
10	23	19	P-H
11	25	18	P-H
12	25	19	P-H
13	16	26	P-H
14	10	26	P-H
15	23	26	P-H
16	25	26	P-H
17	24	25	P-H
18	6	28	A-S
19	6	29	A-S
20	6	31	A-S
21	6	32	A-S
22	26	34	A-S
23	26	35	A-S
24	32	37	P-H
25	32	38	P-H
26	32	40	P-H
27	35	40	P-H
28	32	41	P-H
29	35	41	P-H
30	41	42	P-H
31	41	43	P-H
32	41	44	P-H
33	29	46	A-S
34	29	47	A-S
35	38	49	A-S
36	38	50	A-S
37	44	52	A-S
38	44	53	A-S
39	44	55	A-S
40	44	56	A-S
41	56	57	P-H
42	56	58	P-H
43	56	59	P-H
44	47	61	A-S
45	47	62	A-S
46	47	64	A-S
47	50	64	A-S
48	47	65	A-S
49	50	65	A-S
50	47	66	A-S
51	50	66	A-S
52	56	69	A-S
53	56	70	A-S
54	53	72	A-S
55	53	73	A-S
56	76	78	P-H
57	76	79	P-H
58	82	87	P-H
59	85	87	P-H
60	82	88	P-H
61	85	88	P-H
62	91	95	P-H
63	91	97	P-H
64	94	98	P-H
65	97	98	P-H
66	94	100	P-H
67	97	100	P-H
68	94	101	P-H
69	97	101	P-H
70	79	106	A-S
71	79	107	A-S
72	107	109	P-H
73	107	110	P-H
74	110	112	P-H
75	88	112	A-S
76	110	113	P-H
77	88	113	A-S
78	94	115	A-S
79	94	116	A-S
80	104	118	A-S
81	104	119	A-S
82	113	121	A-S
83	113	122	A-S
84	122	124	P-H
85	122	125	P-H
86	122	127	P-H
87	122	128	P-H
88	116	130	A-S
89	116	131	A-S
90	131	133	P-H
91	131	134	P-H
92	131	136	P-H
93	131	137	P-H
94	119	139	A-S
95	119	140	A-S
96	149	151	P-H
97	149	152	P-H
98	143	157	A-S
99	143	158	A-S
100	152	160	A-S
101	152	161	A-S
102	161	163	P-H
103	146	163	A-S
104	161	164	P-H
105	146	164	A-S
106	56	165	A-S
107	47	166	A-S
108	50	166	A-S
109	47	167	A-S
110	47	168	A-S
111	47	169	A-S
112	53	170	A-S
113	56	171	A-S
114	56	172	A-S
115	47	173	A-S
116	50	173	A-S
117	56	174	A-S
\.


--
-- Name: relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('relacion_id_seq', 117, true);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY rol (id, fase_id, nombre, "codigoTipo", "codigoItem", "codigoLB") FROM stdin;
1	1	Jefe de Ingenieria	111	1000	1
2	1	Analista	0	11110111	0
3	2	Jefe de Ingenieria	11	1000	1
4	2	Arquitecto	0	11110111	0
5	3	Jefe de Ingenieria	111	1000	1
6	3	Ingeniero	0	11110111	0
7	4	Jefe de Ingenieria	111	11111111	1
8	5	Aprobador	111	1000	1
9	5	Dibujante	0	11110111	0
10	6	Dibujante	0	11110111	0
11	6	Aprobador	111	1000	1
12	7	Dibujante	0	11110111	0
13	7	Aprobador	111	1000	1
14	8	estudiante	111	11111111	1
15	9	estudiante	111	11111111	1
\.


--
-- Name: rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('rol_id_seq', 15, true);


--
-- Data for Name: tipoitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY tipoitem (id, nombre, comentario, defase, "fechaCreacion", "fechaModificacion", usuario_creador_id, usuario_modificador_id) FROM stdin;
1	Analisis	Analisis de los requisitos y experiencias en micropocesadores	1	2013-07-04 21:56:50.609927	2013-07-04 21:56:50.609927	2	2
2	Requisito	Requisitos previos para iniciar el proceso	1	2013-07-04 21:58:18.16285	2013-07-04 21:58:18.16285	2	2
3	Dis. Logico	Estructura logica de la microarquitectura	2	2013-07-05 12:54:55.150259	2013-07-05 12:54:55.150259	2	2
4	Dis. Fisico	Estructura hardware de la microarquitectura	2	2013-07-05 12:56:10.325671	2013-07-05 12:56:10.325671	2	2
5	Microprocesador	Un nuevo microprocesador fabricado	3	2013-07-05 13:18:11.352978	2013-07-05 13:18:11.352978	2	2
6	Documentacion	Documentos que describen los nuevos microprocesadores	3	2013-07-05 13:19:29.636127	2013-07-05 13:19:29.636127	2	2
7	Homologacion	estandarizacion de documentos y metodos	4	2013-07-05 13:28:30.199366	2013-07-05 13:28:30.199366	2	2
8	Prueba Hardware	Prueba sobre la circuiteria del nuevo microprocesador	4	2013-07-05 13:29:08.621747	2013-07-05 13:29:08.621747	2	2
9	Rendimiento	Pruebas de rendimiento y limites sobre los microprocesadores	4	2013-07-05 13:29:27.621682	2013-07-05 13:29:27.621682	2	2
10	Circulo	Conjunto de puntos equidistantes de un punto llamado centro	5	2013-07-05 13:43:52.99449	2013-07-05 13:43:52.99449	3	3
11	Triangulo	Poligono convexo de tres lados	5	2013-07-05 13:44:33.616168	2013-07-05 13:44:33.616168	3	3
12	Cuadrado	Poligono convexo de cuatro lados iguales	5	2013-07-05 13:46:12.39744	2013-07-05 13:46:12.39744	3	3
13	Linea	Conjunto infinito de puntos que unen dos punto dados	5	2013-07-05 13:47:10.101196	2013-07-05 13:47:10.101196	3	3
14	Rectangulo	Cuadrilatero con angulos rectos	6	2013-07-05 14:09:13.678211	2013-07-05 14:09:13.678211	3	3
15	Pentagono	Poligono cerrado de cinco lados iguales	6	2013-07-05 14:10:14.894773	2013-07-05 14:10:14.894773	3	3
16	Elipse	Conjunto de puntos cuya distancia a dos puntos dados es constante	6	2013-07-05 14:11:03.642696	2013-07-05 14:11:03.642696	3	3
17	Cruz	Conjunto de dos lineas que se intersectan en un punto	6	2013-07-05 14:11:59.231448	2013-07-05 14:11:59.231448	3	3
18	Hexagono	Poligono cerrado de seis lados iguales	7	2013-07-05 14:21:22.089815	2013-07-05 14:21:22.089815	3	3
19	Octogono	Poligono cerrado de ocho lados iguales	7	2013-07-05 14:28:05.574817	2013-07-05 14:28:05.574817	3	3
20	Amorfo	Grafico o estructura amorfa	7	2013-07-05 14:28:44.279768	2013-07-05 14:28:44.279768	3	3
21	Estrella	Trazos con forma de estrella	7	2013-07-05 14:29:32.254028	2013-07-05 14:29:32.254028	3	3
22	Libro	Texto escrito por conocidos autores sobre un tema particular	8	2013-07-05 15:29:07.533558	2013-07-05 15:29:07.533558	4	4
23	Cuaderno	Apuntes de un estudiante	8	2013-07-05 15:29:49.566461	2013-07-05 15:29:49.566461	4	4
24	TP	Trabajo practico	9	2013-07-05 15:36:46.275497	2013-07-05 15:36:46.275497	4	4
25	Examen	Prueba de conocimientos sobre una manteria	9	2013-07-05 15:37:19.327579	2013-07-05 15:37:19.327579	4	4
\.


--
-- Name: tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipoitem_id_seq', 25, true);


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: -
--

COPY user_rol (usuario_id, rol_id) FROM stdin;
2	1
3	1
2	2
4	2
2	3
3	3
2	4
4	4
2	5
3	5
4	6
2	6
2	7
3	8
2	8
3	9
5	9
5	10
3	10
3	11
2	11
3	12
5	12
2	13
3	13
2	14
3	14
4	14
2	15
4	15
3	15
3	7
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: -
--

COPY usuario (id, nombre, nombredeusuario, clave, "isAdmin") FROM stdin;
1	Administrador	admin	7c4a8d09ca3762af61e59520943dc26494f8941b	t
2	Natalia Valdez	natalia	2298625f2ba17912b286ad9afd8f089e460241b9	t
3	Martin Poletti	martin	54669547a225ff20cba8b75a4adca540eef25858	f
4	Dan Thor	dan	7c4a8d09ca3762af61e59520943dc26494f8941b	t
5	Anna Dyst	anna	7c4a8d09ca3762af61e59520943dc26494f8941b	f
6	Ryunosuke Asakura	ryu	7c4a8d09ca3762af61e59520943dc26494f8941b	f
\.


--
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('usuario_id_seq', 6, true);


--
-- Data for Name: valorbool; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorbool (atributo_id, item_id, valor) FROM stdin;
2	1	f
2	2	f
2	3	t
2	4	t
2	5	t
2	6	t
2	7	f
2	8	f
2	9	f
2	10	f
6	11	f
6	12	f
6	13	f
6	14	f
6	15	f
6	16	f
6	17	f
6	18	t
6	19	t
2	20	f
2	21	t
2	22	t
2	23	f
6	24	f
6	25	f
6	26	t
7	27	f
10	27	f
7	28	f
10	28	t
7	29	f
10	29	t
7	30	f
10	30	f
7	31	t
10	31	t
7	32	t
10	32	t
7	33	f
10	33	f
7	34	t
10	34	f
7	35	t
10	35	f
16	36	f
16	37	t
16	38	t
16	39	f
16	40	f
16	41	f
7	42	f
10	42	f
7	43	f
10	43	t
7	44	f
10	44	t
19	45	f
20	45	f
19	46	f
20	46	t
19	47	f
20	47	t
19	48	f
20	48	f
19	49	t
20	49	t
19	50	t
20	50	t
19	51	f
20	51	f
19	52	f
20	52	f
19	53	f
20	53	f
21	54	f
21	55	f
21	56	f
21	57	f
21	58	t
21	59	t
30	60	f
30	61	t
30	62	t
27	63	f
27	64	t
27	65	t
27	66	t
24	67	f
24	68	f
24	69	t
24	70	t
30	71	f
30	72	f
30	73	f
32	74	f
32	75	t
32	76	t
32	77	f
32	78	f
32	79	f
36	80	f
36	81	f
36	82	f
36	83	f
36	84	f
36	85	f
36	86	f
36	87	t
36	88	t
32	92	f
32	93	t
32	94	t
40	102	f
40	103	f
40	104	f
52	117	f
52	118	t
52	119	t
53	120	f
53	121	t
53	122	t
53	126	f
53	127	f
53	128	f
61	129	f
61	130	f
61	131	f
61	132	f
61	133	f
61	134	f
61	135	f
61	136	t
61	137	t
63	138	f
63	139	t
63	140	t
69	150	f
69	151	f
69	152	f
70	153	f
71	153	f
70	154	f
71	154	f
73	155	f
73	156	f
73	157	t
73	158	t
70	159	f
71	159	f
70	160	t
71	160	f
70	161	t
71	161	f
73	162	f
73	163	f
73	164	f
24	165	t
27	166	t
30	167	t
30	168	t
30	169	t
30	170	f
24	171	f
24	172	t
27	173	t
24	174	t
\.


--
-- Data for Name: valordate; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valordate (atributo_id, item_id, valor) FROM stdin;
3	1	\N
3	2	\N
3	3	2013-06-12 00:00:00
3	4	2013-06-13 00:00:00
3	5	\N
3	6	\N
3	7	\N
3	8	2013-06-14 00:00:00
3	9	2013-06-14 00:00:00
3	10	\N
3	20	\N
3	21	2013-06-07 00:00:00
3	22	\N
3	23	\N
8	27	\N
8	28	2013-09-02 00:00:00
8	29	\N
8	30	\N
8	31	2013-09-05 00:00:00
8	32	\N
8	33	\N
8	34	2013-09-10 00:00:00
8	35	\N
12	36	\N
12	37	2013-09-15 00:00:00
12	38	\N
12	39	\N
12	40	2013-09-20 00:00:00
12	41	\N
8	42	\N
8	43	2013-09-27 00:00:00
8	44	\N
18	45	\N
18	46	2013-12-02 00:00:00
18	47	\N
18	48	\N
18	49	2013-09-03 00:00:00
18	50	\N
18	51	\N
18	52	2013-09-02 00:00:00
18	53	\N
46	111	\N
46	112	2013-07-05 00:00:00
46	113	\N
56	120	\N
56	121	2013-08-05 00:00:00
56	122	\N
56	126	\N
56	127	2013-08-07 00:00:00
56	128	\N
60	129	\N
60	130	2013-08-10 00:00:00
60	131	\N
60	132	\N
60	133	2013-08-09 00:00:00
60	134	\N
60	135	\N
60	136	2013-08-17 00:00:00
60	137	\N
65	138	\N
65	139	2013-08-25 00:00:00
65	140	\N
68	150	\N
68	151	2013-07-01 00:00:00
68	152	\N
\.


--
-- Data for Name: valorfile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorfile (id, item_id, valor, nombre) FROM stdin;
\.


--
-- Name: valorfile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('valorfile_id_seq', 1, true);


--
-- Data for Name: valorint; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorint (atributo_id, item_id, valor) FROM stdin;
4	11	0
4	12	1
4	13	1
4	14	0
4	15	2
4	16	2
4	17	0
4	18	3
4	19	3
4	24	1
4	25	2
4	26	3
28	60	0
28	61	5
28	62	5
25	63	0
25	64	9
25	65	9
25	66	9
28	71	0
28	72	9
28	73	9
31	74	0
31	75	3
31	76	3
31	77	0
31	78	10
31	79	10
33	80	0
34	80	0
35	80	0
33	81	5
34	81	5
35	81	3
33	82	5
34	82	5
35	82	3
33	83	0
34	83	0
35	83	0
33	84	3
34	84	4
35	84	5
33	85	3
34	85	4
35	85	5
33	86	0
34	86	0
35	86	0
33	87	3
34	87	3
35	87	3
33	88	3
34	88	3
35	88	3
37	89	0
37	90	4
37	91	0
31	92	0
31	93	6
31	94	6
37	95	0
37	96	3
37	97	0
37	98	0
37	99	1
37	100	1
37	101	1
39	102	0
39	103	7
39	104	7
43	105	0
44	105	0
43	106	8
44	106	9
43	107	8
44	107	9
43	108	0
44	108	0
43	109	6
44	109	4
43	110	6
44	110	4
45	111	0
45	112	5
45	113	5
47	114	0
48	114	0
47	115	5
48	115	9
47	116	5
48	116	9
50	117	0
51	117	0
50	118	4
51	118	5
50	119	4
51	119	5
54	120	0
54	121	7
54	122	7
57	123	0
57	124	8
57	125	8
54	126	0
54	127	6
54	128	6
62	138	0
62	139	5
62	140	5
66	141	0
66	142	500
66	143	500
66	144	0
66	145	300
66	146	300
66	147	0
66	148	900
66	149	900
25	166	9
28	167	8
28	168	8
28	169	8
28	170	9
25	173	11
\.


--
-- Data for Name: valorstr; Type: TABLE DATA; Schema: public; Owner: -
--

COPY valorstr (atributo_id, item_id, valor) FROM stdin;
1	1	
1	2	
1	3	Se toman experiencias pasadas en arquitecturas anteriores para la fabricacion de la nueva
1	4	Se hacen mejoras a la nueva arquitectura en base a las arquitecturas anteriores y lo aprendido
1	5	Se toman experiencias pasadas en arquitecturas anteriores para la fabricacion de la nueva
1	6	Se hacen mejoras a la nueva arquitectura en base a las arquitecturas anteriores y lo aprendido
1	7	
1	8	Se hacen análisis sobre el impacto en temperatura de la nueva arquitectura
1	9	Se hacen análisis sobre el impacto en temperatura de la nueva arquitectura
1	10	Se hacen análisis sobre el impacto en temperatura de la nueva arquitectura
5	11	
5	12	Extraccion de minerales en busca de cuarzo
5	13	Extraccion de minerales en busca de cuarzo
5	14	
5	15	Obtencion de obleas de cuarzo
5	16	Obtencion de obleas de cuarzo
5	17	
5	18	Prueba de temperatura critica sobre las obleas
5	19	Prueba de temperatura critica sobre las obleas
1	20	
1	21	Analisis de las instalaciones necesarias para la fabricacion de microprocesadores
1	22	Analisis de las instalaciones necesarias para la fabricacion de microprocesadores
1	23	Se hacen análisis sobre el impacto en temperatura de la nueva arquitectura
5	24	Extraccion de minerales en busca de cuarzo
5	25	Obtencion de obleas de cuarzo
5	26	Prueba de temperatura critica sobre las obleas
9	27	
9	28	Extensiones implementadas a la nueva microarquitectura
9	29	Extensiones implementadas a la nueva microarquitectura
9	30	
9	31	Esquematico fuente para el prototipo de microprocesador
9	32	Esquematico fuente para el prototipo de microprocesador
9	33	
9	34	Pruebas de tolerancia y limites de temperatura sobre la oblea de cuarzo
9	35	Pruebas de tolerancia y limites de temperatura sobre la oblea de cuarzo
15	36	
15	37	MOBILE
15	38	MOBILE
15	39	
15	40	BROADWELL
15	41	BROADWELL
9	42	
9	43	Descripcion de la nueva ISA
9	44	Descripcion de la nueva ISA
17	45	
17	46	EXTREMEWELL
17	47	EXTREMEWELL
17	48	
17	49	MOBILEWELL
17	50	MOBILEWELL
17	51	
17	52	BROADWELL
17	53	BROADWELL
22	54	
22	55	Manual para implementadores de compiladores
22	56	Manual para implementadores de compiladores
22	57	
22	58	Fallas y Errores encontrados en procesos y documentos
22	59	Fallas y Errores encontrados en procesos y documentos
29	60	
29	61	Pruebas en operaciones de Punto Flotante
29	62	Pruebas en operaciones de Punto Flotante
26	63	
26	64	Limite termico del encapsulado
26	65	Limite termico del encapsulado
26	66	Limite termico del encapsulado
23	67	
23	68	
23	69	Implementacion del ISA en el compilador GCC
23	70	Implementacion del ISA en el compilador GCC
29	71	
29	72	Operaciones producto Matriz por vector para el microprocesador
29	73	Operaciones producto Matriz por vector para el microprocesador
38	89	
38	90	Primer Cuadrado
38	91	
38	95	
38	96	Segundo cuadrado
38	97	
38	98	
38	99	Tercer Cuadrado
38	100	Final Square
38	101	Final Square
41	102	
41	103	Primera Linea
41	104	Primera Linea
42	105	
42	106	Rectangulo UNO
42	107	Rectangulo UNO
42	108	
42	109	Segundo Rectangulo
42	110	Segundo Rectangulo
49	114	
49	115	Elipse horizontal
49	116	Elipse horizontal
55	120	
55	121	Hexagono Estable
55	122	Hexagono Estable
58	123	
58	124	Octogono Final
58	125	Octogono Final
55	126	
55	127	Hexagono inestable 
55	128	Hexagono inestable 
59	129	
59	130	Grafico Amorfo
59	131	Grafico Amorfo
59	132	
59	133	Forma con puntas y estructura amorfa
59	134	Forma con puntas y estructura amorfa
59	135	
59	136	Solido de revolucion
59	137	Solido de revolucion
64	138	
64	139	Pentagrama punteado
64	140	Pentagrama punteado
67	141	
67	142	Piskunov
67	143	Piskunov
67	144	
67	145	Piskunov
67	146	Piskunov
67	147	
67	148	Sears
67	149	Sears
72	155	
72	156	
72	157	Calculo II
72	158	Calculo II
72	162	
72	163	Fisica II
72	164	Fisica II
23	165	Implementacion del ISA en el compilador GCC
26	166	Limite termico del encapsulado
29	167	Pruebas en operaciones de Punto Flotante
29	168	Pruebas en operaciones de Punto Flotante
29	169	Pruebas en operaciones de Punto Flotante
29	170	Operaciones producto Matriz por vector para el microprocesador
23	171	Implementacion del ISA en el compilador GCC
23	172	Implementacion del ISA en el compilador GCC
26	173	Limite termico del encapsulado
23	174	Implementacion del ISA en el compilador GCC
\.


--
-- Data for Name: vitem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY vitem (id, version, nombre, estado, actual, costo, dificultad, "fechaModificacion", deitem, usuario_modificador_id) FROM stdin;
1	0	Arq. Anteriores	Activo	f	30000	4	2013-07-04 22:00:04.308328	1	2
2	0	Mejoras	Activo	f	15000	5	2013-07-04 22:00:24.883391	2	2
3	1	Arq. Anteriores	Activo	f	30000	4	2013-07-04 22:01:06.768276	1	2
4	1	Mejoras	Activo	f	15000	5	2013-07-04 22:01:44.741746	2	2
7	0	Temperatura	Activo	f	10000	3	2013-07-04 22:03:18.754222	3	2
8	1	Temperatura	Activo	f	10000	3	2013-07-04 22:03:50.501876	3	2
9	2	Temperatura	Activo	f	10000	3	2013-07-04 22:05:21.12339	3	2
11	0	Minerales	Activo	f	500000	7	2013-07-04 22:05:47.856005	4	2
12	1	Minerales	Activo	f	500000	7	2013-07-04 22:06:29.65898	4	2
14	0	Cuarzo	Activo	f	150000	8	2013-07-05 09:59:17.016962	5	2
15	1	Cuarzo	Activo	f	150000	8	2013-07-05 09:59:36.126006	5	2
17	0	Prueba Termica	Activo	f	100000	5	2013-07-05 10:00:08.301692	6	2
18	1	Prueba Termica	Activo	f	100000	5	2013-07-05 10:00:42.135695	6	2
20	0	Instalaciones	Activo	f	14000	2	2013-07-05 10:02:22.618785	7	2
21	1	Instalaciones	Activo	f	14000	2	2013-07-05 10:03:05.668734	7	2
22	2	Instalaciones	Eliminado	t	14000	2	2013-07-05 10:03:15.748074	7	2
5	2	Arq. Anteriores	Bloqueado	t	30000	4	2013-07-04 22:02:26.966118	1	2
6	2	Mejoras	Bloqueado	t	15000	5	2013-07-04 22:02:34.69344	2	2
29	2	Extensiones	Bloqueado	t	10000	7	2013-07-05 12:59:58.574674	8	2
32	2	Esquematico	Bloqueado	t	10000	5	2013-07-05 13:09:03.268535	9	2
35	2	Tolerancia y Limites	Bloqueado	t	50000	6	2013-07-05 13:10:11.520061	10	2
10	3	Temperatura	Bloqueado	f	10000	3	2013-07-04 22:05:29.59474	3	2
13	2	Minerales	Bloqueado	f	500000	7	2013-07-05 09:59:00.544779	4	2
16	2	Cuarzo	Bloqueado	f	150000	8	2013-07-05 09:59:50.755375	5	2
41	2	Prototipo	Bloqueado	t	75000	8	2013-07-05 13:12:31.988008	12	2
19	2	Prueba Termica	Conflicto	f	100000	5	2013-07-05 10:01:29.227822	6	2
38	2	Empotrado	Bloqueado	t	15000	9	2013-07-05 13:11:20.474018	11	2
44	2	WhiteCard	Bloqueado	t	20000	4	2013-07-05 13:14:36.184077	13	2
23	4	Temperatura	Bloqueado	t	10000	3	2013-07-05 12:20:53.510539	3	2
24	3	Minerales	Bloqueado	t	500000	7	2013-07-05 12:20:53.695803	4	2
25	3	Cuarzo	Bloqueado	t	150000	8	2013-07-05 12:20:53.863304	5	2
26	3	Prueba Termica	Bloqueado	t	100000	5	2013-07-05 12:20:54.058462	6	2
27	0	Extensiones	Activo	f	10000	7	2013-07-05 12:57:33.98838	8	2
28	1	Extensiones	Activo	f	10000	7	2013-07-05 12:59:10.035942	8	2
30	0	Esquematico	Activo	f	10000	5	2013-07-05 13:00:29.39333	9	2
31	1	Esquematico	Activo	f	10000	5	2013-07-05 13:01:00.420765	9	2
33	0	Tolerancia y Limites	Activo	f	50000	6	2013-07-05 13:09:21.794007	10	2
34	1	Tolerancia y Limites	Activo	f	50000	6	2013-07-05 13:09:49.179329	10	2
36	0	Empotrado	Activo	f	15000	9	2013-07-05 13:10:42.384573	11	2
37	1	Empotrado	Activo	f	15000	9	2013-07-05 13:10:57.618555	11	2
39	0	Prototipo	Activo	f	75000	8	2013-07-05 13:11:40.548171	12	2
40	1	Prototipo	Activo	f	75000	8	2013-07-05 13:12:05.86476	12	2
42	0	WhiteCard	Activo	f	20000	4	2013-07-05 13:12:49.384376	13	2
43	1	WhiteCard	Activo	f	20000	4	2013-07-05 13:14:27.869749	13	2
45	0	Extreme	Activo	f	100000	7	2013-07-05 13:20:53.728145	14	2
46	1	Extreme	Activo	f	100000	7	2013-07-05 13:21:06.904532	14	2
48	0	Mobile	Activo	f	75000	9	2013-07-05 13:21:37.616806	15	2
49	1	Mobile	Activo	f	75000	9	2013-07-05 13:21:57.315058	15	2
51	0	Normal	Activo	f	50000	3	2013-07-05 13:22:30.632315	16	2
52	1	Normal	Activo	f	50000	3	2013-07-05 13:22:44.887296	16	2
54	0	Manual de Ref.	Activo	f	10000	6	2013-07-05 13:23:49.302305	17	2
55	1	Manual de Ref.	Activo	f	10000	6	2013-07-05 13:24:04.227335	17	2
57	0	Errata	Activo	f	5000	3	2013-07-05 13:24:41.222259	18	2
58	1	Errata	Activo	f	5000	3	2013-07-05 13:25:11.315728	18	2
47	2	Extreme	Bloqueado	t	100000	7	2013-07-05 13:21:20.869678	14	2
50	2	Mobile	Bloqueado	t	75000	9	2013-07-05 13:22:12.387634	15	2
53	2	Normal	Bloqueado	t	50000	3	2013-07-05 13:23:08.400135	16	2
56	2	Manual de Ref.	Bloqueado	t	10000	6	2013-07-05 13:24:21.012852	17	2
59	2	Errata	Bloqueado	t	5000	3	2013-07-05 13:25:22.930902	18	2
60	0	Op Punto Flotante	Activo	f	10000	3	2013-07-05 13:31:11.050432	19	2
61	1	Op Punto Flotante	Activo	f	10000	3	2013-07-05 13:31:25.559312	19	2
63	0	Barrera Termica	Activo	f	30000	8	2013-07-05 13:32:23.287148	20	2
64	1	Barrera Termica	Activo	f	30000	8	2013-07-05 13:32:46.213816	20	2
65	2	Barrera Termica	Aprobado	f	30000	8	2013-07-05 13:33:08.257943	20	2
67	0	Op Matriz Vector	Activo	f	10000	8	2013-07-05 13:34:19.897199	21	2
68	1	Homologacion	Activo	f	50000	9	2013-07-05 13:34:49.046806	21	2
69	2	Homologacion	Activo	f	50000	9	2013-07-05 13:35:08.663858	21	2
71	0	Op Matriz Vector	Activo	f	10000	8	2013-07-05 13:35:44.607363	22	2
72	1	Op Matriz Vector	Activo	f	10000	8	2013-07-05 13:36:08.990693	22	2
74	0	C1	Activo	f	2	5	2013-07-05 13:48:18.240736	23	3
75	1	C1	Activo	f	2	5	2013-07-05 13:48:29.985779	23	3
77	0	C2	Activo	f	5	2	2013-07-05 13:52:31.871646	24	3
78	1	C2	Activo	f	5	2	2013-07-05 13:52:39.310182	24	3
80	0	T1	Activo	f	3	3	2013-07-05 13:53:03.749773	25	3
81	1	T1	Activo	f	3	3	2013-07-05 13:53:17.22105	25	3
83	0	T2	Activo	f	5	5	2013-07-05 13:53:46.728944	26	3
84	1	T2	Activo	f	5	5	2013-07-05 13:54:01.43068	26	3
86	0	T3	Activo	f	5	7	2013-07-05 13:54:21.315959	27	3
87	1	T3	Activo	f	5	7	2013-07-05 13:54:32.159179	27	3
89	0	Q1	Activo	f	4	4	2013-07-05 13:55:22.864941	28	3
90	1	Q1	Activo	f	4	4	2013-07-05 13:55:53.781805	28	3
92	0	C3	Activo	f	5	5	2013-07-05 13:56:31.854397	29	3
93	1	C3	Activo	f	5	5	2013-07-05 13:56:57.116842	29	3
79	2	C2	Bloqueado	t	5	2	2013-07-05 13:52:50.557565	24	3
82	2	T1	Bloqueado	t	3	3	2013-07-05 13:53:31.598989	25	3
85	2	T2	Bloqueado	t	5	5	2013-07-05 13:54:08.852129	26	3
88	2	T3	Bloqueado	t	5	7	2013-07-05 13:55:03.027474	27	3
94	2	C3	Bloqueado	t	5	5	2013-07-05 13:57:05.744981	29	3
91	2	Q1	Bloqueado	t	4	4	2013-07-05 13:56:10.20642	28	3
95	0	Q2	Activo	f	6	7	2013-07-05 13:57:32.119984	30	3
96	1	Q2	Activo	f	6	7	2013-07-05 14:00:36.601618	30	3
98	0	Q3	Activo	f	5	3	2013-07-05 14:01:25.487166	31	3
99	1	Q3	Activo	f	5	3	2013-07-05 14:01:46.788419	31	3
100	2	Q3	Activo	f	5	3	2013-07-05 14:03:14.933257	31	3
102	0	L1	Activo	f	1	1	2013-07-05 14:05:47.166599	32	3
66	3	Barrera Termica	Aprobado	f	30000	8	2013-07-05 13:33:08.944449	20	2
62	2	Op Punto Flotante	Aprobado	f	10000	3	2013-07-05 13:32:07.137001	19	2
73	2	Op Matriz Vector	Aprobado	f	10000	8	2013-07-05 13:36:26.463043	22	2
103	1	L1	Activo	f	1	1	2013-07-05 14:06:14.403356	32	3
76	2	C1	Bloqueado	t	2	5	2013-07-05 13:48:38.23817	23	3
97	2	Q2	Bloqueado	t	6	7	2013-07-05 14:00:58.558463	30	3
101	3	Q3	Bloqueado	t	5	3	2013-07-05 14:05:27.603847	31	3
104	2	L1	Bloqueado	t	1	1	2013-07-05 14:06:26.950007	32	3
105	0	R1	Activo	f	6	5	2013-07-05 14:13:42.237696	33	3
106	1	R1	Activo	f	6	5	2013-07-05 14:13:56.378265	33	3
108	0	R2	Activo	f	7	5	2013-07-05 14:14:24.27631	34	3
109	1	R2	Activo	f	7	5	2013-07-05 14:14:43.583087	34	3
111	0	P1	Activo	f	8	8	2013-07-05 14:15:20.351715	35	3
112	1	P1	Activo	f	8	8	2013-07-05 14:15:33.919794	35	3
114	0	E1	Activo	f	9	8	2013-07-05 14:16:31.91073	36	3
115	1	E1	Activo	f	9	8	2013-07-05 14:16:52.41589	36	3
117	0	X1	Activo	f	3	2	2013-07-05 14:18:34.297967	37	3
118	1	X1	Activo	f	3	2	2013-07-05 14:18:45.287656	37	3
107	2	R1	Bloqueado	t	6	5	2013-07-05 14:14:12.556679	33	3
110	2	R2	Bloqueado	t	7	5	2013-07-05 14:14:55.060209	34	3
113	2	P1	Bloqueado	t	8	8	2013-07-05 14:16:05.069371	35	3
116	2	E1	Bloqueado	t	9	8	2013-07-05 14:18:17.559755	36	3
119	2	X1	Bloqueado	t	3	2	2013-07-05 14:19:01.123305	37	3
120	0	H1	Activo	f	7	7	2013-07-05 15:16:42.462378	38	3
121	1	H1	Activo	f	7	7	2013-07-05 15:17:03.211082	38	3
123	0	O1	Activo	f	9	8	2013-07-05 15:17:29.799642	39	3
124	1	O1	Activo	f	9	8	2013-07-05 15:17:39.995299	39	3
126	0	H2	Activo	f	9	9	2013-07-05 15:18:12.666601	40	3
127	1	H2	Activo	f	9	9	2013-07-05 15:18:34.151341	40	3
129	0	A1	Activo	f	10	9	2013-07-05 15:19:11.855038	41	3
130	1	A1	Activo	f	10	9	2013-07-05 15:19:24.699421	41	3
132	0	A2	Activo	f	10	9	2013-07-05 15:20:00.103931	42	3
133	1	A2	Activo	f	10	9	2013-07-05 15:20:27.57768	42	3
135	0	A3	Activo	f	10	10	2013-07-05 15:21:02.57153	43	3
136	1	A3	Activo	f	10	10	2013-07-05 15:21:23.449389	43	3
138	0	S1	Activo	f	10	10	2013-07-05 15:21:59.648496	44	3
139	1	S1	Activo	f	10	10	2013-07-05 15:22:21.082875	44	3
122	2	H1	Bloqueado	t	7	7	2013-07-05 15:17:18.510255	38	3
128	2	H2	Bloqueado	t	9	9	2013-07-05 15:18:57.065593	40	3
125	2	O1	Bloqueado	t	9	8	2013-07-05 15:18:01.622315	39	3
131	2	A1	Bloqueado	t	10	9	2013-07-05 15:19:44.605776	41	3
134	2	A2	Bloqueado	t	10	9	2013-07-05 15:20:45.505887	42	3
137	2	A3	Bloqueado	t	10	10	2013-07-05 15:21:48.744792	43	3
140	2	S1	Bloqueado	t	10	10	2013-07-05 15:22:44.499067	44	3
141	0	Calculo Infinitesima	Activo	f	30000	8	2013-07-05 15:31:46.327095	45	4
142	1	Calculo Infinitesima	Activo	f	30000	8	2013-07-05 15:31:56.751117	45	4
144	0	Calculo Integral	Activo	f	35000	9	2013-07-05 15:32:29.146505	46	4
145	1	Calculo Integral	Activo	f	35000	9	2013-07-05 15:32:40.472802	46	4
147	0	Fisica	Activo	f	45000	6	2013-07-05 15:32:57.828194	47	4
148	1	Fisica	Activo	f	45000	6	2013-07-05 15:33:07.970116	47	4
150	0	Fisica II	Activo	f	2500	5	2013-07-05 15:33:39.985293	48	4
151	1	Fisica II	Activo	f	2500	5	2013-07-05 15:33:56.828835	48	4
143	2	Calculo Infinitesima	Bloqueado	t	30000	8	2013-07-05 15:32:04.461678	45	4
146	2	Calculo Integral	Bloqueado	t	35000	9	2013-07-05 15:32:46.936732	46	4
149	2	Fisica	Bloqueado	t	45000	6	2013-07-05 15:33:16.893395	47	4
152	2	Fisica II	Bloqueado	t	2500	5	2013-07-05 15:34:11.295059	48	4
153	0	Calculo I Final	Activo	f	4500	8	2013-07-05 15:37:59.932601	49	4
154	1	Calculo I Final	Eliminado	t	4500	8	2013-07-05 15:38:09.465056	49	4
155	0	Calculo I	Activo	f	4500	8	2013-07-05 15:38:19.296975	50	4
156	1	Primer Final	Activo	f	4500	8	2013-07-05 15:38:37.651008	50	4
157	2	Primer Final	Activo	f	4500	8	2013-07-05 15:38:48.3537	50	4
158	3	Primer Final	Aprobado	t	4500	8	2013-07-05 15:39:01.28035	50	4
159	0	Electromagnetismo	Activo	f	8000	5	2013-07-05 15:39:14.923822	51	4
160	1	Electromagnetismo	Activo	f	8000	5	2013-07-05 15:39:29.584228	51	4
161	2	Electromagnetismo	Aprobado	t	8000	5	2013-07-05 15:39:47.90519	51	4
162	0	Tercer Parcial	Activo	f	4500	6	2013-07-05 15:40:10.917323	52	4
163	1	Tercer Parcial	Activo	f	4500	6	2013-07-05 15:40:20.566258	52	4
164	2	Tercer Parcial	Aprobado	t	4500	6	2013-07-05 15:40:41.83049	52	4
70	3	Homologacion	Aprobado	f	50000	9	2013-07-05 13:35:27.210716	21	2
167	3	Op Punto Flotante	Aprobado	f	10000	3	2013-07-05 23:26:33.101279	19	2
168	4	Op Punto Flotante	Aprobado	f	10000	3	2013-07-05 23:26:50.872275	19	2
169	5	Op Punto Flotante	Activo	t	10000	4	2013-07-05 23:27:04.143072	19	2
170	3	Op Matriz Vector	Activo	t	17000	8	2013-07-05 23:29:29.503892	22	2
165	4	Homologacion	Activo	f	55000	9	2013-07-05 23:26:04.286481	21	2
171	5	Homologacion	Activo	f	55000	9	2013-07-05 23:30:34.576673	21	2
166	4	Barrera Termica	Activo	f	35000	8	2013-07-05 23:26:18.550287	20	2
173	5	Barrera Termica	Activo	t	35000	8	2013-07-05 23:30:59.522477	20	2
172	6	Homologacion	Activo	f	55000	9	2013-07-05 23:30:44.97489	21	2
174	7	Homologacion y Prueb	Activo	t	55000	9	2013-07-05 23:44:42.668246	21	3
\.


--
-- Name: vitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('vitem_id_seq', 174, true);


--
-- Data for Name: voto; Type: TABLE DATA; Schema: public; Owner: -
--

COPY voto (peticion_id, user_id, valor) FROM stdin;
1	2	t
1	4	t
1	3	t
2	2	f
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
-- Name: lb_ver_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY lb_ver
    ADD CONSTRAINT lb_ver_pkey PRIMARY KEY (lb_id, ver_id);


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
-- Name: lb_ver_lb_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lb_ver
    ADD CONSTRAINT lb_ver_lb_id_fkey FOREIGN KEY (lb_id) REFERENCES lineabase(id);


--
-- Name: lb_ver_ver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY lb_ver
    ADD CONSTRAINT lb_ver_ver_id_fkey FOREIGN KEY (ver_id) REFERENCES vitem(id);


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

