from django.urls import path

from api_app.views import GetAllData ,GetFaveData,UpdateFaveData,PostModelData,PostData,SearchData,DeleteData,allApi,SetData

urlpatterns = [
    path('getAllData', GetAllData.as_view()),
    path('allApi', allApi),
    path('GetFaveData', GetFaveData.as_view()),
    path('UpdateFaveData/<int:pk>', UpdateFaveData.as_view()),
    path('SetData', SetData),
    path('PostModelData', PostModelData.as_view()),
    path('PostData', PostData.as_view()),
    path('Search', SearchData.as_view()),
    path('DeleteData/<int:pk>', DeleteData.as_view()),
]