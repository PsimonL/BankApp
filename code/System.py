#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Programista
import wnioski
import Pracownik
from typing import List

class System(object):
	def waliduj_wniosek_kredytowy(self, aWniosek) -> long:
		pass

	def przekaz_wniosek_pracownikowi(self):
		pass

	def pokaz_decyzje(self):
		pass

	def Wyswietl_komunikat_o_powodzeniu_operacji(self, aId : int) -> str:
		pass

	def aktualizuj_zabezpieczenia(self):
		pass

	def aktualizuj_funkcjonalnosci(self):
		pass

	def __init__(self):
		self.___czy_wymaga_aktualicacji : long = None
		self._unnamed_Programista_ : Programista = None
		self._unnamed_wnioski_ : wnioski = None
		"""# @AssociationKind Aggregation"""
		self._unnamed_Pracownik_ : Pracownik = None

