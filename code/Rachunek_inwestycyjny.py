#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Klient_indywidualny
import Papiery_wartosciowe
from typing import List

class Rachunek_inwestycyjny(object):
	def Kup_papiery_wartosciowe(self) -> long:
		pass

	def Sprzedaj_papiery_wartosciowe(self) -> long:
		pass

	def __init__(self):
		self.___stan_rachunku : complex = None
		self._unnamed_Klient_indywidualny_ : Klient_indywidualny = None
		self._unnamed_Papiery_wartosciowe_ : Papiery_wartosciowe = None
		"""# @AssociationKind Composition"""

