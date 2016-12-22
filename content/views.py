from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from menu.models import Menu
from sub_menu.models import Sub_Menu
from django.shortcuts import render_to_response, redirect
import re
#import xmltodict as xmltodict
from category_menu.models import Category_Menu
from content.models import Content, Comments, Category, language
from geolocation.models import Geolocation, Views
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth import logout
from datetime import datetime, time, date, timedelta
import json
from django.http import StreamingHttpResponse
from django.contrib.auth import authenticate
from django.db.models import Q
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.template import *
from django.contrib.gis.geoip import GeoIP



def auth_required(function):
    def check_auth(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/error/')
        return function(request)
    return check_auth

def get_news(request, error=''):
    lang = getLangSession(request)
    args = {}
    photo = []
    args.update(csrf(request))
    args['error_login'] = error
    args.update(getMenu_and_Lang(request))
    args['news'] = Content.objects.filter(cat_id=3, language=lang, state=1).order_by('-id')
    contents = Content.objects.filter(cat_id=3, language=lang, state=1).order_by('-id')
    for content in contents:
        # ----- get img link from object ---#
            pat = re.compile(r'<img [^>]*src="([^"]+)')
            photo.append({'id': content.id, 'images': pat.findall(content.full_text)})
        # -----------------------------------#
    args['photos'] = photo
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('home.html', args, context_instance=RequestContext(request))

# @auth_required  имеет доступ только авторизованные пользователи
def about_us(request):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['about'] = Content.objects.filter(cat_id=4, language=lang, state=1).order_by('-id')
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('about_us.html', args, context_instance=RequestContext(request))


def news(request, content_id):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['news_menu'] = Content.objects.filter(~Q(id=content_id), cat_id=3, language=lang, state=1)
    args['news'] = Content.objects.filter(id=content_id, language=lang, state=1)
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    # ----- get img link from object ---#
    imgs = Content.objects.filter(id=content_id, language=lang, state=1)
    for img in imgs:
        pat = re.compile(r'<img [^>]*src="([^"]+)')
        args['photos'] = pat.findall(img.full_text)
    # -----------------------------------#
    return render_to_response('news.html', args, context_instance=RequestContext(request))


def service(request):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['services'] = Content.objects.filter(cat_id=6, language=lang, state=1).order_by('-id')
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('services.html', args, context_instance=RequestContext(request))


def portfolio(request):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['porfolios'] = Content.objects.filter(cat_id=7, language=lang, state=1).order_by('-id')
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('portfolio.html', args, context_instance=RequestContext(request))


def lecca(request, content_id):
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['Lecca'] = Content.objects.filter(id=content_id, state=1)
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('lecca.html', args, context_instance=RequestContext(request))


def contact(request):
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('contact.html', args, context_instance=RequestContext(request))


def details(request, content_id, menu_id=0):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args.update(getMenu_and_Lang(request))
    args['submenus'] = Sub_Menu.objects.filter(cat_id=menu_id)
    args['details'] = Content.objects.filter(id=content_id, language=lang, state=1)
    args['request'] = request
    args['username'] = auth.get_user(request).username
    """" *****---- geo location info ----***** """
    args.update(getVisitorInfo(request))
    """" *****---- end geo location info ----***** """
    return render_to_response('details.html', args, context_instance=RequestContext(request))


def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect('/')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect('/error/')


def user_logout(request):
    auth.logout(request)
    request.session['0'] = 0
    # Redirect to a success page.
    return HttpResponseRedirect('/')


def usersignin(request):
    username = request.POST['username_signin']
    password = request.POST['password_signin']
    email = request.POST['email_signin']
    user = User.objects.create_user(username, email, password)
    user.is_staff = True
    user.save()
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
    return HttpResponseRedirect('/')


def getlang(request, lang):
    request.session['0'] = lang
    # back_url = request.META['HTTP_REFERER'] #Перенаправляет на текущую страницу
    back_url = '/'
    return HttpResponseRedirect(back_url)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location(request):
    g = GeoIP()
    # location = g.country('reserve.kg')
    ip = get_client_ip(request)
    location = g.country(ip)
    return location

def save_locations(ip_address, country_name, country_code):
    SaveVisit = Views.objects.filter(ip_address=ip_address, view_date=date.today()).count()
    if SaveVisit == 0:
        SaveVisit = Geolocation(ip_address=ip_address, country_name=country_name, country_code=country_code, visit_date=date.today())
        SaveVisit.save()
    num_result = Views.objects.filter(ip_address=ip_address, view_date=date.today()).count()
    if num_result > 0:
        saveViews = Views.objects.get(ip_address=ip_address, view_date=date.today())
        saveViews.views_count += 1
        saveViews.save()
    else:
        saveViews = Views(ip_address=ip_address, views_count=1, view_date=date.today())
        saveViews.save()

def getVisits():
    args = {}
    all_location = Geolocation.objects.raw(
        'SELECT id, ip_address, country_name, country_code, visit_date FROM visits '
        'NATURAL JOIN (SELECT country_code, MAX(id) AS id FROM visits GROUP BY country_code) p ORDER BY id DESC LIMIT 5')
    args['all_visitors'] = all_location
    args['visitors_count'] = Geolocation.objects.all().count()
    return args


def getViews():
    from django.db.models import Sum
    views = Views.objects.aggregate(Sum('views_count'))
    return views


def getVisitorInfo(request):
    args = {}
    location = get_location(request)
    args['Views'] = getViews()
    visitors_args = getVisits()
    args['all_visitors'] = visitors_args['all_visitors']
    args['visitors_count'] = visitors_args['visitors_count']
    ip_address = get_client_ip(request)
    country_name = location['country_name']
    country_code = location['country_code']
    save_locations(ip_address, country_name, country_code)
    return args


def getMenu_and_Lang(request):
    lang = getLangSession(request)
    args = {}
    args.update(csrf(request))
    args['catmenus'] = Category_Menu.objects.filter(language=lang)
    args['menus'] = Menu.objects.all()
    args['languages'] = language.objects.filter(~Q(id=lang))
    args['langs'] = language.objects.filter(id=lang)
    return args


def getLangSession(request):
    if '0' not in request.session or request.session['0'] == 0:
        request.session['0'] = 2
    return request.session['0']
