def throwExcessPayloadError(payload, allowed_keys):
    excess_keys = payload.keys() - allowed_keys
    if excess_keys:
        raise Exception(f"Unexpected keys in payload: {', '.join(excess_keys)}")
        # expected_keys = {'username', 'password',"repeatPassword", "admin", "role"}
    # payload_keys = set(request.json.keys())
    # if not payload_keys.issubset(expected_keys):
    #     excess_keys = payload_keys - expected_keys
    #     return jsonify({"msg": f"Unexpected keys in payload: {', '.join(excess_keys)}"}), 400
