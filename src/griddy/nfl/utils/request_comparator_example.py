import os
import requests
from datetime import datetime
import sys
from griddy.nfl import GriddyNFL
from griddy.nfl.errors.griddynfldefaulterror import GriddyNFLDefaultError
from griddy.core.utils import parse_cookies_txt
from request_comparator import (
    RequestComparator,
    compare_requests,
    print_direct_request_details,
)

# Enable SDK debug logging
# os.environ['GRIDDY_NFL_DEBUG'] = '1'

# Optional: Set output file (None = stdout only, or provide a filename)
OUTPUT_FILE = "request_comparison.log"  # Set to None to disable file output

_, bearer_token = sys.argv

nfl = GriddyNFL(nfl_auth=f"Bearer {bearer_token}")

# response = nfl.football.get_weekly_game_details(
#     season=2025,
#     type_="REG",
#     week=5,
#     include_drive_chart=True,
#     include_replays=True,
#     include_standings=True,
#     include_tagged_videos=False,
# )
# game = response[0]
# replay = game.replays[0]
from pprint import pprint

# pprint(replay.model_dump(), indent=4)
pro_server_url = "https://pro.nfl.com"

additional_headers = {
    # ":method": "GET",
    "authority": "pro.nfl.com",
    # ":scheme": "https",
    "path": "/api/secured/stats/players-offense/passing/season?limit=1&sortKey=cpoe&sortValue=DESC&qualifiedPasser=true&season=2024&seasonType=REG",
    "sec-ch-ua-platform": '"Windows"',
    "cache-control": "max-age=60",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://pro.nfl.com/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i",
    # "cookie": "AMCVS_F75C3025512D2C1D0A490D44%40AdobeOrg=1; OTGPPConsent=DBABLA~BVQqAAAAAAKA.QA; nflcs.prod.crossDomainStorageCleared=true; gig_bootstrap_4_9iJVkTyrOzMJlUu66ZBRKg=auth-id_ver4; OptanonAlertBoxClosed=2025-10-16T10:54:35.698Z; kndctr_F75C3025512D2C1D0A490D44_AdobeOrg_identity=CiY5MDU2ODQxMTEzNDcyOTA4MTg3Mzc4OTgzMTAzNzIwMzAzMDUzM1IQCKSfoeWeMxgBKgNWQTYwA_ABpJ-h5Z4z; kndctr_F75C3025512D2C1D0A490D44_AdobeOrg_cluster=va6; s_ecid=MCMID%7C90568411134729081873789831037203030533; AMCV_F75C3025512D2C1D0A490D44%40AdobeOrg=179643557%7CMCIDTS%7C20378%7CMCMID%7C90568411134729081873789831037203030533%7CMCAAMLH-1761216873%7C7%7CMCAAMB-1761216873%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1760619313s%7CNONE%7CMCSYNCSOP%7C411-20385%7CvVersion%7C5.5.0%7CMCAID%7CNONE; gig_bootstrap_3_3g_DApOD0TCeN6ZJpzQMr7H1cIbtqtHwDjKVESN3N5oohMleIozT0I9WecPZeytT=auth-id_ver4; _scor_uid=44cea8c374d94ad7ad9065c2c2c12be3; _gcl_au=1.1.275167758.1760612124; _gid=GA1.2.556601655.1760612125; _gat_gtag_UA_142289554_3=1; nfl_web_sdk_plugin_storage={%22s_ppv%22:{%22noScrollClick%22:1%2C%22scrollDelta%22:0%2C%22footerSeen%22:false%2C%22lastRecPage%22:%22nfl%20pro:account:account:splash%20loading%22%2C%22percentPageViewed%22:100%2C%22initialPageViewed%22:100%2C%22maxPageViewed%22:739}}; _ga_M6JHFFXV8K=GS2.1.s1760612124$o1$g1$t1760612150$j34$l0$h0; _ga=GA1.1.1409002658.1760612125; glt_3_3g_DApOD0TCeN6ZJpzQMr7H1cIbtqtHwDjKVESN3N5oohMleIozT0I9WecPZeytT=st2.s.AtLtW82k3g.doTZHEGQY1_r__aN7us8HbhAl5_Wxqp5zgnLOurSMy2B_AWMaD1VruqZYylq7ETwAm9SD0_Okxogzg4myleMF4zkDf1RooSqnSl0ogHd_iItW5yHW2iLWQDkNIj8-ZBV.M50Oervnx0lb5JBqHtjviPqg8-svkDUgD-LpatZeqerwi9vBMQLKRaH6WOWuY1c8-LWuOSQPo1k3aU8e5oC1Ow.sc3; nflcs.prod.keyStoreDomainSyncList=id.nfl.com; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Oct+16+2025+06%3A56%3A02+GMT-0400+(Eastern+Daylight+Time)&version=202506.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=18bd35c1-0b1d-41a2-bf72-25bf856404be&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&GPPCookiesCount=1&gppSid=7&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CBG64%3A1&intType=1&geolocation=US%3BGA&AwaitingReconsent=false; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Afalse%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; glt_4_9iJVkTyrOzMJlUu66ZBRKg=st2.s.AtLtW82k3g.doTZHEGQY1_r__aN7us8HbhAl5_Wxqp5zgnLOurSMy2B_AWMaD1VruqZYylq7ETwAm9SD0_Okxogzg4myleMF4zkDf1RooSqnSl0ogHd_iItW5yHW2iLWQDkNIj8-ZBV.M50Oervnx0lb5JBqHtjviPqg8-svkDUgD-LpatZeqerwi9vBMQLKRaH6WOWuY1c8-LWuOSQPo1k3aU8e5oC1Ow.sc3; nflcs.prod.nfl.user=eyJkYXRhIjp7Im93bklkIjp7ImNvbm5lY3Rpb25zIjpbeyJmaWRvMkNyZWRlbnRpYWxJZCI6IkpJQzk2dmozRmI0Tk1TNjJGV0RQOFlpSmNDUSIsImlkIjoiSklDOTZ2ajNGYjROTVM2MkZXRFA4WWlKY0NRIiwiZmlkbzJTaWduYXR1cmVDb3VudGVyIjoiMCIsInNvdXJjZSI6InJlZ2lzdGVyIiwiYWRkaXRpb25hbERhdGEiOiJ7XCJmaWRvMlJwSURcIjpcIm5mbC5jb21cIixcIm9zXCI6XCJpb3NcIixcIm9zVmVyc2lvblwiOlwiMTguM1wiLFwiYnJvd3NlclwiOlwic2FmYXJpXCIsXCJjcmVhdGlvblNvdXJjZVwiOlwiYnJvd3NlclwiLFwiY3JlYXRlZFRpbWVzdGFtcFwiOlwiMjAyNS0wMi0xOFQyMjo0MDoyMi4yNDg0MTE1WlwiLFwiaXNTaGFyYWJsZVwiOnRydWV9IiwiYXV0aFR5cGUiOiJmaWRvMiIsInB1YktleSI6InBRRUNBeVlnQVNGWUlOeEg4c3J3RmpCV2pyeXNTTzVjRG1ucDV6ek80V2hfR2ZBUFMtUXVjajJvSWxnZ1gtUXh6ZThFZzdVWWxUUm1nOGdlM3N1NFRUY1Z2SF9ac2FvWnBONUUwWjgifSx7ImZpZG8yQ3JlZGVudGlhbElkIjoidWlJclJDemh1X0ZObHJmSHVaV1ZvSVI5VVZhc2VZYW9RaThWUzctMmVqMCIsImlkIjoidWlJclJDemh1X0ZObHJmSHVaV1ZvSVI5VVZhc2VZYW9RaThWUzctMmVqMCIsImZpZG8yU2lnbmF0dXJlQ291bnRlciI6IjIiLCJzb3VyY2UiOiJyZWdpc3RlciIsImFkZGl0aW9uYWxEYXRhIjoie1wiZmlkbzJScElEXCI6XCJuZmwuY29tXCIsXCJvc1wiOlwid2luZG93cyBudFwiLFwib3NWZXJzaW9uXCI6XCIxMC4wXCIsXCJicm93c2VyXCI6XCJmaXJlZm94XCIsXCJjcmVhdGlvblNvdXJjZVwiOlwiYnJvd3NlclwiLFwiY3JlYXRlZFRpbWVzdGFtcFwiOlwiMjAyNS0wNC0yMlQxOToyMToxOC44MTIzNDEyWlwiLFwiaXNTaGFyYWJsZVwiOmZhbHNlfSIsImF1dGhUeXBlIjoiZmlkbzIiLCJwdWJLZXkiOiJwUUVDQXlZZ0FTRllJTGQ4MERFYzlHWU5ReTRMVm5DSFZEVUx2dHpMZ2FUZ1UzTWlOS08zTGlQMUlsZ2duWk1VWFlXUHhQeUNVbHJkV295LTVjU1d2NUlwRDFTcFhPdGFaRHJ5VHZFIn0seyJmaWRvMkNyZWRlbnRpYWxJZCI6ImJjOEV5MVdTYXo4OWlJcjlpLW1HajN4WnJsUU1MUTM4X0lkcEktTGVQMTQiLCJpZCI6ImJjOEV5MVdTYXo4OWlJcjlpLW1HajN4WnJsUU1MUTM4X0lkcEktTGVQMTQiLCJmaWRvMlNpZ25hdHVyZUNvdW50ZXIiOiIzIiwic291cmNlIjoicmVnaXN0ZXIiLCJhZGRpdGlvbmFsRGF0YSI6IntcImZpZG8yUnBJRFwiOlwibmZsLmNvbVwiLFwib3NcIjpcIndpbmRvd3MgbnRcIixcIm9zVmVyc2lvblwiOlwiMTAuMFwiLFwiYnJvd3NlclwiOlwiY2hyb21lXCIsXCJjcmVhdGlvblNvdXJjZVwiOlwiYnJvd3NlclwiLFwiY3JlYXRlZFRpbWVzdGFtcFwiOlwiMjAyNS0wNi0wMlQxMDoxOToyMy40MTA5MDg0WlwiLFwiaXNTaGFyYWJsZVwiOmZhbHNlfSIsImF1dGhUeXBlIjoiZmlkbzIiLCJwdWJLZXkiOiJwUUVDQXlZZ0FTRllJUGpic0Y0b2dHdk5JbUx6NHdISndDdnF2UVBfclE4ZTFSWHMyNFhKbEJ0a0lsZ2dHLUJaOG8yQTJ3dEVTX1dXMDZsS2EyT2JEWmNSdnJROGgwbkpidWV3ejl3In1dfSwibGVhZ3VlIjp7ImZhdm9yaXRlVGVhbXMiOlsiMTA0MDM5MDAtODI1MS02ODkyLWQ4MWMtNDM0ODUyNWMyZDQ3Il19LCJzaGE1MTJIYXNoZWRMb3dlcmVkRW1haWwiOiI3NjM0ZTQ4ZmM3YzVjYzEzY2Y5NDkxYzU2MmI0ZDI5MzRhMzg5NDcyYWVmNDg3OWQ3ODRiYjE0MjlhODk5NWY1YjhkYTJiM2IxZjNmYzc4MTIyYTAzNjQ4YzgxOWY0ZDNhZjk1ZjFiNDU4YWVkZmFjM2E5ZDU1YWI0NWZmZjg0MCIsImxvd2VyZWRfZW1haWxfaGFzaCI6IjkwZTQ0NzIwMjhjNjcyYWZiZmQzN2VkNDYzNzcyMGI4NjM0ZDg5MzZmNmY1MTMxZGM2YzFmZDkxMTdjYmE5NzYifSwiZXhwIjoxNzYwNjEyMjI0MDE0LCJmaXJzdE5hbWUiOiJKb2huIiwiZ2lneWFVSUQiOiJkZjk5MGFjZDk1MWU0YmQ2OTQwYzNiYWJjNDM0MTU4NCIsImdpZ3lhVUlEU2lnbmF0dXJlIjoiRmt4YU5VNFRMSWlreTFLVU44aWhJSnpxdVM4PSIsImhhc2hlZEVtYWlsIjoiOTBlNDQ3MjAyOGM2NzJhZmJmZDM3ZWQ0NjM3NzIwYjg2MzRkODkzNmY2ZjUxMzFkYzZjMWZkOTExN2NiYTk3NiIsImxhc3ROYW1lIjoiR3JpZWJlbCJ9"
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImNsaWVudEtleSI6IjRjRlVXNkRtd0pwelQ5TDdMckczcVJBY0FCRzVzMDRnIiwiZGV2aWNlSWQiOiJjNDY2NTgxMC02M2JiLTQwODQtODQxOC01ZGYzMmM2OTYyMDYiLCJpc3MiOiJORkwiLCJwbGFucyI6W3sicGxhbiI6ImZyZWUiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjYtMTAtMTYiLCJzb3VyY2UiOiJORkwiLCJzdGFydERhdGUiOiIyMDI1LTEwLTE2Iiwic3RhdHVzIjoiQUNUSVZFIiwidHJpYWwiOmZhbHNlfSx7InBsYW4iOiJORkxfUExVU19QUkVNSVVNIiwiYmlsbGluZ1R5cGUiOiJtb250aGx5IiwiZXhwaXJhdGlvbkRhdGUiOiIyMDI1LTEwLTI4IiwiZXh0ZXJuYWxTdWJzY3JpcHRpb25JZCI6Ind6cmw0ZDBpd2wxbiIsInNvdXJjZSI6IldFQiIsInN0YXJ0RGF0ZSI6IjIwMjUtMDktMjgiLCJzdGF0dXMiOiJBQ1RJVkUiLCJ0cmlhbCI6ZmFsc2V9XSwiRGlzcGxheU5hbWUiOiJXRUJfREVTS1RPUF9ERVNLVE9QIiwiTm90ZXMiOiIiLCJmb3JtRmFjdG9yIjoiREVTS1RPUCIsImx1cmFBcHBLZXkiOiJTWnM1N2RCR1J4Ykw3MjhsVnA3RFlRIiwicGxhdGZvcm0iOiJERVNLVE9QIiwicHJvZHVjdE5hbWUiOiJXRUIiLCJyb2xlcyI6WyJjb250ZW50IiwiZXhwZXJpZW5jZSIsImZvb3RiYWxsIiwidXRpbGl0aWVzIiwidGVhbXMiLCJwbGF5IiwibGl2ZSIsImlkZW50aXR5IiwibmdzX3N0YXRzIiwicGF5bWVudHNfYXBpIiwibmdzX3RyYWNraW5nIiwibmdzX3BsYXRmb3JtIiwibmdzX2NvbnRlbnQiLCJuZ3NfY29tYmluZSIsIm5nc19hZHZhbmNlZF9zdGF0cyIsIm5mbF9wcm8iLCJlY29tbSIsIm5mbF9pZF9hcGkiLCJ1dGlsaXRpZXNfbG9jYXRpb24iLCJpZGVudGl0eV9vaWRjIiwibmdzX3NzZSIsImFjY291bnRzIiwiY29uc2VudHMiLCJzdWJfcGFydG5lcnNoaXBzIiwiY29uY3VycmVuY3kiLCJrZXlzdG9yZSIsImZyZWUiLCJORkxfUExVU19QUkVNSVVNIl0sImNpdHkiOiJhdGxhbnRhIiwiY291bnRyeUNvZGUiOiJVUyIsImRtYUNvZGUiOiI1MjQiLCJobWFUZWFtcyI6WyIxMDQwMDIwMC1mNDAxLTRlNTMtNTE3NS0wOTc0ZTRmMTZjZjciXSwicmVnaW9uIjoiR0EiLCJ6aXBDb2RlIjoiMzAzNDkiLCJicm93c2VyIjoiQ2hyb21lIiwiY2VsbHVsYXIiOmZhbHNlLCJlbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJ1aWQiOiJkZjk5MGFjZDk1MWU0YmQ2OTQwYzNiYWJjNDM0MTU4NCIsImV4cCI6MTc2MDYyMDU4M30.BOd_Ld7uq0RMwS7eGgZCdRWlic6TtSy6oUKKWd7CCyA",
}

