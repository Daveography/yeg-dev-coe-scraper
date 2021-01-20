import ast
import os

import yaml


class ConfigService:
    """
    Attempts to obtain arbitrary config values first from EnvVars,
    and if not found then attempts to obtain from config.yaml.
    (Basically yaml values can be overridden via EnvVars values)

    Values that exist in neither location return None.

    Expects EnvVars values to be UPPERCASE, yaml values lowercase.
    """

    def __init__(self) -> None:
        """
        Parse YAML file
        """
        with open("./scraper/services/config/config.yaml", "r") as config:
            self.config = yaml.load(config, Loader=yaml.FullLoader)

    def __getattr__(self, attr: str):
        try_env_var = self.__try_get_env_var_value(attr)
        if try_env_var is not None and try_env_var != "":
            return try_env_var

        return self.__try_get_config_value(attr)

    def __try_get_env_var_value(self, attr: str) -> str:
        env_var = os.getenv(attr.upper())

        if env_var is not None:
            if env_var.startswith("["):
                # Format the list
                return ast.literal_eval(env_var)

        return env_var

    def __try_get_config_value(self, attr: str) -> str:
        try:
            return self.config[attr.lower()]
        except KeyError:
            return None
