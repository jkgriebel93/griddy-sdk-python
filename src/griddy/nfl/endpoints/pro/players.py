import requests

headers = {   'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, zstd',
    'authorization': 'Bearer '
                     'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImNsaWVudEtleSI6IjRjRlVXNkRtd0pwelQ5TDdMckczcVJBY0FCRzVzMDRnIiwiZGV2aWNlSWQiOiJmZjRkMzg2NC04NWU3LTRlNjMtOTBjZS05ZGM5ZmZlOGI2YzUiLCJpc3MiOiJORkwiLCJwbGFucyI6W3sicGxhbiI6ImZyZWUiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjYtMTAtMzAiLCJzb3VyY2UiOiJORkwiLCJzdGFydERhdGUiOiIyMDI1LTEwLTMwIiwic3RhdHVzIjoiQUNUSVZFIiwidHJpYWwiOmZhbHNlfV0sIkRpc3BsYXlOYW1lIjoiV0VCX0RFU0tUT1BfREVTS1RPUCIsIk5vdGVzIjoiIiwiZm9ybUZhY3RvciI6IkRFU0tUT1AiLCJsdXJhQXBwS2V5IjoiU1pzNTdkQkdSeGJMNzI4bFZwN0RZUSIsInBsYXRmb3JtIjoiREVTS1RPUCIsInByb2R1Y3ROYW1lIjoiV0VCIiwicm9sZXMiOlsiY29udGVudCIsImV4cGVyaWVuY2UiLCJmb290YmFsbCIsInV0aWxpdGllcyIsInRlYW1zIiwicGxheSIsImxpdmUiLCJpZGVudGl0eSIsIm5nc19zdGF0cyIsInBheW1lbnRzX2FwaSIsIm5nc190cmFja2luZyIsIm5nc19wbGF0Zm9ybSIsIm5nc19jb250ZW50IiwibmdzX2NvbWJpbmUiLCJuZ3NfYWR2YW5jZWRfc3RhdHMiLCJuZmxfcHJvIiwiZWNvbW0iLCJuZmxfaWRfYXBpIiwidXRpbGl0aWVzX2xvY2F0aW9uIiwiaWRlbnRpdHlfb2lkYyIsIm5nc19zc2UiLCJhY2NvdW50cyIsImNvbnNlbnRzIiwic3ViX3BhcnRuZXJzaGlwcyIsImNvbmN1cnJlbmN5Iiwia2V5c3RvcmUiLCJmcmVlIl0sIm5ldHdvcmtUeXBlIjoib3RoZXIiLCJjaXR5IjoiYXRsYW50YSIsImNvdW50cnlDb2RlIjoiVVMiLCJkbWFDb2RlIjoiNTI0IiwiaG1hVGVhbXMiOlsiMTA0MDAyMDAtZjQwMS00ZTUzLTUxNzUtMDk3NGU0ZjE2Y2Y3Il0sInJlZ2lvbiI6IkdBIiwiemlwQ29kZSI6IjMwMzQ5IiwiYnJvd3NlciI6Ik90aGVyIiwiY2VsbHVsYXIiOmZhbHNlLCJlbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJleHAiOjE3NjE4MjIxNjB9.HSWefFleY31XAUbIs5uA6mxVkZPR7oCfTPTu78YRqK0',
    'connection': 'keep-alive',
    'host': 'pro.nfl.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 '
                  'Safari/537.36'}


def get_player(player_id: int):
    url = f"https://pro.nfl.com/api/players/player?nflId={player_id}"
    return requests.get(url=url, headers=headers)
