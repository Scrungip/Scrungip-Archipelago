from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class AM2RItem(Item):
    game = str = "AM2R"


item_table = {
    "Missile": ItemData(1, ItemClassification.progression),
    "Super_Missile": ItemData(1, ItemClassification.progression),
    "Power_Bomb": ItemData(1, ItemClassification.progression),
    "Energy_Tank": ItemData(1, ItemClassification.useful),
    #  "Morph_ball": ItemData(1, ItemClassification.progression)
    #  "Power_Grip": ItemData(1, ItemClassification.progression)
    "Bombs": ItemData(1, ItemClassification.progression),
    "Spider_Ball": ItemData(1, ItemClassification.progression),
    "Hi_Jump": ItemData(1, ItemClassification.progression),
    "Spring_Ball": ItemData(1, ItemClassification.progression),
    "Space_Jump": ItemData(1, ItemClassification.progression),
    "Speed_Booster": ItemData(1, ItemClassification.progression),
    "Screw_Attack": ItemData(1, ItemClassification.progression),
    "Varia_Suit": ItemData(1, ItemClassification.useful),
    "Gravity_Suit": ItemData(1, ItemClassification.progression),
    "Charge_Beam": ItemData(1, ItemClassification.useful),
    "Wave_Beam": ItemData(1, ItemClassification.useful),
    "S_P_A_Z_E_R": ItemData(1, ItemClassification.useful),
    "Plasma_Beam": ItemData(1, ItemClassification.useful),
    "Ice_Beam": ItemData(1, ItemClassification.progression),
    "Equipment_Trap": ItemData(1, ItemClassification.trap),
    "Freeze_Trap": ItemData(1, ItemClassification.trap),
    "Short_Beam": ItemData(1, ItemClassification.trap),
    "EMP_Trap": ItemData(1, ItemClassification.trap),
    "Metroid": ItemData(1, ItemClassification.progression),
}
item_frequencies = {
    "Missile": 44,
    "Super_Missile": 10,
    "Power_Bomb": 10,
    "Energy Tank": 10,
}