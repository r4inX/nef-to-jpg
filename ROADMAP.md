# 🗺️ NEF to JPG Converter - Product Roadmap

## 📋 Overview

This document outlines planned features, improvements, and ideas for future versions of the NEF to JPG Converter.

---

## 🚀 v2.2.0 - Enhanced User Experience (Q1 2026)

### 🎨 GUI Improvements
- [ ] **Drag & Drop Files**: Allow dragging NEF files directly into the GUI (not just folders)
- [ ] **Preview Images**: Show thumbnail previews of NEF files before conversion
- [ ] **Conversion History**: Display recently converted batches with statistics
- [ ] **Dark Mode**: Add theme toggle for light/dark mode
- [ ] **Progress Details**: Show which file is currently being converted
- [ ] **Cancel Button**: Allow stopping conversion mid-process
- [ ] **Queue System**: Show list of files to be converted with ability to reorder

### 🔧 CLI Enhancements
- [ ] **Recursive Mode**: Add `--recursive` flag to process subdirectories
- [ ] **File Filtering**: Add `--include-pattern` and `--exclude-pattern` options
- [ ] **Dry Run Mode**: Add `--dry-run` to preview what would be converted
- [ ] **JSON Output**: Add `--json` flag for machine-readable output
- [ ] **Resume Failed**: Save state and resume failed conversions
- [ ] **Smart Retry**: Automatically retry failed conversions with different settings

### 📊 Statistics & Reporting
- [ ] **Detailed Report**: Generate HTML/PDF report after batch conversion
- [ ] **File Size Comparison**: Show NEF vs JPG file size savings
- [ ] **Quality Metrics**: Display histogram/quality analysis
- [ ] **CSV Export**: Export conversion statistics to CSV
- [ ] **Performance Graphs**: Visualize conversion speed over time

---

## 🎯 v2.3.0 - Professional Features (Q2 2026)

### 📸 Advanced Image Processing
- [ ] **Auto-Rotate**: Automatically rotate images based on EXIF orientation
- [ ] **Auto-Exposure**: Optional auto-exposure correction
- [ ] **White Balance**: Adjustable white balance presets (Auto, Daylight, Cloudy, etc.)
- [ ] **Sharpening**: Optional sharpening filter with adjustable strength
- [ ] **Noise Reduction**: Optional noise reduction for high ISO images
- [ ] **Crop Support**: Allow cropping during conversion
- [ ] **Batch Resize**: Add optional output resolution settings
- [ ] **Watermarking**: Add text/image watermarks to converted files

### 🖼️ Format Support
- [ ] **Multiple Output Formats**: Support PNG, TIFF, WebP, HEIC
- [ ] **RAW Format Support**: Support CR2 (Canon), ARW (Sony), DNG (Adobe)
- [ ] **Batch Format Mix**: Convert different input formats in one run
- [ ] **Format Presets**: Predefined settings for web, print, archive

### 🎨 Color Management
- [ ] **ICC Profile Support**: Apply and embed ICC color profiles
- [ ] **Color Space Conversion**: Support sRGB, Adobe RGB, ProPhoto RGB
- [ ] **Bit Depth Options**: Support 8-bit and 16-bit output

---

## 🌐 v2.4.0 - Web & Integration (Q3 2026)

### 🌍 Web Interface
- [ ] **Local Web UI**: Browser-based interface running on localhost
- [ ] **REST API**: HTTP API for programmatic access
- [ ] **WebSocket Support**: Real-time progress updates
- [ ] **Mobile Responsive**: Mobile-friendly web interface
- [ ] **Multi-User Support**: Multiple concurrent conversion sessions

### 🔌 Integration & Automation
- [ ] **Cloud Storage**: Direct upload to Dropbox, Google Drive, OneDrive
- [ ] **FTP/SFTP**: Automatic upload to FTP servers
- [ ] **Webhook Support**: Trigger webhooks on conversion complete
- [ ] **Email Notifications**: Send email when batch completes
- [ ] **Slack/Discord Integration**: Post notifications to team channels

### 📦 Workflow Automation
- [ ] **Configuration Presets**: Save and load conversion presets
- [ ] **Batch Scripts**: Create reusable conversion scripts
- [ ] **Hot Folders**: Multiple watch directories with different settings
- [ ] **Scheduling**: Schedule conversions at specific times
- [ ] **Auto-Organize**: Automatically organize output by date/camera/settings

---

## 🐳 v2.5.0 - DevOps & Deployment (Q3 2026)

### 🐳 Containerization
- [ ] **Docker Image**: Official Docker image for easy deployment
- [ ] **Docker Compose**: Multi-container setup with web UI
- [ ] **Kubernetes Support**: Helm charts for K8s deployment
- [ ] **Health Checks**: Built-in health check endpoints

