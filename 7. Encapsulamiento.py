#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  encaps.py
#  
#  Copyright 2020 Pyr0 Maniac <Pyro@Pyro>
class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave
        
Usuario1 = usuario ("Roberto", "qwerty")
print (Usuario1.nombre, Usuario1._usuario__clave)