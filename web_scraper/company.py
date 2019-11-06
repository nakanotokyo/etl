__all__ = ['company']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['data'])
var.put('data', Js({'fuente':Js('Web Service'),'empresa':Js('EDENOR'),'totalUsuariosSinSuministro':Js('1.484'),'totalUsuariosConSuministro':Js('2.997.007'),'ultimaActualizacion':Js('13:35'),'totalUsuariosAyer':Js('54.468'),'cortesPreventivos':Js([]),'cortesProgramados':Js([Js({'partido':Js('LA MATANZA'),'localidad':Js('RAMOS MEJIA'),'subestacion_alimentador':Js('164-SAN JUSTO / R:164-TR1 / 164-5514'),'usuarios':Js('84'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('VIRREY DEL PINO'),'subestacion_alimentador':Js('353-EL PINO / R:353-TR1 / 353-5517'),'usuarios':Js('7'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('VIRREY DEL PINO'),'subestacion_alimentador':Js('353-EL PINO / R:353-TR2 / 353-5524'),'usuarios':Js('68'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('MALVINAS ARGENTINAS'),'localidad':Js('EL TRIANGULO'),'subestacion_alimentador':Js('252-TORTUGUITAS / R:252-TR1 / 252-5547'),'usuarios':Js('22'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('MALVINAS ARGENTINAS'),'localidad':Js('PABLO NOGUES'),'subestacion_alimentador':Js('252-TORTUGUITAS / R:252-TR1 / 252-5547'),'usuarios':Js('239'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('MARCOS PAZ'),'localidad':Js('MARCOS PAZ'),'subestacion_alimentador':Js('353-EL PINO / R:353-TR1 / 353-5517'),'usuarios':Js('2'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('MORENO'),'localidad':Js('LA REJA'),'subestacion_alimentador':Js('163-LA REJA / R:163-TR1 / 163-5515'),'usuarios':Js('289'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('PILAR'),'localidad':Js('VILLA ROSA'),'subestacion_alimentador':Js('51-MATHEU / R:51-TR4 / 51-5481'),'usuarios':Js('122'),'normalizacion':Js('Sin datos')})]),'cortesServicioMedia':Js([Js({'partido':Js('GRAL SAN MARTIN'),'localidad':Js('C JARDIN EL LIBERTADOR'),'subestacion_alimentador':Js('262-ROTONDA / R:262-TR1 / 262-5511'),'usuarios':Js('109'),'normalizacion':Js('Sin datos')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('LA TABLADA'),'subestacion_alimentador':Js('162-TAPIALES / R:162-TR1 / 162-5514'),'usuarios':Js('406'),'normalizacion':Js('Sin datos')})]),'cortesComunicados':Js([]),'cortesServicioBaja':Js([Js({'partido':Js('CAPITAL FEDERAL'),'localidad':Js('CHACARITA'),'usuarios':Js('21')}), Js({'partido':Js('CAPITAL FEDERAL'),'localidad':Js('PALERMO'),'usuarios':Js('14')}), Js({'partido':Js('CAPITAL FEDERAL'),'localidad':Js('VILLA PUEYRRED?N'),'usuarios':Js('10')}), Js({'partido':Js('GRAL RODRIGUEZ'),'localidad':Js('GRAL RODRIGUEZ'),'usuarios':Js('21')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('CIUDAD EVITA'),'usuarios':Js('12')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('TAPIALES'),'usuarios':Js('4')}), Js({'partido':Js('LA MATANZA'),'localidad':Js('VIRREY DEL PINO'),'usuarios':Js('1')}), Js({'partido':Js('MORENO'),'localidad':Js('TRUJUI'),'usuarios':Js('16')}), Js({'partido':Js('PILAR'),'localidad':Js('LA LONJA'),'usuarios':Js('10')}), Js({'partido':Js('PILAR'),'localidad':Js('VILLA ROSA'),'usuarios':Js('17')}), Js({'partido':Js('SAN ISIDRO'),'localidad':Js('BOULOGNE'),'usuarios':Js('4')}), Js({'partido':Js('SAN ISIDRO'),'localidad':Js('MARTINEZ'),'usuarios':Js('6')})])}))


# Add lib to the module scope
company = var.to_python()