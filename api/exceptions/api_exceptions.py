from rest_framework import status
from rest_framework.exceptions import APIException

class MissingParameterError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Required parameter is missing'
    default_code = 'missing_parameter' 