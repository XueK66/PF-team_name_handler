import re

from typing import Optional

from mcdreforged.api.utils.serializer import Serializable
from mcdreforged.handler.impl import VanillaHandler

class Config(Serializable):
    skip_name_check: bool = False
    regular_expression: str = r'<(?:\[[^\[\]]+\])?(?P<name>[^>\[\]]+)> (?P<message>.*)'

class TeamNameHandler(VanillaHandler):
    def __init__(self, skip_name_check:bool = False, regular_expression: Optional[str] = None):

        if regular_expression is None:
            regular_expression = r'<(?:\[[^\[\]]+\])?(?P<name>[^>\[\]]+)> (?P<message>.*)'

        self.regular_expression = regular_expression
        self._skip_name_check = skip_name_check

        super().__init__()

    def get_name(self) -> str:
        return 'team_name_handler'

    def parse_server_stdout(self, text: str):
        info = super().parse_server_stdout(text)
        if info.player is None:
            m = re.fullmatch(self.regular_expression, info.content)
            if m is not None and (self._skip_name_check or self._verify_player_name(m['name'])):
                info.player, info.content = m['name'], m['message']
        return info


def on_load(server, prev_module):

    config = server.load_config_simple(
        "config.json",
        target_class=Config
    )

    server.register_server_handler(TeamNameHandler(**config.serialize()))