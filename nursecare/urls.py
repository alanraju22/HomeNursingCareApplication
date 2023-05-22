
from django.contrib import admin
from django.urls import path, include

from nursecare import views
import nursecare
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('reply', views.reply, name='reply'),
    path('AdminHomePage', views.AdminHomePage, name='AdminHomePage'),
    path('registernurse', views.registernurse, name='registernurse'),
    path('viewAllNewRequest', views.viewAllNewRequest, name='viewAllNewRequest'),
    path('selectpatient', views.selectpatient, name='selectpatient'),
    path('viewnurseApprove', views.viewnurseApprove, name='viewnurseApprove'),
    path('patientenqueiry', views.patientenqueiry, name='patientenqueiry'),
    path('viewComplient', views.viewComplient, name='viewComplient'),
    path('nursequery', views.nursequery, name='nursequery'),
    path('replyC/<int:id>', views.replyC, name='replyC'),
    path('replyquery', views.replyquery, name='replyquery'),

path('view_feedback', views.view_feedback, name='view_feedback'),
path('reply_feedback_action', views.reply_feedback_action, name='reply_feedback_action'),

path('link_reply_feedback/<int:id>', views.link_reply_feedback, name='link_reply_feedback'),


path('link_reply_query/<int:id>', views.link_reply_query, name='link_reply_query'),
    path('reply_admin_amount', views.reply_admin_amount, name='reply_admin_amount'),
    path('select_assigned_patient', views.select_assigned_patient, name='select_assigned_patient'),
path('reply/<int:id>', views.reply, name='reply'),


path('view_nurse_details/<str:id>', views.view_nurse_details, name='view_nurse_details'),


path('view_nurse_pro/<str:id>', views.view_nurse_pro, name='view_nurse_pro'),
path('reply_amount/<int:id>', views.reply_amount, name='reply_amount'),
path('view_approved_patient_enqueiry', views.view_approved_patient_enqueiry, name='view_approved_patient_enqueiry'),

    path('replyadmin2', views.replyadmin2, name='replyadmin2'),
    path('approve/<int:id>', views.approve, name='approve'),
    path('Reject/<int:id>', views.Reject, name='Reject'),
    path('assignnurse/<str:nid>', views.assignnurse, name='assignnurse'),
    path('selectnurse/<int:id>/<str:sid>', views.selectnurse, name='selectnurse'),
    path('delete_nurse/<str:id>', views.delete_nurse, name='delete_nurse'),
    path('Addcategory', views.Addcategory, name='Addcategory'),
    path('viewCategory', views.viewCategory, name='viewCategory'),
    path('editCategory/<int:id>', views.editCategory, name='editCategory'),
    path('updatecategory/<int:id>', views.updatecategory, name='updatecategory'),
    path('deleteCategory/<int:id>', views.deleteCategory, name='deleteCategory'),
]
