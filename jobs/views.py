from django.shortcuts import render
from .models import JobApplication
from .forms import JobApplicationForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import csv
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth import views as auth_views
from .forms import RegisterForm
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def home(request):
    return render(request, 'jobs/home.html')

@login_required

def application_list(request):

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    applications = JobApplication.objects.filter(
    user=request.user
)

    if search_query:
        applications = applications.filter(
            company_name__icontains=search_query
        )

    if status_filter:
        applications = applications.filter(
            status=status_filter
        )

    context = {
        'applications': applications,
        'search_query': search_query,
        'status_filter': status_filter
    }

    return render(
        request,
        'jobs/application_list.html',
        context
    )

@login_required


def add_application(request):

    if request.method == 'POST':

        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            
            return redirect('application_list')

    else:

        form = JobApplicationForm()

    return render(
        request,
        'jobs/add_application.html',
        {'form': form}
    )

@login_required

def edit_application(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk
    )

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()

            return redirect(
                'application_list'
            )

    else:

        form = JobApplicationForm(
            instance=application
        )

    return render(
        request,
        'jobs/edit_application.html',
        {'form': form}
    )

@login_required

def delete_application(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk
    )

    application.delete()

    return redirect(
        'application_list'
    )

@login_required

def dashboard(request):

    total_applications = JobApplication.objects.filter(
    user=request.user
).count()

    recent_applications = JobApplication.objects.filter(
    user=request.user
).order_by('-id')[:5]

    applied_count = JobApplication.objects.filter(
    user=request.user,
    status='Applied'
).count()

    interview_count = JobApplication.objects.filter(
        user=request.user,
        status='Interview'
    ).count()

    offer_count = JobApplication.objects.filter(
        user=request.user,
        status='Offer'
    ).count()

    rejected_count = JobApplication.objects.filter(
        user=request.user,
        status='Rejected'
    ).count()

    context = {
        'total_applications': total_applications,
        'applied_count': applied_count,
        'interview_count': interview_count,
        'offer_count': offer_count,
        'rejected_count': rejected_count,
        'recent_applications': recent_applications,

        'chart_labels': [
    'Applied',
    'Interview',
    'Offer',
    'Rejected'
],

'chart_data': [
    applied_count,
    interview_count,
    offer_count,
    rejected_count
]
    }

    return render(
        request,
        'jobs/dashboard.html',
        context
    )

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'jobs/register.html',
        {'form': form}
    )
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def export_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = (
        'attachment; filename="applications.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        'Company',
        'Job Title',
        'Location',
        'Applied Date',
        'Status'
    ])

    applications = JobApplication.objects.filter(
        user=request.user
    )

    for app in applications:

        writer.writerow([
            app.company_name,
            app.job_title,
            app.job_location,
            app.applied_date,
            app.status
        ])

    return response