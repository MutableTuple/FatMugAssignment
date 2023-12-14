from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profiles
        fields = "__all__"
        


