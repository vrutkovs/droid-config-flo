# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device deb
%define vendor asus
%define vendor_pretty Assu
%define device_pretty Nexus 7 (2013)
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
