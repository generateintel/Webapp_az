import requests
from django.contrib.auth.models import User
from django.shortcuts import render
import random
import re
import string
# import requests
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMessage
from rest_framework.utils import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status, viewsets, mixins, generics, response

# Generate Jwt-Token
from rest_framework_jwt.settings import api_settings

from TOOLS.helium_scrapper import helium_script

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your views here.
class Black_Box(viewsets.ViewSet):#User class
    @action(detail=False,methods=['post'])
    def Filter_Data(self, request):
        try:
            category=request.data['category']
            monthlyRevenue_min=request.data['monthlyRevenue_min']
            monthlyRevenue_max=request.data['monthlyRevenue_max']
            price_min=request.data['price_min']
            price_max = request.data['price_max']
            reviewCount_min=request.data['reviewCount_min']
            reviewCount_max=request.data['reviewCount_max']
            reviewRating_min=request.data['reviewRating_min']
            reviewRating_max=request.data['reviewRating_max']
            sizeTier=request.data['sizeTier']
            salesYearOverYear_min=request.data['salesYearOverYear_min']
            salesYearOverYear_max=request.data['salesYearOverYear_max']
            priceChange_min = request.data['priceChange_min']
            priceChange_max = request.data['priceChange_max']
            salesChange_min = request.data['salesChange_min']
            salesChange_max = request.data['salesChange_max']
            bestMonth=request.data['bestMonth']
            salesToReviews_min = request.data['salesToReviews_min']
            salesToReviews_max = request.data['salesToReviews_max']
            monthlySales_min = request.data['monthlySales_min']
            monthlySales_max = request.data['monthlySales_max']
            salesRank_min = request.data['salesRank_min']
            salesRank_max = request.data['salesRank_max']
            numberOfSellers_min = request.data['numberOfSellers_min']
            numberOfSellers_max = request.data['numberOfSellers_max']
            fulfillment=request.data['fulfillment']
            numberOfImages_min = request.data['numberOfImages_min']
            numberOfImages_max = request.data['numberOfImages_max']
            variationCount_min = request.data['variationCount_min']
            variationCount_max = request.data['variationCount_max']
            weight_min = request.data['weight_min']
            weight_max = request.data['weight_max']
            age_min = request.data['age_min']
            age_max = request.data['age_max']
            reviewVelocity_min = request.data['reviewVelocity_min']
            reviewVelocity_max = request.data['reviewVelocity_max']
            titleKeyword = request.data['titleKeyword']
            titleExcludeKeyword = request.data['titleExcludeKeyword']


            data={
                # 'filters': '[{"id":"category","options":[1]},{"id":"monthlyRevenue","min":null,"max":null},{"id":"price","min":null,"max":null},{"id":"reviewCount","min":null,"max":null},{"id":"reviewRating","min":null,"max":null},{"id":"sizeTier","options":[]},{"id":"salesYearOverYear","min":null,"max":null},{"id":"priceChange","min":null,"max":null},{"id":"salesChange","min":null,"max":null},{"id":"bestMonth","value":null},{"id":"salesToReviews","min":null,"max":null},{"id":"monthlySales","min":null,"max":null},{"id":"salesRank","min":null,"max":null},{"id":"numberOfSellers","min":null,"max":null},{"id":"fulfillment","options":[]},{"id":"numberOfImages","min":null,"max":null},{"id":"variationCount","min":null,"max":null},{"id":"weight","min":null,"max":null},{"id":"age","min":null,"max":null},{"id":"reviewVelocity","min":null,"max":null},{"id":"titleKeyword","value":null},{"id":"titleExcludeKeyword","value":null}]'
                'filters': '[{"id":"category","options":'+category+'},{"id":"monthlyRevenue","min":'+monthlyRevenue_min+',"max":'+monthlyRevenue_max+'},{"id":"price","min":'+price_min+',"max":'+price_max+'},{"id":"reviewCount","min":'+reviewCount_min+',"max":'+reviewCount_max+'},{"id":"reviewRating","min":'+reviewRating_min+',"max":'+reviewRating_max+'},{"id":"sizeTier","options":'+sizeTier+'},{"id":"salesYearOverYear","min":'+salesYearOverYear_min+',"max":'+salesYearOverYear_max+'},{"id":"priceChange","min":'+priceChange_min+',"max":'+priceChange_max+'},{"id":"salesChange","min":'+salesChange_min+',"max":'+salesChange_max+'},{"id":"bestMonth","value":'+bestMonth+'},{"id":"salesToReviews","min":'+salesToReviews_min+',"max":'+salesToReviews_max+'},{"id":"monthlySales","min":'+monthlySales_min+',"max":'+monthlySales_max+'},{"id":"salesRank","min":'+salesRank_min+',"max":'+salesRank_max+'},{"id":"numberOfSellers","min":'+numberOfSellers_min+',"max":'+numberOfSellers_max+'},{"id":"fulfillment","options":'+fulfillment+'},{"id":"numberOfImages","min":'+numberOfImages_min+',"max":'+numberOfImages_max+'},{"id":"variationCount","min":'+variationCount_min+',"max":'+variationCount_max+'},{"id":"weight","min":'+weight_min+',"max":'+weight_max+'},{"id":"age","min":'+age_min+',"max":'+age_max+'},{"id":"reviewVelocity","min":'+reviewVelocity_min+',"max":'+reviewVelocity_max+'},{"id":"titleKeyword","value":'+titleKeyword+'},{"id":"titleExcludeKeyword","value":null}]'
            }
            result=helium_script(data)
            dumps = json.dumps(result)
            # print(type(dumps))
            return Response({"Records":dumps},status=status.HTTP_200_OK)
        except:
            return Response({"msg":"Send all Fields"},status=status.HTTP_400_BAD_REQUEST)

# {
#         "category":"[1,2,3]",
#         "monthlyRevenue_min":"0",
#         "monthlyRevenue_max":"20000",
#         "price_min":"12",
#         "price_max":"23",
#         "reviewCount_min":"1",
#         "reviewCount_max":"5",
#         "reviewRating_min":"1",
#         "reviewRating_max":"3",
#         "sizeTier":"[1,2,3]"
# }



#no data
# {
#         "category":"[1]",
#         "monthlyRevenue_min":"1",
#         "monthlyRevenue_max":"3",
#         "price_min":"3",
#         "price_max":"5",
#         "reviewCount_min":"12",
#         "reviewCount_max":"30",
#         "reviewRating_min":"4",
#         "reviewRating_max":"6",
#         "sizeTier":"[1,2,6]"
# }




# [{"id":"category","options":[1,2,3]},{"id":"monthlyRevenue","min":0,"max":2000},{"id":"price","min":12,"max":23},{"id":"reviewCount","min":1,"max":5},{"id":"reviewRating","min":1,"max":3},{"id":"sizeTier","options":[1,2,3]},{"id":"salesYearOverYear","min":null,"max":null},{"id":"priceChange","min":null,"max":null},{"id":"salesChange","min":null,"max":null},{"id":"bestMonth","value":null},{"id":"salesToReviews","min":null,"max":null},{"id":"monthlySales","min":null,"max":null},{"id":"salesRank","min":null,"max":null},{"id":"numberOfSellers","min":null,"max":null},{"id":"fulfillment","options":[]},{"id":"numberOfImages","min":null,"max":null},{"id":"variationCount","min":null,"max":null},{"id":"weight","min":null,"max":null},{"id":"age","min":null,"max":null},{"id":"reviewVelocity","min":null,"max":null},{"id":"titleKeyword","value":null},{"id":"titleExcludeKeyword","value":null}]
