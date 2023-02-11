JAZZMIN_SETTINGS = {
    "site_logo": "img/logo1.png",
    "site_title": "Core Inventory",
    "site_header": "Core Inventory",
    "site_brand": "Core Inventory",
    "welcome_sign": "Core Inventory",
    "copyright": "Core Inventory",
    "show_ui_builder": False,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        "BillingProfiles.billingprofile":"fas fa-credit-card",
        "Orders.order":"fas fa-box",
        "Products.product":"fas fa-lemon",
        "PromoCodes.promocode":"fas fa-tags",
        "Providers.supplier":"fas fa-truck",
        "ShippingAddresses.shippingaddress":"fas fa-map",
        "Users.user":"fas fa-users",
        "Sales.sale":"fas fa-store",
        "Purchases.purchase":"fas fa-plus"
    },
    # Icons that are used when one is not manually specified

    "related_modal_active": True,

    "topmenu_links": [
        # external url that opens in a new window (Permissions can be added)
        {"name": "Ir al catálogo", "url": "index", "permissions": ["auth.view_user"], "new_window": True},
    ],
    "custom_css": "css/custom_admin.css"
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    # "accent": "accent-danger",
    # "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    # "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "journal",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False,
    "related_modal_active": True,
}