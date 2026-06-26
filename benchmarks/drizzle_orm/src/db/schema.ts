import { pgTable, serial, varchar, boolean, index, foreignKey, text, timestamp, integer, uniqueIndex, doublePrecision, smallint, bigint, numeric, json } from "drizzle-orm/pg-core"
import { sql } from "drizzle-orm"



export const baseUser = pgTable("base_user", {
	id: serial().primaryKey().notNull(),
	username: varchar({ length: 255 }).default('').notNull(),
	email: varchar({ length: 255 }).default('').notNull(),
	superuser: boolean().default(false).notNull(),
});

export const question = pgTable("question", {
	id: serial().primaryKey().notNull(),
	title: varchar({ length: 255 }).default('').notNull(),
	content: text().default('').notNull(),
	createdAt: timestamp("created_at", { withTimezone: true, mode: 'string' }).default(sql`CURRENT_TIMESTAMP`).notNull(),
	updatedAt: timestamp("updated_at", { withTimezone: true, mode: 'string' }).default(sql`CURRENT_TIMESTAMP`).notNull(),
	views: integer().default(0).notNull(),
	likes: integer().default(0).notNull(),
	userId: integer("user_id"),
}, (table) => [
	index("idx_question_user_id").using("btree", table.userId.asc().nullsLast().op("int4_ops")),
	foreignKey({
			columns: [table.userId],
			foreignColumns: [baseUser.id],
			name: "question_user_id_fkey"
		}).onUpdate("cascade").onDelete("cascade"),
]);

export const tag = pgTable("tag", {
	id: serial().primaryKey().notNull(),
	name: varchar({ length: 255 }).default('').notNull(),
});

export const questionTag = pgTable("question_tag", {
	id: serial().primaryKey().notNull(),
	questionId: integer("question_id"),
	tagId: integer("tag_id"),
}, (table) => [
	index("idx_question_tag_question_id").using("btree", table.questionId.asc().nullsLast().op("int4_ops")),
	index("idx_question_tag_tag_id").using("btree", table.tagId.asc().nullsLast().op("int4_ops")),
	uniqueIndex("uq_question_tag_pair").using("btree", table.questionId.asc().nullsLast().op("int4_ops"), table.tagId.asc().nullsLast().op("int4_ops")),
	foreignKey({
			columns: [table.questionId],
			foreignColumns: [question.id],
			name: "question_tag_question_id_fkey"
		}).onUpdate("cascade").onDelete("cascade"),
	foreignKey({
			columns: [table.tagId],
			foreignColumns: [tag.id],
			name: "question_tag_tag_id_fkey"
		}).onUpdate("cascade").onDelete("cascade"),
]);

export const answer = pgTable("answer", {
	id: serial().primaryKey().notNull(),
	content: text().default('').notNull(),
	createdAt: timestamp("created_at", { withTimezone: true, mode: 'string' }).default(sql`CURRENT_TIMESTAMP`).notNull(),
	updatedAt: timestamp("updated_at", { withTimezone: true, mode: 'string' }).default(sql`CURRENT_TIMESTAMP`).notNull(),
	likes: integer().default(0).notNull(),
	userId: integer("user_id"),
	questionId: integer("question_id"),
}, (table) => [
	index("idx_answer_question_id").using("btree", table.questionId.asc().nullsLast().op("int4_ops")),
	index("idx_answer_user_id").using("btree", table.userId.asc().nullsLast().op("int4_ops")),
	foreignKey({
			columns: [table.userId],
			foreignColumns: [baseUser.id],
			name: "answer_user_id_fkey"
		}).onUpdate("cascade").onDelete("cascade"),
	foreignKey({
			columns: [table.questionId],
			foreignColumns: [question.id],
			name: "answer_question_id_fkey"
		}).onUpdate("cascade").onDelete("cascade"),
]);

export const megaTable = pgTable("mega_table", {
	id: serial().primaryKey().notNull(),
	floatCol1: doublePrecision("float_col_1").default(2.2).notNull(),
	smallintCol1: smallint("smallint_col_1").default(2).notNull(),
	integerCol1: integer("integer_col_1").default(2000000).notNull(),
	// You can use { mode: "bigint" } if numbers are exceeding js number limitations
	bigintCol1: bigint("bigint_col_1", { mode: "number" }).default(99999999).notNull(),
	varcharCol1: varchar("varchar_col_1", { length: 255 }).default('value1').notNull(),
	textCol1: text("text_col_1").default('Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.').notNull(),
	numericCol1: numeric("numeric_col_1", { precision: 5, scale:  2 }).default('2.2').notNull(),
	jsonCol1: json("json_col_1").default({"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}).notNull(),
	floatCol2: doublePrecision("float_col_2").default(2.2).notNull(),
	smallintCol2: smallint("smallint_col_2").default(2).notNull(),
	integerCol2: integer("integer_col_2").default(2000000).notNull(),
	// You can use { mode: "bigint" } if numbers are exceeding js number limitations
	bigintCol2: bigint("bigint_col_2", { mode: "number" }).default(99999999).notNull(),
	varcharCol2: varchar("varchar_col_2", { length: 255 }).default('value1').notNull(),
	textCol2: text("text_col_2").default('Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.').notNull(),
	numericCol2: numeric("numeric_col_2", { precision: 5, scale:  2 }).default('2.2').notNull(),
	jsonCol2: json("json_col_2").default({"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}).notNull(),
	floatCol3: doublePrecision("float_col_3").default(2.2).notNull(),
	smallintCol3: smallint("smallint_col_3").default(2).notNull(),
	integerCol3: integer("integer_col_3").default(2000000).notNull(),
	// You can use { mode: "bigint" } if numbers are exceeding js number limitations
	bigintCol3: bigint("bigint_col_3", { mode: "number" }).default(99999999).notNull(),
	varcharCol3: varchar("varchar_col_3", { length: 255 }).default('value1').notNull(),
	textCol3: text("text_col_3").default('Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.').notNull(),
	numericCol3: numeric("numeric_col_3", { precision: 5, scale:  2 }).default('2.2').notNull(),
	jsonCol3: json("json_col_3").default({"a":1,"b":"b","c":[2],"d":{"e":3},"f":true}).notNull(),
});
