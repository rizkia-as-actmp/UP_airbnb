-- name: CreateTicket :execresult
INSERT INTO ticket (
    holder_id,
    host_id,
    valid_at,
    expired_at,
    is_finish,
    price
) VALUES (
    ?, ?, ?, ?, ?, ? 
) ;

-- name: UpdateTicket :execresult
UPDATE ticket 
SET is_finish= TRUE
WHERE id = ?;

-- name: GetListTicket :many
SELECT * FROM ticket WHERE holder_id = ?;