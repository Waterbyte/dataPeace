from webargs import fields

from backendAPI import constants

argsGetUsers = {
    constants.Filter.PAGE.name: fields.Int(
    ),
    constants.Filter.LIMIT.name: fields.Int(
    ),
    constants.Filter.NAME.name: fields.Str(
    ),
    constants.Filter.SORT.name: fields.Str(
    )
}

argsPostUsers = {

}
