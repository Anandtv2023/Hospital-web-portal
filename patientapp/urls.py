
from django.urls import path
from patientapp import views

urlpatterns=[

path('register/',views.Registrationview.as_view(),name='register'),
path('profile/',views.Patientview.as_view(),name='p_profile'),
path('update_profile/<int:pk>/',views.Update_profile.as_view(),name='update_profile'),
path('p_view/<int:pk>',views.Patientdetailview.as_view(),name='p_view'),
path('booking/',views.Bookingview.as_view(),name='booking'),
path('history/',views.Bookinghistory.as_view(),name='history'),
path('delete_bookig/<int:pk>',views.Delete_booking.as_view(),name='del'),

path('booking/edit/<int:pk>/',views.BookStatusUpdate.as_view(),name='edit'),#update the visiting status,doctor can update the status

path('prescription/<int:pk>/',views.Prescibe.as_view(),name='pres'),
path('viewrecords/<int:pk>/',views.ViewRecord.as_view(),name='viewrecord'),
]