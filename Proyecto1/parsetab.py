
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA CORA CORC DECIMAL DIV ENTERO IGUAL LLAA LLAC RAZUL RBLANCO RCAFE RCELESTE RCOLOR RCONTENIDO RCOSENO RDESCRIPCION RDIVISION RESCRIBIR RESTILO RFUNCION RGRIS RINVERSO RMULTIPLICACION RNEGRO RNUMERO ROPERACION ROPERACIONES RPOTENCIA RRAIZ RRESTA RROJO RSENO RSUMA RTAMANIO RTANGENTE RTEXTO RTEXTO2 RTIPO RTIPO2 RTITULO RVERDEinit : instruccionesinstrucciones    : instrucciones instruccion\n                        |   instruccioninstruccion  : INSTIPO\n                    | INSTEXTO\n                    | INSTFUNCION\n                    | INSTESTILOINSTIPO    :   LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLACINSTEXTO   :   LLAA RTEXTO LLAC CADENA LLAA DIV RTEXTO LLACINSTFUNCION    :   LLAA RFUNCION IGUAL RESCRIBIR LLAC instrucciones_2 LLAA DIV RFUNCION LLACINSTESTILO     :   LLAA RESTILO LLAC instrucciones_2 LLAA DIV RESTILO LLACinstrucciones_2 : instrucciones_2 instruccion_2instrucciones_2 :  instruccion_2instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLACinstruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC instruccion_2 : CADENAinstruccion_2 : LLAA RTITULO LLAC ROPERACIONES LLAA DIV RTITULO LLACinstruccion_2 : LLAA RDESCRIPCION LLAC CORA RTEXTO2 CORC LLAA DIV RDESCRIPCION LLACinstruccion_2 : LLAA RCONTENIDO LLAC CORA RTIPO2 CORC LLAA DIV RCONTENIDO LLACinstruccion_2 : LLAA RTITULO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLACinstruccion_2 : LLAA RDESCRIPCION RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLACinstruccion_2 : LLAA RCONTENIDO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLACCOLOR    : RAZUL \n                | RVERDE \n                | RROJO \n                | RNEGRO \n                | RBLANCO \n                | RGRIS \n                | RCELESTE \n                | RCAFEtipo :   RSUMA\n            |   RRESTA\n            |   RMULTIPLICACION\n            |   RDIVISION\n            |   RINVERSO\n            |   RRAIZ\n            |   RPOTENCIA\n            |   RSENO\n            |   RCOSENO\n            |   RTANGENTE\n    '
    
