#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:56:01 2018

@author: su.bhandari
"""
import datetime
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.dialects.mysql import TINYINT, LONGTEXT
from sqlalchemy.orm import relationship, backref
from App import *

class GlpiAlerts(db.Model):
    __tablename__ = 'glpi_alerts'
    id = db.Column(db.Integer, primary_key=True)
    itemtype = db.Column(db.String(100), nullable=False, default=0)
    items_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (UniqueConstraint('itemtype', 'items_id', 'type', name='unicity'),)



class GlpiBookmarks(db.Model):
    __tablename__ = 'glpi_bookmarks'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=True)
    type = db.Column(db.Integer, nullable=False, default=0)
    itemtype = db.Column(db.String(100), nullable=False)
    users_id = db.Column(db.Integer, nullable=False)
    is_private = db.Column(TINYINT, nullable=False, default=-1)
    entities_id = db.Column(db.Integer, nullable=False, default=-1)
    is_recursive = db.Column(TINYINT, nullable=False, default=0)
    path = db.Column(db.String(255), nullable=True)
    query = db.Column(LONGTEXT)

class GlpiTickets(db.Model):
    __tablename__ = 'glpi_tickets'
    id = db.Column(db.Integer, primary_key=True, nullable=False, default=0)
    entities_id = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(255), nullable=True, default=None)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    closedate = db.Column(db.DateTime, default=None, nullable=True)
    solvedate = db.Column(db.DateTime, default=None, nullable=True)
    date_mod = db.Column(db.DateTime, default=None, nullable=True)
    users_id_lastupdater = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=1)
    users_id_recipient = db.Column(db.Integer, nullable=False, default=0)
    requesttypes_id = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(LONGTEXT)
    urgency = db.Column(db.Integer, nullable=False, default=1)
    impact = db.Column(db.Integer, nullable=False, default=1)
    priority = db.Column(db.Integer, nullable=False, default=1)
    itilcategories_id = db.Column(db.Integer, nullable=False, default=0)
    type = db.Column(db.Integer, nullable=False, default=1)
    solutiontypes_id = db.Column(db.Integer, nullable=False, default=0)
    solution = db.Column(LONGTEXT)
    global_validation = db.Column(db.Integer, nullable=False, default=1)
    slas_id = db.Column(db.Integer, nullable=False, default=0)
    slalevels_id = db.Column(db.Integer, nullable=False, default=0)
    due_date = db.Column(db.DateTime, default=None, nullable=True)
    begin_waiting_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    sla_waiting_duration = db.Column(db.Integer, nullable=False, default=0)
    waiting_duration = db.Column(db.Integer, nullable=False, default=0)
    close_delay_stat = db.Column(db.Integer, nullable=False, default=0)
    solve_delay_stat = db.Column(db.Integer, nullable=False, default=0)
    takeintoaccount_delay_stat = db.Column(db.Integer, nullable=False, default=0)
    actiontime = db.Column(db.Integer, nullable=False, default=0)
    is_deleted = db.Column(TINYINT, nullable=False)
    locations_id = db.Column(db.Integer, nullable=False, default=0)
    validation_percent = db.Column(db.Integer, nullable=False, default=0)
    glpi_followup = relationship("GlpiTicketFollowups", backref=backref("followup_id", uselist=False))

class GlpiUsers(db.Model):
    __tablename__ = 'glpi_users'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=True, default=None)
    password = db.Column(db.String(255), nullable=True, default=None)
    phone = db.Column(db.String(255), nullable=True, default=None)
    phone2 = db.Column(db.String(255), nullable=True, default=None)
    mobile = db.Column(db.String(255), nullable=True, default=None)
    realname = db.Column(db.String(255), nullable=True, default=None)
    firstname = db.Column(db.String(255), nullable=True, default=None)
    locations_id = db.Column(db.Integer, nullable=False, default=0)
    language = db.Column(db.CHAR(10), nullable=True, default=None)
    use_mode = db.Column(db.Integer, nullable=False, default=0)
    list_limit = db.Column(db.Integer, nullable=True, default=None)
    is_active = db.Column(TINYINT, nullable=False, default=1)
    comment = db.Column(db.Text)
    auths_id = db.Column(db.Integer, nullable=False, default=0)
    authtype = db.Column(db.Integer, nullable=False, default=0)
    last_login = db.Column(db.DateTime, nullable=True, default=None)
    date_mod = db.Column(db.DateTime, nullable=True, default=None)
    date_sync = db.Column(db.DateTime, nullable=True, default=None)
    is_deleted = db.Column(TINYINT, nullable=False, default=0)
    profiles_id = db.Column(db.Integer, nullable=False, default=0)
    entities_id = db.Column(db.Integer, nullable=False, default=0)
    usertitles_id = db.Column(db.Integer, nullable=False, default=0)
    usercategories_id = db.Column(db.Integer, nullable=False, default=0)
    date_format = db.Column(db.Integer, nullable=True, default=None)
    number_format = db.Column(db.Integer, nullable=True, default=None)
    names_format = db.Column(db.Integer, nullable=True, default=None)
    csv_delimiter = db.Column(db.CHAR(1), nullable=True, default=None)
    is_ids_visible = db.Column(TINYINT, nullable=True, default=None)
    use_flat_dropdowntree = db.Column(TINYINT, nullable=True, default=None)
    show_jobs_at_login = db.Column(TINYINT, nullable=True, default=None)
    priority_1 = db.Column(db.CHAR(20), nullable=True, default=None)
    priority_2 = db.Column(db.CHAR(20), nullable=True, default=None)
    priority_3 = db.Column(db.CHAR(20), nullable=True, default=None)
    priority_4 = db.Column(db.CHAR(20), nullable=True, default=None)
    priority_5 = db.Column(db.CHAR(20), nullable=True, default=None)
    priority_6 = db.Column(db.CHAR(20), nullable=True, default=None)
    followup_private = db.Column(TINYINT, nullable=True, default=None)
    task_private = db.Column(TINYINT, nullable=True, default=None)
    default_requesttypes_id = db.Column(db.Integer, nullable=True, default=None)
    password_forget_token = db.Column(db.CHAR(40), nullable=True, default=None)
    password_forget_token_date = db.Column(db.DateTime, nullable=True, default=None)
    user_dn = db.Column(db.Text)
    registration_number = db.Column(db.String(255), nullable=True, default=None)
    show_count_on_tabs = db.Column(TINYINT, nullable=True, default=None)
    refresh_ticket_list = db.Column(db.Integer, nullable=True, default=None)
    set_default_tech = db.Column(TINYINT, nullable=True, default=None)
    personal_token = db.Column(db.String(255), nullable=True, default=None)
    personal_token_date = db.Column(db.DateTime, nullable=True, default=None)
    display_count_on_home = db.Column(db.Integer, nullable=True, default=None)
    notification_to_myself = db.Column(TINYINT, nullable=True, default=False)
    duedateok_color = db.Column(db.String(255), nullable=True, default=None)
    duedatewarning_color = db.Column(db.String(255), nullable=True, default=None)
    duedatecritical_color = db.Column(db.String(255), nullable=True, default=None)
    duedatewarning_less = db.Column(db.Integer, nullable=True, default=None)
    duedatecritical_less = db.Column(db.Integer, nullable=True, default=None)
    duedatewarning_unit = db.Column(db.String(255), nullable=True, default=None)
    duedatecritical_unit = db.Column(db.String(255), nullable=True, default=None)
    display_options = db.Column(db.Text)
    is_deleted_ldap = db.Column(TINYINT, nullable=False, default=0)
    pdffont = db.Column(db.String(255), nullable=True, default=None)
    picture = db.Column(db.String(255), nullable=True, default=None)
    begin_date = db.Column(db.DateTime, nullable=True, default=None)
    end_date = db.Column(db.DateTime, nullable=True, default=None)
    keep_devices_when_purging_item = db.Column(TINYINT, nullable=True, default=None)
    privatebookmarkorder = db.Column(LONGTEXT)
    backcreated = db.Column(TINYINT, nullable=True, default=None)
    task_state = db.Column(db.Integer, nullable=True, default=None)
    layout = db.Column(db.CHAR(20), nullable=True, default=None)
    palette = db.Column(db.CHAR(20), nullable=True, default=None)
    ticket_timeline = db.Column(TINYINT, nullable=True, default=None)
    ticket_timeline_keep_replaced_tabs = db.Column(TINYINT, nullable=True, default=None)
    __table_args__ = (UniqueConstraint('name', name='unicity'),)


class GlpiTicketFollowups(db.Model):
    __tablename__ = 'glpi_ticketfollowups'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    tickets_id = db.Column(db.Integer, db.ForeignKey('glpi_tickets.id'), nullable=False, default=0)
    date = db.Column(db.DateTime, nullable=True)
    users_id = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(LONGTEXT)
    is_private = db.Column(TINYINT, nullable=False, default=0)
    requesttypes_id = db.Column(db.Integer, nullable=False, default=0)

class GlpiItilCategories(db.Model):
    __tablename__ = 'glpi_itilcategories'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    entities_id = db.Column(db.Integer, nullable=False, default=0)
    is_recursive = db.Column(TINYINT, nullable=False, default=0)
    itilcategories_id = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(255), nullable=True, default=None)
    completename = db.Column(db.Text)
    comment = db.Column(db.Text)
    level = db.Column(db.Integer, nullable=False, default=0)
    knowbaseitemcategories_id = db.Column(db.Integer, nullable=False, default=0)
    users_id = db.Column(db.Integer, nullable=False, default=0)
    groups_id = db.Column(db.Integer, nullable=False, default=0)
    ancestor_cache = db.column(LONGTEXT)
    sons_cache = db.Column(LONGTEXT)
    is_helpdeskvisible = db.Column(TINYINT, nullable=False, default=1)
    tickettemplates_id_incident = db.Column(db.Integer, nullable=False, default=0)
    tickettemplates_id_demand = db.Column(db.Integer, nullable=False, default=0)
    is_incident = db.Column(db.Integer, nullable=False, default=1)
    is_request = db.Column(db.Integer, nullable=False, default=1)
    is_change = db.Column(db.Integer, nullable=False, default=1)


class GlpiSLAs(db.Model):
    __tablename__ = 'glpi_slas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=True)
    entities_id = db.Column(db.Integer, nullable=False, default=0)
    is_recursive = db.Column(TINYINT, nullable=True, default=0)
    comment = db.Column(db.Text)
    resolution_time = db.Column(db.Integer, nullable=False)
    calendars_id = db.Column(db.Integer, nullable=False, default=0)
    date_mod = db.Column(db.DateTime, nullable=True)
    definition_time = db.Column(db.String(255), nullable=True)
    end_of_working_day = db.Column(TINYINT, nullable=False, default=0)

class GlpiRatings(db.Model):
    __tablename__ = 'glpi_ratings'
    rating_id = db.Column(db.Integer, nullable=False)
    ticket_id = db.Column(db.Integer,  primary_key=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # __table_args__ = (UniqueConstraint("rating_id","ticket_id"))

# GlpiRatings.__table__.create(engine)