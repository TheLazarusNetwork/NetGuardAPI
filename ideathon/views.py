from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .eth_utils import Contract, NetGuard_Ideathon
from NetGuard.contract_config import *

# Create your views here.





class CreateNewGuardView(APIView):
    api_view=['POST',]

    def post(self, request):
        try:
            content = request.data.get('content')
            domain = request.data.get('domain')

            print(content)
            print(domain)

            contract = Contract(rpc_url, contract_address, contract_abi)
            netguard = NetGuard_Ideathon(contract)
            if content.lower() == 'malwares':
                tx_hash = netguard.create("bot", domain)
            else:
                tx_hash = netguard.create(content.lower(), domain)
            if tx_hash:
                return Response({"transaction_hash" : contract.web3.toHex(tx_hash)}, status.HTTP_200_OK)
            else:
                return Response({"error" : "Something Went Wrong"}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error" : "Something Went Wrong"}, status.HTTP_400_BAD_REQUEST)


class GetNetGuardView(APIView):
    api_view=['GET',]

    def get(self, request):
        try:
            domain = request.query_params.get('domain', None)
            if domain:
                contract = Contract(rpc_url, contract_address, contract_abi)
                netguard = NetGuard_Ideathon(contract)
                data = netguard.getValues(domain)
            else:
                return Response({"error" : "Something Went Wrong"}, status.HTTP_400_BAD_REQUEST)
            
            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : "Something Went Wrong"}, status.HTTP_400_BAD_REQUEST)