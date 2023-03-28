from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.views import APIView
from ..models import studentdetailsStudentMainModel,studentdetailsStudentModel
from .serializiers import studentdetailsClientSWithBranchSerializer,studentdetailsClientSDSerializer,studentClientCreateSSerializer,studentdetailsCreateSDWithBranchAndMarksSerializer,getStudentMarksSerializer,postStudentMarksSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_206_PARTIAL_CONTENT,HTTP_200_OK
from rest_framework.pagination import LimitOffsetPagination
class studentdetailsClientSDView(ListAPIView):
    queryset=studentdetailsStudentModel.objects.all()
    serializer_class = studentdetailsClientSWithBranchSerializer
    pagination_class = LimitOffsetPagination
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset is not None:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)





class studentdetailsClientSingleSdetailsView(APIView):
    def get(self,request,id):
        try:
            m=studentdetailsStudentModel.objects.get(id=id)
        except:
            return Response("{message:Object not found}",status=HTTP_404_NOT_FOUND)
        instance=studentdetailsClientSWithBranchSerializer(m)
        return Response(instance.data,status=HTTP_200_OK)
    def put(self,request,id):
        object=studentdetailsStudentModel.objects.all().get(id=id)
        m=studentdetailsClientSWithBranchSerializer(object,data=request.data)
        if m.is_valid():
            m.save()
            return Response(m.data,status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_206_PARTIAL_CONTENT)
class studentdetailsclientcreatestudent(CreateAPIView):
    queryset=studentdetailsStudentModel.objects.all()
    serializer_class = studentdetailsClientSDSerializer



class studentdetailsClientUploadingMarksView(APIView):

    def post(self, request, id, *args, **kwargs):
        request.data['owner'] = id
        serializer = postStudentMarksSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_206_PARTIAL_CONTENT)


0


class studentdetailsClientGradesandFinalgradeView(APIView):
    def get(self,request,id):
        try:
            student = studentdetailsStudentModel.objects.get(id=id)
        except:
            return Response("message:Object not found",status=HTTP_404_NOT_FOUND)
        serializer = studentdetailsClientSDSerializer(student)
        return Response(serializer.data,status=HTTP_200_OK)
    def put(self,request,id):
        obj=studentdetailsStudentModel(id=id)
        m=getStudentMarksSerializer(obj,data=request.data)
        if m.is_valid():
            m.save()
            return m
        else:
            return Response(m.errors)

class studentdetailsCreateStudentView(APIView):
    def post(self,request):
        serializer = studentClientCreateSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "object created"},status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_206_PARTIAL_CONTENT)

class studentdetailsCreateSDWithBranchAndMarksView(APIView):
    def post(self,request):
        serialize=studentdetailsCreateSDWithBranchAndMarksSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)









