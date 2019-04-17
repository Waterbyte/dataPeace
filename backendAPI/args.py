from webargs import fields, validate

import backendAPI.auth
from backendAPI import constants, utils

argsGetUsers = {

    ############### mandatory ######################

    constants.misc_webargs.PAGE.name: fields.Str(
        
    ),

    constants.misc_webargs.LIMIT.name: fields.Str(
        
    ),
    constants.misc_webargs.NAME.name : fields.Str(
        
    )
}
