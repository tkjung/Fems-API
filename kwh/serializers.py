from rest_framework import serializers
from .models import FemsTrans,FemsPayload


class kwhFemsPayload_serializers(serializers.ModelSerializer):

    class Meta:
        model = FemsPayload
        fields =  ('payload_data',)

class kwhFemsTrans_serializer(serializers.ModelSerializer):

    class Meta:
        model = FemsTrans
        fields = ('transaction_id', 'site_id', 'eng_type', 'version','dev_id', 'dev_time')

