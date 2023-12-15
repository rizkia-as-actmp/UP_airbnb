from vyper import v

class Config:
    pass

def loadConfig(path, type):
    v.add_config_path(path)
    v.set_config_type(type)
    v.read_in_config()

    config = v.unmarshall(Config)

    return config
