import configparser

def load_ini(file_path: str) -> dict:
    """Loads an INI file into a dictionary.

    Parses an INI file at the provided path and returns its contents as a nested dictionary.
    Each top-level key corresponds to a section in the INI file, and each sub-dictionary contains
    the options and their values for that section.

    Args:
        `file_path (str)`: Path to the INI file to be loaded.

    Returns:
        `dict`: Nested dictionary containing the parsed INI file data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        configparser.Error: If there is an issue parsing the INI file.
    """

    config = configparser.ConfigParser()
    config.read(file_path)

    config_dict = {}

    for section in config.sections():
        config_dict[section] = {}

        for option in config.options(section):
            config_dict[section][option] = config.get(section, option)

    return config_dict
