#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm8850-common',
    'hardware/qcom-caf/sm8850',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8850-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    (
        'odm/etc/camera/snsc_bokeh_motiontuning.xml',
        'odm/etc/camera/snsc_enhance_motiontuning.xml',
        'odm/etc/camera/snsc_noface_motiontuning.xml',
        'odm/etc/camera/snsc_motiontuning.xml'
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    (
        'vendor/lib64/libcameraopt.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    (
       'odm/lib64/camera/components/com.qti.node.dewarp.so',
       'odm/lib64/hw/com.qti.chi.override.so',
       'odm/lib64/libcamximageformatutils.so',
       'odm/lib64/libchifeature2.so',
       'odm/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so'
        ),
    (
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-V1-ndk.so',
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-client.so',
       'vendor/lib64/vendor.xiaomi.hardware.camera.injection-service.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.camera.device-V1-ndk.so',
            'android.hardware.camera.device-V2-ndk.so'
        ),
    (
        'vendor/lib64/libultrahdr_myron.so', 
    ): blob_fixup()
        .replace_needed(
            'libjpegencoder.so',
            'libjpegencoder_myron.so'
        )
        .replace_needed(
            'libjpegdecoder.so',
            'libjpegdecoder_myron.so'
        ),
    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.losslessjpeg.so'
    ): blob_fixup()
        .replace_needed(
            'libdng_sdk.so',
            'libdng_sdk-myron.so'
        ),
    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.jpegrAggr.so', 
        'odm/lib64/camera/plugins/com.xiaomi.plugin.gainmap.so'
    ): blob_fixup()
        .replace_needed(
            'libultrahdr.so',
            'libultrahdr_myron.so'
        ),
}  # fmt: skip

module = ExtractUtilsModule(
    'myron',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8850-common', module.vendor
    )
    utils.run()