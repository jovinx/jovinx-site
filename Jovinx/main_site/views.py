from django.shortcuts import render, redirect
from .models import MailSubscriber, ServiceRequest, Message, JovinxInfo, WhyJovinx, Service, Client, Testimony, WebGallery, GraphicsGallery, IllustrationGallery, ArtGallery, MotionGraphicsGallery
from datetime import date
from .forms import MessageForm, ServiceRequstForm
from django.core.mail import send_mail
from django.contrib import messages


today = date.today()
this_year = today.year
# Create your views here.

def index(request):
    services = Service.objects.all()
    clients = Client.objects.all()
    testimonies = Testimony.objects.all()
    reasons = WhyJovinx.objects.all()
    jovinx_data = JovinxInfo.objects.get(pk=1)
    web_projects = WebGallery.objects.all().order_by('-pk')[:3]
    graphics_projects = GraphicsGallery.objects.all().order_by('-pk')[:4]
    ill_projects = IllustrationGallery.objects.all().order_by('-pk')[:3]

    our_works = {
        'web': web_projects,
        'graphics': graphics_projects,
        'illustrations': ill_projects
    }


    context = {
        'services':services,
        'clients':clients,
        'testimonies':testimonies,
        'reasons': reasons,
        'jovinx_data': jovinx_data,
        'this_year':this_year,
        'home_active': 'active',
        'our_works': our_works,
        'service_request_form': ServiceRequstForm        
    }
    return render(request, 'main_site/index.html',context)

def service(request):
    services = Service.objects.all()
    jovinx_data = JovinxInfo.objects.get(pk=1)
    

    context = {
        'services': services,
        'jovinx_data': jovinx_data,
        'service_active': 'active',
        'this_year':this_year,
        'service_request_form': ServiceRequstForm 
    }
    return render(request, 'main_site/services.html', context )

def service_detail(request, pk):
    details = Service.objects.get(pk=pk)
    services = Service.objects.all()
    jovinx_data = JovinxInfo.objects.get(pk=1)
    
    context = {
        'service_info': details,
        'services': services,
        'jovinx_data': jovinx_data,
        'service_active': 'active',
        'this_year':this_year,
        'service_request_form': ServiceRequstForm 
    }
    return render(request, 'main_site/service_detail.html', context)

def gallery(request):
    websites = WebGallery.objects.all()
    graphics = GraphicsGallery.objects.all()
    illustrations = IllustrationGallery.objects.all()
    services = Service.objects.all()
    arts = ArtGallery.objects.all()
    services = Service.objects.all()
    jovinx_data = JovinxInfo.objects.get(pk=1)
    

    context = {
        'websites': websites,
        'graphics': graphics,
        'illustrations':illustrations,
        'arts': arts,
        'jovinx_data': jovinx_data,
        'services': services,
        'gallery_active': 'active',
        'this_year':this_year
    }
    return render(request, 'main_site/gallery.html', context)


def contact(request):
    jovinx_data = JovinxInfo.objects.get(pk=1)
    services = Service.objects.all()

    context = {
        'jovinx_data':jovinx_data,
        'services': services,
        'contact_active': 'active',
        'this_year':this_year,
        'message_form':MessageForm,
        'service_request_form': ServiceRequstForm
    }
    return render(request, 'main_site/contact.html', context)

def about(request):
    jovinx_data = JovinxInfo.objects.get(pk=1)
    services = Service.objects.all()    
    context = {
        'jovinx_data':jovinx_data,
        'services': services,
        'about_active': 'active',
        'this_year':this_year
    }
    return render(request, 'main_site/about.html', context)

def service_request(request):
    if request.method == 'POST':

        current_page_url = request.POST['next']

        form = ServiceRequstForm(request.POST)
        if form.is_valid():
            try:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone = form.cleaned_data['phone']
                sender = form.cleaned_data['email']
                service_requested = form.cleaned_data['service_requested']
                specifications = form.cleaned_data['specifications']

                #saving to the database
                new_service_request = ServiceRequest(first_name=first_name, last_name=last_name, phone=phone, email=sender, service_requested=service_requested, specifications=specifications)
                new_service_request.save()

                #send message as mail
                subject = 'SERVICE REQUEST FROM '+first_name.upper() +' '+last_name.upper()
                message = service_requested.upper() + 'SERVICE REQUEST FROM '+first_name.upper() +' '+last_name.upper() + ' \nPhone: '+str(phone)+  '\n\n' +specifications
                recipients = ['jovinxcreative@gmail.com', 'johngorithm@gmail.com']

                send_mail(subject, message, sender, recipients)

                messages.add_message(request, messages.SUCCESS, 'Your request has been sent successfully')
                return redirect(current_page_url)
            except:
                messages.add_message(request, messages.ERROR, 'Sorry, You submitted an Invalid data. Please try again')            
                return redirect(current_page_url)
        else:
            messages.add_message(request, messages.ERROR, 'Sorry, This email alreay exist. Please change it and try again')            
            return redirect(current_page_url)

    else:
        messages.add_message(request, messages.INFO, 'No Data Received')
        return redirect('/')


def client_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            try:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone = form.cleaned_data['phone']
                sender = form.cleaned_data['email']
                message = form.cleaned_data['message']

                #Saving Client's Message to the Message Model
                new_message = Message.objects.create(first_name=first_name, last_name=last_name, phone=phone, email=sender, message=message)
                new_message.save()

                #Sending Client's Message as Mail
                subject = 'MESSAGE FROM '+first_name.upper() +' '+last_name.upper()
                message = 'MESSAGE FROM '+first_name.upper() +' '+last_name.upper() + '\nPhone: '+str(phone)+ '\n\n' +message
                recipients = ['jovinxcreative@gmail.com', 'johngorithm@gmail.com']

                send_mail(subject, message, sender, recipients)

                
                messages.add_message(request, messages.SUCCESS, 'Your Message was sent successfully')
                return redirect('/contact')
            except: 
                messages.add_message(request, messages.ERROR, 'Sorry, Something went wrong. Please try again')
                return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Sorry, You submitted an Invalid Data. Please try again')
            return redirect('/contact')
    else:
        messages.add_message(request, messages.INFO, 'No Data Received')
        return redirect('/contact')

def newsletter_sub(request):
    if request.method == 'POST':
        #current page url
        current_page_url = request.POST.get('next')

        user_email = request.POST['user_email']
        try:
            new_subscription = MailSubscriber.objects.create(user_email = user_email)
            new_subscription.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to our news letters. Thanks')            
            return redirect(current_page_url)
        except:
            messages.add_message(request, messages.ERROR, 'The email address you entered already exist. Change it and try again')            
            return redirect(current_page_url)
    else:
        messages.add_message(request, messages.INFO, 'No Data submitted. Try again')        
        return redirect('/')

