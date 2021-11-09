from django.urls import path

from . import views

app_name = 'ipitem'

urlpatterns = [
    path('items/user/', views.items_list, name='all_user_ip'),
    path('items/addnew/', views.item_add, name='new_ip'),
    path('item/edit/<str:pk>/', views.item_edit, name='edit_ip'),
    path('item/ip_info/<str:pk>/', views.item_info, name='ip_info'),
    path('item/delete_confirmation/<str:pk>/',
         views.item_delete_confirmation,
         name='delete_ip_confirmation'),
    path('item/delete/<str:pk>/', views.item_delete, name='delete_ip'),
    path('item/item_check_on_fips/<str:pk>/',
         views.item_check_on_fips,
         name='item_check_on_fips'),
    path('item/item_prepare_letter/<str:pk>/',
         views.item_prepare_letter,
         name='item_prepare_letter'),
    path('item/item_prepare_letter/<str:pk>/no_send_email/',
         views.item_prepare_letter_no_send_email,
         name='item_prepare_letter_no_send_email'),
    path('item/item_yearly_payment/<str:pk>/',
         views.item_payments,
         name='item_yearly_payment'),
    path('fips_pars/', views.fips_pars, name='fips_pars'),
]
