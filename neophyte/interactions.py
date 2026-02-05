from interactions.context import InteractionContext
from neophyte.modinfo import ModInfo

from typing import Any

from sims.sim import Sim


from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.classes.testing.common_execution_result import CommonExecutionResult
from sims4communitylib.classes.testing.common_test_result import CommonTestResult
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.objects.common_object_spawn_utils import CommonObjectSpawnUtils
from sims4communitylib.utils.sims.common_sim_spawn_utils import CommonSimSpawnUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.common_type_utils import CommonTypeUtils

 
log: CommonLog = CommonLogRegistry().register_log(ModInfo.get_identity(), 'InteractionsNeophyte')
log.enable()


class InteractionsNeophyte(CommonImmediateSuperInteraction):

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        # log.debug(f"InteractionsHotkeys: on_test({interaction_sim}, {interaction_target}, {interaction_context})")
        return CommonTestResult.TRUE


    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        log.debug(f"on_started({interaction_sim}, {interaction_target}, )")
        if CommonTypeUtils.is_sim_instance(interaction_target):
            target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
            CommonSimSpawnUtils.despawn_sim(target_sim_info)
        else:
           CommonObjectSpawnUtils.destroy_object(interaction_target)
        return CommonExecutionResult.TRUE

r'''
GameObject
        super().__init__(definition, **kwargs)
        self._on_location_changed_callbacks = None
        self._transient = None
        self._created_constraints = None
        self._created_constraints_dirty = True
        self._household_owner_id = None
        self.new_in_inventory = True
        self.is_new_object = False
        self._provided_surface = UNSET
        zone = services.current_zone()
        account_id = build_buy.get_user_in_build_buy(zone.id)
        if account_id is not None:
            self.set_household_owner_id(zone.lot.zone_owner_household_id)
            self.set_post_bb_fixup_needed()
            zone.set_to_fixup_on_build_buy_exit(self)
        self._hidden_flags = 0
        self._local_tags = None
        self._persisted_tags = None
        self._is_routable_terrain = None
        self._is_surface = None
        self._build_buy_use_flags = 0
        self._scheduled_elements = None
        self._work_locks = WeakSet()
        self._on_hidden_or_shown_callbacks = None
        self._provided_mobile_posture_operations = None
'''