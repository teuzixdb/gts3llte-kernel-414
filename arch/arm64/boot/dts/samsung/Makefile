# SPDX-License-Identifier: GPL-2.0
# gts3llte (SM-T825) - Target hardware revision 05
dtb-y += msm8996-sec-gts3llte-eur-kor-r05.dtb

ifeq ($(CONFIG_ARM64),y)
always          := $(dtb-y)
subdir-y        := $(dts-dirs)
else
targets += dtbs
targets += $(addprefix ../, $(dtb-y))

$(obj)/../%.dtb: $(src)/%.dts FORCE
	$(call if_changed_dep,dtc)

dtbs: $(addprefix $(obj)/,$(dtb-y))
endif
clean-files := *.dtb *.reverse.dts