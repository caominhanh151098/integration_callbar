{
    'name': 'CallCenter',
    'version': '2.1.5',
    'category': 'Tools',
    "summary": "Antbuddy softphone",
    'author': 'Antbuddy',
    'website': 'https://www.antbuddy.com',
    'depends': ['web', 'contacts'],
    'assets': {
        'web.assets_common': [
            'integration_callbar/static/src/scss/callbar.scss',
        ],
        'web.assets_backend': [
            'integration_callbar/static/src/js/callbar.js',
            'integration_callbar/static/src/js/callbar_container.js',
            'integration_callbar/static/src/xml/callbar_container_template.xml',
            'integration_callbar/static/src/xml/callbar_systray.xml',
            'integration_callbar/static/src/xml/callbar_phone_field.xml',
        ],
    },
    'data': [
        'views/callbar_configuration_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}