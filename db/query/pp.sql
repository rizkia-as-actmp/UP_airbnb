-- name: CreatePP :execresult
INSERT INTO pp (
    account_id,
    image_bytes
) VALUES (
    ?, ?
) ;

-- name: GetPP :one
SELECT * FROM pp WHERE account_id = ?;

-- name: DeletePP :execresult
DELETE FROM pp WHERE account_id = ?;