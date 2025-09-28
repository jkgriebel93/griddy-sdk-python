import os
import sys

from pathlib import Path

from core.utils import YAMLConsolidator

_, *args = sys.argv

spec_dir = os.getcwd()
pattern = "nfl-complete-api*"
output_dir = f"{spec_dir}/SortedSpecs"
suffix = "-sorted"

print(f"Spec Dir: {spec_dir}")
print(f"Pattern: {pattern}")
print(f"Output Dir: {output_dir}")
print(f"Suffix: {suffix}")

yc = YAMLConsolidator(spec_dir=spec_dir,
                      pattern=pattern)
common_info = {
    "openapi": "3.0.3",
    "info": {
        "title": "NFL REST APIs",
        "description": """
        Regular API - NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. 
        This API provides comprehensive access to NFL data including real-time game information, team rosters, 
        seasonal statistics, and historical data. 
        The NFL Pro API is for accessing advanced statistics, film room content, player data, and fantasy information.
        This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis,
        player projections, and game insights.""",
        "version": "1.0.0",
        "contact": {
            "name": "NFL",
            "url": "htttps://www.nfl.com"
        },
    },
    "servers": [
        {
            "url": "https://api.nfl.com",
            "description": "Production Regular NFL API"
        },
        {
            "url": "https://pro.nfl.com",
            "description": "Production NFL Pro API"
        }
    ],
    "security": [
        {
            "BearerAuth": []
        }
    ]
}

yc.set_common_info(**common_info)
yc.add_spec(spec_path=Path("/mnt/e/GriddyOpenAPISpecs/reg-nfl-api-complete-working.yaml"))
yc.add_spec(spec_path=Path("/mnt/e/GriddyOpenAPISpecs/reg-nfl-identity-api.yaml"))


yc.combine_all_specs()
yc.output_diff()

yc.combined_spec = yc.get_sorted_spec(spec=yc.combined_spec)
yc.write_spec_to_disk(file_name="nfl-reg-pro-combined-api.yaml",
                      spec=yc.combined_spec)

