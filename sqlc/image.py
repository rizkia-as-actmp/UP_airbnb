# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.24.0
# source: image.sql
import dataclasses
from typing import Any, Iterator, Optional

import sqlalchemy

from sqlc import models


CREATE_IMAGE = """-- name: create_image \\:execresult
INSERT INTO image (
    host_id,
    image_bytes
) VALUES (
    :p1, :p2
)
"""


@dataclasses.dataclass()
class CreateImageParams:
    host_id: Optional[Any]
    image_bytes: Any


DELETE_IMAGE = """-- name: delete_image \\:execresult
DELETE FROM image WHERE host_id = :p1
"""


GET_IMAGE = """-- name: get_image \\:one
SELECT id, host_id, image_bytes FROM image WHERE host_id = :p1
"""

GET_LIST_IMAGE = """-- name: get_list_image \\:many
SELECT id, host_id, image_bytes FROM image WHERE host_id IN (:p1)
"""

UPDATE_IMAGE = """-- name: update_image \\:execresult
UPDATE image 
SET image_bytes= :p1
WHERE id = :p2
"""


@dataclasses.dataclass()
class UpdateImageParams:
    image_bytes: Any
    id: Any


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_image(self, arg: CreateImageParams) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(CREATE_IMAGE), {"p1": arg.host_id, "p2": arg.image_bytes})

    def delete_image(self, *, host_id: Optional[Any]) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(DELETE_IMAGE), {"p1": host_id})

    def get_image(self, *, host_id: Optional[Any]) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(GET_IMAGE), {"p1": host_id})
    
    def get_list_image(self, *, host_id: Optional[Any]) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(GET_LIST_IMAGE), {"p1": host_id})

    def update_image(self, arg: UpdateImageParams) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(UPDATE_IMAGE), {"p1": arg.image_bytes, "p2": arg.id})