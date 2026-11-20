/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Compatibility shim: dma-attrs.h for kernel 4.14
 *
 * In kernel 3.18, DMA attributes were a struct (struct dma_attrs).
 * In kernel 4.6+, they became unsigned long bitfields (DMA_ATTR_*).
 * This header provides backward compatibility for drivers written for 3.18
 * that use init_dma_attrs(), dma_set_attr(), dma_get_attr().
 *
 * Added for gts3llte-4.14-port
 */
#ifndef _LINUX_DMA_ATTRS_H
#define _LINUX_DMA_ATTRS_H

#include <linux/dma-mapping.h>

/*
 * In 4.14, dma_attrs is just unsigned long.
 * Provide compat macros for old-style code.
 */
static inline void init_dma_attrs(unsigned long *attrs)
{
	*attrs = 0;
}

static inline void dma_set_attr(unsigned long attr, unsigned long *attrs)
{
	*attrs |= attr;
}

static inline int dma_get_attr(unsigned long attr, unsigned long *attrs)
{
	return !!(*attrs & attr);
}

#endif /* _LINUX_DMA_ATTRS_H */
