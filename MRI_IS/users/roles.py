from rolepermissions.roles import AbstractUserRole

class Doctor(AbstractUserRole):
    available_permissions = {
        'create_inspection': True,
    }

class Director(AbstractUserRole):
    available_permissions = {
        'create_clinic': True,
    }
