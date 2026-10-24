
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Route to the course list page
    path(route='', view=views.CourseListView.as_view(), name='index'),

    # Routes for user registration and authentication
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Route to display course details
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Route to enroll in a course
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Route to submit the exam
    path('<int:course_id>/submit/', views.submit, name='submit'),

    # Route to display exam results
    path(
        '<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
