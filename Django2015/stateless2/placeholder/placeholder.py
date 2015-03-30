import hashlib
import os
import sys

from io import BytesIO
from PIL import Image, ImageDraw
#Pillow上用中文
from PIL import ImageFont

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'renqh)05f(74v^91=3yv5+ie*k4wvo)c4s&-#=1)nu2@m)0uf#')

BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS =(
        'django.contrib.staticfiles',
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR,'templates'),
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR,'static'),
    ),
    STATIC_URL='/static/',
)

from django import forms
from django.conf.urls import url
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import etag

class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""
    height = forms.IntegerField(min_value=1, max_value=2000)
    width  = forms.IntegerField(min_value=1, max_value=2000)



    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes"""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']

        key = '{}.{}.{}'.format(width,height,image_format)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGB',(width,height))

            draw = ImageDraw.Draw(image)
            #添加文字到图片
            # font = ImageFont.truetype('simsun.ttc', 24, encoding="utf-8")
            #我自己硬去找了osx上的fonts绝对地址－》
            font = ImageFont.truetype(os.path.join("fonts", "/Library/Fonts/华文仿宋.ttf"), 18)
            text = u'中文abel:{} X {}'.format(width, height)
            # textwidth, textheight = draw.textsize(text)
            #unicode转字符串：http://book.51cto.com/art/201005/198275.htm
            utf8string = text.encode("utf-8")
            textwidth, textheight = draw.textsize(utf8string)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, font=font)

            content = BytesIO()
            image.save(content,image_format)
            content.seek(0)
            cache.set(key,content, 60*60)

        return content


def generate_etag(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)
def placeholder(request, width, height):
    #TODO: rest of the view will go here
    form = ImageForm({'height':height,'width':width})
    if form.is_valid():
        image = form.generate()
        # return HttpResponse('OK')
        return  HttpResponse(image,content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')


def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height':50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)
    # return HttpResponse('Hello World from placeholder!')


urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
        name='placeholder'),
    url(r'^$', index, name='homepage'),
)



application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
