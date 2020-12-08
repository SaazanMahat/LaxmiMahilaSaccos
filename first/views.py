from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm
from first.models import Notice, Slideshow, ScrollNews, Image, PostImage, Video, Report, Form, Statistic, PopUp, Saving, Loan, Other_program

from django.views.generic import DetailView
from django.core.paginator import Paginator
# Create your views here.


def homepage(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            template = get_template('contact_form.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "Contact Email",
                content,
                "Laxmi Mahila Mail" + '',
                ['sajanmahat491@gmail.com', 'pythonsm491@gmail.com'],
                headers={'Reply To': email}
            )

            email.send()
            messages.success(request, 'Email Sent! Thank You!')

    context = {
        'form': Contact_Form,
        'popups': PopUp.objects.all(),
        'pics': Slideshow.objects.all(),
        'scrollnews': ScrollNews.objects.all(),
        'notices': Notice.objects.all()[:2]

    }
    return render(request, 'homepage.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')


def affiliations(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'affiliations.html', context)


def msg_chairperson(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'msg_chairperson.html', context)


def msg_manager(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'msg_manager.html', context)


def savings(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
        'savings': Saving.objects.all(),
    }
    return render(request, 'savings.html', context)


def remittance(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'remittance.html', context)


def insurance(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'insurance.html', context)


def term(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'term_deposits.html', context)


def loans(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
        'loans': Loan.objects.all(),
    }
    return render(request, 'loans.html', context)


def other_programs(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
        'programs': Other_program.objects.all(),
    }
    return render(request, 'other_programs.html', context)


def msg_manager(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'msg_manager.html', context)


def org_profile(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'org_profile.html', context)


def vision(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),

    }
    return render(request, 'vision.html', context)


def management_team(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'management_team.html', context)


def communication_team(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'communication_team.html', context)


def probesan_team(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'probesan_team.html', context)


def other_teams(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'other_teams.html', context)


def account(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'account.html', context)


def loan(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'loan.html', context)


def policies(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),

    }
    return render(request, 'policies.html', context)


def employees(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'employees.html', context)


def branch_office(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'branch_office.html', context)


def services(request):
    context = {
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'services.html', context)


class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice_detail.html'


def notice(request):
    notices = Notice.objects.all().order_by('-date_posted')
    paginator = Paginator(notices, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'scrollnews': ScrollNews.objects.all(),
        'page_obj': page_obj,
        'statistics': Statistic.objects.all(),

    }
    return render(request, 'notice.html', context)


def photo(request):
    photo = Image.objects.all()
    paginator = Paginator(photo, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'scrollnews': ScrollNews.objects.all(),
        'page_obj': page_obj,
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'photo.html', context)


def photo_detail(request, id):

    post = get_object_or_404(Image, id=id)
    all_photos = PostImage.objects.filter(post=post)
    return render(request, 'photo_detail.html', {
        'post': post,

        'all_photos': all_photos,
        'scrollnews': ScrollNews.objects.all()
    })


def video(request):
    videos = Video.objects.all()

    paginator = Paginator(videos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'video.html', context)


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_detail.html'


def calender(request):
    return render(request, 'calender.html')


def forms(request):
    context = {
        'forms': Form.objects.all(),
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'forms.html', context)


def reports(request):

    reports = Report.objects.all()
    paginator = Paginator(reports, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'scrollnews': ScrollNews.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'reports.html', context)


def contact(request):

    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            template = get_template('contact_form.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "Contact Email",
                content,
                "Laxmi Mahila Mail" + '',
                ['sajanmahat491@gmail.com', 'pythonsm491@gmail.com'],
                headers={'Reply To': email}
            )

            email.send()
            messages.success(request, 'Email Sent! Thank You!')
    context = {
        'form': Contact_Form,
        'scrollnews': ScrollNews.objects.all()
    }
    return render(request, 'contact.html', context)
