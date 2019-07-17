from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.family_datastructure import Family
import json

# initialize a 'Doe' family
family = Family(last_name='Doe')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class MembersView(APIView):
    def get(self, request, member_id=None):
        # fill this method and update the return
        if member_id is not None:
            zorro=family.get_member(member_id)
            Response(zorro, status=status.HTTP_200_OK)
        else:
            zorro=family.get_all_members()
        return Response(zorro, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        alce=family.add_member(request)
        result = None
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, member_id=None):
        if member_id is not None:
            mapache=family.update_member(member_id, request.data)
            Response(mapache, status=status.HTTP_200_OK)
        else:
            mapache=family.get_all_members()
        return Response(mapache, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, member_id=None):
        if member_id is not None:
            lobo=family.delete_member(member_id)
            Response(lobo, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
        return Response({ "status": "ok" }, status=status.HTTP_200_OK)