# FinishingStatusService

A list of all methods in the `FinishingStatusService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                 | Description                                                                                                                                                                                           |
| :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_of_all_finishing_status_codes](#list_of_all_finishing_status_codes)                                               | Every driver has a finishing status like 'finished', disqualified', 'accident', '+1 lap', '+2 lap', etc. This endpoint will give the list of all such statuses. Example request and response attached |
| [list_of_finishing_status_for_a_specific_season](#list_of_finishing_status_for_a_specific_season)                       | To fetch the list of finishing status of a specific season(year).                                                                                                                                     |
|  |
| [list_of_finishing_status_for_a_specific_round_in_a_season](#list_of_finishing_status_for_a_specific_round_in_a_season) | To fetch the list of finishing status of a specific race(round) in a season(year).                                                                                                                    |

## list_of_all_finishing_status_codes

Every driver has a finishing status like 'finished', disqualified', 'accident', '+1 lap', '+2 lap', etc. This endpoint will give the list of all such statuses. Example request and response attached

- HTTP Method: `GET`
- Endpoint: `/api/f1/status`

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.finishing_status.list_of_all_finishing_status_codes()

with open("output-file.ext", "w") as f:
    f.write(result)
```

## list_of_finishing_status_for_a_specific_season

To fetch the list of finishing status of a specific season(year).

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/status`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| year | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.finishing_status.list_of_finishing_status_for_a_specific_season(year="year")

print(result)
```

## list_of_finishing_status_for_a_specific_round_in_a_season

To fetch the list of finishing status of a specific race(round) in a season(year).

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/{round}/status`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| year  | str  | ✅       |             |
| round | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.finishing_status.list_of_finishing_status_for_a_specific_round_in_a_season(
    year="year",
    round="round"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
