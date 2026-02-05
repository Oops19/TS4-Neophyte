
from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.utils.common_type_utils import CommonTypeUtils
from sims4communitylib.enums.tags_enum import CommonGameTag
from sims4communitylib.utils.objects.common_object_tag_utils import CommonObjectTagUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class RegisterInteractionsNeophyteNeophyte0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0x465598B8180AB505,  # 'Destroy!' - fnv('o19_Neophyte_PMC__Neophyte_PMA_Destroyx21_debug')
            0x977098562E1A6F64,  # 'I Will Have That Power!' - fnv('o19_Neophyte_PMC__Neophyte_PMA_I_Will_Have_That_Powerx21_debug')
            0x5943263343511F47,  # 'Exterminate!' - fnv('o19_Neophyte_PMC__Neophyte_PMA_Exterminatex21_debug')
            0xB9CF2D274CDA8AA7,  # 'I move by psychokinetic power' - fnv('o19_Neophyte_PMC__Neophyte_PMA_I_move_by_psychokinetic_power_debug')
            0xBB0F1C2790917140,  # 'There is no such thing as society' - fnv('o19_Neophyte_PMC__Neophyte_PMA_There_is_no_such_thing_as_society_debug')
            0x49B88AF60B5C9681,  # 'The night is not for turning' - fnv('o19_Neophyte_PMC__Neophyte_PMA_The_night_is_not_for_turning_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True
