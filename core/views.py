from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document, Project
from contact.models import Message
from contact.forms import ContactForm
from django.http import JsonResponse

# Create your views here.
def contact_form(request):
    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            contact_form.send_mail()

            success = True
            message = 'Contact from sent successfully.'
        else:
            success = False
            message = 'Request method is not valid.'
    else:
        success = False
        message = 'Request method is not valid.'

    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj


def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj


def layout(request):
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')
    birth_date = get_general_setting('birth_date')
    phone_number = get_general_setting('phone_number')
    email = get_general_setting('email')
    location = get_general_setting('location')

    # Images
    header_logo = get_image_setting('header_logo')
    home_banner_image = get_image_setting('home_banner_image')
    site_favicon = get_image_setting('site_favicon')

    projects = Project.objects.all()
    projects_count = projects.count()

    social_medias = SocialMedia.objects.all()
    documents = Document.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'birth_date': birth_date,
        'phone_number': phone_number,
        'email': email,
        'location': location,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'documents': documents,
        'social_medias': social_medias,
        'projects': projects,
        'projects_count': projects_count,
    }
    return context


def index(request):
    # Skills
    skills = Skill.objects.all()

    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')
    contact_form = ContactForm(request.POST or None)

    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'projects_count': layout(request)['projects_count'],
        'contact_form': contact_form,
    }

    return render(request, 'index.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)
