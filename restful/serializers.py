from rest_framework import serializers

from restful.models import Profile


class ProfileSerializer(serializers.Serializer):

    name = serializers.CharField()
    phone = serializers.IntegerField()

    '''
    class Meta:
        model = Profile
        fields = ('id','name','phone')
    '''