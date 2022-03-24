# coding: utf-8
from lxml.builder import unicode
from maxipago.exceptions import ValidationError


class Requester(object):
    def __init__(self, fields, data):
        self.fields = fields
        self.data = data

        self.full_clean()

    def _clean_fields(self):
        for field_name, field_options in self.fields:
            if field_name in self.cleaned_data:
                if hasattr(self, 'clean_{0}'.format(field_name)):
                    value = getattr(self, 'clean_{0}'.format(field_name))
                else:
                    value = self.data.get(field_name)

                self.cleaned_data[field_name] = value

    def _translate_data(self):
        self.translated_data = []
        for field_name, field_options in self.fields:
            if field_name in self.cleaned_data:
                translated_name = field_options.get('translated_name', field_name)
                self.translated_data.append((translated_name, unicode(self.cleaned_data.get(field_name))))

    def full_clean(self):
        self.cleaned_data = {}

        for field_name, field_options in self.fields:
            default = field_options.get('default', None)
            required = field_options.get('required', True)
            blank = field_options.get('blank', False)

            if ('default' not in field_options) and required and (field_name not in self.data):
                raise ValidationError('The field "{0}" is required.'.format(field_name))

            if field_name in self.data or 'default' in field_options:
                if not blank and not self.data.get(field_name, default):
                    raise ValidationError('The field "{0}" can not be empty.'.format(field_name))

                self.cleaned_data[field_name] = self.data.get(field_name, default)

        self._clean_fields()
        self._translate_data()
