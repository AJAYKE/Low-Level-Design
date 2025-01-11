def validate_request_body(data, fields):
    for field in fields:
        if not (field in data):
            return False
    return True
