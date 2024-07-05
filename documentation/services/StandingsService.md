# StandingsService

A list of all methods in the `StandingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                           |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------- |
| [driver_standings_after_a_race](#driver_standings_after_a_race)           | To fetch the driver standings after a specific race(round) in a season(year), use this endpoint.      |
| [constructor_standings_after_a_race](#constructor_standings_after_a_race) | To list the constructor standings after a specific race (round) in a season(year), use this endpoint. |

|
|[season_end_driver_standings](#season_end_driver_standings)| Driver Standings at the end of the season(year). |
|[season_end_constructor_standing](#season_end_constructor_standing)| Constructor Standings at the end of the season(year). |
|[current_drivers_standing](#current_drivers_standing)| Current driver standings can always be obtained using this endpoint. |
|[current_constructor_s_standing](#current_constructor_s_standing)| Current constructor standings can always be obtained using this endpoint. |
|[all_winners_of_drivers_championships](#all_winners_of_drivers_championships)| To fetch all the winners information of drivers. |
|[all_winners_of_constructors_championships](#all_winners_of_constructors_championships)| To fetch all the winners information of constructors. |
|[driver_standings_by_specifying_the_driver](#driver_standings_by_specifying_the_driver)| Driver standings by giving in the driverid(name of the driver). |
|[constructor_standings_by_specifying_the_constructor](#constructor_standings_by_specifying_the_constructor)| Constructor standings by giving in the constructorid(name of the constructor). |

## driver_standings_after_a_race

To fetch the driver standings after a specific race(round) in a season(year), use this endpoint.

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/{round}/driverStandings`

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

result = sdk.standings.driver_standings_after_a_race(
    year="year",
    round="round"
)

print(result)
```

## constructor_standings_after_a_race

To list the constructor standings after a specific race (round) in a season(year), use this endpoint.

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/{round}/constructorStandings`

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

result = sdk.standings.constructor_standings_after_a_race(
    year="year",
    round="round"
)

print(result)
```

## season_end_driver_standings

Driver Standings at the end of the season(year).

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/driverStandings`

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

result = sdk.standings.season_end_driver_standings(year="year")

print(result)
```

## season_end_constructor_standing

Constructor Standings at the end of the season(year).

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/constructorStandings`

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

result = sdk.standings.season_end_constructor_standing(year="year")

print(result)
```

## current_drivers_standing

Current driver standings can always be obtained using this endpoint.

- HTTP Method: `GET`
- Endpoint: `/api/f1/current/driverStandings`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.current_drivers_standing()

print(result)
```

## current_constructor_s_standing

Current constructor standings can always be obtained using this endpoint.

- HTTP Method: `GET`
- Endpoint: `/api/f1/current/constructorStandings`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.current_constructor_s_standing()

print(result)
```

## all_winners_of_drivers_championships

To fetch all the winners information of drivers.

- HTTP Method: `GET`
- Endpoint: `/api/f1/driverStandings/1`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.all_winners_of_drivers_championships()

print(result)
```

## all_winners_of_constructors_championships

To fetch all the winners information of constructors.

- HTTP Method: `GET`
- Endpoint: `/api/f1/constructorStandings/1`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.all_winners_of_constructors_championships()

print(result)
```

## driver_standings_by_specifying_the_driver

Driver standings by giving in the driverid(name of the driver).

- HTTP Method: `GET`
- Endpoint: `/api/f1/drivers/{driverid}/driverStandings`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| driverid | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.driver_standings_by_specifying_the_driver(driverid="driverid")

print(result)
```

## constructor_standings_by_specifying_the_constructor

Constructor standings by giving in the constructorid(name of the constructor).

- HTTP Method: `GET`
- Endpoint: `/api/f1/constructors/{constructorid}/constructorStandings`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| constructorid | str  | ✅       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.constructor_standings_by_specifying_the_constructor(constructorid="constructorid")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
