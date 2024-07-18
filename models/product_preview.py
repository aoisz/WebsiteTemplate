from odoo import _, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request

class ProductPreview(models.Model):
    _inherit = "product.template"

    website_preview_url = fields.Html("Preview", sanitize = False, compute = '_get_html')
    mobile_view = fields.Boolean("Mobile", default=False)

    def toggle_publish(self):
        for record in self:
            record.website_published = not record.website_published
        return True

    def refesh_iframe(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }

    def change_view_mode(self):
        id = self.env.context.get("id")
        for product in self:
            if(product.id == id):
                product.mobile_view = not product.mobile_view
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload'
        # }

    def _get_html(self):
        for product in self:
            url = f"{request.httprequest.host_url}shop/{slug(product)}"
            if(product.mobile_view == True):
                product.website_preview_url = f'<div class="smartphone"><div class="content"><iframe src="{url}" class="shadow" id="preview_iframe"><p>Your browser does not support iframes.</p></iframe></div></div>'
            else:
                product.website_preview_url = f'<iframe src="{url}" class="shadow" id="product_preview_iframe"><p>Your browser does not support iframes.</p></iframe>'
