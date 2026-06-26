package main

import (
	"database/sql"
	"log"
	"net/http"
	"strconv"

	"sinisaos/env/orm-benchmarks/benchmarks/sqlc/db"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/goccy/go-json"
	_ "github.com/jackc/pgx/v5/stdlib"
)

func main() {
	// Standard sql.DB
	conn, err := sql.Open("pgx", "postgres://postgres:postgres@localhost:5432/perfdb")
	if err != nil {
		log.Fatal(err)
	}
	conn.SetMaxIdleConns(20)
	conn.SetMaxOpenConns(20)

	// sqlc Queries object
	queries := db.New(conn)

	r := chi.NewRouter()
	r.Use(middleware.Recoverer)

	// Small Table routes
	r.Get("/small-table/", GetSmallTableList(queries))
	r.Get("/small-table/{id}/", GetSmallTableSingle(queries))

	// Mega Table routes
	r.Get("/mega-table/", GetMegaTableList(queries))
	r.Get("/mega-table/{id}/", GetMegaTableSingle(queries))

	// Related Table routes
	r.Get("/related-table/", GetQuestionsList(queries))
	r.Get("/related-table/{id}/", GetSingleQuestion(queries))

	http.ListenAndServe(":8000", r)
}

// JSON helper
func writeJSON(w http.ResponseWriter, data []byte) {
	w.Header().Set("Content-Type", "application/json")
	w.Write(data)
}

func GetQuestionsList(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		items, err := q.ListRelated(r.Context())
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		// We need to encode
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(items)
	}
}

func GetSingleQuestion(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id, _ := strconv.Atoi(idStr)

		item, err := q.SingleRelated(r.Context(), int32(id))
		if err != nil {
			http.Error(w, "Not found", http.StatusNotFound)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(item)
	}
}

func GetSmallTableList(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		data, err := q.ListTags(r.Context())
		if err != nil {
			http.Error(w, err.Error(), 500)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func GetSmallTableSingle(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id, _ := strconv.Atoi(idStr)

		data, err := q.SingleTag(r.Context(), int32(id))
		if err != nil {
			http.Error(w, "Not found", 404)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func GetMegaTableList(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		data, err := q.ListMega(r.Context())
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}

func GetMegaTableSingle(q *db.Queries) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		idStr := chi.URLParam(r, "id")
		id, err := strconv.Atoi(idStr)
		if err != nil {
			http.Error(w, "Invalid ID", http.StatusBadRequest)
			return
		}

		data, err := q.SingleMega(r.Context(), int32(id))
		if err != nil {
			http.Error(w, "Not found", http.StatusNotFound)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(data)
	}
}
