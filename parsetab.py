
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COUNT END SYMBOLstart : atom \n             | ENDatom : atom symbol\n            | emptysymbol   : SYMBOL suffixsuffix : COUNT empty\n              | empty empty   : '
    
_lr_action_items = {'END':([0,],[3,]),'SYMBOL':([0,2,4,5,6,7,8,9,10,],[-8,6,-4,-3,-8,-5,-8,-7,-6,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,],[-8,0,-1,-2,-4,-3,-8,-5,-8,-7,-6,]),'COUNT':([6,],[8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'atom':([0,],[2,]),'empty':([0,6,8,],[4,9,10,]),'symbol':([2,],[5,]),'suffix':([6,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> atom','start',1,'p_start','molecule.py',9),
  ('start -> END','start',1,'p_start','molecule.py',10),
  ('atom -> atom symbol','atom',2,'p_atom','molecule.py',13),
  ('atom -> empty','atom',1,'p_atom','molecule.py',14),
  ('symbol -> SYMBOL suffix','symbol',2,'p_symbol','molecule.py',20),
  ('suffix -> COUNT empty','suffix',2,'p_suffix','molecule.py',24),
  ('suffix -> empty','suffix',1,'p_suffix','molecule.py',25),
  ('empty -> <empty>','empty',0,'p_empty','molecule.py',30),
]