### ☁️ Cloud Deployment
- [ ] **AWS Lambda**: Serverless conversion function
- [ ] **Azure Functions**: Microsoft Azure serverless support
- [ ] **Google Cloud Functions**: GCP serverless deployment
- [ ] **Terraform Modules**: Infrastructure as code templates

### 📊 Monitoring & Logging
- [ ] **Prometheus Metrics**: Export conversion metrics
- [ ] **Grafana Dashboards**: Pre-built monitoring dashboards
- [ ] **Structured Logging**: JSON structured logs
- [ ] **OpenTelemetry**: Distributed tracing support

---

## 💼 v2.6.0 - Licensing & Monetization (Q4 2026)

### 📜 Dual License Model

This version introduces a **dual license model** to support sustainable development:

- [ ] **AGPLv3 License**: Free for open source and personal use
- [ ] **Commercial License**: For proprietary/commercial use without copyleft obligations
- [ ] **License Documentation**: Clear guidelines on which license to use
- [ ] **Commercial Pricing**: Tiered pricing (Small Business, Enterprise, OEM)
- [ ] **License Management**: System for commercial license verification
- [ ] **Purchase Portal**: Website for buying commercial licenses

### 🛡️ Legal & Compliance
- [ ] **Contributor License Agreement (CLA)**: For future contributors
- [ ] **License Headers**: Add license headers to all source files
- [ ] **Grandfathering**: All v2.5.x and earlier remain MIT licensed
- [ ] **Migration Guide**: Help users understand license change
- [ ] **Legal Documentation**: Terms of service, privacy policy

### 💰 Commercial Features
- [ ] **Priority Support**: Commercial customers get 24h response time
- [ ] **Custom Branding**: White-label options for OEM customers
- [ ] **Service Level Agreements (SLA)**: Guaranteed uptime for enterprise
- [ ] **Dedicated Support Channel**: Private support portal for commercial users

**Note**: All versions before v2.6.0 remain MIT licensed forever!

See `.github/DUAL-LICENSE-PLAN.md` for detailed migration information.

---

## 🎓 v3.0.0 - Enterprise & Advanced (2027)

### 🏢 Enterprise Features
- [ ] **License Management**: Multi-seat licensing support
- [ ] **User Authentication**: LDAP/AD integration
- [ ] **Role-Based Access**: Different permission levels
- [ ] **Audit Logging**: Comprehensive audit trail
- [ ] **Batch Processing Queue**: Distributed job queue with Redis
- [ ] **Load Balancing**: Multiple worker nodes

### 🤖 AI/ML Features
- [ ] **Smart Scene Detection**: Auto-detect scene type (portrait, landscape, etc.)
- [ ] **Intelligent Quality**: AI-optimized quality settings per image
- [ ] **Auto-Tagging**: Automatic keyword/tag generation
- [ ] **Face Detection**: Detect and preserve faces during processing
- [ ] **Object Recognition**: Identify objects in images
- [ ] **Smart Cropping**: AI-powered composition-aware cropping

### 📱 Native Apps
- [ ] **Windows Store App**: Native Windows application
- [ ] **macOS App Store**: Native macOS application
- [ ] **iOS App**: Mobile app for on-the-go conversion
- [ ] **Android App**: Android mobile application
- [ ] **Cross-Platform Sync**: Sync settings across devices

---

## 🔨 Technical Improvements (Ongoing)

### ⚡ Performance
- [ ] **GPU Acceleration**: Use GPU for image processing (CUDA/OpenCL)
- [ ] **Memory Optimization**: Reduce memory footprint for large batches
- [ ] **Streaming Processing**: Process files larger than available RAM
- [ ] **Incremental Conversion**: Only convert changed/new files
- [ ] **Cache Layer**: Cache processed images for quick re-export

### 🧪 Testing & Quality
- [ ] **Visual Regression Tests**: Automated image comparison tests
- [ ] **Load Testing**: Performance benchmarks for large batches
- [ ] **Fuzzing**: Security fuzzing for file parsers
- [ ] **Integration Tests**: End-to-end workflow testing
- [ ] **Property-Based Testing**: Hypothesis/QuickCheck style tests

### 📚 Documentation
- [ ] **Video Tutorials**: YouTube tutorial series
- [ ] **Interactive Docs**: Live code examples in documentation
- [ ] **API Documentation**: Swagger/OpenAPI documentation
- [ ] **Cookbook**: Common use-case recipes
- [ ] **Troubleshooting Guide**: Comprehensive error solutions
- [ ] **Multi-Language Docs**: Translate docs to DE, FR, ES, JP

### 🌍 Internationalization
- [ ] **i18n Support**: Full internationalization framework
- [ ] **German Translation**: Deutsche Übersetzung
- [ ] **French Translation**: Traduction française
- [ ] **Spanish Translation**: Traducción al español
- [ ] **Japanese Translation**: 日本語翻訳
- [ ] **Chinese Translation**: 中文翻译

---

## 🎨 Nice-to-Have Features

