
from django.urls import path,include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('about_us',about_us,name='about_us'),
    
    
    # Company_auth
    path('comp_reg',company_reg,name='company_reg'),
    path('comp_log',company_log,name='company_log'),
    path('comp_logout',company_logout,name='comp_logout'),
    path('comp_profile',company_profile,name='company_profile'),
    path('download/resume/<path:filename>/', download_resume, name='download_resume'),

    # company_functional
    path('company_home',company_home,name='company_home'),
    path('create_job_post',create_job_post,name='create_job_post'),
    path('update_job_post/<int:job_post_id>',update_job_post,name='update_job_post'),
    path('view_responses/<int:job_post_id>',view_responses,name='view_responses'),
    path('my_posts',my_posts,name='my_posts'),


    # recruiter_auth
    path('rec_reg',recruiter_reg,name='recruiter_reg'),
    path('rec_log',recruiter_log,name='recruiter_log'),
    path('rec_logout',rec_logout,name='rec_logout'),

    # recruiter fucntion
    path('rec_home',rec_home,name='rec_home'),
    path('rec_profile',rec_profile,name='rec_profile'),
    path('all_jobs',all_jobs,name='all_jobs'),
    path('job_detail/<int:job_id>',job_detail,name='job_detail'),
    path('search_job',search_job,name='search_job'),
    path('delete_resume/<int:resume_id>',delete_resume,name='delete_resume'),
    path('upload_resumes',upload_resumes,name='upload_resumes'),
    path('send_resumes/<int:job_id>',send_resumes,name='send_resumes'),
    path('candidates_per_job',candidates_per_job,name='candidates_per_job'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)