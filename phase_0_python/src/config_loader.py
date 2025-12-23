class LogisticRegression:
    def __init__(self, lr, epochs):
        self.lr = lr
        self.epochs = epochs

    def __repr__(self):
        return f"LogisticRegression(lr={self.lr}, epochs={self.epochs})"

MODEL_REGISTRY = {
    "logistic_regression": LogisticRegression,
}

import json

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

def build_from_config(config):
    data_path = config["data"]["path"]

    model_type = config["model"]["type"]          
    model_params = config["model"]["params"]      

    ModelClass = MODEL_REGISTRY[model_type]
    model = ModelClass(**model_params)

    output_path = config["output"]["model_path"]

    return data_path, model, output_path


config = load_config("/phase_0_python/notebooks/06.json")
data_path, model, output_path = build_from_config(config)

print(data_path)
print(model)
print(output_path)
