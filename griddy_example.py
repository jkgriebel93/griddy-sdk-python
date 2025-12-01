import json
import sys
from datetime import date
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.settings import NFL

_, *args = sys.argv

#
# # Lamar Jackson = 46101
if len(args) == 1:
    with open(args[0], "r") as infile:
        custom_auth_info = json.load(infile)
    nfl = GriddyNFL(nfl_auth=custom_auth_info)
else:
    nfl = GriddyNFL(
        login_email=NFL["login_email"], login_password=NFL["login_password"]
    )

result = nfl.ngs.league.get_teams()

pprint(result, indent=4)

# result = nfl.ngs
# dumpable = [w.model_dump() for w in result]
# with open("wgd.json", "w") as outfile:
#     json.dump(dumpable, outfile, indent=4)
