from modeltranslation.translator import translator, TranslationOptions

from .models import Address


class AddressTranslationOptions(TranslationOptions):
    fields = ('region', 'district', 'street')


translator.register(Address, AddressTranslationOptions)
