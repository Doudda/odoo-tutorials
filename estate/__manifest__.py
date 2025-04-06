{
    'name': "Estate App",

    'description': """
        My new app called Estate App"
    """,

    'installable': True,
    'application': True,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],

}
