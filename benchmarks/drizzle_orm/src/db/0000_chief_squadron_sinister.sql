-- Current sql file was generated after introspecting the database
-- If you want to run this migration please uncomment this code before executing migrations
/*
CREATE TABLE "base_user" (
	"id" serial PRIMARY KEY NOT NULL,
	"username" varchar(255) DEFAULT '' NOT NULL,
	"email" varchar(255) DEFAULT '' NOT NULL,
	"superuser" boolean DEFAULT false NOT NULL
);
--> statement-breakpoint
CREATE TABLE "question" (
	"id" serial PRIMARY KEY NOT NULL,
	"title" varchar(255) DEFAULT '' NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"created_at" timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
	"updated_at" timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
	"views" integer DEFAULT 0 NOT NULL,
	"likes" integer DEFAULT 0 NOT NULL,
	"user_id" integer
);
--> statement-breakpoint
CREATE TABLE "tag" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" varchar(255) DEFAULT '' NOT NULL
);
--> statement-breakpoint
CREATE TABLE "question_tag" (
	"id" serial PRIMARY KEY NOT NULL,
	"question_id" integer,
	"tag_id" integer
);
--> statement-breakpoint
CREATE TABLE "answer" (
	"id" serial PRIMARY KEY NOT NULL,
	"content" text DEFAULT '' NOT NULL,
	"created_at" timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
	"updated_at" timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
	"likes" integer DEFAULT 0 NOT NULL,
	"user_id" integer,
	"question_id" integer
);
--> statement-breakpoint
CREATE TABLE "mega_table" (
	"id" serial PRIMARY KEY NOT NULL,
	"float_col_1" double precision DEFAULT 2.2 NOT NULL,
	"smallint_col_1" smallint DEFAULT 2 NOT NULL,
	"integer_col_1" integer DEFAULT 2000000 NOT NULL,
	"bigint_col_1" bigint DEFAULT 99999999 NOT NULL,
	"varchar_col_1" varchar(255) DEFAULT 'value1' NOT NULL,
	"text_col_1" text DEFAULT 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.' NOT NULL,
	"numeric_col_1" numeric(5, 2) DEFAULT '2.2' NOT NULL,
	"json_col_1" json DEFAULT '{"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}'::json NOT NULL,
	"float_col_2" double precision DEFAULT 2.2 NOT NULL,
	"smallint_col_2" smallint DEFAULT 2 NOT NULL,
	"integer_col_2" integer DEFAULT 2000000 NOT NULL,
	"bigint_col_2" bigint DEFAULT 99999999 NOT NULL,
	"varchar_col_2" varchar(255) DEFAULT 'value1' NOT NULL,
	"text_col_2" text DEFAULT 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.' NOT NULL,
	"numeric_col_2" numeric(5, 2) DEFAULT '2.2' NOT NULL,
	"json_col_2" json DEFAULT '{"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}'::json NOT NULL,
	"float_col_3" double precision DEFAULT 2.2 NOT NULL,
	"smallint_col_3" smallint DEFAULT 2 NOT NULL,
	"integer_col_3" integer DEFAULT 2000000 NOT NULL,
	"bigint_col_3" bigint DEFAULT 99999999 NOT NULL,
	"varchar_col_3" varchar(255) DEFAULT 'value1' NOT NULL,
	"text_col_3" text DEFAULT 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.' NOT NULL,
	"numeric_col_3" numeric(5, 2) DEFAULT '2.2' NOT NULL,
	"json_col_3" json DEFAULT '{"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}'::json NOT NULL
);
--> statement-breakpoint
ALTER TABLE "question" ADD CONSTRAINT "question_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."base_user"("id") ON DELETE cascade ON UPDATE cascade;--> statement-breakpoint
ALTER TABLE "question_tag" ADD CONSTRAINT "question_tag_question_id_fkey" FOREIGN KEY ("question_id") REFERENCES "public"."question"("id") ON DELETE cascade ON UPDATE cascade;--> statement-breakpoint
ALTER TABLE "question_tag" ADD CONSTRAINT "question_tag_tag_id_fkey" FOREIGN KEY ("tag_id") REFERENCES "public"."tag"("id") ON DELETE cascade ON UPDATE cascade;--> statement-breakpoint
ALTER TABLE "answer" ADD CONSTRAINT "answer_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."base_user"("id") ON DELETE cascade ON UPDATE cascade;--> statement-breakpoint
ALTER TABLE "answer" ADD CONSTRAINT "answer_question_id_fkey" FOREIGN KEY ("question_id") REFERENCES "public"."question"("id") ON DELETE cascade ON UPDATE cascade;--> statement-breakpoint
CREATE INDEX "idx_question_user_id" ON "question" USING btree ("user_id" int4_ops);--> statement-breakpoint
CREATE INDEX "idx_question_tag_question_id" ON "question_tag" USING btree ("question_id" int4_ops);--> statement-breakpoint
CREATE INDEX "idx_question_tag_tag_id" ON "question_tag" USING btree ("tag_id" int4_ops);--> statement-breakpoint
CREATE UNIQUE INDEX "uq_question_tag_pair" ON "question_tag" USING btree ("question_id" int4_ops,"tag_id" int4_ops);--> statement-breakpoint
CREATE INDEX "idx_answer_question_id" ON "answer" USING btree ("question_id" int4_ops);--> statement-breakpoint
CREATE INDEX "idx_answer_user_id" ON "answer" USING btree ("user_id" int4_ops);
*/