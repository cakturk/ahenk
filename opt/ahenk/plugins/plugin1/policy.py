#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>


def handle_policy(profile_data,context):
    context.put('data','dataa')
    context.put('content_type','type')
    print("This is policy file - plugin 1")
