from django.db import models
from django.utils.translation import gettext as _


# TODO: fill constants and move to separate file
SCHOOLS = []  # schools of magic
SUBCHOOLS = []  # subschools of magic
SOURCES = []  # sources
DEITIES = []  # deities
# Create your models here.


class Spell(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    school = models.CharField(max_length=255, verbose_name=_('School'))
    subschool = models.CharField(
        max_length=255, verbose_name=_('Subschool'), blank=True)
    descriptor = models.CharField(
        max_length=255, verbose_name=_('Descriptor'), blank=True)
    spell_level = models.CharField(
        max_length=255, verbose_name=_('Spell level'))
    casting_time = models.CharField(
        max_length=255, verbose_name=_('Casting time'))
    components = models.CharField(max_length=255, verbose_name=_('Components'))
    costly_components = models.CharField(
        max_length=255, verbose_name=_('Costly components'))
    range = models.CharField(
        max_length=255, verbose_name=_('Range'), blank=True)
    area = models.CharField(
        max_length=255, verbose_name=_('Area'), blank=True)
    effect = models.CharField(
        max_length=255, verbose_name=_('Effect'), blank=True)
    targets = models.CharField(
        max_length=255, verbose_name=_('Targets'), blank=True)
    duration = models.CharField(
        max_length=255, verbose_name=_('Duration'), blank=True)
    dismissible = models.BooleanField(verbose_name=_('Dismissible'))
    shapeable = models.BooleanField(verbose_name=_('Shapeable'))
    saving_throw = models.CharField(
        max_length=255, verbose_name=_('Saving throw'), blank=True)
    spell_resistence = models.CharField(
        max_length=255, verbose_name=_('Spell resistence'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    description_formated = models.TextField(
        verbose_name=_('Description formatted'))
    source = models.CharField(max_length=100, verbose_name=_('Source'))
    full_text = models.TextField(verbose_name=_('Full text'))

    # components
    verbal = models.BooleanField(verbose_name=_('Verbal'))
    somatic = models.BooleanField(verbose_name=_('Somatic'))
    material = models.BooleanField(verbose_name=_('Material'))
    focus = models.BooleanField(verbose_name=_('Focus'))
    divine_focus = models.BooleanField(verbose_name=_('Devine Focus'))

    # class levels
    sor = models.IntegerField(verbose_name=_('Sorcerer lvl'), null=True)
    wiz = models.IntegerField(verbose_name=_('Wizard lvv'), null=True)
    cleric = models.IntegerField(verbose_name=_('Cleric lvl'), null=True)
    druid = models.IntegerField(verbose_name=_('Druid lvl'), null=True)
    ranger = models.IntegerField(verbose_name=_('Ranger lvl'), null=True)
    bard = models.IntegerField(verbose_name=_('Bard lvl'), null=True)
    paladin = models.IntegerField(verbose_name=_('Paladin lvl'), null=True)
    alchemist = models.IntegerField(verbose_name=_('Alchemist lvl'), null=True)
    summoner = models.IntegerField(verbose_name=_('Summoner lvl'), null=True)
    witch = models.IntegerField(verbose_name=_('Witch lvl'), null=True)
    inquisitor = models.IntegerField(
        verbose_name=_('Inquisitor lvl'), null=True)
    oracle = models.IntegerField(verbose_name=_('Oracle lvl'), null=True)
    antipaladin = models.IntegerField(
        verbose_name=_('Antipaladin lvl'), null=True)
    magus = models.IntegerField(verbose_name=_('Magus lvl'), null=True)
    adept = models.IntegerField(verbose_name=_('Adept lvl'), null=True)
    bloodrager = models.IntegerField(
        verbose_name=_('Bloodranger lvl'), null=True)
    shaman = models.IntegerField(verbose_name=_('Shaman lvl'), null=True)
    psychic = models.IntegerField(verbose_name=_('Psychic lvl'), null=True)
    medium = models.IntegerField(verbose_name=_('Medium lvl'), null=True)
    mesmerist = models.IntegerField(verbose_name=_('Mesmerist lvl'), null=True)
    occultist = models.IntegerField(verbose_name=_('Occultist lvl'), null=True)
    spiritualist = models.IntegerField(
        verbose_name=_('Spiritualist lvl'), null=True)
    skald = models.IntegerField(verbose_name=_('Skald lvl'), null=True)
    investigator = models.IntegerField(
        verbose_name=_('Investigator lvl'), null=True)
    hunter = models.IntegerField(verbose_name=_('Hunter lvl'), null=True)
    summoner_unchained = models.IntegerField(
        verbose_name=_('Summoner unchaned lvl'), null=True)

    deity = models.CharField(
        max_length=100, verbose_name=_('Deity'), blank=True)
    sla_level = models.IntegerField(
        null=True, verbose_name=_('Spell-like Ability lvl'))
    domain = models.CharField(
        max_length=100, verbose_name=_('Domain'), blank=True)
    short_description = models.TextField(
        verbose_name=_('Short description'), blank=True)
    acid = models.BooleanField(verbose_name=_('Acid'))
    air = models.BooleanField(verbose_name=_('Air'))
    chaotic = models.BooleanField(verbose_name=_('Chaotic'))
    cold = models.BooleanField(verbose_name=_('Cold'))
    curse = models.BooleanField(verbose_name=_('Curse'))
    darkness = models.BooleanField(verbose_name=_('Darkness'))
    death = models.BooleanField(verbose_name=_('Death'))
    disease = models.BooleanField(verbose_name=_('Disease'))
    earth = models.BooleanField(verbose_name=_('Earth'))
    electricity = models.BooleanField(verbose_name=_('Electricity'))
    emotion = models.BooleanField(verbose_name=_('Emotion'))
    evil = models.BooleanField(verbose_name=_('Evil'))
    fear = models.BooleanField(verbose_name=_('Fear'))
    fire = models.BooleanField(verbose_name=_('Fire'))
    force = models.BooleanField(verbose_name=_('Force'))
    good = models.BooleanField(verbose_name=_('Good'))
    language_dependency = models.BooleanField(
        verbose_name=_('Language dependency'))
    lawful = models.BooleanField(verbose_name=_('Lawful'))
    light = models.BooleanField(verbose_name=_('Light'))
    mind_affecting = models.BooleanField(verbose_name=_('Mind affecting'))
    pain = models.BooleanField(verbose_name=_('Pain'))
    poison = models.BooleanField(verbose_name=_('Poiscon'))
    shadow = models.BooleanField(verbose_name=_('Shadow'))
    sonic = models.BooleanField(verbose_name=_('Sonic'))
    water = models.BooleanField(verbose_name=_('Water'))
    material_cost = models.IntegerField(
        verbose_name=_('Material cost'), null=True)
    bloodline = models.CharField(
        max_length=255, verbose_name=_('Bloodline'), blank=True)
    patron = models.CharField(
        max_length=255, verbose_name=_('Patron'), blank=True)
    mythic = models.BooleanField(verbose_name=_('Mythic'))
    mythic_text = models.TextField(verbose_name=_('Mythic text'), blank=True)
    augmented = models.TextField(verbose_name=_('Aumented'), blank=True)
    haunt_statistic = models.CharField(
        max_length=255, blank=True, verbose_name=_('Haunt statistic'))
    ruse = models.BooleanField(verbose_name=_('Ruse'))
    draconic = models.BooleanField(verbose_name=_('Draconic'))
    meditative = models.BooleanField(verbose_name=_('Meditative'))

    def __str__(self):
        return self.name
