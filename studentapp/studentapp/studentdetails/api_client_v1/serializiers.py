
from ..models import studentdetailsStudentMainModel,studentdetailsStudentModel,studentdetailsStudentMainMarksModel
from rest_framework import serializers

# <editor-fold desc="studentdetailsClientStudentDetailsSerializer">
class studentdetailsClientStudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentdetailsStudentModel
        fields="__all__"
# </editor-fold>

# <editor-fold desc="studentdetailsClientSWithBranchSerializer">
class studentdetailsClientSWithBranchSerializer(serializers.ModelSerializer):
    branch=serializers.SerializerMethodField(read_only=True)

    def get_branch(self,obj):
        try:
            instance = studentdetailsStudentMainModel.objects.get(Owner=obj)
        except Exception as e:
            return {"message":"field notfound"}
        return instance.Branch

    class Meta:
        model=studentdetailsStudentModel
        fields="__all__"
# </editor-fold>

# <editor-fold desc="getStudentMarksSerializer">
class getStudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentdetailsStudentMainMarksModel
        fields = "__all__"
# </editor-fold>


# <editor-fold desc="studentdetailsClientSDSerializer">
class studentdetailsClientSDSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField(read_only=True)
    finalgrade=serializers.SerializerMethodField(read_only=True)

    def get_marks(self,obj):
        try:
            marks = studentdetailsStudentMainMarksModel.objects.values("Grade","Sem").filter(owner=obj)
        except:
            return "{message: object not found}"
        return marks


    def get_finalgrade(self,obj):
        marks = studentdetailsStudentMainMarksModel.objects.values("Grade").filter(owner=obj)
        gradeslist=[]
        A=B=C=D=0
        for i in marks:
            gradeslist.append(i["Grade"])
        for i in gradeslist:
            if i=='A':
                A+=1
            elif i=='B':
                B+=1
            elif i=="C":
                C+=1
            else:
                D+=1
        MAX=max(A,B,C,D)
        if(A==MAX and A==B):
            return 'A'
        elif(A==MAX and A==C):
            return "B"
        elif(A==MAX and A==D):
            return 'C'
        elif(A==MAX):
            return 'A'
        if(B==MAX and B==C):
            return "B"
        elif(B==MAX and B==D):
            return 'C'
        if(C==MAX and C==D):
            return 'C'
        elif(A==MAX and A==B and A==C):
            return 'B'
        elif(B==MAX and B==C and B==D):
            return 'C'
        else:
            return "C"




        # # for i in marks:
        # #     s.append(i["Grade"])
        # # average=max(s,key=s.count)
        #
        # return average


    class Meta:
        model=studentdetailsStudentModel
        fields="__all__"
# </editor-fold>

# <editor-fold desc="studentClientCreateSSerializer">
class studentClientCreateSSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,required=True)
    date_of_birth = serializers.DateField(required=True)
    gender = serializers.CharField(max_length=100,required=True)
    image = serializers.ImageField()
    branch = serializers.CharField(max_length=100,required=True)

    class Meta:
        fields = "__all__"



    def create(self, validated_data):
        try:
            student = studentdetailsStudentModel.objects.create(Name=validated_data["name"],
                                                      Date_Of_Birth=validated_data["date_of_birth"],
                                                                Gender=validated_data["gender"],
                                                                Image=validated_data["image"])
        except Exception as e:
            print(e)
            raise serializers.ValidationError(f"student not created {e}")
        try:
            student_details = studentdetailsStudentMainModel.objects.create(Owner=student,Branch=validated_data["branch"])
        except:
            student.delete()
            raise serializers.ValidationError("student details not created")

        return validated_data
# </editor-fold>

# <editor-fold desc="studentdetailsCreateSDWithBranchAndMarksSerializer">
class studentdetailsCreateSDWithBranchAndMarksSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=100,required=True)
    Date_Of_Birth = serializers.DateField(required=True)
    Gender = serializers.CharField(max_length=20,required=True)
    Image = serializers.ImageField()
    Branch=serializers.CharField(max_length=100,required=True)
    Grade = serializers.CharField(max_length=10,required=True)
    Sem=serializers.CharField(max_length=100,required=True)
    def create(self,validated_data):
        try:
            student = studentdetailsStudentModel.objects.create(Name=validated_data["Name"],
                                                                Date_Of_Birth=validated_data["Date_Of_Birth"],
                                                                Gender=validated_data["Gender"],
                                                                Image=validated_data["Image"])
        except Exception as e:
            raise serializers.ValidationError(f"student not created at:- normalstudent {e}")
        try:
            object=studentdetailsStudentMainMarksModel.objects.create(owner=student,Grade=validated_data["Grade"],Sem=validated_data["Sem"])
        except Exception as e:
            raise serializers.ValidationError(f"student not created:- at marks {e}")
            student.delete()
        try:
            student_main_instance=studentdetailsStudentMainModel.objects.create(Owner=student,Branch=validated_data["Branch"])
            student_main_instance.Marks.add(object)
        except Exception as e:
            raise serializers.ValidationError(f"student not created:-at student formal {e}")
            object.delete()
            student.delete()
        return validated_data
# </editor-fold>

# <editor-fold desc="postStudentMarksSerializer">
class postStudentMarksSerializer(serializers.ModelSerializer):
    # user_id=serializers.CharField(max_length=100,required=True)

    class Meta:
        model=studentdetailsStudentMainMarksModel
        fields="__all__"
# </editor-fold>
