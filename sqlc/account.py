# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.24.0
# source: account.sql
import dataclasses
from typing import Any

import sqlalchemy

from sqlc import models


CREATE_ACCOUNT = """-- name: create_account \\:execresult
INSERT INTO account ( 
    full_name, 
    email, 
    password
) VALUES (
    :p1, :p2, :p3
)
"""


@dataclasses.dataclass()
class CreateAccountParams:
    full_name: Any
    email: Any
    password: Any


GET_ACCOUNT = """-- name: get_account \\:one
SELECT id, full_name, email, password FROM account WHERE id = :p1 LIMIT 1
"""

GET_ACCOUNT_BY_EMAIL = """-- name: get_account_by_email \\:one
SELECT id, full_name, email, password FROM account WHERE email = :p1 LIMIT 1
"""


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_account(self, arg: CreateAccountParams) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(CREATE_ACCOUNT), {"p1": arg.full_name, "p2": arg.email, "p3": arg.password})

    def get_account(self, *, id: Any) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(GET_ACCOUNT), {"p1": id})
    
    def get_account_by_email(self, *, email: Any) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(GET_ACCOUNT_BY_EMAIL), {"p1": email})
