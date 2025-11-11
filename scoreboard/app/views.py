from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET", "POST", "PUT", "DELETE"])
def getData(req):
    person = {"name": "test"}
    return Response(person)
