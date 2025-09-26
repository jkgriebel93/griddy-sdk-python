import sys

from pathlib import Path

from core.utils import YAMLConsolidator

_, *args = sys.argv

spec_dir = "/mnt/e/GriddyOpenAPISpecs"
pattern = "pro-nfl*"
output_dir = f"{spec_dir}/SortedSpecs"
suffix = "-sorted"

print(f"Spec Dir: {spec_dir}")
print(f"Pattern: {pattern}")
print(f"Output Dir: {output_dir}")
print(f"Suffix: {suffix}")

yc = YAMLConsolidator(spec_dir=spec_dir,
                      pattern=pattern)
yc.combine_all_specs()
yc.output_diff()
from pprint import pprint
pprint(yc.diff_counts, indent=4)