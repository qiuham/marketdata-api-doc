---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/devtools/download-rc
api_type: Guide
updated_at: 2026-11-18 02:20:23.485917
---

# Download Developer Version

## [2.56.0-development.2] 2025-09-18

\*\*Download:
[MacOS(205.20 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.56.0-development.2.dmg)

### Bug Fixes

- fix: filter standalone-chunk from addEntry

### Features

- feat: check node enviroment before download bundler
- feat: feature request 2547 & 1893
- feat: support EventSource for IDE
- feat: support five themes
- feat: midnight -> dark_midnight
- feat: support midnight
- feat: enhance change bundler feature
- feat: implement lite-timeline devtool panel ui
- feat: support dynamic bundler
- feat: support standalone-chunks
- feat(ide): add diagnosticPage

## [2.56.0-development.1] 2025-01-17

\*\*Download:
[MacOS(196.78 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.56.0-development.1.dmg)

## [2.55.0-development.1] 2025-01-10

\*\*Download:
[MacOS(196.78 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.55.0-development.1.dmg)

## [2.50.0-development.2024082101] 2024-08-21

\*\*Download:
[MacOS(193.36 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.50.0-development.2024082101.dmg)

### Features

- feat: update bundle watch add entry

## [2.33.0-development.1] 2023-06-30

**Download:
[MacOS(182.34 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.33.0-development.1.dmg)
**

### Bug Fixes

- fix: [clamp] min should not be greater than max

## [2.32.1-development.1] 2023-06-12

**Download:
[MacOS(182.35 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.32.1-development.1.dmg)
**

### Bug Fixes

- fix: loading project not end
- fix: appid undefined

## [2.31.0-development.1] 2023-04-27

**Download:
[MacOS(175.06 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.31.0-development.1.dmg)
**

### Bug Fixes

- fix: bindings not found issue
- fix: preview issue

### Features

- feat: bundler error ui
- feat: login extension support dev mode
- feat: add metric data for IPC channel
- feat: data report for login extension

### Performance Improvements

- perf: setup server on demand

## [2.26.0-development.1] 2023-01-11

**Download:
[MacOS(154.61 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.26.0-development.1.dmg)
**

### Bug Fixes

- fix: date picker style align native
- fix: force update issue
- fix: resolve pika and inner bmp path
- fix: code quality issue and upload sentry symbols
- fix: performance measure point no report

### Features

- feat: add otf fonts for BinancePlex
- feat: all the point
- feat: support multi match
- feat: reporter build duration in cicd
- feat: auto fill upload form when last upload fail
- feat: provide login extension for internal developers
- feat: auto update by env

## [2.25.0-development.2] 2022-12-13

**Download:
[MacOS(154.16 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.25.0-development.2.dmg)
**

### Bug Fixes

- fix: csp protocol for blob
- fix: msv auto fill not works

## [2.25.0-development.1] 2022-12-12

**Download:
[MacOS(154.16 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.25.0-development.1.dmg)
**

### Bug Fixes

- fix: reload app lead to BXML panel empty

### Features

- feat: provide code quality panel UI
- feat: metrics data collection
- feat: write msv to project.config.json
- feat: hide useless bxml panel and breadcrumbs

## [2.24.1-development.1] 2022-12-09

**Download:
[MacOS(145.17 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.24.1-development.1.dmg)
**

### Bug Fixes

- fix: eslint
- fix: reload app lead to BXML panel empty

### Features

- feat: metrics data collection

## [2.24.0-development.1]

**Download:
[MacOS(143.42 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.24.0-development.1.dmg)
**

### Bug Fixes

- fix: remove BXML spaces
- fix: high cpu load issue
- fix: page log not show
- fix: default value not set in the form instance

### Features

- feat: hide internal requests

## [2.23.2-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.2-development.1.dmg)
**

### Bug Fixes

- fix: high cpu load issue
- fix: default value not set in the form instance

## [2.23.1-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.1-development.1.dmg)
**

### Bug Fixes

- fix: yarn lock cause withFileTypes of null

### Internal

- ci: use prod check instead
- chore(changelog): update changelog for version v2.23.0
- chore(changelog): update changelog for version v2.23.0-development.1

## [2.23.0-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.0-development.1.dmg)
**

### Bug Fixes

- fix: yarn lock cause withFileTypes of null
- fix: use bn-image tag instead of img to detect
- fix: add same local network info when preview
- fix: preview logo image styles
- fix: show error when user's libVersion field not valid
- fix: latest version has cache in yarn.lock
- fix: audit panel export to html

### Features

- feat: support msv auto fill
- feat: migrate buitin sdk from 3.4.0 to 3.6.2

### Refactor

- refactor: remove plugin
- refactor: remove share menu and network plugin
- refactor(sdk): move plugin into skd host plugin

### Internal

- ci: use prod check instead
- chore(changelog): update changelog for version v2.23.0
- chore(changelog): update changelog for version v2.23.0-development.1
- ci: add package size when release
- fead(ide): update bundler version
- docs: custom compilation
- chore: update settings
- docs: setting
- doc: public doc- Detail Dialog
- doc: remote debug public doc
- chore(changelog): update changelog for version v2.22.3
- chore(changelog): update changelog for version v2.22.3-development.1
- docs: startup page
- docs: simulator
- doc: public doc about main page and toolbar
- doc: public doc about main page and toolbar
- chore(changelog): update changelog for version v2.22.2
- chore(changelog): update changelog for version v2.22.2-development.1
- chore: upgrade @mp/host
- docs: update img url
- docs: update readme and overview
- chore(changelog): update changelog for version v2.22.1
- chore(changelog): update changelog for version v2.22.1-development.1

## [2.22.3-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.3-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.3-development.1.exe)**

### Features

- feat: update bundler to ^3.0.0

## [2.22.2-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.2-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.2-development.1.exe)**

### Internal

- chore: upgrade @mp/host

## [2.22.1-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.1-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.1-development.1.exe)**

### Bug Fixes

- fix: update error message
- fix: skip loading when launch if no auto compile

### Features

- feat: audit panel support base64 image cheking

### Internal

- chore: update electron builder
- chore(cicd): migrate prowjobs
- chore(cicd): migrate prowjobs
- ci(flow): migrate to flow cicd pipeline
- chore(changelog): update changelog for version v2.22.0

## [2.22.0-development.2]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.0-development.2.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.0-development.2.exe)**

### Bug Fixes

- fix: capture time and timeout update
- fix(ide): upload dialog issues
- fix(ide): open project type error in hostRenderer
- fix: copy source-code ignore node_module & .git
- fix: msv support multiselection

### Features

- feat(sdk): loadScriptSync rpc
- feat(ide): create project validate
- feat: validate upload parameters and refactor the dialog
- feat(ide): capture preview of mp
- feat(ide): update deps
- feat: support webview template
- feat(ide): support create webview

### Internal

- doc: devtool panels
- chore(changelog): update changelog for version v2.22.0-development.1

## [2.22.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.0-development.1.exe)**

### Bug Fixes

- fix(ide): open project type error in hostRenderer
- fix: copy source-code ignore node_module & .git
- fix: msv support multiselection

### Features

- feat(ide): capture preview of mp
- feat(ide): update deps
- feat: support webview template
- feat(ide): support create webview

### Internal

- doc: devtool panels
- chore(changelog): update changelog for version v2.21.1-development.1

## [2.21.1-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.21.1-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.21.1-development.1.exe)**

### Bug Fixes

- fix: sourcemap dev mode link not works
- fix: add file size field
- fix: changelog issue
- fix: reload devtool if needed

### Features

- feat(ide): update deps
- feat(panel): audit panel support exporting JSON
- feat(plugin): plugin refactor and better types
- feat: sourcemap zip with version
- feat: guide user to use `code quality`
- feat: support sourcemap download

### Internal

- chore(ide): compile check
- chore: update MSV
- chore(changelog): update changelog for version v2.21.0
- WIP: remote debug devtools use ws as protocol channel
- chore(changelog): update changelog for version v2.21.0-development.1

## [2.21.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.21.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.21.0-development.1.exe)**

### Features

- feat(applog-panel): implement applog panel
- feat: [IDE] Static analyze mp code using bundler's ability
- feat: [IDE] Make console panel log more clean on production version

### Internal

- chore: update bundler version
- chore: update dependency
- chore(changelog): update changelog for version v2.20.0
- chore(changelog): update changelog for version v2.20.0-development.1

## [2.20.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.20.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.20.0-development.1.exe)**

### Bug Fixes

- fix(ide-devtools-panel): fix audits
- fix(audit-score): fix light theme color
- fix: handle taro built mp
- fix: replace template chinese comment and add logs page
- fix: fix mock method no data
- fix: fix mock fail template

### Features

- feat: Audit panel detect performance remaining metrics
- feat: repeat call warn in ide
- feat: check local sdk version
- feat(audit-panel): deal with taro mp setData
- feat(audit-score): research and implement audit score calculation
- feat(audit-experience): add more columns into experience metrics
- feat(audit-panel): Audit panel detect performance remaining metrics
- feat(audit-panel): detect render cost time | init render, setData render
- feat(audit): add experience related metric
- feat(audit-panel): implement audit panel best practice metrics
- feat(ide): mock open-type getPhoneNumber getEmailAddress behavior
- feat(audit-panel): optimize report context
- feat(ide-devtools-panel): audit panel render performance metrics
- feat(mock panel): optimize mock panel
- feat: show error message when webview fails to load

### Internal

- chore: bump @mp/host version
- docs: update v2.19.0-development.1 change log
- chore(changelog): update changelog for version v2.19.0

## [2.19.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.19.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.19.0-development.1.exe)**

### Bug Fixes

- fix: remove duplicate them change emit event
- fix: executeJavaScript causes bxml not to be displayed
- fix: bxml page node has redundant spaces
- fix(mock panel): fix ordered before existing data & generated template error
- fix(mock panel): fix some bugs
- fix: loading assets from resources
- fix: fix no proxy method when open IDE for the first time
- fix: fix-select-method
- fix(ide): remote debug
- fix: remove zx dependency

### Features

- feat: clean console context
- feat: clean console panel context selector
- feat: close watcher to stop compile
- feat: add mock sys
- feat: setdata cnt adjust and bug fix
- feat: integrate @mp/extended-lib
- feat(devtools): implement audit panel for detect setData

### Refactor

- refactor: plugin remove location, download-package, login
- refactor: Mock Panel Better user behavior
- refactor: move sensor plugin

### Internal

- chore(ide): @mp/host upgrade to 0.2.25
- chore: optimization code
- chore: universal link
- chore(changelog): update changelog for version v2.18.1
- chore: changelog automation

---

# Download Developer Version

## [2.56.0-development.2] 2025-09-18

\*\*Download:
[MacOS(205.20 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.56.0-development.2.dmg)

### Bug Fixes

- fix: filter standalone-chunk from addEntry

### Features

- feat: check node enviroment before download bundler
- feat: feature request 2547 & 1893
- feat: support EventSource for IDE
- feat: support five themes
- feat: midnight -> dark_midnight
- feat: support midnight
- feat: enhance change bundler feature
- feat: implement lite-timeline devtool panel ui
- feat: support dynamic bundler
- feat: support standalone-chunks
- feat(ide): add diagnosticPage

## [2.56.0-development.1] 2025-01-17

\*\*Download:
[MacOS(196.78 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.56.0-development.1.dmg)

## [2.55.0-development.1] 2025-01-10

\*\*Download:
[MacOS(196.78 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.55.0-development.1.dmg)

## [2.50.0-development.2024082101] 2024-08-21

\*\*Download:
[MacOS(193.36 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.50.0-development.2024082101.dmg)

### Features

- feat: update bundle watch add entry

## [2.33.0-development.1] 2023-06-30

**Download:
[MacOS(182.34 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.33.0-development.1.dmg)
**

### Bug Fixes

- fix: [clamp] min should not be greater than max

## [2.32.1-development.1] 2023-06-12

**Download:
[MacOS(182.35 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.32.1-development.1.dmg)
**

### Bug Fixes

- fix: loading project not end
- fix: appid undefined

## [2.31.0-development.1] 2023-04-27

**Download:
[MacOS(175.06 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.31.0-development.1.dmg)
**

### Bug Fixes

- fix: bindings not found issue
- fix: preview issue

### Features

- feat: bundler error ui
- feat: login extension support dev mode
- feat: add metric data for IPC channel
- feat: data report for login extension

### Performance Improvements

- perf: setup server on demand

## [2.26.0-development.1] 2023-01-11

**Download:
[MacOS(154.61 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.26.0-development.1.dmg)
**

### Bug Fixes

- fix: date picker style align native
- fix: force update issue
- fix: resolve pika and inner bmp path
- fix: code quality issue and upload sentry symbols
- fix: performance measure point no report

### Features

- feat: add otf fonts for BinancePlex
- feat: all the point
- feat: support multi match
- feat: reporter build duration in cicd
- feat: auto fill upload form when last upload fail
- feat: provide login extension for internal developers
- feat: auto update by env

## [2.25.0-development.2] 2022-12-13

**Download:
[MacOS(154.16 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.25.0-development.2.dmg)
**

### Bug Fixes

- fix: csp protocol for blob
- fix: msv auto fill not works

## [2.25.0-development.1] 2022-12-12

**Download:
[MacOS(154.16 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.25.0-development.1.dmg)
**

### Bug Fixes

- fix: reload app lead to BXML panel empty

### Features

- feat: provide code quality panel UI
- feat: metrics data collection
- feat: write msv to project.config.json
- feat: hide useless bxml panel and breadcrumbs

## [2.24.1-development.1] 2022-12-09

**Download:
[MacOS(145.17 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.24.1-development.1.dmg)
**

### Bug Fixes

- fix: eslint
- fix: reload app lead to BXML panel empty

### Features

- feat: metrics data collection

## [2.24.0-development.1]

**Download:
[MacOS(143.42 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.24.0-development.1.dmg)
**

### Bug Fixes

- fix: remove BXML spaces
- fix: high cpu load issue
- fix: page log not show
- fix: default value not set in the form instance

### Features

- feat: hide internal requests

## [2.23.2-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.2-development.1.dmg)
**

### Bug Fixes

- fix: high cpu load issue
- fix: default value not set in the form instance

## [2.23.1-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.1-development.1.dmg)
**

### Bug Fixes

- fix: yarn lock cause withFileTypes of null

### Internal

- ci: use prod check instead
- chore(changelog): update changelog for version v2.23.0
- chore(changelog): update changelog for version v2.23.0-development.1

## [2.23.0-development.1]

**Download:
[MacOS(143.23 MB)](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.23.0-development.1.dmg)
**

### Bug Fixes

- fix: yarn lock cause withFileTypes of null
- fix: use bn-image tag instead of img to detect
- fix: add same local network info when preview
- fix: preview logo image styles
- fix: show error when user's libVersion field not valid
- fix: latest version has cache in yarn.lock
- fix: audit panel export to html

### Features

- feat: support msv auto fill
- feat: migrate buitin sdk from 3.4.0 to 3.6.2

### Refactor

- refactor: remove plugin
- refactor: remove share menu and network plugin
- refactor(sdk): move plugin into skd host plugin

### Internal

- ci: use prod check instead
- chore(changelog): update changelog for version v2.23.0
- chore(changelog): update changelog for version v2.23.0-development.1
- ci: add package size when release
- fead(ide): update bundler version
- docs: custom compilation
- chore: update settings
- docs: setting
- doc: public doc- Detail Dialog
- doc: remote debug public doc
- chore(changelog): update changelog for version v2.22.3
- chore(changelog): update changelog for version v2.22.3-development.1
- docs: startup page
- docs: simulator
- doc: public doc about main page and toolbar
- doc: public doc about main page and toolbar
- chore(changelog): update changelog for version v2.22.2
- chore(changelog): update changelog for version v2.22.2-development.1
- chore: upgrade @mp/host
- docs: update img url
- docs: update readme and overview
- chore(changelog): update changelog for version v2.22.1
- chore(changelog): update changelog for version v2.22.1-development.1

## [2.22.3-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.3-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.3-development.1.exe)**

### Features

- feat: update bundler to ^3.0.0

## [2.22.2-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.2-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.2-development.1.exe)**

### Internal

- chore: upgrade @mp/host

## [2.22.1-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.1-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.1-development.1.exe)**

### Bug Fixes

- fix: update error message
- fix: skip loading when launch if no auto compile

### Features

- feat: audit panel support base64 image cheking

### Internal

- chore: update electron builder
- chore(cicd): migrate prowjobs
- chore(cicd): migrate prowjobs
- ci(flow): migrate to flow cicd pipeline
- chore(changelog): update changelog for version v2.22.0

## [2.22.0-development.2]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.0-development.2.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.0-development.2.exe)**

### Bug Fixes

- fix: capture time and timeout update
- fix(ide): upload dialog issues
- fix(ide): open project type error in hostRenderer
- fix: copy source-code ignore node_module & .git
- fix: msv support multiselection

### Features

- feat(sdk): loadScriptSync rpc
- feat(ide): create project validate
- feat: validate upload parameters and refactor the dialog
- feat(ide): capture preview of mp
- feat(ide): update deps
- feat: support webview template
- feat(ide): support create webview

### Internal

- doc: devtool panels
- chore(changelog): update changelog for version v2.22.0-development.1

## [2.22.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.22.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.22.0-development.1.exe)**

### Bug Fixes

- fix(ide): open project type error in hostRenderer
- fix: copy source-code ignore node_module & .git
- fix: msv support multiselection

### Features

- feat(ide): capture preview of mp
- feat(ide): update deps
- feat: support webview template
- feat(ide): support create webview

### Internal

- doc: devtool panels
- chore(changelog): update changelog for version v2.21.1-development.1

## [2.21.1-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.21.1-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.21.1-development.1.exe)**

### Bug Fixes

- fix: sourcemap dev mode link not works
- fix: add file size field
- fix: changelog issue
- fix: reload devtool if needed

### Features

- feat(ide): update deps
- feat(panel): audit panel support exporting JSON
- feat(plugin): plugin refactor and better types
- feat: sourcemap zip with version
- feat: guide user to use `code quality`
- feat: support sourcemap download

### Internal

- chore(ide): compile check
- chore: update MSV
- chore(changelog): update changelog for version v2.21.0
- WIP: remote debug devtools use ws as protocol channel
- chore(changelog): update changelog for version v2.21.0-development.1

## [2.21.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.21.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.21.0-development.1.exe)**

### Features

- feat(applog-panel): implement applog panel
- feat: [IDE] Static analyze mp code using bundler's ability
- feat: [IDE] Make console panel log more clean on production version

### Internal

- chore: update bundler version
- chore: update dependency
- chore(changelog): update changelog for version v2.20.0
- chore(changelog): update changelog for version v2.20.0-development.1

## [2.20.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.20.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.20.0-development.1.exe)**

### Bug Fixes

- fix(ide-devtools-panel): fix audits
- fix(audit-score): fix light theme color
- fix: handle taro built mp
- fix: replace template chinese comment and add logs page
- fix: fix mock method no data
- fix: fix mock fail template

### Features

- feat: Audit panel detect performance remaining metrics
- feat: repeat call warn in ide
- feat: check local sdk version
- feat(audit-panel): deal with taro mp setData
- feat(audit-score): research and implement audit score calculation
- feat(audit-experience): add more columns into experience metrics
- feat(audit-panel): Audit panel detect performance remaining metrics
- feat(audit-panel): detect render cost time | init render, setData render
- feat(audit): add experience related metric
- feat(audit-panel): implement audit panel best practice metrics
- feat(ide): mock open-type getPhoneNumber getEmailAddress behavior
- feat(audit-panel): optimize report context
- feat(ide-devtools-panel): audit panel render performance metrics
- feat(mock panel): optimize mock panel
- feat: show error message when webview fails to load

### Internal

- chore: bump @mp/host version
- docs: update v2.19.0-development.1 change log
- chore(changelog): update changelog for version v2.19.0

## [2.19.0-development.1]

**Download:
[MacOS](https://ftp.binance.com/mp-ide/mac/development/binance-devtools-2.19.0-development.1.dmg) |
[Windows](https://ftp.binance.com/mp-ide/windows/development/binance-devtools-setup-2.19.0-development.1.exe)**

### Bug Fixes

- fix: remove duplicate them change emit event
- fix: executeJavaScript causes bxml not to be displayed
- fix: bxml page node has redundant spaces
- fix(mock panel): fix ordered before existing data & generated template error
- fix(mock panel): fix some bugs
- fix: loading assets from resources
- fix: fix no proxy method when open IDE for the first time
- fix: fix-select-method
- fix(ide): remote debug
- fix: remove zx dependency

### Features

- feat: clean console context
- feat: clean console panel context selector
- feat: close watcher to stop compile
- feat: add mock sys
- feat: setdata cnt adjust and bug fix
- feat: integrate @mp/extended-lib
- feat(devtools): implement audit panel for detect setData

### Refactor

- refactor: plugin remove location, download-package, login
- refactor: Mock Panel Better user behavior
- refactor: move sensor plugin

### Internal

- chore(ide): @mp/host upgrade to 0.2.25
- chore: optimization code
- chore: universal link
- chore(changelog): update changelog for version v2.18.1
- chore: changelog automation