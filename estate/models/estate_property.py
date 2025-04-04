
from odoo import fields, models


orientation_choices = [
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
]


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"
    _order = "sequence, create_date DESC"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Text(string="Postcode")
    date_availability = fields.Date(string="Date Availability")
    expected_price = fields.Integer(string="Expected Price", required=True)
    selling_price = fields.Integer(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=orientation_choices
    )

    # def _compute_post_count(self):
    #     for record in self:
    #         record.post_count = self.env['estate.post'].search_count(
    #             [('forum_id', '=', record.id)])
