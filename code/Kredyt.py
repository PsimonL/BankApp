#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Klient_indywidualny
import Zdolnosc_kredytowa
import Waluty
from typing import List

class Kredyt(object):
	def Rejestracja_kredytu_w_systemie(self) -> complex:
		pass

	def __init__(self):
		self.___kwota_kredytu : int = None
		self.___okres_splaty : int = None
		self.___oprocentowanie : complex = None
		self.___rata : int = None
		self._unnamed_Klient_indywidualny_ : Klient_indywidualny = None
		self._unnamed_Zdolnosc_kredytowa_ : Zdolnosc_kredytowa = None
		self._unnamed_Waluty_ : Waluty = None

