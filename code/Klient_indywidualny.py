#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Logowanie
import Kredyt
import Zdolnosc_kredytowa
import Przelew
import Waluty
import Portfel_kryptowalutowy
import Karta_Debetowa
import Lokata
import Klient_biznesowy
import Rachunek_inwestycyjny
from typing import List

class Klient_indywidualny(object):
	def Zloz_wniosek_kredytowy(self) -> long:
		pass

	def Sprawdz_zdolnosc_kredytowa(self) -> complex:
		pass

	def Wykonaj_przelew(self, aIdKlienta : str, aKwota : int = 0) -> long:
		pass

	def Przewalutuj(self, aKwota : int, aWaluta : Waluty) -> complex:
		pass

	def Przelew_na_konto_kryptowalutowe(self) -> complex:
		pass

	def Otwarcie_lokaty(self) -> long:
		pass

	def Zamnkiecie_lokaty(self) -> long:
		pass

	def Sprawdz_stan_konta(self) -> str:
		pass

	def Zlozenie_pieniedzy_na_lokacie(self):
		pass

	def Zaloz_rachunek_inwestycyjny(self):
		pass

	def Klient_indywidualny(self, aImie : string.nazwisko__string, aPesel : str):
		pass

	def Zaloz_konto(self) -> long:
		pass

	def __init__(self):
		self.___imie : str = None
		self.___nazwisko : str = None
		self.___pesel : str = None
		self.___liczba_kredytow : int = 0
		self.___stan_konta : complex = None
		self.___numer_konta : str = None
		self.___attribute = None
		self._unnamed_Logowanie_ : Logowanie = None
		self._unnamed_Kredyt_ : Kredyt = None
		"""# @AssociationKind Composition"""
		self._unnamed_Zdolnosc_kredytowa_ : Zdolnosc_kredytowa = None
		"""# @AssociationKind Composition"""
		self._unnamed_Przelew_ : Przelew = None
		"""# @AssociationKind Composition"""
		self._unnamed_Waluty_ : Waluty = None
		"""# @AssociationKind Aggregation"""
		self._unnamed_Portfel_kryptowalutowy_ : Portfel_kryptowalutowy = None
		"""# @AssociationKind Composition"""
		self._unnamed_Karta_Debetowa_ : Karta_Debetowa = None
		"""# @AssociationKind Composition"""
		self._unnamed_Lokata_ : Lokata = None
		"""# @AssociationKind Composition"""
		self._unnamed_Klient_biznesowy_ : Klient_biznesowy = None
		self._unnamed_Rachunek_inwestycyjny_ : Rachunek_inwestycyjny = None
		"""# @AssociationKind Composition"""

