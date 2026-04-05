# 運行所有慈悲框架測試
# 執行 compassion-core-modules.py 入面所有 21 個測試函數

import sys
sys.path.insert(0, 'C:\\Users\\User\\.openclaw\\workspace-evolver-agent\\research')

from compassion-core-modules import (
    test_prajna_wisdom_module,
    test_metta_module,
    test_karuna_module,
    test_mudita_module,
    test_upekkha_module,
    test_five_relationships_module
)

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
