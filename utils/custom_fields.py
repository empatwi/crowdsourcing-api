from flask_restplus import fields

class NullableBoolean(fields.Boolean):
    __schema_type__ = ['boolean', 'null']
    __schema_example__ = "Nullable boolean"