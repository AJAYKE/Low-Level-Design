def validate_request_body(data, fields):
    for field in fields:
        if not ((field in data) or (data[field] is None)):
            return False
    return True


def validate_location(location):
    if not isinstance(location, list) or len(location) != 2:
        return False
    return all(isinstance(coord, (int, float)) for coord in location)
