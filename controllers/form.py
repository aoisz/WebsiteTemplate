# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import json
from urllib.parse import urlparse, parse_qs

import requests
from werkzeug import urls
from werkzeug.exceptions import Forbidden
from werkzeug.utils import redirect

from odoo import _, http, models
from odoo.http import request
from odoo.exceptions import ValidationError
from odoo.tools import html_escape

_logger = logging.getLogger(__name__)


class MyController(http.Controller):

    @http.route(
        "/website/form/", type="http", auth="public", methods=["POST"], website=True
    )
    def process_form(self, **post):
        # Lấy dữ liệu từ form
        type = post.get("type")
        title = post.get("title")
        description = post.get("description")
        image1 = request.httprequest.files.get("image")
        image2 = request.httprequest.files.get("image2")
        image3 = request.httprequest.files.get("image3")

        # Tạo bản ghi mới cho đối tượng ProductTable
        product_table = (
            request.env["product_table_block_description"]
            .sudo()
            .create(
                {
                    "product_table_block_type": type,
                    "product_table_block_title": title,
                    "product_table_block_description": description,
                    # Gán các giá trị hình ảnh ở đây
                }
            )
        )

        return "Form submitted successfully!"
