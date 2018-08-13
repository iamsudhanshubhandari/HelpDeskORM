#!/usr/bin/env python
from HelpdeskModels import *
from App import *
from flask import request, jsonify

@app.route('/tickets_data', methods=['GET'])
def fetch_ticket_details():
    passed_ticket_id = request.args.get('ticket_id')
    ticket_id = GlpiTickets.query.filter_by(id=passed_ticket_id).first()
    output = []
    ticket_data = {}
    followups = []
    ticket_data['id'] = ticket_id.id
    ticket_data['ticket_subject'] = ticket_id.name
    ticket_data['ticket_description'] = ticket_id.content
    ticket_data['solving_date'] = ticket_id.solvedate
    ticket_data['closing_date'] = ticket_id.closedate
    ticket_data['requested_user_id'] = ticket_id.users_id_recipient
    ticket_data['requester'] = GlpiUsers.query.filter_by(
        id=ticket_id.users_id_recipient).first().firstname + " " + GlpiUsers.query.filter_by(
        id=ticket_id.users_id_recipient).first().realname
    ticket_data['item_type'] = ticket_id.id
    ticket_data['type'] = ticket_id.type
    ticket_data['opening_date'] = ticket_id.date
    ticket_data['status'] = ticket_id.status
    ticket_data['assigned_to_groups'] = GlpiItilCategories.query.filter_by(
        id=ticket_id.itilcategories_id).first().completename
    ticket_data['priority'] = ticket_id.priority
    ticket_data['impact'] = ticket_id.impact
    ticket_data['associated_item'] = ''
    ticket_data['sla'] = GlpiSLAs.query.filter_by(id=ticket_id.slas_id).first().name
    followup_data = GlpiTicketFollowups.query.filter_by(tickets_id=passed_ticket_id).order_by(
        GlpiTicketFollowups.date.desc()).all()
    for i in followup_data:
        followup_dictionary = {}
        followup_dictionary['date'] = i.date
        followup_dictionary['content'] = i.content
        followup_dictionary['users_id'] = i.users_id
        followup_dictionary['users_name'] = GlpiUsers.query.filter_by(
            id=i.users_id).first().firstname + " " + GlpiUsers.query.filter_by(id=i.users_id).first().realname
        followups.append(followup_dictionary)
    ticket_data['followups'] = followups

    output.append(ticket_data)
    return jsonify({'tickets_data': output})

@app.route('/submit_ticket_ratings', methods=['POST'])
def insert_ticket_ratings():
    print "Hello World"

if __name__ == '__main__':
    app.run(debug=True)