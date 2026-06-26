package main

import (
	"context"
	"database/sql"
	"ent_orm/ent"
	"ent_orm/ent/megatable"
	"ent_orm/ent/question"
	"ent_orm/ent/tag"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"time"

	"entgo.io/ent/dialect"
	entsql "entgo.io/ent/dialect/sql"
	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/goccy/go-json"

	_ "github.com/jackc/pgx/v5/stdlib"
)

// Open new connection
func Open(dsn string) *ent.Client {
	db, err := sql.Open("pgx", dsn)
	if err != nil {
		log.Fatal(err)
	}
	db.SetMaxIdleConns(20)
	db.SetMaxOpenConns(20)
	db.SetConnMaxLifetime(time.Hour)

	// Create an Ent driver from the existing sql.DB connection
	drv := entsql.OpenDB(dialect.Postgres, db)

	// Initialize the Ent client with that driver
	return ent.NewClient(ent.Driver(drv))
}

func main() {
	client := Open("postgres://postgres:postgres@localhost:5432/perfdb")

	defer client.Close()

	if err := client.Schema.Create(context.Background()); err != nil {
		log.Fatalf("failed creating schema resources: %v", err)
	}

	r := chi.NewRouter()
	r.Use(middleware.Recoverer)

	// Small Table routes
	r.Get("/small-table/", GetSmallTableList(client))
	r.Get("/small-table/{id}/", GetSmallTableSingle(client))
	r.Post("/small-table/bulk/", BulkInsert(client))

	// Mega Table routes
	r.Get("/mega-table/", GetMegaTableList(client))
	r.Get("/mega-table/{id}/", GetMegaTableSingle(client))

	// Related Table routes
	r.Get("/related-table/", GetQuestionsList(client))
	r.Get("/related-table/{id}/", GetSingleQuestion(client))

	http.ListenAndServe(":8000", r)
}

func GetQuestionsList(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// Eager loading for relations (User and Tags)
		questions, err := client.Question.Query().
			WithBaseUser().
			WithQuestionTags().
			Limit(50).
			All(r.Context())

		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		// goccy/go-json is extremely fast for these operations
		json.NewEncoder(w).Encode(questions)
	}
}

func GetSingleQuestion(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id64, err := strconv.ParseUint(idStr, 10, 64)
		if err != nil {
			http.Error(w, "Invalid ID format", http.StatusBadRequest)
			return
		}
		id := uint(id64)

		q, err := client.Question.Query().
			Where(question.ID(id)).
			WithBaseUser().
			WithQuestionTags().
			WithAnswers().
			Only(r.Context())

		if err != nil {
			http.Error(w, "Not found", http.StatusNotFound)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(q)
	}
}

func GetSmallTableList(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		data, err := client.Tag.Query().Limit(50).All(r.Context())
		if err != nil {
			http.Error(w, err.Error(), 500)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func GetSmallTableSingle(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id64, err := strconv.ParseUint(idStr, 10, 64)
		if err != nil {
			http.Error(w, "Invalid ID format", http.StatusBadRequest)
			return
		}
		id := uint(id64)

		data, err := client.Tag.Query().Where(tag.ID(id)).Only(r.Context())
		if err != nil {
			http.Error(w, "Not found", 404)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func BulkInsert(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		builders := make([]*ent.TagCreate, 100)

		for i := 0; i < 100; i++ {
			builders[i] = client.Tag.Create().SetName(fmt.Sprintf("item_%d", i))
		}

		_, err := client.Tag.CreateBulk(builders...).Save(r.Context())
		if err != nil {
			http.Error(w, err.Error(), 500)
			return
		}

		w.Write([]byte("ok"))
	}
}

func GetMegaTableList(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		data, err := client.MegaTable.Query().Limit(50).All(r.Context())
		if err != nil {
			http.Error(w, err.Error(), 500)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func GetMegaTableSingle(client *ent.Client) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id64, err := strconv.ParseUint(idStr, 10, 64)
		if err != nil {
			http.Error(w, "Invalid ID format", http.StatusBadRequest)
			return
		}
		id := uint(id64)

		data, err := client.MegaTable.Query().
			Where(megatable.ID(id)).
			Only(r.Context())

		if err != nil {
			http.Error(w, "Not found", 404)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}
