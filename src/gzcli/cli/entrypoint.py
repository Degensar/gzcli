from gzcli.cli.gz import gz
from gzcli.cli.groups.account import account
from gzcli.cli.groups.challenge import challenge
from gzcli.cli.groups.game import game
from gzcli.cli.groups.team import team
from gzcli.cli.config import CLI_PATH

if not CLI_PATH.exists():
    CLI_PATH.mkdir(parents=True, exist_ok=True)

gz.add_command(account)
gz.add_command(challenge)
gz.add_command(game)
gz.add_command(team)