### User Experience
- [ ] **Undo/Redo**: Undo last conversion operations
- [ ] **Comparison View**: Side-by-side NEF vs JPG comparison
- [ ] **Keyboard Shortcuts**: Comprehensive keyboard navigation
- [ ] **Tooltips & Help**: Context-sensitive help system
- [ ] **First-Run Tutorial**: Interactive onboarding
- [ ] **Update Notifications**: Auto-check for new versions

### Image Features
- [ ] **HDR Support**: Merge multiple exposures to HDR
- [ ] **Panorama Stitching**: Automatic panorama creation
- [ ] **Time-Lapse**: Create time-lapse videos from sequences
- [ ] **GIF Creation**: Convert image sequences to animated GIFs
- [ ] **Collage Maker**: Create photo collages
- [ ] **Before/After Slider**: Interactive comparison slider

### Metadata & Organization
- [ ] **GPS Map View**: Show photo locations on map
- [ ] **Metadata Editor**: Edit EXIF data before conversion
- [ ] **Keyword Management**: Add/edit keywords and tags
- [ ] **Copyright Templates**: Quick copyright info insertion
- [ ] **Lens Correction**: Automatic lens distortion correction
- [ ] **Auto-Categorize**: Smart folders by date/location/camera

### Social & Sharing
- [ ] **Social Media Export**: Optimized export for Instagram, Facebook, Twitter
- [ ] **Share Links**: Generate shareable links for converted images
- [ ] **Photo Gallery**: Built-in web gallery generator
- [ ] **QR Code**: Generate QR codes for easy sharing
- [ ] **Print Layouts**: Templates for photo prints

---

## 📊 Community Requests

Track feature requests from GitHub Issues and Discussions:

### High Priority (Most Requested)
1. [ ] **#XXX** - Batch rename files during conversion
2. [ ] **#XXX** - Preserve folder structure in output
3. [ ] **#XXX** - Add progress percentage to title bar
4. [ ] **#XXX** - Remember last used settings
5. [ ] **#XXX** - Add sound notification on completion

### Medium Priority
1. [ ] **#XXX** - Add file conflict resolution options
2. [ ] **#XXX** - Support for RAW+JPEG pairs
3. [ ] **#XXX** - Exclude already converted files
4. [ ] **#XXX** - Add logging to file option
5. [ ] **#XXX** - Network drive support improvements

### Long Term
1. [ ] **#XXX** - Plugin system for custom processors
2. [ ] **#XXX** - Scripting API (Python/JavaScript)
3. [ ] **#XXX** - Batch action recorder
4. [ ] **#XXX** - Command chaining (convert → resize → upload)
5. [ ] **#XXX** - Custom output filename templates

---

## 🎯 Quick Wins (Easy Implementations)

These features can be implemented relatively quickly:

- [ ] **--version flag improvement**: Show all dependencies versions
- [ ] **Color-coded output**: Use colors in CLI for better readability
- [ ] **Sound effects**: Optional completion sound
- [ ] **System tray icon**: Minimize to tray with quick actions
- [ ] **Context menu integration**: Right-click "Convert to JPG" in Explorer
- [ ] **Last settings memory**: Remember previous conversion settings
- [ ] **Output folder templates**: Use {date}, {camera}, {iso} in paths
- [ ] **Duplicate detection**: Warn before overwriting files
- [ ] **Estimated time**: Show estimated time remaining
- [ ] **CPU/Memory usage display**: Real-time resource monitoring

---

## 🐛 Known Issues to Address

Track and prioritize known bugs:

- [ ] Large memory usage with >1000 files
- [ ] GUI freezes on very slow network drives
- [ ] Progress bar accuracy with varying file sizes
- [ ] Watch mode CPU usage on macOS
- [ ] EXIF GPS coordinates format inconsistencies

---

## 📝 Notes

### Version Numbering
- **Major (X.0.0)**: Breaking changes, major rewrites
- **Minor (x.X.0)**: New features, backwards compatible
- **Patch (x.x.X)**: Bug fixes, minor improvements

### Priority Levels
- 🔴 **Critical**: Security, data loss, crashes
- 🟠 **High**: Major features, common use cases
- 🟡 **Medium**: Nice-to-have features
- 🟢 **Low**: Long-term goals, experimental

### Decision Criteria
When prioritizing features, consider:
1. User impact (how many users benefit?)
2. Implementation effort (time/complexity)
3. Maintenance cost (ongoing support needed)
4. Strategic value (aligns with project goals?)
5. Community demand (votes/requests)

---

## 🤝 Contributing

Want to help implement these features?

1. Check the [Issues](https://github.com/r4inX/nef-to-jpg/issues) page
2. Comment on features you're interested in
3. Fork the repository and submit PRs
4. Join discussions in [Discussions](https://github.com/r4inX/nef-to-jpg/discussions)

---

**Last Updated**: October 28, 2025  
**Current Version**: v2.1.0  
**Next Planned Release**: v2.2.0 (Q1 2026)
