#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Klient_indywidualny
from typing import List

class Przelew(object):
	def __init__(self):
		self.___imie_adresata : str = None
		self.___nazwisko_adresata : str = None
		self.___numer_konta_adresata : str = None
		self.___kwota_przelewu : complex = None
		self._unnamed_Klient_indywidualny_ : Klient_indywidualny = None

