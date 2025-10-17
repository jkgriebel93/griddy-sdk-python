# NFLCoverageMetrics

Explanation of coverage-specific metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_rate_over_expected** | [**NFLNFLCoverageMetricsCompletionRateOverExpected**](NFLCoverageMetricsCompletionRateOverExpected.md) |  | [optional] 
**coverage_snaps** | [**NFLNFLCoverageMetricsCoverageSnaps**](NFLCoverageMetricsCoverageSnaps.md) |  | [optional] 
**receiver_separation** | [**NFLNFLCoverageMetricsReceiverSeparation**](NFLCoverageMetricsReceiverSeparation.md) |  | [optional] 
**targets_allowed** | [**NFLNFLCoverageMetricsTargetsAllowed**](NFLCoverageMetricsTargetsAllowed.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_coverage_metrics import NFLCoverageMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCoverageMetrics from a JSON string
nfl_coverage_metrics_instance = NFLCoverageMetrics.from_json(json)
# print the JSON string representation of the object
print(NFLCoverageMetrics.to_json())

# convert the object into a dict
nfl_coverage_metrics_dict = nfl_coverage_metrics_instance.to_dict()
# create an instance of NFLCoverageMetrics from a dict
nfl_coverage_metrics_from_dict = NFLCoverageMetrics.from_dict(nfl_coverage_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


