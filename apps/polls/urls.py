from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_exercise', views.create_exercise, name='create_exercise'),
    path('redact_exercise/<int:exercise_id>', views.edit_exercise, name='redact_exercise'),
    path('view_exercise/<int:exercise_id>', views.view_exercise, name='view_exercise'),
    path('view_pupil_results/<int:results_id>',
         views.view_pupil_results,
         name='view_pupil_results'
         ),

]
