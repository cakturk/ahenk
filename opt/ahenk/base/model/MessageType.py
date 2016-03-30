#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>
from enum import Enum

class MessageType(Enum):
    TASK_STATUS = 'TASK_STATUS'
    REGISTER = 'REGISTER'
    UNREGISTER = 'UNREGISTER'
    REGISTER_LDAP = 'REGISTER_LDAP'
    GET_POLICIES = 'GET_POLICIES'
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'
    POLICY_STATUS = 'POLICY_STATUS'
    EXECUTE_POLICY = 'EXECUTE_POLICY'
    EXECUTE_TASK = 'EXECUTE_TASK'
    MOVE_FILE = 'MOVE_FILE'
    REQUEST_FILE = 'REQUEST_FILE'
    EXECUTE_SCRIPT = 'EXECUTE_SCRIPT'
