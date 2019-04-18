from webargs import fields

from backendAPI import constants

argsGetUsers = {
    constants.Filter.page.name: fields.Int(allow_none=None),
    constants.Filter.limit.name: fields.Int(allow_none=None, missing=5),
    constants.Filter.name.name: fields.Str(allow_none=None),
    constants.Filter.sort.name: fields.Str(allow_none=None)
}

argsPostUsers = {
    constants.UserEntry.id.name: fields.Int(required=True),
    constants.UserEntry.first_name.name: fields.Str(required=True),
    constants.UserEntry.last_name.name: fields.Str(required=True),
    constants.UserEntry.company_name.name: fields.Str(required=True),
    constants.UserEntry.city.name: fields.Str(required=True),
    constants.UserEntry.state.name: fields.Str(required=True),
    constants.UserEntry.zip.name: fields.Int(required=True),
    constants.UserEntry.email.name: fields.Str(required=True),
    constants.UserEntry.web.name: fields.Str(required=True),
    constants.UserEntry.age.name: fields.Int(required=True)
}

argsUpdateUser = {
    constants.UserEntry.first_name.name: fields.Str(allow_none=None),
    constants.UserEntry.last_name.name: fields.Str(allow_none=None),
    constants.UserEntry.age.name: fields.Int(allow_none=None)
}
