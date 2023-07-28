from modeltranslation.translator import TranslationOptions, translator

from .models.product import Product, Variant
from .models.product_parameters import BuildingMaterial, Style, PictureType, TargetRoom, ManufacturingMethod


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Product, ProductTranslationOptions)


class VariantTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Variant, VariantTranslationOptions)


class BuildingMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(BuildingMaterial, BuildingMaterialTranslationOptions)


class StyleTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Style, StyleTranslationOptions)


class PictureTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(PictureType, PictureTypeTranslationOptions)


class TargetRoomTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(TargetRoom, TargetRoomTranslationOptions)


class ManufacturingMethodTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(ManufacturingMethod, ManufacturingMethodTranslationOptions)
