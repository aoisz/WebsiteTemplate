from odoo import _, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request

class ProductPreview(models.Model):
    _inherit = "product.template"
    def refesh_iframe(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }

    website_preview_url = fields.Html("Preview", sanitize = False, compute = '_get_html')

    def _get_html(self):
        for product in self: 
            url = f"{request.httprequest.host_url}shop/{slug(product)}"
            product.website_preview_url = f'<iframe src="{url}" width="100%" height="100%" class="shadow" id="product_preview_iframe"><p>Your browser does not support iframes.</p></iframe>'
