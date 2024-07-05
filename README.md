# FormulaOne Python SDK 1.0.0

Welcome to the FormulaOne SDK documentation. This guide will help you get started with integrating and using the FormulaOne SDK in your project.

## Versions

- API version: `1.0.0`
- SDK version: `1.0.0`

## About the API

This is the Postman collection with documentation for the Formula One API hosted at [Ergast API](https://ergast.com/mrd/). **Overview** All API queries require a GET request using a URL of the form: http[s]://ergast.com/api/<series>/<season>/<round>/... This web service which provides a historical record of Formula one motor racing data for non-commercial purposes. Please read the terms and conditions of use. The API provides data for the Formula One series, from the beginning of the world championships in 1950. Non-programmers can query the database using the [manual interface](http://ergast.com/mrd/query/) or [download the database tables in CSV format](https://ergast.com/mrd/db/#csv) for import into spreadsheets or analysis software. If you have any comments or suggestions please post them on the [Feedback page](https://ergast.com/mrd/feedback/). If you find any bugs or errors in the data please report them on the [Bug Reports page](https://ergast.com/mrd/bugs/). Any enhancements to the API will be reported on the [News page](https://ergast.com/mrd/news/). Example applications are shown in the [Application Gallery](https://ergast.com/mrd/gallery). **Response formats** The API supports XML, JSON and JSONP response formats. XML is returned by default or when .xml is appended to URLs. JSON is obtained by appending .json to URLs. JSONP is obtained by appending .json and a query parameter named callback which must specify a valid Javascript function name or object property function reference. For example: http://ergast.com/api/f1/drivers.json?callback=myParser XML responses conform to the Ergast Motor Racing XML Schema. **Response paging** The number of results that are returned can be controlled using a limit query parameter, up to a maximum value of 1000. Please use the smallest value that your application needs. If not specified, the default value is 30. An offset into the result set can also be specified using an offset query parameter. If not specified the default offset is zero. For example, the following URL returns the third page of driver information containing ten entries per page: http://ergast.com/api/f1/drivers?limit=10&offset=20 The total number of available results is indicated by a total attribute in the root element of the response. **_Where_**: <series> should be set to f1 <season> is a 4 digit integer <round> is a 1 or 2 digit integer For queries concerning a whole season, or final standings, the round element may be omitted. For example: http://ergast.com/api/f1/2008/... For queries concerning the whole series both the round and the season elements may be omitted. For example: http://ergast.com/api/f1/... To specify the current season the <season> field may be set to current . To specify the previous or next race within a season the <round> field may be set to last or next respectively. For example: http://ergast.com/api/f1/2005/last/... http://ergast.com/api/f1/current/next/...

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install formula-one-client
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                       |
| :------------------------------------------------------------------------- |
| [DriversService](documentation/services/DriversService.md)                 |
| [ConstructorsService](documentation/services/ConstructorsService.md)       |
| [CircuitsService](documentation/services/CircuitsService.md)               |
| [SeasonsService](documentation/services/SeasonsService.md)                 |
| [ResultsService](documentation/services/ResultsService.md)                 |
| [QualifyingService](documentation/services/QualifyingService.md)           |
| [SchedulesService](documentation/services/SchedulesService.md)             |
| [StandingsService](documentation/services/StandingsService.md)             |
| [FinishingStatusService](documentation/services/FinishingStatusService.md) |
| [LapTimesService](documentation/services/LapTimesService.md)               |
| [PitStopsService](documentation/services/PitStopsService.md)               |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
