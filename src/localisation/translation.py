import os
from mylocale import TR
from flet_localisation import locale

trfile = f"{os.path.dirname(__file__)}/localisation.csv"


def BIRTHDAY(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="BIRTHDAY",
        langcode=langcode,
    )


def FATHERSDAY(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="FATHERSDAY",
        langcode=langcode,
    )


def HAPPYFATHERSDAY(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="HAPPYFATHERSDAY",
        langcode=langcode,
    )


def HAPPYMOTHERSDAY(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="HAPPYMOTHERSDAY",
        langcode=langcode,
    )


def MOTHERSDAY(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="MOTHERSDAY",
        langcode=langcode,
    )


def THANKYOU(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="THANKYOU",
        langcode=langcode,
    )


def FORMALNAME(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="FORMALNAME",
        langcode=langcode,
    )


def DESCRIPTION(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="DESCRIPTION",
        langcode=langcode,
    )


def SUPPORTEDPLATFORM(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="SUPPORTEDPLATFORM",
        langcode=langcode,
    )
