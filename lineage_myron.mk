#
# Copyright (C) 2024 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from myron device.
$(call inherit-product, device/xiaomi/myron/device.mk)

## Device identifier
PRODUCT_DEVICE := myron
PRODUCT_NAME := lineage_myron
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 25102RKBEC
PRODUCT_MANUFACTURER := Xiaomi

EVO_BUILD_TYPE := Unofficial
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_BUILD_APERTURE_CAMERA := false
TARGET_INCLUDE_ACCORD := false

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="myron-user 17 CP2A.260605.016 OS4.0.0.33.XPMCNXM release-keys" \
    BuildFingerprint=Redmi/myron/myron:17/CP2A.260605.016/OS4.0.0.33.XPMCNXM:user/release-keys \
    DeviceName=myron \
    DeviceProduct=myron \
    SystemDevice=missi \
    SystemName=missi
