# tools/config_api.py
config = {"plan": "Basic", "email_verified": True}

def read_config(key):
    print(f"[Config API] Reading {key}: {config.get(key)}")
    return config.get(key)

def write_config(key, value):
    print(f"[Config API] Updating {key} → {value}")
    config[key] = value
    return True
