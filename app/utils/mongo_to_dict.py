def mongo_to_dict(obj, fieldToRemove=None):
    return_data = []
    for field_name in obj._fields:
        if fieldToRemove and field_name in fieldToRemove:
            continue
        if field_name == "id":
            return_data.append(("id", str(obj.id)))
        else:
            return_data.append((field_name, obj[field_name]))
    return dict(return_data)