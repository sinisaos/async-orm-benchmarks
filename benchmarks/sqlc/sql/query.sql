-- name: ListTags :many
SELECT * FROM tag LIMIT 50;

-- name: SingleTag :one
SELECT * FROM tag WHERE id = $1;

-- name: ListMega :many
SELECT * FROM mega_table LIMIT 50;

-- name: SingleMega :one
SELECT * FROM mega_table WHERE id = $1;

-- name: ListRelated :many
SELECT q.*,
    JSONB_BUILD_OBJECT(
        'id', u.id,
        'username', u.username,
        'email', u.email,
        'superuser', u.superuser
    ) as question_user,
    ARRAY_TO_JSON(
        ARRAY_REMOVE(ARRAY_AGG(DISTINCT t), NULL)
    ) as question_tags
FROM question q
LEFT JOIN base_user u ON q.user_id = u.id
LEFT JOIN question_tag qt ON qt.question_id = q.id
LEFT JOIN tag t ON t.id = qt.tag_id
GROUP BY q.id, u.id
ORDER BY q.id
LIMIT 50;

-- name: SingleRelated :one
SELECT q.*,
    JSONB_BUILD_OBJECT(
        'id', u.id,
        'username', u.username,
        'email', u.email,
        'superuser', u.superuser
    ) as question_user,
    ARRAY_TO_JSON(
        ARRAY_REMOVE(ARRAY_AGG(DISTINCT t), NULL)
    ) as question_tags,
    ARRAY_TO_JSON(
        ARRAY_REMOVE(ARRAY_AGG(DISTINCT a), NULL)
    ) as question_answers
FROM question q
JOIN base_user u ON q.user_id = u.id
LEFT JOIN question_tag qt ON qt.question_id = q.id
LEFT JOIN tag t ON t.id = qt.tag_id
LEFT JOIN answer a ON a.question_id = q.id
WHERE q.id = $1
GROUP BY q.id, u.id;