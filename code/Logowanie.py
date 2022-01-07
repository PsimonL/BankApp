#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Nowy_klient
import Klient_indywidualny
from typing import List

class Logowanie(object):
	def Zaloguj(self, aIleLogowan : int = 0) -> long:
		pass

	def Odzyskaj_haslo(self) -> None:
		pass

	def Czy_zalogowany(self) -> long:
		pass

	def __init__(self):
		self.___login : str = None
		self.___haslo : str = None
		self._unnamed_Nowy_klient_ : Nowy_klient = None
		self._unnamed_Klient_indywidualny_ : Klient_indywidualny = None
		"""# @AssociationKind Composition"""

