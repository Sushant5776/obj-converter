from uuid import uuid4


def generate_id(as_uuid_obj: bool = False):
    return uuid4() if as_uuid_obj else str(uuid4())
