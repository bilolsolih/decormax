from modeltranslation.translator import TranslationOptions, translator

from .models.product import Collection
from .models.product_parameters import BuildingMaterial, Style, PictureType, TargetRoom, ManufacturingMethod


class CollectionTranslationOptions(TranslationOptions):
    fields = ('description', 'description_2')


class BuildingMaterialTranslationOptions(TranslationOptions):
    fields = ('title',)


class StyleTranslationOptions(TranslationOptions):
    fields = ('title',)


class PictureTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


class TargetRoomTranslationOptions(TranslationOptions):
    fields = ('title',)


class ManufacturingMethodTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(TargetRoom, TargetRoomTranslationOptions)
translator.register(Collection, CollectionTranslationOptions)
translator.register(BuildingMaterial, BuildingMaterialTranslationOptions)
translator.register(ManufacturingMethod, ManufacturingMethodTranslationOptions)
translator.register(Style, StyleTranslationOptions)
translator.register(PictureType, PictureTypeTranslationOptions)
