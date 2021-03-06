# -*- encoding: utf-8 -*-
##############################################################################
#
#    Fiscal Company for Account Voucher Module for Odoo
#    Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
#    @author Julien WESTE
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv.orm import Model


class account_voucher(Model):
    _inherit = 'account.voucher'

    def writeoff_move_line_get(
            self, cr, uid, voucher_id, line_total, move_id,
            name, company_currency, current_currency, context=None):
        if context.get('force_company', False):
            del context['force_company']
        return super(account_voucher, self).writeoff_move_line_get(
            cr, uid, voucher_id, line_total, move_id,
            name, company_currency, current_currency, context=context)
