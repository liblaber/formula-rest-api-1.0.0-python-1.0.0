# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class PitStopsService(BaseService):

    @cast_models
    def pit_stop_data_for_a_race(self, year: str, round: str) -> str:
        """This endpoint requires the season(year) and race(round) to be specified.

        :param year: year
        :type year: str
        :param round: round
        :type round: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Pit stop data for a race- Example- 2019- Race 1
        :rtype: str
        """

        Validator(str).validate(year)
        Validator(str).validate(round)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/f1/{{year}}/{{round}}/pitstops",
                self.get_default_headers(),
            )
            .add_path("year", year)
            .add_path("round", round)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def information_for_a_specific_pit_stop(
        self, year: str, round: str, pitstopnumber: str
    ) -> str:
        """This endpoint requires the season(year), race(round) and pit stop number(pitstopnumber) to be specified.

        :param year: year
        :type year: str
        :param round: round
        :type round: str
        :param pitstopnumber: pitstopnumber
        :type pitstopnumber: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Information for a specific pit stop- Example- 2019- Race 1- PitStop 2
        :rtype: str
        """

        Validator(str).validate(year)
        Validator(str).validate(round)
        Validator(str).validate(pitstopnumber)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/f1/{{year}}/{{round}}/pitstops/{{pitstopnumber}}",
                self.get_default_headers(),
            )
            .add_path("year", year)
            .add_path("round", round)
            .add_path("pitstopnumber", pitstopnumber)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response
