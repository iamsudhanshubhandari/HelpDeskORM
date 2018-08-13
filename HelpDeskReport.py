#!/usr/bin/env python

import os
import sys
import pandas as pd
import numpy as np
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email_id = "sudhanshu.bhandari@geminisolutions.in"
my_password = open('password').read()
server = smtplib.SMTP('smtp.gmail.com', 587)


class HelpDeskReport:
    def __init__(self):
        print "Inside init"
        self.url = "http://127.0.0.1:5000/tickets_data?ticket_id={}"
        self.create_requests()
        self.generate_report()
        self.send_report()

    def create_requests(self):
        print "Inside Create Requests"
        temp_url = self.url
        temp_url = temp_url.format(2144)
        print temp_url
        response = requests.get(temp_url)
        self.report_data = response.json()

    def generate_report(self):
        print "Hi Inside Generate Report"
        self.message = """<html><head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head><body>"""
        self.message += "Ticket Id = {}<br/>".format(self.report_data['tickets_data'][0]['id'])
        self.message += "Ticket Submitter = {}<br/>".format(self.report_data['tickets_data'][0]['requester'])
        self.message += "Ticket Submitted On = {}<br/>".format(self.report_data['tickets_data'][0]['opening_date'])
        self.message += "Ticket Subject = {}<br/>".format(self.report_data['tickets_data'][0]['ticket_subject'])
        self.message += "Ticket Description = {}<br/>".format(self.report_data['tickets_data'][0]['ticket_description'])
        self.message += "Number of Followups = {}<br/>".format(len(self.report_data['tickets_data'][0]['followups']))
        self.message += "Followups = <br/>"
        for item in self.report_data['tickets_data'][0]['followups']:
            self.message += "*********************************<br/>"
            self.message += item['content']
            self.message += "<br/>*********************************<br/>"
        self.message += """<i class="fa fa-smile-o"></i>   <i class="fa fa-meh-o" aria-hidden="true"></i>  <i class="fa fa-frown-o" aria-hidden="true"></i>"""
        self.message += "</body></html>"
        print self.message
        with open('file.html', 'w') as fh:
            fh.write(self.message)

    def send_report(self):
        print "Hi Inside send Report"
        server.starttls()
        server.login(my_email_id, my_password)
        msg = MIMEMultipart('alternative')
        msg['From'] = my_email_id
        msg['To'] = "bhandarisudhanshu13496@gmail.com"
        msg['Subject'] = "Test Mail Helpdesk"
        msg.attach(MIMEText(self.message, 'html'))
        server.sendmail(my_email_id, "bhandarisudhanshu13496@gmail.com", msg.as_string())
        del msg


def main():
    print "Hello World"
    HelpDeskReport()


if __name__ == '__main__':
    main()
