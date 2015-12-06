# coding: utf-8


from openerp import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        teachers = http.request.env['teachers']
        return http.request.render('academy.index', {
            'teachers': teachers.search([])
        })

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        #return '<h1>{}</h1>'.format(name)
        return http.request.render('academy.biography', {
            'person': teacher
        })
