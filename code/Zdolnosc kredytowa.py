#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Klient_indywidualny
import Kredyt
from typing import List

class Zdolnosc_kredytowa(object):
	def __init__(self):
		self.___dochod : int = None
		self.___liczba_osob_w_rodzinie : int = None
		self.___aktualne_kredyty : int = None
		self._kwota_kredytu : int = None
		self.___wysokosc_raty : int = None
		self._unnamed_Klient_indywidualny_ : Klient_indywidualny = None
		self._unnamed_Kredyt_ : Kredyt = None

