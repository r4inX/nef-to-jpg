# 📜 Dual License Migration Plan

## Overview

Starting with **v2.6.0** (planned Q4 2026), NEF to JPG Converter will transition from MIT License to a Dual License model:

1. **AGPLv3** - Free for open source and personal use
2. **Commercial License** - For proprietary/commercial use

## Timeline

- **v2.1.0 - v2.5.x** (2025-2026): Remains MIT Licensed
- **v2.6.0+** (Q4 2026): Dual License (AGPLv3 + Commercial)

## Why This Change?

As the project matures and gains enterprise adoption, we want to:
- ✅ Continue supporting the open source community
- ✅ Ensure improvements flow back to the community
- ✅ Generate revenue from commercial use to fund development
- ✅ Provide professional support for businesses

## What This Means

### For Open Source Users (AGPLv3)
**✅ You can continue to:**
- Use NEF Converter for free
- Modify the source code
- Distribute your modifications
- Use it in open source projects

**⚠️ You must:**
- Share your modifications under AGPLv3
- If you offer it as a service (SaaS), make your code public
- Provide attribution

### For Commercial Users (Commercial License)
**💰 Purchase a commercial license if you want to:**
- Integrate into closed-source/proprietary software
- Offer as a paid service without sharing code
- Remove AGPLv3 obligations
- Get priority support

**Pricing (to be determined):**
- Small Business: $X/year
- Enterprise: $X/year
- Lifetime License: $X (one-time)
- Custom/OEM: Contact us

## Grandfathering

**All versions before v2.6.0 remain MIT licensed forever:**
- v2.1.0 through v2.5.x: MIT License (no restrictions)
- You can continue using these versions under MIT
- No retroactive license changes

## Migration Steps (Q4 2026)

### 1. Pre-Release (2 months before)
- [ ] Announce license change on GitHub
- [ ] Update documentation
- [ ] Email major users/contributors
- [ ] Post in Discussions

### 2. At v2.6.0 Release
- [ ] Add LICENSE-AGPL.txt
- [ ] Add LICENSE-COMMERCIAL.md
- [ ] Update README with dual license info
- [ ] Add license headers to all source files
- [ ] Create pricing page
- [ ] Set up commercial license sales

### 3. Post-Release
- [ ] Monitor community feedback
- [ ] Provide migration assistance
- [ ] Update website/docs
- [ ] Handle commercial inquiries

## Files to Create at v2.6.0

```
nef-to-jpg/
├── LICENSE-AGPL.txt          # AGPLv3 license text
├── LICENSE-COMMERCIAL.md     # Commercial license terms
├── LICENSE-NOTICE.md         # Which license applies when
├── CONTRIBUTING.md           # Update with CLA info
└── README.md                 # Update with dual license info
```

## Source File Headers (v2.6.0+)

All Python files will include:

```python
# NEF to JPG Converter
# Copyright (c) 2025-2026 r4inX
#
# This file is part of NEF to JPG Converter.
#
# This software is available under two licenses:
#
# 1. AGPLv3 License (Free for Open Source use)
#    See LICENSE-AGPL.txt for details
#
# 2. Commercial License (For proprietary use)
#    See LICENSE-COMMERCIAL.md for details
#    Contact: your-email@example.com
```

## FAQ

### Can I still use older versions under MIT?
**Yes!** All versions v2.5.x and earlier remain MIT licensed forever.

### What if I'm already using it commercially?
Versions before v2.6.0 are MIT, so no restrictions. For v2.6.0+, you'll need a commercial license or use AGPLv3.

### Can I fork the last MIT version?
Yes! You can fork v2.5.x and maintain it under MIT. However, you cannot merge v2.6.0+ changes without respecting the new license.

### What about contributors?
Contributors to v2.6.0+ agree to the new dual license. We may introduce a CLA (Contributor License Agreement).

### Will there be community edition features?
Yes! Core functionality remains in AGPLv3 version. Premium features may be commercial-only.

## Contact

Questions about the license change? 
- 📧 Email: your-email@example.com
- 💬 GitHub Discussions: https://github.com/r4inX/nef-to-jpg/discussions
- 🐛 Issues: https://github.com/r4inX/nef-to-jpg/issues

---

**Last Updated:** October 29, 2025  
**Status:** Planning Phase  
**Effective:** v2.6.0 (Q4 2026)
