#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>

from base.plugin.AbstractCommand import AbstractCommand

class MySamplePlugin(AbstractCommand):
    """docstring for MySamplePlugin"""
    def __init__(self, task):
        super(MySamplePlugin, self).__init__()
        self.task = task

    def handle_task(self):
        print("This is command 1 ")
        print("parameter map="+self.task.parameter_map)


def handle_task(task,context):
    # Do what ever you want here
    # You can create command class but it is not necessary
    # You can use directly this method.
    context.put('my_data_name','my data')
    myPlugin = MySamplePlugin(task)
    myPlugin.handle_task()
