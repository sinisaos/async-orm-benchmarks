import { Hono } from 'hono';
import { serve } from '@hono/node-server';
import { db } from './db/index.js';
import * as schema from './db/schema.js';
import { eq } from 'drizzle-orm';
import { tag } from './db/schema.js';

const app = new Hono();


app.get('/small-table/', async (c) => {
  const data = await db.query.tag.findMany({ limit: 50 });
  return c.json(data);
});

app.get('/small-table/:pk/', async (c) => {
  const pk = parseInt(c.req.param('pk'));
  const data = await db.query.tag.findFirst({
    where: eq(schema.tag.id, pk)
  });
  return c.json(data);
});

app.post('/small-table/bulk/', async (c) => {
  const items = Array.from({ length: 100 }, (_, i) => ({ name: `item_${i}` }));
  await db.insert(tag).values(items);
  return c.json({ status: 'ok' });
});

app.get('/related-table/', async (c) => {
  const data = await db.query.question.findMany({
    limit: 50,
    with: {
      baseUser: true, 
      questionTags: { }
    }
  });
  return c.json(data);
});

app.get('/related-table/:pk/', async (c) => {
  const pk = parseInt(c.req.param('pk'));
  const data = await db.query.question.findFirst({
    where: eq(schema.question.id, pk),
    with: {
      baseUser: true, 
      questionTags: { },
      answers: {
        orderBy: (answers, { desc }) => [desc(answers.id)]
      }
    }
  });
  return c.json(data);
});

// query builder does not have better performance and is much more 
// complicated to write, which means that drizzle is excellently optimized

// app.get('/related-table/', async (c) => {
//   const rows = await db
//     .select()
//     .from(schema.question)
//     .leftJoin(schema.baseUser, eq(schema.question.userId, schema.baseUser.id))
//     .leftJoin(schema.questionTag, eq(schema.question.id, schema.questionTag.questionId))
//     .leftJoin(schema.tag, eq(schema.questionTag.tagId, schema.tag.id))
//     .limit(50);

//   // Ručno ugnježđivanje
//   const map = new Map();
//   for (const row of rows) {
//     if (!map.has(row.question.id)) {
//       map.set(row.question.id, { ...row.question, baseUser: row.base_user, tags: [] });
//     }
//     if (row.tag) map.get(row.question.id).tags.push(row.tag);
//   }
//   return c.json(Array.from(map.values()));
// });

// app.get('/related-table/:pk/', async (c) => {
//   const pk = parseInt(c.req.param('pk'));
//   const rows = await db
//     .select()
//     .from(schema.question)
//     .leftJoin(schema.baseUser, eq(schema.question.userId, schema.baseUser.id))
//     .leftJoin(schema.questionTag, eq(schema.question.id, schema.questionTag.questionId))
//     .leftJoin(schema.tag, eq(schema.questionTag.tagId, schema.tag.id))
//     .where(eq(schema.question.id, pk));

//   const answers = await db
//     .select()
//     .from(schema.answer)
//     .where(eq(schema.answer.questionId, pk))
//     .orderBy(desc(schema.answer.id));

//   const firstRow = rows[0];
//   if (!firstRow) return c.json({ error: "Not found" }, 404);

//   const result = {
//     ...firstRow.question,
//     baseUser: firstRow.base_user,
//     tags: rows
//       .filter(r => r.tag !== null)
//       .map(r => r.tag),
//     answers: answers
//   };
//   return c.json(result);
// });

app.get('/mega-table/', async (c) => {
  const data = await db.query.megaTable.findMany({ limit: 50 });
  return c.json(data);
});

app.get('/mega-table/:pk/', async (c) => {
  const pk = parseInt(c.req.param('pk'));
  const data = await db.query.megaTable.findFirst({
    where: eq(schema.megaTable.id, pk)
  });
  return c.json(data);
});

serve({
  fetch: app.fetch,
  port: 8000
})