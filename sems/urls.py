from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('students/', views.students_view, name='students'),
    path('profile/<int:pk>', views.student_detail, name='student_detail'),
    path('programs/', views.programs_view, name='programs'),
    path('programs/add/', views.program_add, name='program_add'),
    path('programs/edit/<int:pk>', views.program_edit, name='program_edit'),
    path('programs/delete/<int:pk>', views.program_delete, name='program_delete'),
    path('programs/<int:pk>/course/add/', views.course_add, name='course_add'),
    path('programs/<int:p_pk>/course/delete/<int:pk>', views.course_delete, name='course_delete'),
    # path('programs/<int:pk>', views.program_detail, name='programs_detail'),
    path('programs/course/<int:pk>', views.course_detail, name='course_detail'),
    path('program/<int:pk>', views.program_detail, name='program_single'),
    path('program/course/<int:course_id>/upload/', views.handle_file_upload, name='upload_file_view'),
    path('program/course/<int:course_id>/edit/<int:file_id>', views.handle_file_edit, name='upload_file_edit'),
    path('program/course/<int:course_id>/delete/<int:file_id>', views.handle_file_delete, name='upload_file_delete'),
    path('students/add/', views.user_add, name='user_add'),
    path('profile/edit/<int:pk>', views.user_edit, name='user_edit'),
    path('course/<int:course_id>/teacher/edit/', views.select_teacher, name='add_teacher'),
    path('course/<int:course_id>/teacher/confirm/<int:student_id>', views.confirm_select_teacher, name='confirm_teacher'),
    path('course/<int:course_id>/teacher/delete/<int:student_id>', views.confirm_delete_teacher, name='delete_teacher'),
    path('ajax/filter_course/', views.filter_courses_view, name='filter_views'),
    path('post/<int:pk>', views.post_single, name='post_single'),
    path('post/add/', views.post_add, name='post_add'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('course/<int:course_id>/grades/', views.grade_students, name='grade_students'),
    path('posts/', views.post_list, name='post_list'),
    re_path(r'^$', views.home_view, name='home'),
]