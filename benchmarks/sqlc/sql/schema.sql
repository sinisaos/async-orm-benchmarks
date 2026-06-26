--
-- PostgreSQL database dump
--

\restrict APIT6boxJv12HUEK7cRuO6bgcKuwJmZDL6qq8a0v8HgjD648S0blRfB1A6Jbjf5

-- Dumped from database version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    content character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    likes integer NOT NULL,
    user_id integer,
    question_id integer
);


ALTER TABLE public.answer OWNER TO postgres;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.answer_id_seq OWNER TO postgres;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: base_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.base_user (
    id integer NOT NULL,
    username character varying NOT NULL,
    email character varying NOT NULL,
    superuser boolean NOT NULL
);


ALTER TABLE public.base_user OWNER TO postgres;

--
-- Name: base_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.base_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.base_user_id_seq OWNER TO postgres;

--
-- Name: base_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.base_user_id_seq OWNED BY public.base_user.id;


--
-- Name: mega_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mega_table (
    id integer NOT NULL,
    float_col_1 double precision NOT NULL,
    smallint_col_1 smallint NOT NULL,
    integer_col_1 integer NOT NULL,
    bigint_col_1 bigint NOT NULL,
    varchar_col_1 character varying NOT NULL,
    text_col_1 character varying NOT NULL,
    numeric_col_1 double precision NOT NULL,
    json_col_1 jsonb NOT NULL,
    float_col_2 double precision NOT NULL,
    smallint_col_2 smallint NOT NULL,
    integer_col_2 integer NOT NULL,
    bigint_col_2 bigint NOT NULL,
    varchar_col_2 character varying NOT NULL,
    text_col_2 character varying NOT NULL,
    numeric_col_2 double precision NOT NULL,
    json_col_2 jsonb NOT NULL,
    float_col_3 double precision NOT NULL,
    smallint_col_3 smallint NOT NULL,
    integer_col_3 integer NOT NULL,
    bigint_col_3 bigint NOT NULL,
    varchar_col_3 character varying NOT NULL,
    text_col_3 character varying NOT NULL,
    numeric_col_3 double precision NOT NULL,
    json_col_3 jsonb NOT NULL
);


ALTER TABLE public.mega_table OWNER TO postgres;

--
-- Name: mega_table_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mega_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.mega_table_id_seq OWNER TO postgres;

--
-- Name: mega_table_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mega_table_id_seq OWNED BY public.mega_table.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question (
    id integer NOT NULL,
    title character varying NOT NULL,
    content character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    views integer NOT NULL,
    likes integer NOT NULL,
    user_id integer
);


ALTER TABLE public.question OWNER TO postgres;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.question_id_seq OWNER TO postgres;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_tag (
    id integer NOT NULL,
    question_id integer,
    tag_id integer
);


ALTER TABLE public.question_tag OWNER TO postgres;

--
-- Name: question_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.question_tag_id_seq OWNER TO postgres;

--
-- Name: question_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.question_tag_id_seq OWNED BY public.question_tag.id;


--
-- Name: tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.tag OWNER TO postgres;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tag_id_seq OWNER TO postgres;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: base_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.base_user ALTER COLUMN id SET DEFAULT nextval('public.base_user_id_seq'::regclass);


--
-- Name: mega_table id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mega_table ALTER COLUMN id SET DEFAULT nextval('public.mega_table_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: question_tag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_tag ALTER COLUMN id SET DEFAULT nextval('public.question_tag_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Name: answer answer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_pkey PRIMARY KEY (id);


--
-- Name: base_user base_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.base_user
    ADD CONSTRAINT base_user_pkey PRIMARY KEY (id);


--
-- Name: mega_table mega_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mega_table
    ADD CONSTRAINT mega_table_pkey PRIMARY KEY (id);


--
-- Name: question question_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);


--
-- Name: question_tag question_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT question_tag_pkey PRIMARY KEY (id);


--
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- Name: idx_answer_question_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_answer_question_id ON public.answer USING btree (question_id);


--
-- Name: idx_answer_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_answer_user_id ON public.answer USING btree (user_id);


--
-- Name: idx_question_tag_question_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_question_tag_question_id ON public.question_tag USING btree (question_id);


--
-- Name: idx_question_tag_tag_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_question_tag_tag_id ON public.question_tag USING btree (tag_id);


--
-- Name: idx_question_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_question_user_id ON public.question USING btree (user_id);


--
-- Name: uq_question_tag_pair; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX uq_question_tag_pair ON public.question_tag USING btree (question_id, tag_id);


--
-- Name: answer answer_base_user_answers; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_base_user_answers FOREIGN KEY (user_id) REFERENCES public.base_user(id) ON DELETE SET NULL;


--
-- Name: answer answer_question_answers; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_question_answers FOREIGN KEY (question_id) REFERENCES public.question(id) ON DELETE SET NULL;


--
-- Name: question question_base_user_questions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_base_user_questions FOREIGN KEY (user_id) REFERENCES public.base_user(id) ON DELETE SET NULL;


--
-- Name: question_tag question_tag_question_question_tags; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT question_tag_question_question_tags FOREIGN KEY (question_id) REFERENCES public.question(id) ON DELETE SET NULL;


--
-- Name: question_tag question_tag_tag_question_tags; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT question_tag_tag_question_tags FOREIGN KEY (tag_id) REFERENCES public.tag(id) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

\unrestrict APIT6boxJv12HUEK7cRuO6bgcKuwJmZDL6qq8a0v8HgjD648S0blRfB1A6Jbjf5