cookies_list = parse_cookies_txt("cookies.txt")
cookies_dict = {}
for c in cookies_list:
    cookies_dict.update(**c.to_dict())


full_url = "https://pro.nfl.com/api/secured/stats/players-offense/passing/season?limit=1&sortKey=cpoe&sortValue=DESC&qualifiedPasser=true&season=2024&seasonType=REG"

# Open output file if specified
output_file = None
if OUTPUT_FILE:
    output_file = open(OUTPUT_FILE, "w", encoding="utf-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Logging to file: {OUTPUT_FILE}", file=output_file)
    print(f"Timestamp: {timestamp}\n", file=output_file)
    print(f"\n{'='*80}")
    print(f"Request comparison will be saved to: {OUTPUT_FILE}")
    print(f"{'='*80}\n")

# Initialize the request comparator with the output file
comparator = RequestComparator(output_file=output_file)

try:
    # Prepare direct request info for comparison
    direct_request_info = {
        "url": full_url,
        "method": "GET",
        "headers": additional_headers,
    }

    # Display direct request details (to console, and automatically to file if set)
    print_direct_request_details(direct_request_info, file=output_file)

    # Make direct request with requests library
    response = requests.get(full_url, headers=additional_headers, cookies=cookies_dict)

    status_msg = f"Status Code: {response.status_code}"
    print(status_msg)
    if output_file:
        print("DINGO", file=output_file)
        print(status_msg, file=output_file)
        print("ELEPHANT", file=output_file)

    if response.status_code == 200:
        print("FOX", file=output_file)
        import json

        response_preview = json.dumps(response.json(), indent=2)[:500]
        print(f"Response preview: {response_preview}...\n")
        if output_file:
            print(f"Response preview: {response_preview}...\n", file=output_file)
    else:
        print("GIRAFFE", file=output_file)
        error_msg = f"Error: {response.text[:200]}"
        print(error_msg)
        if output_file:
            print(error_msg, file=output_file)

    # Start capturing SDK requests (will auto-log to file if output_file was set)
    comparator.start_capture()

    try:
        sdk_response = nfl.player_statistics.get_player_passing_stats_by_season(
            season=2025,
            season_type="REG",
            server_url=pro_server_url,
            http_headers=additional_headers,
        )
        success_msg = f"SDK Response received: {type(sdk_response)}"
        print(success_msg, file=output_file)
    except GriddyNFLDefaultError as e:
        print(f"Error: {e}")
    finally:
        comparator.stop_capture()

    # Compare the requests (to console)
    if comparator.get_last_request():
        print("ARMADILLO", file=output_file)
        compare_requests(
            direct_request_info, comparator.get_last_request(), file=output_file
        )
    else:
        print("BADGER", file=output_file)
        warning_msg = "\nWarning: No SDK request was captured!"
        print(warning_msg, file=output_file)

finally:
    if output_file:
        print(f"\n{'='*80}")
        print(f"Comparison saved to: {OUTPUT_FILE}")
        print(f"{'='*80}\n")
        output_file.close()
