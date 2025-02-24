import yaml

def load_config():
    try:
        with open("config/config.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception("Configuration file not found. Please check 'config/config.yaml'.")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")