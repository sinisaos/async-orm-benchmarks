SELECT q.*,
    JSONB_BUILD_OBJECT(
        'id', u.id,
        'username', u.username,
        'email', u.email,
        'superuser', u.superuser
    ) question_user,
    ARRAY_TO_JSON(
        ARRAY_REMOVE(
            ARRAY_AGG(DISTINCT t), NULL)
    ) question_tags,
    ARRAY_TO_JSON(
        ARRAY_REMOVE(
            ARRAY_AGG(DISTINCT a), NULL)
    ) question_answers
FROM question q
JOIN base_user u ON q.user_id = u.id
LEFT JOIN question_tag qt ON qt.question_id = q.id
LEFT JOIN tag t ON t.id = qt.tag_id
LEFT JOIN answer a ON a.question_id = q.id
WHERE q.id = $1
GROUP BY q.id, u.id;