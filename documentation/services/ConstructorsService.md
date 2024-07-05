# ConstructorsService

A list of all methods in the `ConstructorsService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                            |
| :---------------------------------------------------- | :----------------------------------------------------- |
| [list_of_all_constructors](#list_of_all_constructors) | This endpoint is to obtain a list of all constructors. |

Constructor lists can be refined by adding one or more of the following criteria:

/circuits/<circuitId>
/constructors/<constructorId>
/drivers/<driverId>
/grid/<position>
/results/<position>
/fastest/<rank>
/status/<statusId>

For example, to list all constructors a specific driver has driven for at a particular circuit:

http://ergast.com/api/f1/drivers/alonso/circuits/monza/constructors

Alternatively, to list all the constructors who have achieved a particular final position in the championship:

http://ergast.com/api/f1/constructorStandings/1/constructors |
|[list_of_all_constructors_within_a_year](#list_of_all_constructors_within_a_year)| This endpoint is to obtain a list of all constructors in a particular season (year) |
|[list_of_all_constructors_within_a_race_in_a_year](#list_of_all_constructors_within_a_race_in_a_year)| This endpoint is to obtain a list of all constructors in a particular race(round) of a season(year) |
|[constructor_information](#constructor_information)| Each constructor listed in the response is identified by a unique constructorId which is used to identify the constructor throughout the API. To obtain information about a particular constructor append the constructorId (name of the constructor)

This endpoint is to obtain the information of a particular constructor based on the constructorId (constructor name) |

## list_of_all_constructors

This endpoint is to obtain a list of all constructors.

Constructor lists can be refined by adding one or more of the following criteria:

/circuits/<circuitId>
/constructors/<constructorId>
/drivers/<driverId>
/grid/<position>
/results/<position>
/fastest/<rank>
/status/<statusId>

For example, to list all constructors a specific driver has driven for at a particular circuit:

http://ergast.com/api/f1/drivers/alonso/circuits/monza/constructors

Alternatively, to list all the constructors who have achieved a particular final position in the championship:

http://ergast.com/api/f1/constructorStandings/1/constructors

- HTTP Method: `GET`
- Endpoint: `/api/f1/constructors`

**Example Usage Code Snippet**

```python
from formula_one import FormulaOne, Environment

sdk = FormulaOne(
    base_url=Environment.DEFAULT.value
)

result = sdk.constructors.list_of_all_constructors()

print(result)
```

## list_of_all_constructors_within_a_year

This endpoint is to obtain a list of all constructors in a particular season (year)

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/constructors`

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

result = sdk.constructors.list_of_all_constructors_within_a_year(year="year")

print(result)
```

## list_of_all_constructors_within_a_race_in_a_year

This endpoint is to obtain a list of all constructors in a particular race(round) of a season(year)

- HTTP Method: `GET`
- Endpoint: `/api/f1/{year}/{round}/constructors`

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

result = sdk.constructors.list_of_all_constructors_within_a_race_in_a_year(
    year="year",
    round="round"
)

print(result)
```

## constructor_information

Each constructor listed in the response is identified by a unique constructorId which is used to identify the constructor throughout the API. To obtain information about a particular constructor append the constructorId (name of the constructor)

This endpoint is to obtain the information of a particular constructor based on the constructorId (constructor name)

- HTTP Method: `GET`
- Endpoint: `/api/f1/constructors/{constructorid}`

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

result = sdk.constructors.constructor_information(constructorid="constructorid")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
