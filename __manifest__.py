{
    # docker compose stop ; docker compose down ; docker compose up
    # Tên module
    "name": "Details Table Block",
    "version": "1.0",
    # Loại module
    "category": "Website",
    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    #### Chấp nhận số âm
    "sequence": 3,
    # Mô tả module
    "summary": "Model used to configure the product",
    "description": "Model create notebook and table used to write description of the product",
    "images": ["static/description/icon.jpg"],
    # Module dựa trên các category nào
    # Khi hoạt động, category trong 'depends' phải được install
    ### rồi module này mới đc install
    "depends": ["base", "product", "website_sale"],
    # Module có được phép install hay không
    # Nếu bạn thắc mắc nếu tắt thì làm sao để install
    # Bạn có thể dùng 'auto_install'
    "installable": True,
    "auto_install": False,
    "application": True,
    # Import các file cấu hình
    # Những file ảnh hưởng trực tiếp đến giao diện (không phải file để chỉnh sửa giao diện)
    ## hoặc hệ thống (file group, phân quyền)
    "data": [
        "security/security.xml",
        "views/view_product_template_add_table.xml",
        "views/product_table.xml",
        # "views/product_table_modal.xml",
        # "views/menu_item.xml",
        "security/ir.model.access.csv",
        "views/custom_block_form.xml",
        "views/preview_product_template.xml",
    ],
    "assets": {
        "web.assets_backend": [
            'WebsiteTemplate/static/scss/custom_chatter_thread.scss',
        ],
    },
    # Import các file cấu hình (chỉ gọi từ folder 'static')
    # Những file liên quan đến
    ## + các class mà hệ thống sử dụng
    ## + các chỉnh sửa giao diện
    ## + t
    "license": "LGPL-3",
}
