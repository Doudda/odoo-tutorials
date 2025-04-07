
from datetime import timedelta
from odoo import fields, models


orientation_choices = [
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
]

state_choices = [
    ('new', 'New'),
    ('offer_received', 'Offer Received'),
    ('offer_accepted', 'Offer Accepted'),
    ('sold', 'Sold'),
    ('canceled', 'Canceled'),
]


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Text(string="Postcode")
    date_availability = fields.Date(
        string="Date Availability", default=fields.Date.today() + timedelta(days=90))
    expected_price = fields.Integer(string="Expected Price", required=True)
    selling_price = fields.Integer(string="Selling Price", readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=orientation_choices
    )
    state = fields.Selection(
        string="State",
        selection=state_choices,
        default='new'
    )
    active = fields.Boolean(string="Active", default=True)
