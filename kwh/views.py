from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import kwhFemsTrans_serializer,kwhFemsPayload_serializers
from .models import FemsTrans, FemsPayload

class addFemsTransData(APIView):
    def post(self, request):
        json_data = []

        for i in range(len(request.data['payload'])):
            #받은 json 형식을 각 테이블에 올바른 방식으로 매핑해줌
            json_data1 = request.data
            json_data1 = dict({key: value for key, value in json_data1.items() if key != 'payload'})

            json_data2 = request.data['payload'][i]
            json_data2['site'] = request.data['site_id']

            payload_data = str({key: value for key, value in json_data2.items() if key != 'dev_id' and key != 'dev_time'})

            json_data1['dev_id'] = json_data2['dev_id']
            json_data1['dev_time'] = json_data2['dev_time']
            json_data2['payload_data'] = payload_data
            json_data2 = dict({key: value for key, value in json_data2.items() if key == 'dev_id' or key == 'dev_time' or key == 'site'or key == 'payload_data'})

            print(json_data2)
            print(json_data1)
            Valid = json_data1.get('dev_id') and json_data1.get('dev_time') and json_data1.get('site_id') and json_data1.get('eng_type') and json_data1.get('version') and json_data1.get('transaction_id') and json_data2.get('payload_data')
            if Valid:
                FemsTrans.objects.create(site_id=json_data1['site_id'], dev_id=json_data1['dev_id'],
                                         dev_time=json_data1['dev_time'], transaction_id=json_data1['transaction_id'],
                                         eng_type=json_data1['eng_type'], version=json_data1['version'])
                dev = FemsTrans.objects.get(site_id=json_data1['site_id'], dev_id=json_data1['dev_id'],
                                            dev_time=json_data1['dev_time'])
                FemsPayload.objects.create(payload_data=json_data2['payload_data'], site_id=json_data1['site_id'],
                                           dev_id=dev, dev_time=dev)
                return Response(request.data, status=status.HTTP_201_CREATED)
            else:
                return Response('fields error', status=status.HTTP_400_BAD_REQUEST)

        # return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def fems_datalist(request):
    if request.method == 'GET':
        qs_trans = FemsTrans.objects.all()
        qs_payload = FemsPayload.objects.all()
        serializer = kwhFemsTrans_serializer(qs_trans, many=True)
        serializer_p = kwhFemsPayload_serializers(qs_payload,many=True)

        return Response(serializer.data+serializer_p.data)
    return Response(kwhFemsPayload_serializers.errors, status=400)

