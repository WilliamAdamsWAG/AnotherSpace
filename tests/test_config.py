from src.AnotherSpace.Config import load_ini

def test_load_ini():
    config = load_ini("tests/test_cases/test.ini")

    assert config["general"]["version"] == "0.0.1"
    assert config["general"]["lang"] == "python"

    assert config["owner"]["name"] == "William"
    assert config["owner"]["email"] == "williamadams.aurora@gmail.com"