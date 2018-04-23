# -*- encoding: utf-8 -*-
##############################################################################
#
#    Fiscal Company for Point Of Sale Module for Odoo
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

{
    'name': 'CIS - Point Of Sale Fiscal Company',
    'version': '1.0',
    'category': 'CIS',
    'description': """
Manage specific account move for cooperative
============================================

TODO: PROBLEM.


Copyright, Author and Licence :
-------------------------------
    * Copyright : 2013-Today, Groupement Régional Alimentaire de Proximité;
    * Author :
        * Julien WESTE;
        * Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence : AGPL-3 (http://www.gnu.org/licenses/)
    """,
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'base_fiscal_company',
        'account_voucher_fiscal_company',
        'product_fiscal_company',
        'point_of_sale',
    ],
    'data': [
        'security/ir_rule.xml',
        'views/view_pos_config.xml',
    ],
    'demo': [
        'demo/ir_sequence.xml',
        'demo/stock_picking_type.xml',
        'demo/pos_config.xml',
        'demo/product_product.xml',
    ],
    'installable': True,
    'auto_install': True,
}
