# coding: utf-8


from openerp import fields, models, api, _


class Teachers(models.Model):
    _name='teachers'

    name = fields.Char(size=10)
    age = fields.Integer(required=True)

    @api.model
    def create(self, values):
        return super(Teachers, self).create(values)
