# These and other macros are documented in dhd/droid-hal-device.inc

%define device moto_msm8960_jbbl
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Photon Q

%define installable_zip 1

%define android_config \
#define QCOM_BSP 1\
%{nil}

%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}

%include rpm/dhd/droid-hal-device.inc
