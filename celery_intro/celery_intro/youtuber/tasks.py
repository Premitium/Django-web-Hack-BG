from __future__ import absolute_import, unicode_literals
import os
import sendgrid
import time
import urllib.request as urllib

from uuid import uuid4
from celery import chain
from pytube import YouTube
from celery import shared_task
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from wsgiref.util import FileWrapper
from sendgrid.helpers.mail import Email, Content, Substitution, Mail

@shared_task
def send_email(song_url, to_email):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    if not sg.apikey:
        raise ValueError('Could not find SENDGRID_API_KEY environment variable!')
    from_email = Email("sp.parvanov@gmail.com")
    to_email = Email(to_email)
    subject = "mp4 to mp3 converter"
    link = song_url
    content = Content("text/plain", 'Your link <strong>{}</strong>'.format(song_url))
    mail = Mail(from_email, subject, to_email, content)
    mail.personalizations[0].add_substitution(Substitution("-content-", content))
    mail.personalizations[0].add_substitution(Substitution("-from_email-", from_email))
    mail.personalizations[0].add_substitution(Substitution("-to_email-", to_email))
    mail.personalizations[0].add_substitution(Substitution("-subject-", subject))
    mail.personalizations[0].add_substitution(Substitution("-link-", link))
    mail.template_id = "5dabab10-9b66-46c8-a30c-55fb6c2b59e3"
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except urllib.HTTPError as e:
        print (e.read())
        exit()
    print(response.status_code)
    print(response.body)
    print(response.headers)


@shared_task
def prepare_link_send_mail(filename, host):
    file_link = host + '/' + str(filename)
    return file_link

@shared_task
def convert_to_mp3(filename):
    inFile = filename
    outFile = filename[:-3] + 'mp3'
    cmd = 'ffmpeg -i "{}" "{}"'.format(inFile, outFile)
    os.system(cmd)
    return outFile

@shared_task
def download_url(url):
    yt = YouTube(url)
    yt.set_filename(yt.filename.split()[0]+time.strftime("%I:%M:%S"))
    video = yt.get('mp4', '360p')
    video.download(settings.MEDIA_ROOT)
    return 'media/{}.mp4'.format(yt.filename)


@shared_task
def chain_tasks(url, email, host):
    return chain(download_url.s(url), convert_to_mp3.s(), prepare_link_send_mail.s(host), send_email.s(to_email=email))
