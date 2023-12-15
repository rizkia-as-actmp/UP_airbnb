-- name: CreateHost :execresult
INSERT INTO host (
    owner_id,
    title,
    description,
    type,
    location,
    facilities,
    price
) VALUES (
    ?, ?, ?, ?, ?, ?, ?
) ;

-- name: GetHost :one
SELECT * FROM host WHERE id = ? LIMIT 1;


-- name: UpdateHost :execresult
UPDATE host
SET 
    title= ?,
    description= ?,
    type= ?,
    location= ?,
    facilities= ?,
    price= ? 
WHERE id= ?;

-- name: ListHost :many
SELECT * from host;

-- name: ListHostByOwner :many
SELECT * from host WHERE owner_id = ? ;

-- name: DeleteHost :execresult
DELETE from host WHERE id = ?;