_lr_action_items = {'LLAA':([0,2,3,4,5,6,7,9,14,17,19,20,21,22,24,31,33,45,58,59,60,70,87,88,90,91,96,98,110,112,113,114,126,127,128,129,130,131,],[8,8,-3,-4,-5,-6,-7,-2,18,18,30,-13,-17,32,34,-12,18,68,71,72,73,18,-8,-9,-11,101,106,108,-10,-15,-16,-18,-14,-21,-19,-22,-20,-23,]),'$end':([1,2,3,4,5,6,7,9,87,88,90,110,],[0,-1,-3,-4,-5,-6,-7,-2,-8,-9,-11,-10,]),'RTIPO':([8,43,],[10,66,]),'RTEXTO':([8,44,],[11,67,]),'RFUNCION':([8,89,],[12,100,]),'RESTILO':([8,46,],[13,69,]),'LLAC':([10,11,13,23,26,27,28,29,47,48,49,50,51,52,53,54,55,56,57,66,67,69,100,102,103,104,120,121,122,123,124,125,],[14,15,17,33,36,37,39,41,70,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,87,88,90,110,112,113,114,126,127,128,129,130,131,]),'IGUAL':([12,25,38,40,42,95,97,99,],[16,35,61,63,65,105,107,109,]),'CADENA':([14,15,17,19,20,21,24,31,33,45,70,91,112,113,114,126,127,128,129,130,131,],[21,22,21,21,-13,-17,21,-12,21,21,21,21,-15,-16,-18,-14,-21,-19,-22,-20,-23,]),'RESCRIBIR':([16,],[23,]),'ROPERACION':([18,30,34,68,101,111,],[25,25,25,25,25,120,]),'RNUMERO':([18,30,34,68,92,93,101,],[26,26,26,26,102,103,26,]),'RTITULO':([18,30,34,68,94,101,],[27,27,27,27,104,27,]),'RDESCRIPCION':([18,30,34,68,101,116,],[28,28,28,28,28,122,]),'RCONTENIDO':([18,30,34,68,101,118,],[29,29,29,29,29,124,]),'RCOLOR':([27,28,29,],[38,40,42,]),'DIV':([30,32,34,68,71,72,73,101,106,108,115,117,119,],[43,44,46,89,92,93,94,111,116,118,121,123,125,]),'RSUMA':([35,],[48,]),'RRESTA':([35,],[49,]),'RMULTIPLICACION':([35,],[50,]),'RDIVISION':([35,],[51,]),'RINVERSO':([35,],[52,]),'RRAIZ':([35,],[53,]),'RPOTENCIA':([35,],[54,]),'RSENO':([35,],[55,]),'RCOSENO':([35,],[56,]),'RTANGENTE':([35,],[57,]),'DECIMAL':([36,],[58,]),'ENTERO':([36,105,107,109,],[59,115,117,119,]),'ROPERACIONES':([37,],[60,]),'CORA':([39,41,],[62,64,]),'RAZUL':([61,63,65,],[75,75,75,]),'RVERDE':([61,63,65,],[76,76,76,]),'RROJO':([61,63,65,],[77,77,77,]),'RNEGRO':([61,63,65,],[78,78,78,]),'RBLANCO':([61,63,65,],[79,79,79,]),'RGRIS':([61,63,65,],[80,80,80,]),'RCELESTE':([61,63,65,],[81,81,81,]),'RCAFE':([61,63,65,],[82,82,82,]),'RTEXTO2':([62,],[83,]),'RTIPO2':([64,],[85,]),'RTAMANIO':([74,75,76,77,78,79,80,81,82,84,86,],[95,-24,-25,-26,-27,-28,-29,-30,-31,97,99,]),'CORC':([83,85,],[96,98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,9,]),'INSTIPO':([0,2,],[4,4,]),'INSTEXTO':([0,2,],[5,5,]),'INSTFUNCION':([0,2,],[6,6,]),'INSTESTILO':([0,2,],[7,7,]),'instrucciones_2':([14,17,33,70,],[19,24,45,91,]),'instruccion_2':([14,17,19,24,33,45,70,91,],[20,20,31,31,20,31,20,31,]),'tipo':([35,],[47,]),'COLOR':([61,63,65,],[74,84,86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','analizador_lexico.py',168),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','analizador_lexico.py',173),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','analizador_lexico.py',174),
  ('instruccion -> INSTIPO','instruccion',1,'p_instruccion','analizador_lexico.py',182),
  ('instruccion -> INSTEXTO','instruccion',1,'p_instruccion','analizador_lexico.py',183),
  ('instruccion -> INSTFUNCION','instruccion',1,'p_instruccion','analizador_lexico.py',184),
  ('instruccion -> INSTESTILO','instruccion',1,'p_instruccion','analizador_lexico.py',185),
  ('INSTIPO -> LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC','INSTIPO',8,'p_instruccionTipo','analizador_lexico.py',189),
  ('INSTEXTO -> LLAA RTEXTO LLAC CADENA LLAA DIV RTEXTO LLAC','INSTEXTO',8,'p_instruccionTexto','analizador_lexico.py',193),
  ('INSTFUNCION -> LLAA RFUNCION IGUAL RESCRIBIR LLAC instrucciones_2 LLAA DIV RFUNCION LLAC','INSTFUNCION',10,'p_instruccionFuncion','analizador_lexico.py',197),
  ('INSTESTILO -> LLAA RESTILO LLAC instrucciones_2 LLAA DIV RESTILO LLAC','INSTESTILO',8,'p_instruccionEstilo','analizador_lexico.py',201),
  ('instrucciones_2 -> instrucciones_2 instruccion_2','instrucciones_2',2,'p_instrucciones_2_lista','analizador_lexico.py',205),
  ('instrucciones_2 -> instruccion_2','instrucciones_2',1,'p_instrucciones_2_instruccion','analizador_lexico.py',210),
  ('instruccion_2 -> LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC','instruccion_2',10,'p_instruccion_2','analizador_lexico.py',214),
  ('instruccion_2 -> LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_decimal','analizador_lexico.py',221),
  ('instruccion_2 -> LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC','instruccion_2',8,'p_instruccion_2_entero','analizador_lexico.py',225),
  ('instruccion_2 -> CADENA','instruccion_2',1,'p_instruccion_2_texto','analizador_lexico.py',229),
  ('instruccion_2 -> LLAA RTITULO LLAC ROPERACIONES LLAA DIV RTITULO LLAC','instruccion_2',8,'p_instruccion_2_titulo','analizador_lexico.py',233),
  ('instruccion_2 -> LLAA RDESCRIPCION LLAC CORA RTEXTO2 CORC LLAA DIV RDESCRIPCION LLAC','instruccion_2',10,'p_instruccion_2_descripcion','analizador_lexico.py',237),
  ('instruccion_2 -> LLAA RCONTENIDO LLAC CORA RTIPO2 CORC LLAA DIV RCONTENIDO LLAC','instruccion_2',10,'p_instruccion_2_contenido','analizador_lexico.py',241),
  ('instruccion_2 -> LLAA RTITULO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC','instruccion_2',10,'p_instruccion_2_titulo_2','analizador_lexico.py',245),
  ('instruccion_2 -> LLAA RDESCRIPCION RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC','instruccion_2',10,'p_instruccion_2_descripcion_2','analizador_lexico.py',249),
  ('instruccion_2 -> LLAA RCONTENIDO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC','instruccion_2',10,'p_instruccion_2_contenido_2','analizador_lexico.py',253),
  ('COLOR -> RAZUL','COLOR',1,'p_color','analizador_lexico.py',257),
  ('COLOR -> RVERDE','COLOR',1,'p_color','analizador_lexico.py',258),
  ('COLOR -> RROJO','COLOR',1,'p_color','analizador_lexico.py',259),
  ('COLOR -> RNEGRO','COLOR',1,'p_color','analizador_lexico.py',260),
  ('COLOR -> RBLANCO','COLOR',1,'p_color','analizador_lexico.py',261),
  ('COLOR -> RGRIS','COLOR',1,'p_color','analizador_lexico.py',262),
  ('COLOR -> RCELESTE','COLOR',1,'p_color','analizador_lexico.py',263),
  ('COLOR -> RCAFE','COLOR',1,'p_color','analizador_lexico.py',264),
  ('tipo -> RSUMA','tipo',1,'p_tipo','analizador_lexico.py',268),
  ('tipo -> RRESTA','tipo',1,'p_tipo','analizador_lexico.py',269),
  ('tipo -> RMULTIPLICACION','tipo',1,'p_tipo','analizador_lexico.py',270),
  ('tipo -> RDIVISION','tipo',1,'p_tipo','analizador_lexico.py',271),
  ('tipo -> RINVERSO','tipo',1,'p_tipo','analizador_lexico.py',272),
  ('tipo -> RRAIZ','tipo',1,'p_tipo','analizador_lexico.py',273),
  ('tipo -> RPOTENCIA','tipo',1,'p_tipo','analizador_lexico.py',274),
  ('tipo -> RSENO','tipo',1,'p_tipo','analizador_lexico.py',275),
  ('tipo -> RCOSENO','tipo',1,'p_tipo','analizador_lexico.py',276),
  ('tipo -> RTANGENTE','tipo',1,'p_tipo','analizador_lexico.py',277),
]
