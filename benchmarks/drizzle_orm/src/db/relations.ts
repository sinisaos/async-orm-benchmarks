import { relations } from "drizzle-orm/relations";
import { baseUser, question, questionTag, tag, answer } from "../db/schema.js";

export const questionRelations = relations(question, ({one, many}) => ({
	baseUser: one(baseUser, {
		fields: [question.userId],
		references: [baseUser.id]
	}),
	questionTags: many(questionTag),
	answers: many(answer),
}));

export const baseUserRelations = relations(baseUser, ({many}) => ({
	questions: many(question),
	answers: many(answer),
}));

export const questionTagRelations = relations(questionTag, ({one}) => ({
	question: one(question, {
		fields: [questionTag.questionId],
		references: [question.id]
	}),
	tag: one(tag, {
		fields: [questionTag.tagId],
		references: [tag.id]
	}),
}));

export const tagRelations = relations(tag, ({many}) => ({
	questionTags: many(questionTag),
}));

export const answerRelations = relations(answer, ({one}) => ({
	baseUser: one(baseUser, {
		fields: [answer.userId],
		references: [baseUser.id]
	}),
	question: one(question, {
		fields: [answer.questionId],
		references: [question.id]
	}),
}));