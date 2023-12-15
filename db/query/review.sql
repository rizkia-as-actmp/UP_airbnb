-- name: CreateReview :execresult
INSERT INTO review (
    ticket_id,
    writer_id,
    host_id,
    writer_name,
    comment,
    created_at
) VALUES (
    ?, ?, ?, ?, ?, ? 
) ;

-- name: GetListReview :many
SELECT * FROM review WHERE host_id = ?;