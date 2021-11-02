# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class spf_course(models.Model):
#     _name = 'spf_course.spf_course'
#     _description = 'spf_course.spf_course'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import fields, models


class Student(models.Model):
    _name = "Student"

    name = fields.Char(string="name", required=True)
    surname = fields.Char(string="surname", required=True)
    enrolled_year = fields.Integer(required=True)
    birth_date = fields.Date()
    index_number = fields.Char('Index number xx/xxxx', string="field of study")


class Teacher(models.Model):
    _name = "Teacher"

    name = fields.Char(string="name", required=True)
    surname = fields.Char(string="surname", required=True)
    email = fields.Char(string="email", required=True)
    courses = fields.Char('Courses Attended')


class Courses(models.Model):
    _name = "Course"

    teacher = fields.One2many('Teacher',string="Teacher")
    name = fields.Char(string="name",required=True)
    field_of_study = fields.Char(string="field of study")
    semester = fields.Integer('Semester')
    state = fields.Char()
    description = fields.Char(string="Description")
    begining_date = fields.Date()
    end_date = fields.Date()
    students = fields.Many2one('Student', 'Course')