from odoo import http
from odoo.http import request
import logging
import random
import string

class CallbarXMLController(http.Controller):

    @http.route('/callbar/get-config', type='http', auth='user')
    def download_callbar_config(self):
        logger = logging.getLogger(__name__)
        
        username = 'antbuddy_system'
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        db_name = request.db
        db_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url') or 'localhost'

        existing_user = request.env['res.users'].sudo().search([('login', '=', username)], limit=1)
        logger.info("🔍 Existing user: %s", existing_user.login)

        if existing_user:
            existing_user.sudo().write({'password': password})
            user = existing_user
        else:
            orphan_partners = request.env['res.partner'].sudo().search([
                ('name', '=', 'Antbuddy System'),
                ('user_ids', '=', False)
            ])
            if orphan_partners:
                orphan_partners.unlink()

            user = request.env['res.users'].sudo().create({
                'name': 'Antbuddy System',
                'login': username,
                'password': password,
                'active': True,
            })
            logger.info("✅ Created new user: %s", user)


        content = f"""<?xml version="1.0"?>
<config>
    <db_name>{db_name}</db_name>
    <username>{username}</username>
    <password>{password}</password>
    <db_url>{db_url}</db_url>
</config>"""

        return request.make_response(
            content,
            headers=[
                ('Content-Type', 'application/xml'),
                ('Content-Disposition', 'attachment; filename="callbar_config.xml"')
            ]
        )
