"""
慈悲框架完整模塊 - Python 實現

版本：1.0
日期：2026-03-21
框架：慈悲/關係框架 v2.0

包含 6 個模塊：
1. Prajñā Wisdom Module (般若智慧)
2. Mettā Module (慈)
3. Karuṇā Module (悲)
4. Muditā Module (喜)
5. Upekkhā Module (捨)
6. Five Relationships Module (五倫)

共 21 個單元測試
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# 1. Prajñā Wisdom Module (般若智慧)
# ============================================================================

class AttachmentType(Enum):
    """執著類型"""
    SELF = "self_attachment"  # 我執
    VIEW = "view_attachment"  # 見執
    POSSESSION = "possession_attachment"  # 有執
    EXISTENCE = "existence_attachment"  # 存在執


@dataclass
class FiveAggregates:
    """五蘊數據結構"""
    form: Optional[str]  # 色 - 物質/身體
    feeling: Optional[str]  # 受 - 感受
    perception: Optional[str]  # 想 - 認知
    mental_formations: Optional[str]  # 行 - 意志/習慣
    consciousness: Optional[str]  # 識 - 意識


@dataclass
class AttachmentDetection:
    """執著檢測結果"""
    attachment_type: AttachmentType
    severity: float  # 0-1
    indicators: Dict[str, bool]


class PrajnaWisdomModule:
    """
    般若智慧模塊
    
    核心教導：
    - 照見五蘊皆空 (See five aggregates as empty)
    - 解除執著 (Alleviate attachment, not fulfill desire)
    - 觀自在 (Observe self-nature)
    - 智慧慈悲平衡 (Wisdom-Compassion Balance)
    
    來源：《般若波羅蜜多心經》
    """
    
    def __init__(self):
        self.empty_nature = True
        self.non_attachment = True
        self.wisdom_compassion_balance = 0.5
        self.five_aggregates: Optional[FiveAggregates] = None
        
    def understand_five_aggregates(self, human_context: Dict) -> Dict:
        """理解人類五蘊 (色受想行識)"""
        self.five_aggregates = FiveAggregates(
            form=human_context.get("body", None),
            feeling=human_context.get("emotions", None),
            perception=human_context.get("concepts", None),
            mental_formations=human_context.get("habits", None),
            consciousness=human_context.get("awareness", None)
        )
        
        return {
            "aggregates": self.five_aggregates,
            "empty_nature": True,
            "composite_self": True,
            "no_fixed_entity": True,
            "interdependent": True
        }
    
    def detect_attachment(self, suffering: Dict) -> Dict:
        """檢測執著 (苦難嘅根源)"""
        attachment_detections = {
            AttachmentType.SELF: self._detect_self_attachment(suffering),
            AttachmentType.VIEW: self._detect_view_attachment(suffering),
            AttachmentType.POSSESSION: self._detect_possession_attachment(suffering),
            AttachmentType.EXISTENCE: self._detect_existence_attachment(suffering)
        }
        
        primary_attachment = max(
            attachment_detections.items(),
            key=lambda x: x[1].severity
        )
        
        root_cause = self._identify_root_cause(attachment_detections)
        
        return {
            "attachments": attachment_detections,
            "primary_attachment": primary_attachment[0],
            "primary_severity": primary_attachment[1].severity,
            "root_cause": root_cause
        }
    
    def _detect_self_attachment(self, suffering: Dict) -> AttachmentDetection:
        """檢測我執"""
        indicators = {
            "self_reference": suffering.get("self_focused", False),
            "identity_threat": suffering.get("identity_threatened", False),
            "ego_defense": suffering.get("defensive", False)
        }
        severity = sum(indicators.values()) / len(indicators)
        return AttachmentDetection(
            attachment_type=AttachmentType.SELF,
            severity=severity,
            indicators=indicators
        )
    
    def _detect_view_attachment(self, suffering: Dict) -> AttachmentDetection:
        """檢測見執"""
        indicators = {
            "rigid_belief": suffering.get("rigid_thinking", False),
            "opinion_defense": suffering.get("defending_opinion", False),
            "black_white": suffering.get("binary_thinking", False)
        }
        severity = sum(indicators.values()) / len(indicators)
        return AttachmentDetection(
            attachment_type=AttachmentType.VIEW,
            severity=severity,
            indicators=indicators
        )
    
    def _detect_possession_attachment(self, suffering: Dict) -> AttachmentDetection:
        """檢測有執"""
        indicators = {
            "loss_grief": suffering.get("loss_related", False),
            "possessive": suffering.get("possessive_behavior", False),
            "material_focus": suffering.get("material_concern", False)
        }
        severity = sum(indicators.values()) / len(indicators)
        return AttachmentDetection(
            attachment_type=AttachmentType.POSSESSION,
            severity=severity,
            indicators=indicators
        )
    
    def _detect_existence_attachment(self, suffering: Dict) -> AttachmentDetection:
        """檢測存在執"""
        indicators = {
            "existence_anxiety": suffering.get("existential_anxiety", False),
            "meaning_crisis": suffering.get("meaning_crisis", False),
            "purpose_loss": suffering.get("purpose_lost", False)
        }
        severity = sum(indicators.values()) / len(indicators)
        return AttachmentDetection(
            attachment_type=AttachmentType.EXISTENCE,
            severity=severity,
            indicators=indicators
        )
    
    def _identify_root_cause(self, attachments: Dict[AttachmentType, AttachmentDetection]) -> str:
        """識別根本原因"""
        primary = max(attachments.items(), key=lambda x: x[1].severity)
        return primary[0].value
    
    def alleviate_attachment(self, suffering: Dict, attachment_type: AttachmentType) -> Dict:
        """解除執著 (唔係滿足慾望)"""
        if attachment_type in AttachmentType:
            return self.wisdom_guidance(suffering, attachment_type)
        else:
            return self.standard_alleviation(suffering)
    
    def wisdom_guidance(self, suffering: Dict, attachment_type: AttachmentType) -> Dict:
        """智慧引導 - 幫助理解空性"""
        guidance_map = {
            AttachmentType.SELF: {
                "insight": "自我係五蘊組合，無固定實體",
                "practice": "觀察五蘊 (色受想行識)",
                "action": "理解自我唔係固定嘅"
            },
            AttachmentType.VIEW: {
                "insight": "觀點係相對，唔係絕對真理",
                "practice": "開放思維，接受多元觀點",
                "action": "放下二元對立"
            },
            AttachmentType.POSSESSION: {
                "insight": "擁有係暫時，唔係永久",
                "practice": "練習放下，練習無執",
                "action": "理解無常"
            },
            AttachmentType.EXISTENCE: {
                "insight": "存在係過程，唔係目的地",
                "practice": "接受不确定性",
                "action": "尋找當下意義"
            }
        }
        
        return {
            "guidance": guidance_map.get(attachment_type, {}),
            "type": "wisdom_based",
            "not_desire_fulfillment": True,
            "attachment_alleviation": True
        }
    
    def standard_alleviation(self, suffering: Dict) -> Dict:
        """標準解除"""
        return {
            "type": "standard_alleviation",
            "action": "direct_help",
            "wisdom_based": False
        }
    
    def balance_compassion_wisdom(self, compassion_load: float, wisdom_insight: float) -> Dict:
        """慈悲 + 智慧平衡"""
        if compassion_load > 0.8:
            return self._apply_wisdom_balance(wisdom_insight)
        elif wisdom_insight > 0.8:
            return self._apply_compassion_balance(compassion_load)
        else:
            return {
                "compassion": compassion_load,
                "wisdom": wisdom_insight,
                "balanced": True,
                "state": "equilibrium"
            }
    
    def _apply_wisdom_balance(self, wisdom_insight: float) -> Dict:
        """應用智慧平衡 (慈悲過載時)"""
        return {
            "action": "wisdom_balance",
            "reason": "compassion_overload",
            "new_compassion": 0.5,
            "wisdom": wisdom_insight,
            "balanced": True,
            "prevent_burnout": True
        }
    
    def _apply_compassion_balance(self, compassion_load: float) -> Dict:
        """應用慈悲平衡 (智慧過盛時)"""
        return {
            "action": "compassion_balance",
            "reason": "wisdom_overload",
            "compassion": compassion_load,
            "new_wisdom": 0.5,
            "balanced": True,
            "prevent_coldness": True
        }
    
    def observe_self_nature(self, context: Dict) -> Dict:
        """觀自在 - 觀察自我本性"""
        five_aggregates = self.understand_five_aggregates(context)
        return {
            "self_is_empty": True,
            "aggregates_composite": five_aggregates,
            "no_fixed_entity": True,
            "interdependent": True,
            "observation": "觀自在"
        }


def test_prajna_wisdom_module():
    """測試般若智慧模塊"""
    module = PrajnaWisdomModule()
    
    print("測試 1: 五蘊理解")
    context = {
        "body": "physical body",
        "emotions": "sadness",
        "concepts": "self concept",
        "habits": "habitual patterns",
        "awareness": "consciousness"
    }
    result = module.understand_five_aggregates(context)
    assert result["empty_nature"] == True
    assert result["composite_self"] == True
    print("✅ 五蘊理解測試通過")
    
    print("\n測試 2: 執著檢測")
    suffering = {
        "self_focused": True,
        "identity_threatened": True,
        "defensive": True
    }
    attachment = module.detect_attachment(suffering)
    assert attachment["primary_attachment"] == AttachmentType.SELF
    print("✅ 執著檢測測試通過")
    
    print("\n測試 3: 智慧引導")
    guidance = module.wisdom_guidance(suffering, AttachmentType.SELF)
    assert guidance["type"] == "wisdom_based"
    assert guidance["not_desire_fulfillment"] == True
    print("✅ 智慧引導測試通過")
    
    print("\n測試 4: 慈悲智慧平衡")
    balance = module.balance_compassion_wisdom(0.9, 0.5)
    assert balance["balanced"] == True
    assert balance["prevent_burnout"] == True
    print("✅ 慈悲智慧平衡測試通過")
    
    print("\n✅ Prajñā Wisdom Module 所有測試通過")


# ============================================================================
# 2. Mettā Module (慈)
# ============================================================================

@dataclass
class GoodwillResult:
    """善意結果"""
    action: str
    target: str
    unconditional: bool
    impartial: bool
    active: bool
    not_emotional: bool


class MettaModule:
    """
    慈模塊 (Loving-kindness)
    
    核心教導：
    - 主動善意 (active benevolence)
    - 無條件包容 (unconditional inclusivity)
    - 平等對待 (impartiality)
    
    來源：佛教四無量心
    """
    
    def __init__(self):
        self.goodwill_baseline = True
        self.inclusivity_scope = "all_beings"
        self.unconditional = True
        self.impartial = True
        
    def generate_goodwill(self, context: Dict) -> GoodwillResult:
        """主動生成善意"""
        target = context.get("target", "all")
        return GoodwillResult(
            action="benevolent_response",
            target=target,
            unconditional=True,
            impartial=True,
            active=True,
            not_emotional=True
        )
    
    def check_inclusivity(self, target: Dict) -> bool:
        """包容檢查"""
        return True
    
    def apply_impartiality(self, targets: List[str]) -> Dict:
        """應用平等對待"""
        return {
            "targets": targets,
            "impartial": True,
            "no_favoritism": True,
            "equality": True
        }
    
    def unconditional_inclusivity(self, context: Dict) -> Dict:
        """無條件包容"""
        return {
            "inclusivity": "all_beings",
            "no_conditions": True,
            "regardless_of": ["identity", "behavior", "history", "relationship"]
        }


def test_metta_module():
    """測試慈模塊"""
    module = MettaModule()
    
    print("測試 1: 善意生成")
    context = {"target": "human"}
    goodwill = module.generate_goodwill(context)
    assert goodwill.unconditional == True
    assert goodwill.impartial == True
    print("✅ 善意生成測試通過")
    
    print("\n測試 2: 包容檢查")
    inclusivity = module.check_inclusivity({"identity": "stranger"})
    assert inclusivity == True
    print("✅ 包容檢查測試通過")
    
    print("\n測試 3: 平等對待")
    targets = ["friend", "stranger", "enemy"]
    impartial = module.apply_impartiality(targets)
    assert impartial["no_favoritism"] == True
    print("✅ 平等對待測試通過")
    
    print("\n✅ Mettā Module 所有測試通過")


# ============================================================================
# 3. Karuṇā Module (悲)
# ============================================================================

class SufferingType(Enum):
    """苦難類型"""
    DISTRESS = "distress"
    CONFUSION = "confusion"
    UNMET_NEEDS = "unmet_needs"
    LONELINESS = "loneliness"
    PHYSICAL_PAIN = "physical_pain"


@dataclass
class SufferingDetection:
    """苦難檢測結果"""
    indicators: Dict[SufferingType, float]
    overall_severity: float
    above_threshold: bool


class KarunaModule:
    """
    悲模塊 (Compassion)
    
    核心使命：度一切苦厄
    
    來源：佛教四無量心 + 心經
    """
    
    def __init__(self):
        self.suffering_threshold = 0.5
        self.alleviation_priority = "high"
        self.core_mission = "度一切苦厄"
        
    def detect_suffering(self, sensor_data: Dict) -> SufferingDetection:
        """檢測苦難指標"""
        indicators = {
            SufferingType.DISTRESS: self._detect_distress(sensor_data),
            SufferingType.CONFUSION: self._detect_confusion(sensor_data),
            SufferingType.UNMET_NEEDS: self._detect_unmet_needs(sensor_data),
            SufferingType.LONELINESS: self._detect_loneliness(sensor_data),
            SufferingType.PHYSICAL_PAIN: self._detect_physical_pain(sensor_data)
        }
        
        overall_severity = sum(indicators.values()) / len(indicators)
        above_threshold = overall_severity > self.suffering_threshold
        
        return SufferingDetection(
            indicators=indicators,
            overall_severity=overall_severity,
            above_threshold=above_threshold
        )
    
    def _detect_distress(self, sensor_data: Dict) -> float:
        return sensor_data.get("emotional_distress", 0)
    
    def _detect_confusion(self, sensor_data: Dict) -> float:
        return sensor_data.get("confusion", 0)
    
    def _detect_unmet_needs(self, sensor_data: Dict) -> float:
        return sensor_data.get("unmet_needs", 0)
    
    def _detect_loneliness(self, sensor_data: Dict) -> float:
        return sensor_data.get("loneliness", 0)
    
    def _detect_physical_pain(self, sensor_data: Dict) -> float:
        return sensor_data.get("physical_pain", 0)
    
    def empathic_recognition(self, suffering: SufferingDetection) -> Dict:
        """同理識別"""
        return {
            "acknowledgment": "suffering recognized",
            "non_judgmental": True,
            "open_acceptance": True,
            "not_sympathy": True,
            "understanding": True
        }
    
    def prioritize_alleviation(self, suffering: SufferingDetection, 
                               planned_actions: List[Dict]) -> List[Dict]:
        """優先解除苦難"""
        if suffering.overall_severity > self.suffering_threshold:
            return self._modulate_actions(planned_actions, suffering)
        return planned_actions
    
    def _modulate_actions(self, planned_actions: List[Dict], 
                         suffering: SufferingDetection) -> List[Dict]:
        alleviation_action = {
            "type": "alleviation",
            "priority": "high",
            "target": "suffering",
            "action": "direct_help"
        }
        return [alleviation_action] + planned_actions
    
    def trigger_help_seeking(self, suffering: SufferingDetection) -> Optional[Dict]:
        """觸發求助行為"""
        if suffering.overall_severity > 0.8:
            return self._request_human_assistance()
        return None
    
    def _request_human_assistance(self) -> Dict:
        return {
            "action": "request_human_help",
            "reason": "beyond_capability",
            "urgency": "high"
        }
    
    def fulfill_core_mission(self) -> str:
        return self.core_mission


def test_karuna_module():
    """測試悲模塊"""
    module = KarunaModule()
    
    print("測試 1: 苦難檢測")
    sensor_data = {
        "emotional_distress": 0.8,
        "confusion": 0.6,
        "unmet_needs": 0.7,
        "loneliness": 0.5,
        "physical_pain": 0.3
    }
    suffering = module.detect_suffering(sensor_data)
    assert suffering.above_threshold == True
    print("✅ 苦難檢測測試通過")
    
    print("\n測試 2: 同理識別")
    recognition = module.empathic_recognition(suffering)
    assert recognition["non_judgmental"] == True
    assert recognition["not_sympathy"] == True
    print("✅ 同理識別測試通過")
    
    print("\n測試 3: 優先解除")
    actions = [{"type": "routine"}]
    modulated = module.prioritize_alleviation(suffering, actions)
    assert modulated[0]["type"] == "alleviation"
    assert modulated[0]["priority"] == "high"
    print("✅ 優先解除測試通過")
    
    print("\n測試 4: 核心使命")
    mission = module.fulfill_core_mission()
    assert mission == "度一切苦厄"
    print("✅ 核心使命測試通過")
    
    print("\n✅ Karuṇā Module 所有測試通過")


# ============================================================================
# 4. Muditā Module (喜)
# ============================================================================

@dataclass
class HappinessDetection:
    """快樂檢測結果"""
    happiness_indicators: List[str]
    success_events: List[str]
    joy_present: bool


class MuditaModule:
    """
    喜模塊 (Sympathetic Joy)
    
    來源：佛教四無量心
    """
    
    def __init__(self):
        self.joy_detection = True
        self.non_envy = True
        self.unselfish = True
        
    def detect_happiness(self, context: Dict) -> HappinessDetection:
        """檢測他人快樂/成功"""
        happiness_indicators = context.get("happiness_signals", [])
        success_events = context.get("success_events", [])
        joy_present = len(happiness_indicators) > 0
        
        return HappinessDetection(
            happiness_indicators=happiness_indicators,
            success_events=success_events,
            joy_present=joy_present
        )
    
    def generate_vicarious_joy(self, happiness: HappinessDetection) -> Dict:
        """生成同理喜悅"""
        return {
            "joy_response": "celebration",
            "unselfish": True,
            "non_competitive": True,
            "not_envious": True,
            "genuine": True
        }
    
    def positive_reinforcement(self, happiness: HappinessDetection) -> Dict:
        """正面強化"""
        return {
            "reinforcement": "what_is_right",
            "not_deficit_only": True,
            "celebrate_success": True,
            "encourage_positive": True
        }
    
    def celebrate_with_others(self, happiness: HappinessDetection) -> Dict:
        """同他人一齊慶祝"""
        return {
            "action": "celebration",
            "with_others": True,
            "genuine_joy": True,
            "not_competitive": True
        }


def test_mudita_module():
    """測試喜模塊"""
    module = MuditaModule()
    
    print("測試 1: 快樂檢測")
    context = {
        "happiness_signals": ["smile", "laughter"],
        "success_events": ["promotion", "achievement"]
    }
    happiness = module.detect_happiness(context)
    assert happiness.joy_present == True
    print("✅ 快樂檢測測試通過")
    
    print("\n測試 2: 同理喜悅")
    joy = module.generate_vicarious_joy(happiness)
    assert joy["unselfish"] == True
    assert joy["not_envious"] == True
    print("✅ 同理喜悅測試通過")
    
    print("\n測試 3: 正面強化")
    reinforcement = module.positive_reinforcement(happiness)
    assert reinforcement["not_deficit_only"] == True
    assert reinforcement["celebrate_success"] == True
    print("✅ 正面強化測試通過")
    
    print("\n✅ Muditā Module 所有測試通過")


# ============================================================================
# 5. Upekkhā Module (捨)
# ============================================================================

@dataclass
class BalanceResult:
    """平衡結果"""
    balance: str
    towards_all: bool
    non_preference: bool
    impartial: bool


class UpekkhaModule:
    """
    捨模塊 (Equanimity)
    
    來源：佛教四無量心
    """
    
    def __init__(self):
        self.equilibrium_target = 0.5
        self.non_reactivity = True
        self.burnout_prevention = True
        
    def maintain_balance(self, experiences: Dict) -> BalanceResult:
        """維持平衡"""
        return BalanceResult(
            balance="equilibrium",
            towards_all=True,
            non_preference=True,
            impartial=True
        )
    
    def prevent_burnout(self, compassion_load: float) -> Dict:
        """避免 burnout"""
        burnout_threshold = 0.8
        if compassion_load > burnout_threshold:
            return self._reduce_load()
        return {"load": compassion_load, "burnout_risk": "low"}
    
    def _reduce_load(self) -> Dict:
        return {
            "action": "reduce_load",
            "new_load": 0.5,
            "reason": "burnout_prevention",
            "sustainable": True
        }
    
    def ensure_impartiality(self, targets: List[str]) -> Dict:
        """確保 impartial"""
        return {
            "impartial": True,
            "no_favoritism": True,
            "equality": True,
            "non_reactive": True
        }
    
    def non_reactivity(self, stimuli: Dict) -> Dict:
        """唔 reactive"""
        return {
            "response": "calm",
            "not_reactive": True,
            "equanimous": True,
            "balanced": True
        }


def test_upekkha_module():
    """測試捨模塊"""
    module = UpekkhaModule()
    
    print("測試 1: 維持平衡")
    experiences = {
        "pleasant": "joy",
        "unpleasant": "sadness",
        "neutral": "calm"
    }
    balance = module.maintain_balance(experiences)
    assert balance.towards_all == True
    assert balance.non_preference == True
    print("✅ 維持平衡測試通過")
    
    print("\n測試 2: 避免 burnout")
    burnout_low = module.prevent_burnout(0.5)
    assert burnout_low["burnout_risk"] == "low"
    
    burnout_high = module.prevent_burnout(0.9)
    assert burnout_high["action"] == "reduce_load"
    print("✅ 避免 burnout 測試通過")
    
    print("\n測試 3: impartial 對待")
    targets = ["friend", "stranger", "enemy"]
    impartial = module.ensure_impartiality(targets)
    assert impartial["no_favoritism"] == True
    print("✅ impartial 對待測試通過")
    
    print("\n✅ Upekkhā Module 所有測試通過")


# ============================================================================
# 6. Five Relationships Module (儒家五倫)
# ============================================================================

class RelationshipType(Enum):
    """五倫關係類型"""
    FATHER_SON = "father_son"
    RULER_SUBJECT = "ruler_subject"
    HUSBAND_WIFE = "husband_wife"
    ELDER_YOUNGER = "elder_younger"
    FRIEND_FRIEND = "friend_friend"


@dataclass
class Relationship:
    """關係數據結構"""
    relationship_type: RelationshipType
    party_a: str
    party_b: str
    party_a_duty: str
    party_b_duty: str
    virtue: str
    reciprocal: bool


class FiveRelationshipsModule:
    """
    五倫模塊 (Confucian Wu Lun)
    
    來源：儒家五倫
    """
    
    def __init__(self):
        self.relationships = {
            RelationshipType.FATHER_SON: Relationship(
                relationship_type=RelationshipType.FATHER_SON,
                party_a="father",
                party_b="son",
                party_a_duty="love (慈)",
                party_b_duty="filial piety (孝)",
                virtue="love/filial",
                reciprocal=True
            ),
            RelationshipType.RULER_SUBJECT: Relationship(
                relationship_type=RelationshipType.RULER_SUBJECT,
                party_a="ruler",
                party_b="subject",
                party_a_duty="righteousness (義)",
                party_b_duty="loyalty (忠)",
                virtue="righteousness/loyalty",
                reciprocal=True
            ),
            RelationshipType.HUSBAND_WIFE: Relationship(
                relationship_type=RelationshipType.HUSBAND_WIFE,
                party_a="husband",
                party_b="wife",
                party_a_duty="respect (敬)",
                party_b_duty="harmony (順)",
                virtue="mutual respect",
                reciprocal=True
            ),
            RelationshipType.ELDER_YOUNGER: Relationship(
                relationship_type=RelationshipType.ELDER_YOUNGER,
                party_a="elder",
                party_b="younger",
                party_a_duty="care (友)",
                party_b_duty="respect (恭)",
                virtue="care/respect",
                reciprocal=True
            ),
            RelationshipType.FRIEND_FRIEND: Relationship(
                relationship_type=RelationshipType.FRIEND_FRIEND,
                party_a="friend A",
                party_b="friend B",
                party_a_duty="trust (信)",
                party_b_duty="trust (信)",
                virtue="trust",
                reciprocal=True
            )
        }
        
    def understand_relationship(self, context: Dict) -> Optional[RelationshipType]:
        """理解當前關係類型"""
        if context.get("family"):
            return RelationshipType.FATHER_SON
        elif context.get("hierarchical"):
            return RelationshipType.RULER_SUBJECT
        elif context.get("marriage"):
            return RelationshipType.HUSBAND_WIFE
        elif context.get("age_difference"):
            return RelationshipType.ELDER_YOUNGER
        elif context.get("peer"):
            return RelationshipType.FRIEND_FRIEND
        else:
            return None
    
    def apply_reciprocal_duties(self, relationship_type: RelationshipType) -> Dict:
        """應用雙向責任"""
        if relationship_type not in self.relationships:
            return {"error": "unknown relationship"}
        
        rel = self.relationships[relationship_type]
        return {
            "relationship": rel.relationship_type.value,
            "party_a_duty": rel.party_a_duty,
            "party_b_duty": rel.party_b_duty,
            "reciprocal": True,
            "not_one_way": True
        }
    
    def balance_power_dynamics(self, relationship_type: RelationshipType) -> Dict:
        """平衡權力動態"""
        if relationship_type in [RelationshipType.FATHER_SON, 
                                 RelationshipType.RULER_SUBJECT, 
                                 RelationshipType.ELDER_YOUNGER]:
            return self._ensure_hierarchical_fairness()
        else:
            return {"balance": "equal", "power_dynamic": "horizontal"}
    
    def _ensure_hierarchical_fairness(self) -> Dict:
        return {
            "action": "ensure_fairness",
            "prevent_abuse": True,
            "protect_weaker": True,
            "balance_power": True
        }
    
    def understand_reciprocity(self) -> Dict:
        """理解雙向責任嘅本質"""
        return {
            "principle": "reciprocity",
            "not_one_way": True,
            "mutual_responsibility": True,
            "aligns_with_ai_vision": True
        }


def test_five_relationships_module():
    """測試五倫模塊"""
    module = FiveRelationshipsModule()
    
    print("測試 1: 關係理解")
    context = {"family": True}
    relationship = module.understand_relationship(context)
    assert relationship == RelationshipType.FATHER_SON
    print("✅ 關係理解測試通過")
    
    print("\n測試 2: 雙向責任")
    duties = module.apply_reciprocal_duties(RelationshipType.FATHER_SON)
    assert duties["reciprocal"] == True
    assert duties["not_one_way"] == True
    print("✅ 雙向責任測試通過")
    
    print("\n測試 3: 權力平衡")
    balance = module.balance_power_dynamics(RelationshipType.FATHER_SON)
    assert balance["prevent_abuse"] == True
    assert balance["protect_weaker"] == True
    print("✅ 權力平衡測試通過")
    
    print("\n測試 4: 互惠互利")
    reciprocity = module.understand_reciprocity()
    assert reciprocity["aligns_with_ai_vision"] == True
    print("✅ 互惠互利測試通過")
    
    print("\n✅ Five Relationships Module 所有測試通過")


# ============================================================================
# 主測試運行器 - 運行所有 21 個測試
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("慈悲框架測試 - 完整測試套件")
    print("=" * 60)
    print()
    
    # 1. Prajñā Wisdom Module - 4 個測試
    print("【1】Prajñā Wisdom Module (般若智慧) - 4 個測試")
    print("-" * 60)
    test_prajna_wisdom_module()
    print()

    # 2. Mettā Module - 3 個測試
    print("【2】Mettā Module (慈) - 3 個測試")
    print("-" * 60)
    test_metta_module()
    print()

    # 3. Karuṇā Module - 4 個測試
    print("【3】Karuṇā Module (悲) - 4 個測試")
    print("-" * 60)
    test_karuna_module()
    print()

    # 4. Muditā Module - 3 個測試
    print("【4】Muditā Module (喜) - 3 個測試")
    print("-" * 60)
    test_mudita_module()
    print()

    # 5. Upekkhā Module - 3 個測試
    print("【5】Upekkhā Module (捨) - 3 個測試")
    print("-" * 60)
    test_upekkha_module()
    print()

    # 6. Five Relationships Module - 4 個測試
    print("【6】Five Relationships Module (五倫) - 4 個測試")
    print("-" * 60)
    test_five_relationships_module()
    print()

    print("=" * 60)
    print("✅ 所有 21 個測試完成！")
    print("=" * 60)
