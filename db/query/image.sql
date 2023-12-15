-- name: CreateImage :execresult
INSERT INTO image (
    host_id,
    image_bytes
) VALUES (
    ?, ?
) ;

-- name: UpdateImage :execresult
UPDATE image 
SET image_bytes= ?
WHERE id = ?;

-- name: GetImage :one
SELECT * FROM image WHERE host_id = ?;

-- name: GetListImage :many
SELECT * FROM image WHERE host_id IN (?);

-- name: DeleteImage :execresult
DELETE FROM image WHERE host_id = ?;