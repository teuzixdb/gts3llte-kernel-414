# Samsung Galaxy Tab S3 LTE — Kernel 4.14 Port

**Device:** Samsung Galaxy Tab S3 LTE (SM-T825 / `gts3llte`)  
**SoC:** Qualcomm Snapdragon 820 (msm8996 / Kryo 4-core + Adreno 530)  
**Base:** `android-linux-stable/msm-4.14` (kernel 4.14.214)  
**Target ROM:** LineageOS 24 / Android 17 (SDK 37)  
**Branch:** `gts3llte-4.14-port`

## Status

> ⚠️ **WIP — Early port. Does NOT boot yet. Work in progress.**

| Component | Status |
|-----------|--------|
| Base kernel 4.14 | ✅ Cloned (android-linux-stable/msm-4.14) |
| defconfig (gts3llte) | 🔄 Initial draft |
| Display (MDSS FB) | 🔄 Present in CAF base, needs panel config |
| GPU (KGSL / Adreno 530) | 🔄 Present in CAF base, needs ION adaptation |
| Touch (Synaptics DSX) | 🔄 Present in CAF base, needs DTS |
| Audio (WCD9335/QDSP6v2) | 🔄 Present in CAF base, needs machine driver |
| WiFi (QCA CLD) | ⏳ Needs driver port |
| LTE / RIL | ⏳ Needs driver port |
| S-Pen (Wacom EMR) | 🔄 wacom_i2c.c present |
| GitHub Actions CI | ✅ Configured |

## Building

The kernel builds via GitHub Actions on every push to `gts3llte-4.14-port`.

### Manual build (Linux only):
```bash
export ARCH=arm64
export CROSS_COMPILE=aarch64-linux-gnu-
make O=out gts3llte_defconfig
make -j$(nproc) O=out CC=clang CLANG_TRIPLE=aarch64-linux-gnu- Image.gz-dtb
```

## References

- [jaydens LineageOS 24 for Tab S3](https://github.com/jaydens-tasty-slop/tabs3-lineageos)
- [awesometic 3.18 kernel](https://github.com/awesometic/android_kernel_samsung_msm8996)
- [jaydens 3.18 kernel](https://github.com/jaydens-tasty-slop/tabs3-android_kernel_samsung_msm8996)
- [Device Tree gts3l-common](https://github.com/jaydens-tasty-slop/tabs3-android_device_samsung_gts3l-common)
- [android-linux-stable msm-4.14](https://github.com/android-linux-stable/msm-4.14)
- [XDA Thread](https://xdaforums.com/t/rom-unofficial-17-sm-t820-sm-t825-2026-10-19-vibecoded-lineageos-24-for-galaxy-tab-s3.4805657/)
