-- name: CreateAccount :execresult
INSERT INTO account ( 
    full_name, 
    email, 
    password
) VALUES (
    ?, ?, ?
) ;

-- name: GetAccount :one
SELECT * FROM account WHERE id = ? LIMIT 1;

-- name: GetAccountByEmail :one
SELECT * FROM account WHERE email = ? LIMIT 1;