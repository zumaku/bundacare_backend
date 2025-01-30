--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: nutritions; Type: TABLE; Schema: public; Owner: fadli
--

CREATE TABLE public.nutritions (
    id integer NOT NULL,
    nama_makanan character varying(255) NOT NULL,
    gambar character varying(255) DEFAULT NULL::character varying,
    kalori integer NOT NULL,
    protein integer NOT NULL,
    karbo integer NOT NULL,
    lemak integer NOT NULL,
    judul_deskripsi character varying(255) NOT NULL,
    isi_deskripsi text NOT NULL,
    user_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.nutritions OWNER TO fadli;

--
-- Name: nutritions_id_seq; Type: SEQUENCE; Schema: public; Owner: fadli
--

CREATE SEQUENCE public.nutritions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.nutritions_id_seq OWNER TO fadli;

--
-- Name: nutritions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fadli
--

ALTER SEQUENCE public.nutritions_id_seq OWNED BY public.nutritions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: fadli
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    nik character varying(16) NOT NULL,
    password character varying(255) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.users OWNER TO fadli;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: fadli
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO fadli;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fadli
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: nutritions id; Type: DEFAULT; Schema: public; Owner: fadli
--

ALTER TABLE ONLY public.nutritions ALTER COLUMN id SET DEFAULT nextval('public.nutritions_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: fadli
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: nutritions; Type: TABLE DATA; Schema: public; Owner: fadli
--

COPY public.nutritions (id, nama_makanan, gambar, kalori, protein, karbo, lemak, judul_deskripsi, isi_deskripsi, user_id, created_at) FROM stdin;
1	Nasi Goreng	nasi_goreng.jpg	400	10	50	15	Makanan favorit	Nasi goreng adalah makanan khas Indonesia.	1	2025-01-25 10:33:07
2	Nasi dengan Ayam Rebus	nasi_ayam.jpg	500	35	60	10	Nasi dengan Ayam Rebus	Makanan ini terdiri dari nasi yang kaya karbohidrat (60g) sebagai sumber energi, dan ayam rebus yang tinggi protein (35g) untuk mendukung perkembangan janin.	1	2025-01-28 00:15:00
3	Sup Bayam dan Tahu	sup_bayam_tahu.jpg	150	10	15	5	Sup Bayam dan Tahu	Sup ini mengandung bayam yang kaya akan zat besi dan kalsium, serta tahu yang memberikan protein (10g) dan lemak sehat (5g).	2	2025-01-28 04:30:00
4	Oatmeal dengan Pisang	oatmeal_pisang.jpg	250	6	45	5	Oatmeal dengan Pisang	Oatmeal ini kaya akan serat dan karbohidrat (45g) untuk energi. Pisang memberikan tambahan kalium dan rasa manis alami.	3	2025-01-28 10:45:00
5	Salmon Panggang	salmon_panggang.jpg	350	30	0	20	Salmon Panggang	Salmon kaya akan omega-3 (20g lemak sehat) untuk perkembangan otak bayi, dan protein (30g) untuk pertumbuhan.	1	2025-01-28 23:10:00
6	Telur Orak-Arik dengan Roti Gandum	telur_roti_gandum.jpg	300	12	35	10	Telur Orak-Arik dengan Roti Gandum	Telur memberikan protein (12g) dan lemak sehat (10g), sedangkan roti gandum memberikan serat dan karbohidrat kompleks (35g).	2	2025-01-29 02:25:00
7	Smoothie Buah Campur	smoothie_buah.jpg	200	5	40	2	Smoothie Buah Campur	Smoothie ini kaya vitamin dari buah-buahan segar dan memberikan karbohidrat (40g) untuk energi.	3	2025-01-29 07:40:00
8	Tumis Brokoli dan Wortel	tumis_brokoli_wortel.jpg	120	4	15	5	Tumis Brokoli dan Wortel	Brokoli kaya akan vitamin C dan zat besi, sedangkan wortel memberikan vitamin A. Makanan ini rendah kalori dan lemak.	1	2025-01-30 00:05:00
9	Ikan Tuna Panggang	ikan_tuna.jpg	300	25	0	15	Ikan Tuna Panggang	Ikan tuna adalah sumber protein tinggi (25g) dan lemak sehat (15g), ideal untuk membantu perkembangan janin.	2	2025-01-30 04:45:00
10	Susu Almond	susu_almond.jpg	100	3	8	2	Susu Almond	Susu almond kaya akan kalsium, rendah kalori, dan mengandung lemak sehat untuk mendukung kesehatan tulang.	3	2025-01-30 12:10:00
11	Yogurt dengan Madu	yogurt_madu.jpg	180	8	25	5	Yogurt dengan Madu	Yogurt kaya akan probiotik untuk pencernaan yang sehat. Tambahan madu memberikan rasa manis alami dan karbohidrat (25g).	1	2025-01-31 00:00:00
12	Nasi Goreng dengan Sayur	nasi_goreng_sayur.jpg	450	12	50	15	Nasi Goreng dengan Sayur	Nasi goreng ini mengandung sayur-sayuran kaya vitamin, karbohidrat (50g), protein (12g), dan lemak (15g) untuk energi.	2	2025-01-31 05:30:00
13	Sandwich Ayam	sandwich_ayam.jpg	350	18	40	8	Sandwich Ayam	Sandwich ayam kaya akan protein (18g) dari ayam, serta serat dan karbohidrat kompleks (40g) dari roti gandum.	3	2025-02-01 01:00:00
14	Tahu Goreng Isi	tahu_goreng.jpg	250	10	20	12	Tahu Goreng Isi	Tahu goreng ini mengandung protein (10g) dari tahu dan karbohidrat (20g) dari isian berupa sayur-sayuran.	1	2025-02-01 07:15:00
15	Jus Jeruk dan Wortel	jus_jeruk_wortel.jpg	100	2	22	0	Jus Jeruk dan Wortel	Jus ini kaya akan vitamin C dari jeruk dan vitamin A dari wortel, ideal untuk kesehatan ibu dan bayi.	2	2025-02-01 12:00:00
16	Bubur Kacang Hijau	bubur_kacang_hijau.jpg	300	10	50	5	Bubur Kacang Hijau	Bubur kacang hijau kaya protein (10g) dan karbohidrat (50g), sangat baik untuk energi dan membantu regenerasi sel.	3	2025-02-01 23:30:00
17	Rendang Daging	rendang.jpg	550	25	15	40	Rendang Daging	Rendang kaya protein (25g) dari daging sapi, dan lemak (40g) sebagai sumber energi tambahan.	1	2025-02-02 04:00:00
18	Pisang Rebus	pisang_rebus.jpg	150	2	35	0	Pisang Rebus	Pisang rebus kaya karbohidrat (35g) untuk energi cepat, serta rendah lemak.	2	2025-02-02 08:30:00
19	Sup Kentang dan Ayam	sup_kentang_ayam.jpg	400	20	50	10	Sup Kentang dan Ayam	Sup ini mengandung kentang yang kaya karbohidrat (50g) dan ayam sebagai sumber protein (20g).	3	2025-02-03 01:15:00
20	Avokad dengan Susu	avokad_susu.jpg	300	5	20	25	Avokad dengan Susu	Avokad kaya lemak sehat (25g) dan vitamin, sedangkan susu memberikan protein tambahan (5g).	1	2025-02-03 10:00:00
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: fadli
--

COPY public.users (id, username, nik, password, created_at) FROM stdin;
1	zuma	1234	admin	2025-01-25 10:32:11
2	ijal	4321	admin	2025-01-25 10:37:52
3	isla	1212	admin	2025-01-25 10:37:54
\.


--
-- Name: nutritions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fadli
--

SELECT pg_catalog.setval('public.nutritions_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fadli
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: nutritions nutritions_pkey; Type: CONSTRAINT; Schema: public; Owner: fadli
--

ALTER TABLE ONLY public.nutritions
    ADD CONSTRAINT nutritions_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: fadli
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: nutritions fk_user; Type: FK CONSTRAINT; Schema: public; Owner: fadli
--

ALTER TABLE ONLY public.nutritions
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

