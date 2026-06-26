import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';
import * as schema from '../db/schema.js';
import * as relations from '../db/relations.js';

const connectionString = 'postgres://postgres:postgres@localhost:5432/perfdb';

const client = postgres(connectionString, {
  max: 20,
  prepare: false,
});

export const db = drizzle(client, { 
  schema: { 
    ...schema, 
    ...relations 
  } 
});