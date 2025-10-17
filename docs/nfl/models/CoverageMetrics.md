# CoverageMetrics

Explanation of coverage-specific metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_rate_over_expected** | [**CoverageMetricsCompletionRateOverExpected**](CoverageMetricsCompletionRateOverExpected.md) |  | [optional] 
**coverage_snaps** | [**CoverageMetricsCoverageSnaps**](CoverageMetricsCoverageSnaps.md) |  | [optional] 
**receiver_separation** | [**CoverageMetricsReceiverSeparation**](CoverageMetricsReceiverSeparation.md) |  | [optional] 
**targets_allowed** | [**CoverageMetricsTargetsAllowed**](CoverageMetricsTargetsAllowed.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.coverage_metrics import CoverageMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CoverageMetrics from a JSON string
coverage_metrics_instance = CoverageMetrics.from_json(json)
# print the JSON string representation of the object
print(CoverageMetrics.to_json())

# convert the object into a dict
coverage_metrics_dict = coverage_metrics_instance.to_dict()
# create an instance of CoverageMetrics from a dict
coverage_metrics_from_dict = CoverageMetrics.from_dict(coverage_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


