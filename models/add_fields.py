from odoo import _, models, fields, api


class ProductImage(models.Model):
    _name = "product_table_block_image_model"
    _description = "Product Table Block Image"
    image = fields.Binary(string="Image", attachment=True)
    sequence = fields.Integer(string="Sequence", index=True)
    product_table_block_id = fields.Many2one(
        "product_table_block_description", string="Product Block"
    )


class ProductTable(models.Model):
    _name = "product_table_block_description"
    product_table_block_id = fields.Many2one("product.template", string="Products")
    product_model_images = fields.One2many(
        "product_table_block_image_model", "product_table_block_id", string="Add Image"
    )

    # binary_fields = fields.Many2many("ir.attachment" , mimetype= "image/webp", string ="Multi Image Upload" , help="If that not a image type , it can be make problem !")

    # product_table_block_id = fields.Many2one(
    #     "product.template", string="Product FK block title ID", compute='_compute_product_table_block_id', store=True)

    product_table_block_type = fields.Selection(
        [
            ("image_right", "Image Right"),  # Lựa chọn 1: Image Right
            ("image_left", "Image Left"),  # Lựa chọn 2: Image Left
            ("picture", "Picture"),  # Lựa chọn 3: Banner
            ("gallery", "Gallery"),
            ("image_wall", "Image Wall"),
        ],
        string="Block Type",
        default="image_right",
    )
    product_table_block_title = fields.Char(string="Title")
    product_block_description = fields.Text(string="Description")
    product_block_title_text_color = fields.Char(string="Title Text Color")
    product_block_description_text_color = fields.Char(string="Description Text Color")
    product_block_sub_description_text_color =fields.Char(string="Sub Description Text Color")

    product_block_background = fields.Char(string="Background Color")
    product_table_block_sub_description = fields.Text(string="Sub Description")

    product_table_block_content_align = fields.Selection(
        [
            ("top", "Align Top"),
            ("middle", "Align Middle"),
            ("bot", "Align Bottom"),
            ("stretch", "Align Stretch "),
        ],
        string="Align Content",
        default="middle",
    )
  
    product_table_block_content_height = fields.Selection(
        [
            ("auto", "Auto"),
            ("half", "Half Display"),
            ("full", "Full Display"),
        ],
        string="Block Height",
        default="auto",
    )
    product_table_block_content_width = fields.Selection(
        [
            ("small", "Small"),
            ("regular", "Regular"),
            ("full", "Full"),
        ],
        string="Content Width",
        default="regular",
    )
    product_table_block_button = fields.Boolean(string="Button")
    product_table_block_button_title = fields.Char(string="Button Title")
    product_table_block_button_link = fields.Char(string="Button Link")
    product_table_block_button_color = fields.Selection(
        [
            ("primary", "Primary"),
            ("secondary", "Secondary"),
            ("success", "Success"),
            ("danger", "Danger"),
            ("warning", "Warning"),
            ("info", "Info"),
            ("light", "Light"),
            ("dark", "Dark"),
        ],
        string="Button Color",
        default="primary",
    )
    product_table_block_hide_desktop = fields.Boolean(string="Hide on Desktop")
    product_table_block_hide_ipad = fields.Boolean(string="Hide on iPad")
    product_table_block_hide_phone = fields.Boolean(string="Hide on Phone")

    product_table_block_image_shape = fields.Selection(
        [
            ("none", "None"),
            ("origin1", "Origin 1"),
            ("bottom_line", "Bottom Line"),
            ("blue_gradiant", "Blue Gradiant"),
            ("arrow_bot", "Arrow Bottom"),
            ("arrow_top", "Arrow Top"),
            ("wave", "Wave"),
            ("right_wave", "Right Wave"),
            ("left_wave", "Left Wave"),
            ("spider_web", "Spider Web"),
            ("grid", "Grid"),
        ],
        string="Background Shape",
        default="none",
    )
    product_table_block_image = fields.Image(string="Image")
    product_table_block_image2 = fields.Image(string="Image 2")
    product_table_block_image3 = fields.Image(string="Image 3")
    sequence = fields.Integer(string="Sequence", index=True)

    # @api.depends('product_table_block_type')
    # def _compute_product_table_block_id(self):
    #     for record in self:
    #         if record.product_table_block_type != 'image_right':
    #             record.product_table_block_id = False  # Ẩn trường khi không phải là 'image_right'


class ProductTableView(models.Model):
    _inherit = "product.template"
    product_template_id = fields.One2many(
        "product_table_block_description",
        "product_table_block_id",
        string="Description Block",
    )

    # checkAddBanner = fields.Boolean(string="Add banner")

    # @api.model
    # def create(self, vals):
    #     # Tạo một đối tượng mới của product.template
    #     product_template = super(ProductTableView, self).create(vals)
    #     # Lấy danh sách các dòng trong product_template
    #     lines = product_template.product_template_id
    #     # Thiết lập giá trị cho trường sl_no của từng dòng
    #     for index, line in enumerate(lines, start=1):
    #         line.sl_no = index
    #     return product_template

    # @api.onchange('product_template_id')
    # def _onchange_product_template_id(self):
    #     # Tính toán và gán lại giá trị cho trường sl_no khi có sự thay đổi trong product_template_id
    #     for index, line in enumerate(self.product_template_id, start=1):
    #         line.sl_no = index

    checkAddDetail = fields.Boolean(string="Description Blocks")
    titleArr = fields.Text() 
    descriptionArr = fields.Text()
    imageArr = fields.Binary()

    @api.model
    def create(self, values):
        if "checkAddDetail" in values:
            values["checkAddDetail"] = values.pop("checkAddDetail")
        return super(ProductTableView, self).create(values)

    def write(self, values):
        if "checkAddDetail" in values:
            values["checkAddDetail"] = values.pop("checkAddDetail")
        return super(ProductTableView, self).write(values)
