---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/download-development
api_type: Guide
updated_at: 2026-11-28 18:36:57.621558
---

# Download Development Version

## [5.12.0-dev.2] 2026-04-28

**Download: [5.12.0-dev.2(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.2.zip)**

### Features

- feat(sdk): editor support rtl

## [5.12.0-dev.1] 2026-04-26

**Download: [5.12.0-dev.1(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.1.zip)**

### Features

- feat(host): add RTL text direction and custom text align for editor

## [5.12.0-dev.0] 2026-04-21

**Download: [5.12.0-dev.0(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.0.zip)**

### Bug Fixes

- fix(sdk): add NODE_OPTIONS=--openssl-legacy-provider for Node 17+ build compat in renderer-mp
- fix(host): remove copy webpack plugin to fix copy-webpack-plugin v11 compat
- fix(host): add tslib 2.8.1 resolution for Node 24 exports compatibility
- fix(host): pin isolated-vm to 6.1.2 for Node 24 / C++20 compatibility
- fix(host): remove isolated-vm resolution, not used in project
- fix(host): return align and divider in editor mark, revert keepOnSplit override
- fix(cli): auto-recover from adb INSTALL_FAILED_UPDATE_INCOMPATIBLE
- fix(ide-cli): prevent infinite recursion in console-to-WebSocket forwarding

### Features

- feat(bundler): renderer components support shared chunks
- feat(native-cli): add Android inspector and native MCP tooling

## [5.11.0-dev.2] 2026-04-02

**Download: [5.11.0-dev.2(2.76 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.11.0-dev.2.zip)**

### Bug Fixes

- Fix/mp renderjs missing
- fix(sdk): add backward compatibility for ViewPager2 in SwiperView
- Fix/native cli preview UI layout
- Fix/type 0331

### Features

- feat(sdk): add QJS bytecode compilation for renderer-service-hummer
- feat(sdk): support virtual appid for widget

## [5.11.0-dev.1] 2026-03-31

**Download: [5.11.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.11.0-dev.1.zip)**

### Bug Fixes

- fix(cli): bundle native-cli resources and resolve adb
- fix: showErrorPage for 600402 page_not_found error
- fix(sdk): mcp bin
- fix(lib): fix ide cli toolbar sync api
- fix(cli): ide cli node version match

### Features

- feat(sdk): add useNewWindow parameter to previewImage API
- feat(cli): native-cli & ide-cli-mcp-server recover capabilities improve
- Feat/ios orba
- feat(cli): mcp tool stability improve
- feat(sdk): screen cast
- feat(cli): ide cli mcp server sync
- feat(cli): add mobile screen viewer and simulator host capture

## [5.10.0-dev.2] 2026-03-11

**Download: [5.10.0-dev.2(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.10.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix video props type
- fix(native-cli): prevent host hang on Ctrl+C

### Features

- feat(sdk): support root portal to specific element
- Feat/hummer lcp
- feat(cli): sub mode default render path
- feat(cli): native cli UI bridge
- feat(cli): orba desktop mp side work
- feat(cli): make get_log_files as example
- feat(cli): native cli UI dev env
- feat(cli): init native-cli project

## [5.10.0-dev.1] 2026-03-03

**Download: [5.10.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.10.0-dev.1.zip)**

### Features

- feat: fix error when stack is empty

## [5.9.0-dev.1] 2026-02-17

**Download: [5.9.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): swiper autoheight child item

### Features

- Feat/hummer swiper
- Feat/hummer event
- feat(cli): use custom ios runtime version
- feat(cli): ios simulator support
- feat(bundler): show error page when load module error

### Misc

- Revert " fix(sdk): sortable items when height changes " (#2522) (#2541)

## [5.8.0-dev.1] 2026-01-29

**Download: [5.8.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick 5.7.1
- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed

### Features

- feat(sdk): hummer gcanvas
- feat(sdk): load appjs when reload worker
- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool

## [5.8.0-dev.1] 2026-01-28

**Download: [5.8.0-dev.1(1.88 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed

### Features

- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool

## [5.7.0-dev.2] 2026-01-07

**Download: [5.7.0-dev.2(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.7.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId

## [5.7.0-dev.1] 2025-12-29

**Download: [5.7.0-dev.1(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.7.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): add internal doc site
- feat(cli): auto perf

## [5.6.0-dev.2] 2025-12-19

**Download: [5.6.0-dev.2(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.6.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix prerender inject data path

## [4.51.5-dev.1] 2025-12-18

**Download: [4.51.5-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.51.5-dev.1.zip)**

### Features

- feat(bundler): update terser
- feat(sdk): theme getter in systemInfo incorrect

## [5.6.0-dev.1] 2025-12-18

**Download: [5.6.0-dev.1(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.6.0-dev.1.zip)**

### Bug Fixes

- fix(sdk,bundler): init nativeScrollNegotiation/enableBackToTop config
- fix(sdk): reuse page issue on ios platform
- fix(sdk): text dont filter nest components
- fix(sdk): chain routechange handler when receviced multiple routechange
- fix(lib): add missing code back to protect web import

### Features

- feat(sdk): add extra type
- feat(sdk): support debug prefetch configuration
- feat(sdk): lottie comp support animationData props
- feat(bundler): update terser avoid bugs of old ver

## [5.5.0-dev.1] 2025-11-27

**Download: [5.5.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.5.0-dev.1.zip)**

### Features

- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.4.0-dev.2] 2025-11-06

**Download: [5.4.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.4.0-dev.2.zip)**

### Features

- feat(sdk): page timeline add check point

## [5.4.0-dev.1] 2025-11-05

**Download: [5.4.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.4.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android

### Features

- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum

## [5.3.0-dev.1] 2025-10-16

**Download: [5.3.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.3.0-dev.1.zip)**

### Features

- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [4.52.0-dev.1] 2025-10-14

**Download: [4.52.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.52.0-dev.1.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [5.3.0-dev.1] 2025-10-10

**Download: [5.3.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.3.0-dev.1.zip)**

### Bug Fixes

- fix(cli): version sort

### Features

- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [5.2.0-dev.1] 2025-09-25

**Download: [5.2.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.2.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix prerender measure
- fix(sdk): sdk5.2 cherry pick bn.removeWidgetSkeleton
- fix(sdk): inst id not exist
- fix(sdk): sdk5.2 cherry pick usePageScroll
- fix(sdk): sdk5.x hummer log & nezha debug flag
- fix(sdk): hotfix scrollview
- fix(sdk): avoid XSS attack
- fix(sdk): mounted to ensure nativeComponents context ready and dom instanceId for native widget
  map
- fix(mpp-service): ai meta info upload without widgets
- fix(sdk): remove unused log

### Features

- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion

## [4.51.0-dev.1] 2025-09-25

**Download: [4.51.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.51.0-dev.1.zip)**

### Features

- Feat call all
- feat(sdk): sdk4.x support support formatter for all echart options

## [5.1.4-dev.2] 2025-09-22

**Download: [5.1.4-dev.2(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.4-dev.2.zip)**

### Features

- feat(sdk): bn.removeWidgetSkeleton

## [5.1.4-dev.1] 2025-09-19

**Download: [5.1.4-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.4-dev.1.zip)**

### Bug Fixes

- fix(sdk): usePageScroll hooks not work
- fix(sdk): hummer renderer support update single child

## [5.1.0-dev.1] 2025-09-03

**Download: [5.1.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.0-dev.1.zip)**

### Bug Fixes

- fix(bmp): pika ci error
- fix(sdk): fix resolve native comp & input update timestamp
- fix(sdk): render child node directly when component need children vnode
- fix(sdk): host mini app events and setData damaged by widget flow
- fix: revert comment
- fix(sdk): @binance/bmp-xx deps
- fix(sdk): scrollViewUpdate rendererId undefined
- fix(lib): define EMPTY_OBJ

### Features

- feat(lib): support legacy dynamic widget slot
- feat(lib): release prod bmp-components and bmp-react
- feat(bundler): remove prerender data after build in
- feat(lib): update bmp component for ts
- feat(lib): support legacy widget-slot
- feat(sdk): update systemInfo cache when shellapp not restart
- feat(sdk): prerender remove skeleton auto
- feat(sdk): prerender support combined data
- feat(lib): update typo and EMPTY_OBJ
- feat(sdk): update taro-bn-components
- feat(lib): remove useTheme
- feat(bundler): support bundler version

### Misc

- Revert "Merge master"
- revert: root condition in setData

## [4.50.0-dev.1] 2025-09-03

**Download: [4.50.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.50.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): mounted to ensure nativeComponents context ready and dom instanceId for native widget
  map
- fix(mpp-service): ai meta info upload without widgets
- fix(sdk): remove unused log

### Features

- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion
- feat(bundler): support bundler version

## [4.48.0-dev.3] 2025-07-25

**Download: [4.48.0-dev.3(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay

## [4.48.0-dev.2] 2025-07-24

**Download: [4.48.0-dev.2(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.2.zip)**

### Features

- feat(sdk): revert autoheight default value to false

## [4.48.0-dev.1] 2025-07-24

**Download: [4.48.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.1.zip)**

### Bug Fixes

- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y

### Features

- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.47.0-dev.3] 2025-07-03

**Download: [4.47.0-dev.3(1.84 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): expose the error before app init

### Features

- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor

## [4.47.0-dev.2] 2025-06-30

**Download: [4.47.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.2.zip)**

### Features

- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar

## [4.47.0-dev.1] 2025-06-24

**Download: [4.47.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.1.zip)**

### Features

- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo

## [4.46.0-dev.3] 2025-06-13

**Download: [4.46.0-dev.3(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.3.zip)**

### Features

- feat(sdk): not set dataurl on style change

## [4.46.0-dev.2] 2025-06-13

**Download: [4.46.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.2.zip)**

### Features

- feat(sdk): w3w timeline monitor

## [4.46.0-dev.1] 2025-06-11

**Download: [4.46.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.3-dev.1] 2025-05-22

**Download: [4.45.3-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.45.3-dev.1.zip)**

## [4.45.0-dev.1] 2025-05-14

**Download: [4.45.0-dev.1(1.73 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.45.0-dev.1.zip)**

### Features

- feat(sdk): suspend & resume lifecycle

## [4.44.0-dev.1] 2025-04-29

**Download: [4.44.0-dev.1(1.73 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.44.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): set scroll top not work / request support enableCache
- fix(sdk): `show-scrollbar` doesn't work

### Features

- feat(sdk): support keyboard accessory item
- feat(sdk): remove sync api
- feat(sdk): domtoimage can ignore error when image not exist or load error
- feat(sdk): scrollview support enableBackToTop
- feat(sdk): showErrorPage support auto detect rendererId
- feat(sdk): flutter scrollView add events
- feat(cli): achieve pkg stability & log process stability optimization
- feat(host): support five themes
- feat(cli): support mcp refresh
- feat(sdk): remove hack worker patch
- feat(sdk): add dark_midnight support
- feat(bundler): support polyfill self and XMLHttpRequest
- feat(bundler): dynamic path by env. BUNDLER_PATCH
- feat(extended-lib): support extended lib uikit flow
- feat(host): support midnight

## [4.43.0-dev.2] 2025-04-10

**Download: [4.43.0-dev.2(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.43.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill

## [4.43.0-dev.1] 2025-04-09

**Download: [4.43.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.43.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix input textarea type adjustPosition

### Features

- feat(sdk): alpha chart for editor
- feat(sdk): new component flutter markdown
- feat(sdk): add `<Flex>` & `<Span>` components
- feat(sdk): support get prefetch data synchronous
- feat: update process-md-paths
- feat(cli): log process status indicator
- feat: update md jobs
- feat: add job to convert md path
- feat(cli): filter standalone-chunks while addEntry
- feat(sdk): input support max-digits-length
- feat(cli): use release version devtool
- feat(sdk): add runtime-plugin-create-event-source
- feat(cli): chrome devtools Integration - console
- feat: update llms.txt title and filter docs
- feat: add upload-docs-md job

## [4.42.0-dev.1] 2025-03-18

**Download: [4.42.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.42.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`

### Features

- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo

## [4.41.0-dev.1] 2025-03-04

**Download: [4.41.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

- feat(sdk): sortable support x-axis/free dragging
- feat(sdk): add image info type
- feat(sdk): init rem to avoid style issue in flutter renderer
- feat(sdk): widget support selectorQuery & intersectionObserver
- feat(sdk): implement lite-timeline sdk part
- feat(sdk): improve virtual scrollview
- feat(sdk): remove webf sync command during the initialization
- feat(sdk): support disableCleanStack and cleanOtherStack
- feat(sdk): increase priority of framework level message
- feat(runtime): add plugin `addEventListenerToBody`
- feat(server-side-bundle): add new qjs compilation

## [4.41.0-dev.3] 2025-02-28

**Download: [4.41.0-dev.3(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.3.zip)**

### Features

- feat(sdk): add image info type

## [4.41.0-dev.2] 2025-02-27

**Download: [4.41.0-dev.2(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.2.zip)**

### Features

- feat(sdk): init rem to avoid style issue in flutter renderer
- feat(sdk): widget support selectorQuery & intersectionObserver

## [4.41.0-dev.1] 2025-02-25

**Download: [4.41.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.1.zip)**

### Bug Fixes

- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

- feat(sdk): implement lite-timeline sdk part
- feat(sdk): improve virtual scrollview
- feat(sdk): remove webf sync command during the initialization
- feat(sdk): support disableCleanStack and cleanOtherStack
- feat(sdk): increase priority of framework level message
- feat(runtime): add plugin `addEventListenerToBody`
- feat(server-side-bundle): add new qjs compilation

## [4.40.0-dev.2] 2025-02-10

**Download: [4.40.0-dev.2(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.40.0-dev.2.zip)**

### Bug Fixes

- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices

### Features

- feat(sdk): add disable-ios-embed props for ios native input

## [4.40.0-dev.1] 2025-02-06

**Download: [4.40.0-dev.1(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.40.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2

### Features

- feat(sdk): get static template theme from body
- feat(sdk): support remove skeleton after static templete rendered
- feat(sdk): drawer support teleportTo
- feat(demo): add fixed page input demo
- feat(sdk): flutter svg support
- feat(sdk): input component can highlight the inputed content
- feat(sdk): flutter deprecated textarea add `cursor-spacing`
- feat(sdk): support auto zip sdk in watch mode
- feat(cli): add socket status indicator
- feat(bundler): support standalone-chunks

## [4.39.5-dev.1] 2025-01-22

**Download: [4.39.5-dev.1(2.57 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.39.5-dev.1.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.38.0-dev.2] 2024-12-26

**Download: [4.38.0-dev.2(2.50 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.38.0-dev.2.zip)**

### Features

- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error

## [4.38.0-dev.1] 2024-12-25

**Download: [4.38.0-dev.1(2.50 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.38.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed

### Features

- feat(sdk): add params in chooseFile
- feat(sdk): scrollview support flex height virtual list
- feat(sdk): svg inline tag performence improve
- feat(bmp): `<Lottie />` support events
- feat(sdk): `<lottie />` support switching animation
- feat(sdk): add `flutter-video` component
- feat(sdk): throw bmp app `onError`
- feat(sdk): add `<DualSlider>` component
- feat(extended-lib): update react/react-dom 18.3.1
- feat(sdk): echarts tooltip formatter support function
- feat(cli): ide cli build failed not catch
- feat(bmp): `PickerView` add options `maskClass|maskStyle|indicatorClass|indicatorStyle`
- feat(cli): fix hot reload & change package name to ide-cli

## [4.37.0-dev.3] 2024-12-05

**Download: [4.37.0-dev.3(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues

### Features

- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component

## [4.37.0-dev.2] 2024-12-03

**Download: [4.37.0-dev.2(2.46 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix page stack update timing

### Features

- feat(lib): bmp-components
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat: bundler
- feat: sortable component

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.37.0-dev.1] 2024-11-26

**Download: [4.37.0-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

## [4.36.0-dev.4] 2024-11-26

**Download: [4.36.0-dev.4(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

## [4.36.0-dev.3] 2024-11-14

**Download: [4.36.0-dev.3(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): change handlePaste defaultValue

## [4.36.0-dev.2] 2024-11-14

**Download: [4.36.0-dev.2(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.2.zip)**

## [4.36.0-dev.1] 2024-11-13

**Download: [4.36.0-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): remove native component background color
- fix(sdk): flutter-image remove eventListener

### Features

- feat(sdk): add switch tab options in api
- feat(sdk): add timeformat api
- feat(sdk): add showBackButton api
- feat(sdk): `native-textarea` add onPaste
- feat(sdk): `native-textarea` add `alwaysEmbed`
- feat(sdk): add the value of input type `decimals`
- feat(sdk): flutter-deprecated-textarea add `autoFocus`

## [4.35.2-dev.1] 2024-11-07

**Download: [4.35.2-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): release flutter image load
- fix(sdk): wrap inline element with bn-span for bn-markdown

### Misc

- Revert "chore: revert ui command"

## [4.35.0-dev.4] 2024-10-25

**Download: [4.35.0-dev.4(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): support inlineLayout for skyline

### Features

- feat(sdk): new api page.updateRouteOptions

## [4.35.0-dev.3] 2024-10-24

**Download: [4.35.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): flutter scroll refresher background color

### Features

- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo

## [4.35.0-dev.2] 2024-10-24

**Download: [4.35.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.2.zip)**

### Features

- feat(sdk): use tap for skyline

## [4.35.0-dev.1] 2024-10-23

**Download: [4.35.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): android quickjs unsupport Unicode Property Escapes
- fix(sdk): cherry pick webview message issue
- fix(sdk): re-publish @mp/runtime-plugin-enable-sheet-gesture
- fix(sdk): fix cursor issue
- fix(runtime): premature return issue in ide enviroment's show-modal api
- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly

### Features

- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.35.0-dev.1] 2024-10-17

**Download: [4.35.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly

### Features

- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.34.0-dev.3] 2024-10-04

**Download: [4.34.0-dev.3(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix webview message action not work

### Features

- feat(host): align response with native

## [4.34.0-dev.2] 2024-10-03

**Download: [4.34.0-dev.2(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.2.zip)**

### Features

- feat(sdk): flutter text component

## [4.34.0-dev.1] 2024-10-02

**Download: [4.34.0-dev.1(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-dev.4] 2024-10-01

**Download: [4.33.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-dev.4] 2024-09-30

**Download: [4.33.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-rc.1] 2024-09-12

**Download: [4.33.0-rc.1(NaN MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-rc.1.zip)**

## [4.33.0-dev.3] 2024-09-12

**Download: [4.33.0-dev.3(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop

### Features

- feat(demo): error handler demo
- feat(sdk): add deeplink target type

## [4.33.0-dev.2] 2024-09-12

**Download: [4.33.0-dev.2(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix component patch error messsage

### Features

- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs

## [4.33.0-dev.1] 2024-09-10

**Download: [4.33.0-dev.1(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type

### Features

- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)

## [4.32.0-dev.2] 2024-08-22

**Download: [4.32.0-dev.2(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.32.0-dev.2.zip)**

### Features

- feat(sdk): drawer component

## [4.32.0-dev.1] 2024-08-22

**Download: [4.32.0-dev.1(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.32.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory

### Features

- feat(bundler): support static script, do not bundle into \_app.js and \_common.js
- feat(bundler): mark build is done before send pageBundled
- feat(bundler): add entry must trigger a rebuild
- feat(sdk): scroll view support extra data prop
- feat(sdk): performance babel plugin log format with timeline
- feat(sdk): flutter scroll-view
- feat(bundler): update watch page utils
- feat(bundler): support ignore qjs options
- feat(bundler): skeleton create style tags by script to avoid webf issues
- feat(sdk): remove game script in sdk
- feat(sdk): flutter scroll view
- feat(sdk): add props for input
- feat(bundler): update bundler for host
- feat(doc): update doc
- feat(demo): add input unfocuse issue
- feat(sdk): lcp element timeline metrics

## [4.31.0-dev.2] 2024-07-31

**Download: [4.31.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.31.0-dev.2.zip)**

### Bug Fixes

- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler

### Features

- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode

## [4.31.0-dev.1] 2024-07-24

**Download: [4.31.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.31.0-dev.1.zip)**

### Features

- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components

## [4.30.0-dev.3] 2024-07-12

**Download: [4.30.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): native component webview message

## [4.30.0-dev.2] 2024-07-11

**Download: [4.30.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): native event in worker
- fix(sdk): fix webview component

### Features

- feat(sdk): webview component event api in queryselector

## [4.30.0-dev.1] 2024-07-10

**Download: [4.30.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error

### Features

- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js

## [4.29.0-dev.2] 2024-06-20

**Download: [4.29.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.29.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure

### Features

- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton

## [4.29.0-dev.1] 2024-06-13

**Download: [4.29.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.29.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cursor is wired when editor tap keyboard enter

### Features

- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%

## [4.28.0-dev.1] 2024-05-28

**Download: [4.28.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.28.0-dev.1.zip)**

### Features

- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line

## [4.27.0-dev.4] 2024-05-09

**Download: [4.27.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload

## [4.27.0-dev.3] 2024-05-08

**Download: [4.27.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.3.zip)**

### Features

- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app

## [4.27.0-dev.2] 2024-04-30

**Download: [4.27.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.2.zip)**

### Features

- feat(sdk): api hide back button

## [4.27.0-dev.1] 2024-04-26

**Download: [4.27.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.1.zip)**

### Bug Fixes

- fix(extended-lib): postpublish script throw error

### Features

- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int

## [4.26.0-w3w] 2024-04-22

**Download: [4.26.0-w3w(NaN MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.26.0-w3w.zip)**

### Bug Fixes

- fix(host): support webassembly on host

### Features

- feat(sdk): web3 plugin use shell app
- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document

## [4.26.0-dev.1] 2024-04-17

**Download: [4.26.0-dev.1(2.41 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.26.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions

### Features

- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded

## [4.25.0-dev.2] 2024-03-27

**Download: [4.25.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.25.0-dev.2.zip)**

### Bug Fixes

- fix(extended-lib): add missing deps

### Features

- feat(sdk): custom native component

## [4.25.0-dev.1] 2024-03-27

**Download: [4.25.0-dev.1(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.25.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type

### Features

- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration

## [4.23.0-dev.2] 2024-02-16

**Download: [4.23.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.23.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): when user delete all content web input may act unexpected

## [4.23.0-dev.1] 2024-02-16

**Download: [4.23.0-dev.1(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.23.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE

### Features

- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define

## [4.22.0-dev.2] 2024-01-24

**Download: [4.22.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.22.0-dev.2.zip)**

### Features

- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable

## [4.22.0-dev.1] 2024-01-22

**Download: [4.22.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.22.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): label trigger itemClick event for radio and checkbox

### Features

- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content

## [4.21.0-dev.1] 2024-01-08

**Download: [4.21.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.21.0-dev.1.zip)**

### Features

- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB

## [4.20.0-dev.1] 2023-12-12

**Download: [4.20.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.20.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter

## [4.19.0-dev.3] 2023-11-22

**Download: [4.19.0-dev.3(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.3.zip)**

### Bug Fixes

- fix(bundler): fix IDE can not reload

### Features

- feat(sdk): cherry-pick: add preloadflutterwebview api

## [4.19.0-dev.2] 2023-11-21

**Download: [4.19.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.2.zip)**

### Features

- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event

## [4.19.0-dev.1] 2023-11-14

**Download: [4.19.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.1.zip)**

### Features

- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor

## [4.18.0-dev.3] 2023-11-02

**Download: [4.18.0-dev.3(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value

### Features

- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection

## [4.18.0-dev.2] 2023-10-30

**Download: [4.18.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.2.zip)**

### Features

- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list

## [4.17.2-dev.1] 2023-10-23

**Download: [4.17.2-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

## [4.18.0-dev.1] 2023-10-23

**Download: [4.18.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

### Features

- feat(sdk): editor support mention and hardBreak

## [4.16.3-dev.1] 2023-10-13

**Download: [4.16.3-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.3-dev.1.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.17.0-dev.2] 2023-10-13

**Download: [4.17.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

### Features

- feat(lib): bmp-api openWidget add support for convention path

## [4.17.0-dev.1] 2023-10-10

**Download: [4.17.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger

### Features

- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget

## [4.16.0-dev.2] 2023-09-19

**Download: [4.16.0-dev.2(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.0-dev.2.zip)**

### Bug Fixes

- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper

### Features

- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles

## [4.16.0-dev.1] 2023-09-11

**Download: [4.16.0-dev.1(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): bundler watch has 60s cache

### Features

- feat(sdk): editor internal plugin link support

## [4.15.0-dev.3] 2023-08-29

**Download: [4.15.0-dev.3(2.34 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots

### Features

- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers

## [4.15.0-dev.2] 2023-08-25

**Download: [4.15.0-dev.2(2.34 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci

### Features

- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter

## [4.15.0-dev.1] 2023-08-17

**Download: [4.15.0-dev.1(1.45 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount

### Features

- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs

## [4.14.0-dev.2] 2023-08-09

**Download: [4.14.0-dev.2(1.45 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.14.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): customize component data not update when return a data getter

### Features

- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata

## [4.14.0-dev.1] 2023-08-01

**Download: [4.14.0-dev.1(1.46 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.14.0-dev.1.zip)**

### Bug Fixes

- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop

### Features

- feat(sdk): editor paste event props
- feat(sdk): echart component

## [4.13.1-dev.1] 2023-07-27

**Download: [4.13.1-dev.1(1.15 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor split figure bugs
- fix(sdk): object spread sytax error
- fix(sdk): add seqId to web input event

## [4.13.0-dev.2] 2023-07-26

**Download: [4.13.0-dev.2(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.0-dev.2.zip)**

### Bug Fixes

- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer

### Misc

- Revert "fix(sdk): iOS native component created failed when container is not visible "

## [4.13.0-dev.1] 2023-07-18

**Download: [4.13.0-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.0-dev.1.zip)**

### Bug Fixes

- fix(demo): editor toolbar bottom 0 when platform is not iOS
- fix(sdk): iOS native component created failed when container is not visible
- fix: cherry-pick from 4.12.1
- fix(sdk): cancel load-script when redirect
- fix(lib): add type of removeSkeleton

### Features

- feat(sdk): editor selectImage api
- feat(mpp-service) add released pr
- feat(sdk): support walletkit and init func
- feat(demo): add manual to web input public demo

## [4.12.0-dev.1] 2023-06-28

**Download: [4.12.0-dev.1(1.13 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.12.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs

### Features

- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image

### Performance Improvements

- perf: add filesystem cache

## [4.11.0-dev.3] 2023-06-09

**Download: [4.11.0-dev.3(1.13 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo

## [4.11.0-dev.2] 2023-06-07

**Download: [4.11.0-dev.2(1.12 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images

### Features

- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider

## [4.10.2-dev.1] 2023-06-06

**Download: [4.10.2-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix startCheckPageTimeline error

## [4.11.0-dev.1] 2023-05-29

**Download: [4.11.0-dev.1(1.11 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work

### Features

- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API

## [4.10.1-dev.1] 2023-05-25

**Download: [4.10.1-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): renderer service compatitable with es5

## [4.10.0-dev.4] 2023-05-19

**Download: [4.10.0-dev.4(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend

### Features

- feat(demo): add prefetchRules

## [4.9.2-dev.1] 2023-05-19

**Download: [4.9.2-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params

## [4.10.0-dev.3] 2023-05-18

**Download: [4.10.0-dev.3(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack

### Features

- feat(sdk): getUserOpenId return token

## [4.9.1-dev.2] 2023-05-17

**Download: [4.9.1-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.1-dev.2.zip)**

## [4.10.0-dev.2] 2023-05-16

**Download: [4.10.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): load page frame after load base.bxml success

## [4.10.0-dev.1] 2023-05-15

**Download: [4.10.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.1.zip)**

### Bug Fixes

- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found

### Features

- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs

## [4.9.1-dev.1] 2023-05-15

**Download: [4.9.1-dev.1(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): update load script error code

### Features

- feat(sdk): use appConfig after init appConfig & add appConfig detection & syncGetPage or
  asyncGetPage
- feat(host): set custom http headers for fetch requests

## [4.9.0-dev.3] 2023-04-26

**Download: [4.9.0-dev.3(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.3.zip)**

### Bug Fixes

- fix(demo): production convertToMPUrl usage

### Features

- feat(sdk): ut from plugin-location to plugin-request-subscribe-message

## [4.9.0-dev.2] 2023-04-25

**Download: [4.9.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise

### Features

- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo

## [4.9.0-dev.1] 2023-04-24

**Download: [4.9.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs

### Features

- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher

## [4.9.0-dev.1] 2023-04-24

**Download: [4.9.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs

### Features

- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher

## [4.8.0-dev.2] 2023-04-06

**Download: [4.8.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.8.0-dev.2.zip)**

### Features

- feat(sdk): bids use monitorupload
- feat(demo): editor component demo

## [4.8.0-dev.1] 2023-04-04

**Download: [4.8.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version

### Features

- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API

# Download Development Version

## [4.7.0-dev.6] 2023-03-17

**Download: [4.7.0-dev.6(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.6.zip)**

### Bug Fixes

- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources

## [4.7.0-dev.5] 2023-03-16

**Download: [4.7.0-dev.5(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue

## [4.7.0-dev.4] 2023-03-16

**Download: [4.7.0-dev.4(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel

## [4.7.0-dev.3] 2023-03-14

**Download: [4.7.0-dev.3(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus

### Features

- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation

## [4.7.0-dev.2] 2023-03-13

**Download: [4.7.0-dev.2(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): editor focus and mark

### Features

- feat(sdk): catch html
- feat(sdk): figure

## [4.7.0-dev.1] 2023-03-09

**Download: [4.7.0-dev.1(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.1.zip)**

### Bug Fixes

- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue

### Features

- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly

## [4.6.0-dev.2] 2023-02-22

**Download: [SDK-4.6.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.6.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): add native-send-appLuanch timer
  ([532dde2e](https://git.toolsfdg.net/fe/mini-program/commit/532dde2e37e8c3ff48cbf655238b88a9a1ff0dcd))
  by finley.x@binance.com

### Internal

- chore: bump commit after write files
  ([9378fed1](https://git.toolsfdg.net/fe/mini-program/commit/9378fed122a9613f50aac333ff8543d12893bbbc))
  by dylan.z@binance.com

## [4.6.0-dev.1] 2023-02-21

**Download: [SDK-4.6.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.6.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): css variables rpx to rem align with wechat
  ([5fcfd131](https://git.toolsfdg.net/fe/mini-program/commit/5fcfd1319437e3fd52389083be12f459cb53d243))
  by dylan.z@binance.com
- fix(sdk): mini game view port size
  ([fc6048f0](https://git.toolsfdg.net/fe/mini-program/commit/fc6048f03ed5b9cb7357654e8a5699124fa38898))
  by henry.w@binance.com
- fix(sdk): getChildrenNode util function
  ([7c5764b6](https://git.toolsfdg.net/fe/mini-program/commit/7c5764b60831fa1c194490a907a1ad10e7ded92b))
  by henry.w@binance.com
- fix(sdk): rendererId zero issue in native ui
  ([c3d9020b](https://git.toolsfdg.net/fe/mini-program/commit/c3d9020b10630ac6c12f71595fb3c80cd3e7d2cf))
  by dylan.z@binance.com
- fix(bundler): catchmove value should be an exp
  ([dc53e87f](https://git.toolsfdg.net/fe/mini-program/commit/dc53e87f6ccb59b859b0eb13171f5038c98910da))
  by lawrence.w@binance.com
- fix(sdk): swiper Item blank
  ([7981ff89](https://git.toolsfdg.net/fe/mini-program/commit/7981ff894557f9145b619a68c823252654826014))
  by finley.x@binance.com
- fix(demo): fix custom demo textarea maxlength
  ([c28c58aa](https://git.toolsfdg.net/fe/mini-program/commit/c28c58aa2556d9e8eb21ef3b46269461bcf308c4))
  by henry.w@binance.com

### Features

- feat(demo): control picker view demo
  ([b80c088c](https://git.toolsfdg.net/fe/mini-program/commit/b80c088cd6307f659af3fba713787becc824479c))
  by lawrence.w@binance.com
- feat(sdk): detect page timeline
  ([0b1381a4](https://git.toolsfdg.net/fe/mini-program/commit/0b1381a4406d0767f736836a8418aede38ccd44f))
  by finley.x@binance.com
- feat(host): support pageReadyCallback
  ([1339544e](https://git.toolsfdg.net/fe/mini-program/commit/1339544ec010a520efab2e822bfe15d4249fdc66))
  by dylan.z@binance.com

### Refactor

- refactor: remove any type in AppCommandMap
  ([9b2411bd](https://git.toolsfdg.net/fe/mini-program/commit/9b2411bde6250820403082572e38070d9c9fc443))
  by lucifer.l@binance.com

### Internal

- docs: add api comment for documentation
  ([7993a741](https://git.toolsfdg.net/fe/mini-program/commit/7993a741307a4049768fcfe771cfbb3ad6231723))
  by dylan.z@binance.com
- chore: update bump with git auto push
  ([e25b674f](https://git.toolsfdg.net/fe/mini-program/commit/e25b674f8ed8fd0638bc25122a9d8c6efb223d6d))
  by dylan.z@binance.com
- chore: change UT coverage scope and threshold
  ([50820980](https://git.toolsfdg.net/fe/mini-program/commit/50820980c6a0d517e0a19df8d2ed740965c36f40))
  by lucifer.l@binance.com
- docs: format issue
  ([05c3cc6e](https://git.toolsfdg.net/fe/mini-program/commit/05c3cc6e632ea84fc316a8db27fa7c9337d2ca24))
  by dylan.z@binance.com
- docs: update config
  ([aaae5561](https://git.toolsfdg.net/fe/mini-program/commit/aaae556164f3bd260fbed971c490f090b6327a25))
  by dylan.z@binance.com
- docs: excited features of the JSCore team 202302
  ([1b38cbfe](https://git.toolsfdg.net/fe/mini-program/commit/1b38cbfe6c2344120f532eed76bda7a6990a7fc8))
  by dylan.z@binance.com
- [WIP]fix(sdk): controlled picker view
  ([661aa89a](https://git.toolsfdg.net/fe/mini-program/commit/661aa89ad9c3289ce614f2b77995d4ebf6d08bfa))
  by lawrence.w@binance.com
- mpp service support binance us host app
  ([fb8edeb8](https://git.toolsfdg.net/fe/mini-program/commit/fb8edeb8c6840cc84ef840c6ca84dcfc3a51fd72))
  by leo.cc@binance.com

# [4.5.1-dev.1] 2023-02-14

**Download: [SDK-4.5.1-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([01449416](https://git.toolsfdg.net/fe/mini-program/commit/01449416c3989a0e9d2e89811987e30c8d40bdbd))
  by lawrence.w@binance.com

## [3.14.16-dev.1] 2023-02-10

**Download: [SDK-3.14.16-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.16-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([d9a10d59](https://git.toolsfdg.net/fe/mini-program/commit/d9a10d599fb2ab6d7c222c2204917dcd7511a888))
  by lawrence.w@binance.com

# [4.5.0-dev.2] 2023-02-01

**Download: [SDK-4.5.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix requestBinanceCardInfo error response & cicd
  ([b18093ab](https://git.toolsfdg.net/fe/mini-program/commit/b18093abab0f1aa938d804d91d93e6c55e2ba949))
  by lawrence.w@binance.com
- fix(bundler): compile optional chaining when using latest caniuse-lite
  ([771dc7af](https://git.toolsfdg.net/fe/mini-program/commit/771dc7af2ea7eb809d3c3834f5733052dfb6df27))
  by jolin.h@binance.com
- fix(sdk): android css transition native component
  ([a70840e6](https://git.toolsfdg.net/fe/mini-program/commit/a70840e6d95fd2488bfe0993377224da6defa855))
  by henry.w@binance.com

### Features

- feat(sdk): add binance-card-info api
  ([65680864](https://git.toolsfdg.net/fe/mini-program/commit/65680864e327d5b81eca872e11ca4db55039948e))
  by lawrence.w@binance.com
- feat(demo): migrate to pika
  ([8cdffe8c](https://git.toolsfdg.net/fe/mini-program/commit/8cdffe8c1f46bb9181a915b7f21fc9a512db2063))
  by dylan.z@binance.com
- feat(sdk): jssdk dashboard rename & calculate
  ([ea78ac01](https://git.toolsfdg.net/fe/mini-program/commit/ea78ac01e11f57278428b190b600e0e008e0fc53))
  by finley.x@binance.com
- feat(sdk): wallet connector use new wallet provider
  ([ca346f5d](https://git.toolsfdg.net/fe/mini-program/commit/ca346f5d4f9560ae2fb59c2c2fdbb251eb8f4a33))
  by zane.x@binance.com

### Refactor

- refactor: throw error for the non-supported apis in IDE
  ([62e2ad65](https://git.toolsfdg.net/fe/mini-program/commit/62e2ad659b2143dd6eac1567fb2016758a4294e6))
  by lucifer.l@binance.com

### Internal

- docs: remove the app.config.json issue since pika will support it
  ([747343ed](https://git.toolsfdg.net/fe/mini-program/commit/747343ed66a9de848d6399a9e9521a6ba5f883e1))
  by dylan.z@binance.com

## [4.5.0-dev.1] 2023-01-18

**Download: [SDK-4.5.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.0-dev.1.zip)**

### Features

- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react

### Internal

- docs: getCurrentInstance query incorrect

## [4.4.0-dev.5] 2023-01-12

**Download: [SDK-4.4.0-dev.5](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type

## [4.4.0-dev.4] 2023-01-11

**Download: [SDK-4.4.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): mpc method
- fix(lib): update types of bmp-react

### Features

- feat(sdk): webview component supports message

### Internal

- chore: update config for FAQ
- docs: faq about app.config.json

## [4.4.0-dev.3] 2023-01-10

**Download: [SDK-4.4.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): types of bn.call & add RootPortal to bmp-components

### Features

- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option

### Internal

- docs(sdk): darkmode

## [4.4.0-dev.2] 2023-01-06

**Download: [SDK-4.4.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.2.zip)**

### Bug Fixes

- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info

### Features

- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114

## [4.4.0-dev.1] 2023-01-04

**Download: [SDK-4.4.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes

### Features

- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal

### Internal

- chore(sdk): cherry pick update sdk loading
- test: add more unit tests for host

## [4.3.0-dev.4] 2022-12-22

**Download: [SDK-4.3.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): mini game keyboard event

### Features

- feat: integrate automator on CI

### Internal

- chore: remove `yarn playwright install --with-deps`

## [4.3.0-dev.3] 2022-12-21

**Download: [SDK-4.3.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.3.zip)**

### Bug Fixes

- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target

### Features

- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar

### Refactor

- refactor: rename host-mp-ide to host-ide

### Internal

- docs(sdk): integrate with doc-system
- chore(package.json): fix installing sqllite3 in macos

## [4.3.0-dev.2] 2022-12-19

**Download: [SDK-4.3.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.2.zip)**

### Bug Fixes

- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14

### Features

- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI

### Internal

- chore(package.json): add packageManager field
- chore: replace resolve with join
- chore(sdk): cherry-pick from 4.2.1
- chore: update version remote and pwd alias

## [4.3.0-dev.1] 2022-12-14

**Download: [SDK-4.3.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.1.zip)**

### Bug Fixes

- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css

### Features

- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo

### Internal

- chore: bump local
- chore: update prefetch rule of component demo
- docs: demos readme

## [4.2.0-dev.4] 2022-11-30

**Download: [SDK-4.2.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.4.zip)**

### Bug Fixes

- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height

### Features

- feat(sdk): gcanvas optimazation

### Internal

- chore: remove useless message in changelog.md by 'bot'

## [4.2.0-dev.3] 2022-11-30

**Download: [SDK-4.2.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.3.zip)**

### Bug Fixes

- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces

### Features

- feat(demo): add a rendererId 0 issue test case

### Refactor

- refactor(sdk): plugins including show-leaderboard, storage and tab-bar

### Internal

- chore: redirect blank page issue

## [4.2.0-dev.2] 2022-11-24

**Download: [SDK-4.2.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.2.zip)**

### Bug Fixes

- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS

### Refactor

- refactor(sdk): native ui plugin
- refactor(sdk): replace enum with union type

### Internal

- chore(changelog): @mp/worker-mg@1.0.23
- chore(changelog): @mp/server-side-bundle@1.0.15
- chore(changelog): @mp/runtime-service-web@0.2.29
- chore(changelog): @mp/gen-sdk@1.0.25
- chore(changelog): @mp/host@0.2.58
- chore(changelog): @binance/mp-automator@2.0.7
- chore(changelog): @mp/remote-debug@1.0.25
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.24
- chore(changelog): @mp/runtime-plugin-user-info@1.0.16
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.15
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.13
- chore(changelog): @mp/plugins-mg@1.0.48
- chore(changelog): @mp/runtime-plugin-download-package@1.0.16
- chore(changelog): @mp/webview@1.0.16
- chore(changelog): @mp/runtime-plugin-performance@1.0.19
- chore(changelog): @mp/runtime-plugin-fps@1.0.9
- chore(changelog): @mp/app-command@1.0.18
- chore(changelog): @mp/runtime-plugin-create-intersection-observer@1.0.9
- chore(changelog): @mp/runtime-plugin-wallet-connector@1.0.5
- chore(changelog): @mp/runtime-plugin-current-ui-event@1.0.9
- chore(changelog): @mp/plugins-mp-internal@1.0.15
- chore(changelog): @mp/runtime-plugin-sensor-compass@1.0.8
- chore(changelog): @mp/runtime-plugin-app-lifecycle@1.0.8
- chore(changelog): @mp/runtime-plugin-system-info@1.0.13
- chore(changelog): @mp/runtime-plugin-sensor-gyroscope@1.0.8
- chore(changelog): @mp/runtime-plugin-keyboard@1.0.8
- chore(changelog): @mp/runtime-plugin-request-subscribe-message@1.0.6
- chore(changelog): @mp/runtime-plugin-sensor-accelerometer@1.0.8
- chore(changelog): @mp/runtime-plugin-app-internal@1.0.10
- chore(changelog): @mp/runtime-plugin-custom-plugin@1.0.13
- chore(changelog): @mp/runtime-plugin-ensure-logged-in@1.0.7
- chore(changelog): @mp/runtime-plugin-share-panel@1.0.11
- chore(changelog): @mp/runtime-plugin-inner-audio@1.0.7
- chore(changelog): @mp/runtime-plugin-update-manager@1.0.13
- chore(changelog): @mp/runtime-plugin-location@1.0.9
- chore(changelog): @mp/runtime-plugin-save-image-to-photos-album@1.0.8
- chore(changelog): @mp/runtime-plugin-audio-interruption@1.0.7
- chore(changelog): @mp/runtime-plugin-websocket@1.0.13
- chore(changelog): @mp/runtime-plugin-sensor-device-motion@1.0.8
- chore(changelog): @mp/runtime-plugin-upload-file@1.0.12
- chore(changelog): @mp/runtime-plugin-share-menu@1.0.5
- chore(changelog): @mp/runtime-plugin-scan-code@1.0.8
- chore(changelog): @mp/runtime-plugin-file-system-manager@1.0.8
- chore(changelog): @mp/runtime-plugin-create-webview@1.0.12
- chore(changelog): @mp/runtime-plugin-authorize@1.0.6
- chore(changelog): @mp/runtime-plugin-error-page@1.0.9
- chore(changelog): @mp/runtime-plugin-image-info@1.0.14
- chore(changelog): @mp/runtime-plugin-make-phone-call@1.0.6
- chore(changelog): @mp/runtime-plugin-can-use@1.0.14
- chore(changelog): @mp/bundler@3.0.9
- chore(changelog): @mp/runtime-plugin-framework-storage@1.0.4
- chore(changelog): @mp/runtime-plugin-choose-image@1.0.8
- chore(changelog): @mp/host-core@1.0.14
- chore(changelog): @binance/mp-cli@2.4.29
- chore(changelog): @mp/mpp-service@1.0.34
- chore(changelog): update changelog for version v4.2.0-dev.1
- chore(changelog): @binance/mp-web@0.0.34
- chore(changelog): @binance/mp-automator@2.0.5
- chore(changelog): @mp/runtime-sdk-electron@0.1.28
- chore(changelog): @mp/host@0.2.57
- chore(changelog): @mp/gen-sdk@1.0.24
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.23
- chore(changelog): @mp/runtime-service-web@0.2.28
- chore(changelog): @mp/remote-debug@1.0.24
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.12
- chore(changelog): @mp/plugins-mp@1.0.47
- chore(changelog): @mp/plugins-mg@1.0.47
- chore(changelog): @mp/runtime-worker-common@1.0.26
- chore(changelog): @mp/runtime-plugin-download-package@1.0.15
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.14

## [4.2.0-dev.1] 2022-11-23

**Download: [SDK-4.2.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.1.zip)**

### Bug Fixes

- fix(automator): fix some bugs & add `.waitFor`
- fix(sdk): native component css
- fix(sdk): (cherry-pick) reduce the blank page
- fix(runtime): no need to add webview when open new page
- fix(demo): input style of storage pages & update privatePrefetchRules
- fix(sdk): cherry pick - load-script-progress event when mp background event to lead blank screen
- fix(sdk): cherry pick fix location plugin
- fix(cli): skip generation of unmatched tags
- fix(demo): request pages issue of component-demo
- fix(sdk): load \_\_app.js after $ready
- fix(sdk): remove generating worker-service-game.qjs
- fix(runtime): vibrate shifting bug
- fix(demo): show isPrefetch in request pages

### Features

- feat(sdk): demo update & delete appTimeline
- feat(sdk): native webview component
- feat(demo): runtime benchmark add getAppBaseInfo apis
- feat(sdk): (cherry-pick)support caretColor for Input and TextArea components
- feat(automator): automator added headless option & refactor `.launch` & demo page
- feat(demo): move sync-api-demo to component-demo & update prefetchRules
- feat(sdk): api on add to favorites
- feat(bundler): generate fileTree for analyzeSource
- feat(sdk): first render new fields
- feat(runtime): support selecting sdk

### Refactor

- refactor(host): plugin user-info
- refactor(host): plugin & remove twoFA demo

### Internal

- chore(changelog): @mp/runtime-service-web@0.2.27
- chore(changelog): @mp/server-side-bundle@1.0.13
- chore(changelog): @binance/mp-automator@2.0.4
- chore(changelog): @binance/mp-web@0.0.33
- chore(changelog): @mp/runtime-sdk-electron@0.1.27
- chore(changelog): @mp/gen-sdk@1.0.23
- chore(changelog): @mp/runtime-worker-common@1.0.25
- chore(changelog): @mp/worker-mg@1.0.21
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.22
- chore(changelog): @mp/remote-debug@1.0.23
- chore(changelog): @mp/host@0.2.56
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.11
- chore(changelog): @mp/plugins-mg@1.0.46
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.13
- chore(changelog): @mp/runtime-plugin-user-info@1.0.15
- chore(changelog): @mp/runtime-plugin-download-package@1.0.14
- chore(changelog): @mp/webview@1.0.15
- chore(changelog): @mp/runtime-plugin-performance@1.0.17
- chore(changelog): @mp/runtime-plugin-fps@1.0.8
- chore(changelog): @mp/app-command@1.0.17
- chore(changelog): @mp/runtime-plugin-create-selector-query@1.0.11
- chore(changelog): @mp/runtime-plugin-wallet-connector@1.0.4
- chore(changelog): @mp/runtime-plugin-create-intersection-observer@1.0.8
- chore(changelog): @mp/runtime-plugin-current-ui-event@1.0.8
- chore(changelog): @mp/runtime-plugin-request-subscribe-message@1.0.5
- chore(changelog): @mp/runtime-plugin-app-lifecycle@1.0.7
- chore(changelog): @mp/runtime-plugin-ensure-logged-in@1.0.6
- chore(changelog): @mp/plugins-mg-internal@1.0.13
- chore(changelog): @mp/runtime-plugin-update-manager@1.0.12
- chore(changelog): @mp/runtime-plugin-auth-capture@1.0.6
- chore(changelog): @mp/runtime-plugin-sensor-gyroscope@1.0.7
- chore(changelog): @mp/runtime-plugin-upload-file@1.0.11
- chore(changelog): @mp/runtime-plugin-web3@1.0.4
- chore(changelog): @mp/runtime-plugin-network@1.0.8
- chore(changelog): @mp/runtime-plugin-websocket@1.0.12
- chore(changelog): @mp/runtime-plugin-save-image-to-photos-album@1.0.7
- chore(changelog): @mp/runtime-plugin-sensor-compass@1.0.7
- chore(changelog): @mp/runtime-plugin-sensor-orientation@1.0.6
- chore(changelog): @mp/runtime-plugin-image-info@1.0.13
- chore(changelog): @mp/runtime-plugin-location@1.0.8
- chore(changelog): @mp/mpp-service@1.0.33
- chore(changelog): @mp/runtime-plugin-app-internal@1.0.9
- chore(changelog): @mp/runtime-plugin-keyboard@1.0.7
- chore(changelog): @mp/runtime-plugin-custom-plugin@1.0.12
- chore(changelog): @mp/runtime-plugin-share-panel@1.0.10
- chore(changelog): @mp/runtime-plugin-download-file@1.0.6
- chore(changelog): @mp/runtime-plugin-choose-image@1.0.7
- chore(changelog): @mp/runtime-plugin-make-phone-call@1.0.5
- chore(changelog): @mp/runtime-plugin-authorize@1.0.5
- chore(changelog): @mp/runtime-plugin-system-info@1.0.12
- chore(changelog): @mp/runtime-plugin-preview-image@1.0.8
- chore(changelog): @mp/runtime-plugin-scan-code@1.0.7
- chore(changelog): @mp/runtime-plugin-on-off@1.0.9
- chore(changelog): @mp/runtime-plugin-create-webview@1.0.11
- chore(changelog): @mp/runtime-plugin-can-use@1.0.13
- chore(changelog): @mp/runtime-plugin-clipboard@1.0.7
- chore(changelog): @mp/bundler@3.0.7
- chore(changelog): @mp/runtime-plugin-file-system-manager@1.0.7
- chore(changelog): @mp/runtime-plugin-favorite@1.0.2
- chore(changelog): @mp/runtime-shared@1.0.15
- chore(changelog): @mp/host-core@1.0.13
- chore(changelog): @binance/mp-cli@2.4.28
- chore(changelog): @binance/mp-web@0.0.32
- chore(changelog): @binance/mp-automator@2.0.3
- chore(changelog): @binance/mp-automator@2.0.2
- chore(changelog): @mp/runtime-sdk-electron@0.1.26
- chore(changelog): @mp/runtime-service-web@0.2.26
- chore(changelog): @binance/mp-web@0.0.31
- chore(changelog): @mp/host@0.2.55
- chore(changelog): @mp/worker-mg@1.0.20
- chore(changelog): @mp/remote-debug@1.0.22
- chore(changelog): @mp/plugins-mg@1.0.45
- chore(changelog): @mp/runtime-worker-common@1.0.24
- chore(changelog): @mp/runtime-plugin-download-package@1.0.13
- chore(changelog): @mp/runtime-plugin-performance@1.0.16
- chore(changelog): update changelog for version v3.14.8
- chore(changelog): @mp/runtime-service-web@0.2.25
- chore(changelog): @mp/gen-sdk@1.0.21
- chore(changelog): @binance/mp-web@0.0.30
- chore(changelog): @mp/runtime-worker-common@1.0.23
- chore(changelog): @mp/worker-mg@1.0.19
- chore(changelog): @mp/remote-debug@1.0.21
- chore(changelog): @mp/runtime-plugin-user-info@1.0.14
- chore(changelog): @mp/plugins-mp@1.0.44
- chore(changelog): update changelog for version v4.0.3
- chore(changelog): @mp/mpp-service@1.0.32
- chore(changelog): @binance/mp-automator@2.0.0
- chore(changelog): @mp/bundler@3.0.6
- chore(changelog): @mp/server-side-bundle@1.0.12
- chore(changelog): @binance/mp-web@0.0.29
- chore(changelog): @mp/runtime-service-web@0.2.24
- chore(changelog): @binance/mp-automator@1.0.14
- chore(changelog): @binance/mp-web@0.0.28
- chore(changelog): @mp/host@0.2.53
- chore(changelog): @mp/gen-sdk@1.0.20
- chore(changelog): @mp/worker-mg@1.0.18
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.19
- chore(changelog): @mp/plugins-mg@1.0.43
- chore(changelog): @mp/runtime-worker-common@1.0.22
- chore(changelog): @mp/remote-debug@1.0.20
- chore(changelog): @mp/plugins-mp@1.0.43
- ci: fix git push tag one by one
- chore(changelog): @mp/server-side-bundle@1.0.11
- chore(changelog): @mp/mpp-service@1.0.31
- chore(changelog): @mp/bundler@3.0.5
- chore(changelog): update changelog for version v3.14.7
- chore: add caretColor demo
- chore(changelog): update changelog for version v3.14.6
- chore(changelog): update changelog for version v4.1.0
- chore(changelog): update changelog for version v4.1.0
- chore(changelog): @binance/mp-cli@2.4.27
- chore(changelog): update changelog for version v4.0.2
- chore(changelog): @mp/gen-sdk@1.0.17
- chore(changelog): @mp/gen-sdk@1.0.16
- chore: gen-sdk local
- chore(changelog): @binance/mp-automator@1.0.9
- chore(changelog): @binance/mp-web@0.0.23
- chore(changelog): update changelog for version v4.1.0-dev.3

## [4.1.0-dev.3] 2022-11-10

**Download: [SDK-4.1.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.3.zip)**

### Bug Fixes

- fix(cli): mpService should support both function api and object api

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo

### Internal

- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2

## [4.1.0-dev.2] 2022-11-09

**Download: [SDK-4.1.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.2.zip)**

### Bug Fixes

- fix(mp-web): support absolute path
- fix(changelog): changelog bug: 3.14.5-dev.1 & 4.0.2-dev.1
- fix(sdk): add readme for deprecated usage
- fix(sdk): cherry pick - await load appJs
- fix(sdk): fix image style not work
- fix(cli): remove .npmrc and add npm token
- fix(cli): duplicate resolve issue of ConditionNamesPlugin
- fix(sdk): network service
- fix(sdk): ready replace uirenderserviceready
- fix(host): create webview files issue
- fix(host): support private-request command
- fix(runtime): download-file not work
- fix(sdk): env undefined
- fix(sdk): revoke native buffer issue
- fix(mp-web): fix sw.js ready timeline issue
- fix(sdk): native-image onload and image bug

### Features

- feat(sdk): load gcanvas on demand
- feat(sdk): add page-frame-resource points
- feat(automator): refactor mp-web & inject mp-web to automator
- feat(sdk): gcanvas createJSBuffer, less cpu cost
- feat(automator): support plugins service to fix service undefined issue
- feat(bundler): add **REPORT_POINTS** for renderer
- feat(sdk): nezhaRenderPageJs point
- feat(automator): allow reloading the mini-program
- feat(cli): update publish yml file
- feat(sdk): truncate long rpc logs limit length
- feat(sdk): shareAppMessage support fallback url
- feat(sdk): add debounce to navigator
- feat(cli): support conditional exports bmp
- feat(sdk): renderer to native page ready
- feat(sdk): add param usePrefetchCache to bn.request
- feat(demo): release component-demo PROD
- feat(sdk): getPerformance support entryType: loadPackage downloadPackage
- feat(sdk): scroll-view support showScrollbar
- feat(sdk): mg keyboard api
- feat(demo): taro version runtime benchmark

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore(changelog): @binance/mp-cli@2.4.24
- chore(demo): update prefetchRules of component-demo
- chore(changelog): @binance/mp-cli@2.4.23
- ci: fix bump exclude checked cache files
- chore(changelog): @mp/gen-sdk@1.0.12
- ci: fix wrong git tag versions for manifest and changelog
- chore(changelog): update changelog for version v3.14.5
- ci: pass the job if there is nothing to be validated
- chore(changelog): @binance/mp-web@0.0.18
- chore(changelog): @binance/mp-web@0.0.17
- docs: update how to fixed log when version validate failed
- chore(changelog): update changelog for version v3.14.5-dev.1
- docs(sdk): add docs about yarn bump
- chore(changelog): update changelog for version v4.0.2-dev.1
- chore: fix submodule error by removing temp file
- chore(changelog): @binance/mp-cli@2.4.22
- chore: bump version issue cause by cicd
- chore: local auto bump support
- chore(changelog): @binance/mp-cli@2.4.21
- chore: update ci
- chore(changelog): update changelog for version v4.0.1
- chore: version validate
- chore: rename pipeline name
- chore: update npm-publish job
- ci: fix release job for git fetch failed on CI
- chore: test new job success
- chore(changelog): update changelog for version v3.14.4
- chore: bump host deps chain
- chore(changelog): update changelog for version v4.0.1-dev.1
- ci: setup ci changelog & release automatically
- chore(sdk): bump plugins version
- chore(sdk): plugin bump version
- chore(sdk): bump versions
- chore(sdk): add mg adapter file
- chore(changelog): update changelog for version v4.1.0-dev.1

## [3.14.5-dev.1] 2022-11-08

**Download: [SDK-3.14.5-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.5-dev.1.zip)**

### Features

- feat(sdk): add page-frame-resource points

## [4.0.2-dev.1] 2022-11-08

**Download: [SDK-4.0.2-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs

## [4.0.1-dev.1] 2022-11-02

**Download: [SDK-4.0.1-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): env undefined

### Internal

- chore(cicd): yaml files

## [4.1.0-dev.1] 2022-10-27

**Download: [SDK-4.1.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.1.zip)**

### Bug Fixes

- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Internal

- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.0.0-dev.3] 2022-10-19

**Download: [SDK-4.0.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files

### Features

- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields

### Internal

- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2

## [4.0.0-dev.2] 2022-10-17

**Download: [SDK-4.0.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event

### Features

- feat(bundler): add monitor NEZHA_RENDER_PAGE_JS & update sorter of pkg
- feat(host): remove canvas useless dep
- feat(sdk): remove deprecated items for sdk4.0
- feat(sdk): getSystemInfo cache
- feat(server-side-bundle): compile & upload worker code into bytecode when enableBytecode
- feat(sdk): bump versions
- feat(sdk): bump version for ide deps
- feat(sdk): validate current page is tabBar page when call tabBar apis
- feat(demo): update prod demo
- feat(sdk): plugin createIntersectionObserver and fix selectorQuery setTimeout issue
- feat(sdk): detect darkmode for appBaseInfo
- feat(sdk): load app js advance after worker send $Ready

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1

## [4.0.0-dev.1] 2022-10-12

**Download: [SDK-4.0.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.1.zip)**

### Bug Fixes

- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Internal

- chore(changelog): update changelog for version v3.14.1

## [3.14.0-dev.4] 2022-09-26

**Download: [SDK-3.14.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue

### Features

- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)

### Internal

- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3

## [3.14.0-dev.3] 2022-09-23

**Download: [SDK-3.14.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue

### Features

- feat(sdk,demo): add private fps api and benchmark for render fps

### Internal

- chore(changelog): update changelog for version v3.14.0-dev.2

## [3.14.0-dev.2] 2022-09-22

**Download: [SDK-3.14.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.2.zip)**

### Bug Fixes

- fix(mpp-service): fix status api empty fail message

### Features

- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption

### Refactor

- refactor(sdk): remove locationReadyManager

### Internal

- chore(changelog): update changelog for version v3.14.0-dev.1

## [3.14.0-dev.1] 2022-09-21

**Download: [SDK-3.14.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): add properties on webgl context
- fix(sdk): fix timeOrigin 0 issues on IOS14
- fix(runtime): cannot resolve the font with url "bnshare://"
- fix(sdk): fix getperformance firstRender
- fix: cherry-pick cachePromise of getSystemInfo
- fix(sdk): use promise polyfill fix promise task order in ios12 - ios14
- fix(sdk): error code detection of remote debug
- fix(sdk): requestAnimationFrame NaN
- fix(automator): web cli core apis
- fix: add dependency to pass build job
- fix(sdk): performance init appLaunch payload
- fix: getPerformance first-render

### Features

- feat(sdk): gcanvas async method
- feat(server-side-bundle): use X-Mp-Open-Api-Token to authorize
- feat(sdk): add warn deprecated info for sdk 4.0
- feat(sdk): support injected prop in webview component
- feat(sdk): add experimental on walletconnector
- feat(bundler): support include options in project.config.json
- feat(sdk): error with stack
- feat(sdk): new render point NEZHA_INJECT_RENDERER_JS_END & update timeline point info
- feat(lib): use body class to control theme rather than prefers-color-scheme
- feat(lib): remote-debug route-change-done notify to render
- feat(cli): add props to webview
- feat(sdk): mpRuntimeLogger rename & add error code
- feat(sdk): webgl finish api
- feat(mpp-service): output version info to MPP_SERVICE_OUTPUT.json
- feat(sdk): time app check after app-launch
- feat(bundler): impl util-function analyzeSource & remove AddEntryAppJsPlugin

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Internal

- chore(changelog): update changelog for version v3.13.2
- chore(tools): remove cicd
- chore: fix dockerfile
- chore(changelog): update changelog for version v3.13.1
- docs(demo): update automator readme
- update cicd tool
- update cicd tool
- docs(docs): provide troubleshooting for canvas dependencies installing issue
- cicd tools
- docs: remove duplicated changelog for 3.13.0
- chore(changelog): update changelog for version v3.13.0
- chore(changelog): update changelog for version v3.13.0

## [3.13.0-dev.5] 2022-09-01

**Download: [SDK-3.13.0-dev.5](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.4

## [3.13.0-dev.4] 2022-08-31

**Download: [SDK-3.13.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.3

## [3.13.0-dev.3] 2022-08-31

**Download: [SDK-3.13.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.3.zip)**

### Features

- feat(sdk): sdk-loading

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.2

## [3.13.0-dev.2] 2022-08-30

**Download: [SDK-3.13.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code

### Features

- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg

### Internal

- docs(sdk): components docs
- chore: changelog automation

## [3.13.0-dev.1] 2022-08-23

**Download: [SDK-3.13.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register

### Features

- feat(sdk): setInterval 0 with warning
- feat(sdk): add api requestSubscribeMessage
- feat(sdk): make-phone-call
- feat(runtime): @mp/host catch error and send to parent window
- feat(sdk): canvas to temp file path api and demo
- feat(sdk): add FP/FCP/LCP entry for performance API
- feat(demo): add readfile api to benchmark
- feat(sdk): add route-change-done event to fix route entry negative duration
- feat(demo): add apiBenchmark at globalThis to run customize api benchmark
- feat(demo): add extended-libs page
- feat(demo): demo for webgl
- feat(cli): quick publish for dev & qa

### Refactor

- refactor(sdk): delete gcanvas useless code

### Internal

- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs

---

# Download Development Version

## [5.12.0-dev.2] 2026-04-28

**Download: [5.12.0-dev.2(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.2.zip)**

### Features

- feat(sdk): editor support rtl

## [5.12.0-dev.1] 2026-04-26

**Download: [5.12.0-dev.1(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.1.zip)**

### Features

- feat(host): add RTL text direction and custom text align for editor

## [5.12.0-dev.0] 2026-04-21

**Download: [5.12.0-dev.0(2.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.12.0-dev.0.zip)**

### Bug Fixes

- fix(sdk): add NODE_OPTIONS=--openssl-legacy-provider for Node 17+ build compat in renderer-mp
- fix(host): remove copy webpack plugin to fix copy-webpack-plugin v11 compat
- fix(host): add tslib 2.8.1 resolution for Node 24 exports compatibility
- fix(host): pin isolated-vm to 6.1.2 for Node 24 / C++20 compatibility
- fix(host): remove isolated-vm resolution, not used in project
- fix(host): return align and divider in editor mark, revert keepOnSplit override
- fix(cli): auto-recover from adb INSTALL_FAILED_UPDATE_INCOMPATIBLE
- fix(ide-cli): prevent infinite recursion in console-to-WebSocket forwarding

### Features

- feat(bundler): renderer components support shared chunks
- feat(native-cli): add Android inspector and native MCP tooling

## [5.11.0-dev.2] 2026-04-02

**Download: [5.11.0-dev.2(2.76 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.11.0-dev.2.zip)**

### Bug Fixes

- Fix/mp renderjs missing
- fix(sdk): add backward compatibility for ViewPager2 in SwiperView
- Fix/native cli preview UI layout
- Fix/type 0331

### Features

- feat(sdk): add QJS bytecode compilation for renderer-service-hummer
- feat(sdk): support virtual appid for widget

## [5.11.0-dev.1] 2026-03-31

**Download: [5.11.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.11.0-dev.1.zip)**

### Bug Fixes

- fix(cli): bundle native-cli resources and resolve adb
- fix: showErrorPage for 600402 page_not_found error
- fix(sdk): mcp bin
- fix(lib): fix ide cli toolbar sync api
- fix(cli): ide cli node version match

### Features

- feat(sdk): add useNewWindow parameter to previewImage API
- feat(cli): native-cli & ide-cli-mcp-server recover capabilities improve
- Feat/ios orba
- feat(cli): mcp tool stability improve
- feat(sdk): screen cast
- feat(cli): ide cli mcp server sync
- feat(cli): add mobile screen viewer and simulator host capture

## [5.10.0-dev.2] 2026-03-11

**Download: [5.10.0-dev.2(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.10.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix video props type
- fix(native-cli): prevent host hang on Ctrl+C

### Features

- feat(sdk): support root portal to specific element
- Feat/hummer lcp
- feat(cli): sub mode default render path
- feat(cli): native cli UI bridge
- feat(cli): orba desktop mp side work
- feat(cli): make get_log_files as example
- feat(cli): native cli UI dev env
- feat(cli): init native-cli project

## [5.10.0-dev.1] 2026-03-03

**Download: [5.10.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.10.0-dev.1.zip)**

### Features

- feat: fix error when stack is empty

## [5.9.0-dev.1] 2026-02-17

**Download: [5.9.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): swiper autoheight child item

### Features

- Feat/hummer swiper
- Feat/hummer event
- feat(cli): use custom ios runtime version
- feat(cli): ios simulator support
- feat(bundler): show error page when load module error

### Misc

- Revert " fix(sdk): sortable items when height changes " (#2522) (#2541)

## [5.8.0-dev.1] 2026-01-29

**Download: [5.8.0-dev.1(2.21 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick 5.7.1
- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed

### Features

- feat(sdk): hummer gcanvas
- feat(sdk): load appjs when reload worker
- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool

## [5.8.0-dev.1] 2026-01-28

**Download: [5.8.0-dev.1(1.88 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed

### Features

- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool

## [5.7.0-dev.2] 2026-01-07

**Download: [5.7.0-dev.2(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.7.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId

## [5.7.0-dev.1] 2025-12-29

**Download: [5.7.0-dev.1(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.7.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): add internal doc site
- feat(cli): auto perf

## [5.6.0-dev.2] 2025-12-19

**Download: [5.6.0-dev.2(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.6.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix prerender inject data path

## [4.51.5-dev.1] 2025-12-18

**Download: [4.51.5-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.51.5-dev.1.zip)**

### Features

- feat(bundler): update terser
- feat(sdk): theme getter in systemInfo incorrect

## [5.6.0-dev.1] 2025-12-18

**Download: [5.6.0-dev.1(1.87 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.6.0-dev.1.zip)**

### Bug Fixes

- fix(sdk,bundler): init nativeScrollNegotiation/enableBackToTop config
- fix(sdk): reuse page issue on ios platform
- fix(sdk): text dont filter nest components
- fix(sdk): chain routechange handler when receviced multiple routechange
- fix(lib): add missing code back to protect web import

### Features

- feat(sdk): add extra type
- feat(sdk): support debug prefetch configuration
- feat(sdk): lottie comp support animationData props
- feat(bundler): update terser avoid bugs of old ver

## [5.5.0-dev.1] 2025-11-27

**Download: [5.5.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.5.0-dev.1.zip)**

### Features

- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.4.0-dev.2] 2025-11-06

**Download: [5.4.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.4.0-dev.2.zip)**

### Features

- feat(sdk): page timeline add check point

## [5.4.0-dev.1] 2025-11-05

**Download: [5.4.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.4.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android

### Features

- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum

## [5.3.0-dev.1] 2025-10-16

**Download: [5.3.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.3.0-dev.1.zip)**

### Features

- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [4.52.0-dev.1] 2025-10-14

**Download: [4.52.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.52.0-dev.1.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [5.3.0-dev.1] 2025-10-10

**Download: [5.3.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.3.0-dev.1.zip)**

### Bug Fixes

- fix(cli): version sort

### Features

- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [5.2.0-dev.1] 2025-09-25

**Download: [5.2.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.2.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix prerender measure
- fix(sdk): sdk5.2 cherry pick bn.removeWidgetSkeleton
- fix(sdk): inst id not exist
- fix(sdk): sdk5.2 cherry pick usePageScroll
- fix(sdk): sdk5.x hummer log & nezha debug flag
- fix(sdk): hotfix scrollview
- fix(sdk): avoid XSS attack
- fix(sdk): mounted to ensure nativeComponents context ready and dom instanceId for native widget
  map
- fix(mpp-service): ai meta info upload without widgets
- fix(sdk): remove unused log

### Features

- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion

## [4.51.0-dev.1] 2025-09-25

**Download: [4.51.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.51.0-dev.1.zip)**

### Features

- Feat call all
- feat(sdk): sdk4.x support support formatter for all echart options

## [5.1.4-dev.2] 2025-09-22

**Download: [5.1.4-dev.2(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.4-dev.2.zip)**

### Features

- feat(sdk): bn.removeWidgetSkeleton

## [5.1.4-dev.1] 2025-09-19

**Download: [5.1.4-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.4-dev.1.zip)**

### Bug Fixes

- fix(sdk): usePageScroll hooks not work
- fix(sdk): hummer renderer support update single child

## [5.1.0-dev.1] 2025-09-03

**Download: [5.1.0-dev.1(1.81 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-5.1.0-dev.1.zip)**

### Bug Fixes

- fix(bmp): pika ci error
- fix(sdk): fix resolve native comp & input update timestamp
- fix(sdk): render child node directly when component need children vnode
- fix(sdk): host mini app events and setData damaged by widget flow
- fix: revert comment
- fix(sdk): @binance/bmp-xx deps
- fix(sdk): scrollViewUpdate rendererId undefined
- fix(lib): define EMPTY_OBJ

### Features

- feat(lib): support legacy dynamic widget slot
- feat(lib): release prod bmp-components and bmp-react
- feat(bundler): remove prerender data after build in
- feat(lib): update bmp component for ts
- feat(lib): support legacy widget-slot
- feat(sdk): update systemInfo cache when shellapp not restart
- feat(sdk): prerender remove skeleton auto
- feat(sdk): prerender support combined data
- feat(lib): update typo and EMPTY_OBJ
- feat(sdk): update taro-bn-components
- feat(lib): remove useTheme
- feat(bundler): support bundler version

### Misc

- Revert "Merge master"
- revert: root condition in setData

## [4.50.0-dev.1] 2025-09-03

**Download: [4.50.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.50.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): mounted to ensure nativeComponents context ready and dom instanceId for native widget
  map
- fix(mpp-service): ai meta info upload without widgets
- fix(sdk): remove unused log

### Features

- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion
- feat(bundler): support bundler version

## [4.48.0-dev.3] 2025-07-25

**Download: [4.48.0-dev.3(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay

## [4.48.0-dev.2] 2025-07-24

**Download: [4.48.0-dev.2(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.2.zip)**

### Features

- feat(sdk): revert autoheight default value to false

## [4.48.0-dev.1] 2025-07-24

**Download: [4.48.0-dev.1(1.85 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.48.0-dev.1.zip)**

### Bug Fixes

- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y

### Features

- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.47.0-dev.3] 2025-07-03

**Download: [4.47.0-dev.3(1.84 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): expose the error before app init

### Features

- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor

## [4.47.0-dev.2] 2025-06-30

**Download: [4.47.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.2.zip)**

### Features

- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar

## [4.47.0-dev.1] 2025-06-24

**Download: [4.47.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.47.0-dev.1.zip)**

### Features

- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo

## [4.46.0-dev.3] 2025-06-13

**Download: [4.46.0-dev.3(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.3.zip)**

### Features

- feat(sdk): not set dataurl on style change

## [4.46.0-dev.2] 2025-06-13

**Download: [4.46.0-dev.2(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.2.zip)**

### Features

- feat(sdk): w3w timeline monitor

## [4.46.0-dev.1] 2025-06-11

**Download: [4.46.0-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.46.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.3-dev.1] 2025-05-22

**Download: [4.45.3-dev.1(1.80 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.45.3-dev.1.zip)**

## [4.45.0-dev.1] 2025-05-14

**Download: [4.45.0-dev.1(1.73 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.45.0-dev.1.zip)**

### Features

- feat(sdk): suspend & resume lifecycle

## [4.44.0-dev.1] 2025-04-29

**Download: [4.44.0-dev.1(1.73 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.44.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): set scroll top not work / request support enableCache
- fix(sdk): `show-scrollbar` doesn't work

### Features

- feat(sdk): support keyboard accessory item
- feat(sdk): remove sync api
- feat(sdk): domtoimage can ignore error when image not exist or load error
- feat(sdk): scrollview support enableBackToTop
- feat(sdk): showErrorPage support auto detect rendererId
- feat(sdk): flutter scrollView add events
- feat(cli): achieve pkg stability & log process stability optimization
- feat(host): support five themes
- feat(cli): support mcp refresh
- feat(sdk): remove hack worker patch
- feat(sdk): add dark_midnight support
- feat(bundler): support polyfill self and XMLHttpRequest
- feat(bundler): dynamic path by env. BUNDLER_PATCH
- feat(extended-lib): support extended lib uikit flow
- feat(host): support midnight

## [4.43.0-dev.2] 2025-04-10

**Download: [4.43.0-dev.2(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.43.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill

## [4.43.0-dev.1] 2025-04-09

**Download: [4.43.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.43.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix input textarea type adjustPosition

### Features

- feat(sdk): alpha chart for editor
- feat(sdk): new component flutter markdown
- feat(sdk): add `<Flex>` & `<Span>` components
- feat(sdk): support get prefetch data synchronous
- feat: update process-md-paths
- feat(cli): log process status indicator
- feat: update md jobs
- feat: add job to convert md path
- feat(cli): filter standalone-chunks while addEntry
- feat(sdk): input support max-digits-length
- feat(cli): use release version devtool
- feat(sdk): add runtime-plugin-create-event-source
- feat(cli): chrome devtools Integration - console
- feat: update llms.txt title and filter docs
- feat: add upload-docs-md job

## [4.42.0-dev.1] 2025-03-18

**Download: [4.42.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.42.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`

### Features

- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo

## [4.41.0-dev.1] 2025-03-04

**Download: [4.41.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

- feat(sdk): sortable support x-axis/free dragging
- feat(sdk): add image info type
- feat(sdk): init rem to avoid style issue in flutter renderer
- feat(sdk): widget support selectorQuery & intersectionObserver
- feat(sdk): implement lite-timeline sdk part
- feat(sdk): improve virtual scrollview
- feat(sdk): remove webf sync command during the initialization
- feat(sdk): support disableCleanStack and cleanOtherStack
- feat(sdk): increase priority of framework level message
- feat(runtime): add plugin `addEventListenerToBody`
- feat(server-side-bundle): add new qjs compilation

## [4.41.0-dev.3] 2025-02-28

**Download: [4.41.0-dev.3(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.3.zip)**

### Features

- feat(sdk): add image info type

## [4.41.0-dev.2] 2025-02-27

**Download: [4.41.0-dev.2(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.2.zip)**

### Features

- feat(sdk): init rem to avoid style issue in flutter renderer
- feat(sdk): widget support selectorQuery & intersectionObserver

## [4.41.0-dev.1] 2025-02-25

**Download: [4.41.0-dev.1(1.72 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.41.0-dev.1.zip)**

### Bug Fixes

- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

- feat(sdk): implement lite-timeline sdk part
- feat(sdk): improve virtual scrollview
- feat(sdk): remove webf sync command during the initialization
- feat(sdk): support disableCleanStack and cleanOtherStack
- feat(sdk): increase priority of framework level message
- feat(runtime): add plugin `addEventListenerToBody`
- feat(server-side-bundle): add new qjs compilation

## [4.40.0-dev.2] 2025-02-10

**Download: [4.40.0-dev.2(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.40.0-dev.2.zip)**

### Bug Fixes

- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices

### Features

- feat(sdk): add disable-ios-embed props for ios native input

## [4.40.0-dev.1] 2025-02-06

**Download: [4.40.0-dev.1(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.40.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2

### Features

- feat(sdk): get static template theme from body
- feat(sdk): support remove skeleton after static templete rendered
- feat(sdk): drawer support teleportTo
- feat(demo): add fixed page input demo
- feat(sdk): flutter svg support
- feat(sdk): input component can highlight the inputed content
- feat(sdk): flutter deprecated textarea add `cursor-spacing`
- feat(sdk): support auto zip sdk in watch mode
- feat(cli): add socket status indicator
- feat(bundler): support standalone-chunks

## [4.39.5-dev.1] 2025-01-22

**Download: [4.39.5-dev.1(2.57 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.39.5-dev.1.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.38.0-dev.2] 2024-12-26

**Download: [4.38.0-dev.2(2.50 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.38.0-dev.2.zip)**

### Features

- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error

## [4.38.0-dev.1] 2024-12-25

**Download: [4.38.0-dev.1(2.50 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.38.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed

### Features

- feat(sdk): add params in chooseFile
- feat(sdk): scrollview support flex height virtual list
- feat(sdk): svg inline tag performence improve
- feat(bmp): `<Lottie />` support events
- feat(sdk): `<lottie />` support switching animation
- feat(sdk): add `flutter-video` component
- feat(sdk): throw bmp app `onError`
- feat(sdk): add `<DualSlider>` component
- feat(extended-lib): update react/react-dom 18.3.1
- feat(sdk): echarts tooltip formatter support function
- feat(cli): ide cli build failed not catch
- feat(bmp): `PickerView` add options `maskClass|maskStyle|indicatorClass|indicatorStyle`
- feat(cli): fix hot reload & change package name to ide-cli

## [4.37.0-dev.3] 2024-12-05

**Download: [4.37.0-dev.3(2.48 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues

### Features

- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component

## [4.37.0-dev.2] 2024-12-03

**Download: [4.37.0-dev.2(2.46 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix page stack update timing

### Features

- feat(lib): bmp-components
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat: bundler
- feat: sortable component

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.37.0-dev.1] 2024-11-26

**Download: [4.37.0-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.37.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

## [4.36.0-dev.4] 2024-11-26

**Download: [4.36.0-dev.4(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

## [4.36.0-dev.3] 2024-11-14

**Download: [4.36.0-dev.3(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): change handlePaste defaultValue

## [4.36.0-dev.2] 2024-11-14

**Download: [4.36.0-dev.2(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.2.zip)**

## [4.36.0-dev.1] 2024-11-13

**Download: [4.36.0-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.36.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): remove native component background color
- fix(sdk): flutter-image remove eventListener

### Features

- feat(sdk): add switch tab options in api
- feat(sdk): add timeformat api
- feat(sdk): add showBackButton api
- feat(sdk): `native-textarea` add onPaste
- feat(sdk): `native-textarea` add `alwaysEmbed`
- feat(sdk): add the value of input type `decimals`
- feat(sdk): flutter-deprecated-textarea add `autoFocus`

## [4.35.2-dev.1] 2024-11-07

**Download: [4.35.2-dev.1(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): release flutter image load
- fix(sdk): wrap inline element with bn-span for bn-markdown

### Misc

- Revert "chore: revert ui command"

## [4.35.0-dev.4] 2024-10-25

**Download: [4.35.0-dev.4(2.43 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): support inlineLayout for skyline

### Features

- feat(sdk): new api page.updateRouteOptions

## [4.35.0-dev.3] 2024-10-24

**Download: [4.35.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): flutter scroll refresher background color

### Features

- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo

## [4.35.0-dev.2] 2024-10-24

**Download: [4.35.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.2.zip)**

### Features

- feat(sdk): use tap for skyline

## [4.35.0-dev.1] 2024-10-23

**Download: [4.35.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): android quickjs unsupport Unicode Property Escapes
- fix(sdk): cherry pick webview message issue
- fix(sdk): re-publish @mp/runtime-plugin-enable-sheet-gesture
- fix(sdk): fix cursor issue
- fix(runtime): premature return issue in ide enviroment's show-modal api
- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly

### Features

- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.35.0-dev.1] 2024-10-17

**Download: [4.35.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.35.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly

### Features

- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.34.0-dev.3] 2024-10-04

**Download: [4.34.0-dev.3(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix webview message action not work

### Features

- feat(host): align response with native

## [4.34.0-dev.2] 2024-10-03

**Download: [4.34.0-dev.2(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.2.zip)**

### Features

- feat(sdk): flutter text component

## [4.34.0-dev.1] 2024-10-02

**Download: [4.34.0-dev.1(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.34.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-dev.4] 2024-10-01

**Download: [4.33.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-dev.4] 2024-09-30

**Download: [4.33.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.0-rc.1] 2024-09-12

**Download: [4.33.0-rc.1(NaN MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-rc.1.zip)**

## [4.33.0-dev.3] 2024-09-12

**Download: [4.33.0-dev.3(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop

### Features

- feat(demo): error handler demo
- feat(sdk): add deeplink target type

## [4.33.0-dev.2] 2024-09-12

**Download: [4.33.0-dev.2(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix component patch error messsage

### Features

- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs

## [4.33.0-dev.1] 2024-09-10

**Download: [4.33.0-dev.1(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.33.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type

### Features

- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)

## [4.32.0-dev.2] 2024-08-22

**Download: [4.32.0-dev.2(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.32.0-dev.2.zip)**

### Features

- feat(sdk): drawer component

## [4.32.0-dev.1] 2024-08-22

**Download: [4.32.0-dev.1(2.20 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.32.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory

### Features

- feat(bundler): support static script, do not bundle into \_app.js and \_common.js
- feat(bundler): mark build is done before send pageBundled
- feat(bundler): add entry must trigger a rebuild
- feat(sdk): scroll view support extra data prop
- feat(sdk): performance babel plugin log format with timeline
- feat(sdk): flutter scroll-view
- feat(bundler): update watch page utils
- feat(bundler): support ignore qjs options
- feat(bundler): skeleton create style tags by script to avoid webf issues
- feat(sdk): remove game script in sdk
- feat(sdk): flutter scroll view
- feat(sdk): add props for input
- feat(bundler): update bundler for host
- feat(doc): update doc
- feat(demo): add input unfocuse issue
- feat(sdk): lcp element timeline metrics

## [4.31.0-dev.2] 2024-07-31

**Download: [4.31.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.31.0-dev.2.zip)**

### Bug Fixes

- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler

### Features

- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode

## [4.31.0-dev.1] 2024-07-24

**Download: [4.31.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.31.0-dev.1.zip)**

### Features

- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components

## [4.30.0-dev.3] 2024-07-12

**Download: [4.30.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): native component webview message

## [4.30.0-dev.2] 2024-07-11

**Download: [4.30.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): native event in worker
- fix(sdk): fix webview component

### Features

- feat(sdk): webview component event api in queryselector

## [4.30.0-dev.1] 2024-07-10

**Download: [4.30.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.30.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error

### Features

- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js

## [4.29.0-dev.2] 2024-06-20

**Download: [4.29.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.29.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure

### Features

- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton

## [4.29.0-dev.1] 2024-06-13

**Download: [4.29.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.29.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cursor is wired when editor tap keyboard enter

### Features

- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%

## [4.28.0-dev.1] 2024-05-28

**Download: [4.28.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.28.0-dev.1.zip)**

### Features

- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line

## [4.27.0-dev.4] 2024-05-09

**Download: [4.27.0-dev.4(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload

## [4.27.0-dev.3] 2024-05-08

**Download: [4.27.0-dev.3(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.3.zip)**

### Features

- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app

## [4.27.0-dev.2] 2024-04-30

**Download: [4.27.0-dev.2(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.2.zip)**

### Features

- feat(sdk): api hide back button

## [4.27.0-dev.1] 2024-04-26

**Download: [4.27.0-dev.1(2.42 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.27.0-dev.1.zip)**

### Bug Fixes

- fix(extended-lib): postpublish script throw error

### Features

- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int

## [4.26.0-w3w] 2024-04-22

**Download: [4.26.0-w3w(NaN MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.26.0-w3w.zip)**

### Bug Fixes

- fix(host): support webassembly on host

### Features

- feat(sdk): web3 plugin use shell app
- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document

## [4.26.0-dev.1] 2024-04-17

**Download: [4.26.0-dev.1(2.41 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.26.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions

### Features

- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded

## [4.25.0-dev.2] 2024-03-27

**Download: [4.25.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.25.0-dev.2.zip)**

### Bug Fixes

- fix(extended-lib): add missing deps

### Features

- feat(sdk): custom native component

## [4.25.0-dev.1] 2024-03-27

**Download: [4.25.0-dev.1(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.25.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type

### Features

- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration

## [4.23.0-dev.2] 2024-02-16

**Download: [4.23.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.23.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): when user delete all content web input may act unexpected

## [4.23.0-dev.1] 2024-02-16

**Download: [4.23.0-dev.1(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.23.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE

### Features

- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define

## [4.22.0-dev.2] 2024-01-24

**Download: [4.22.0-dev.2(2.40 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.22.0-dev.2.zip)**

### Features

- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable

## [4.22.0-dev.1] 2024-01-22

**Download: [4.22.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.22.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): label trigger itemClick event for radio and checkbox

### Features

- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content

## [4.21.0-dev.1] 2024-01-08

**Download: [4.21.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.21.0-dev.1.zip)**

### Features

- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB

## [4.20.0-dev.1] 2023-12-12

**Download: [4.20.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.20.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter

## [4.19.0-dev.3] 2023-11-22

**Download: [4.19.0-dev.3(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.3.zip)**

### Bug Fixes

- fix(bundler): fix IDE can not reload

### Features

- feat(sdk): cherry-pick: add preloadflutterwebview api

## [4.19.0-dev.2] 2023-11-21

**Download: [4.19.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.2.zip)**

### Features

- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event

## [4.19.0-dev.1] 2023-11-14

**Download: [4.19.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.19.0-dev.1.zip)**

### Features

- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor

## [4.18.0-dev.3] 2023-11-02

**Download: [4.18.0-dev.3(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value

### Features

- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection

## [4.18.0-dev.2] 2023-10-30

**Download: [4.18.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.2.zip)**

### Features

- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list

## [4.17.2-dev.1] 2023-10-23

**Download: [4.17.2-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

## [4.18.0-dev.1] 2023-10-23

**Download: [4.18.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.18.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

### Features

- feat(sdk): editor support mention and hardBreak

## [4.16.3-dev.1] 2023-10-13

**Download: [4.16.3-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.3-dev.1.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.17.0-dev.2] 2023-10-13

**Download: [4.17.0-dev.2(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

### Features

- feat(lib): bmp-api openWidget add support for convention path

## [4.17.0-dev.1] 2023-10-10

**Download: [4.17.0-dev.1(2.39 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.17.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger

### Features

- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget

## [4.16.0-dev.2] 2023-09-19

**Download: [4.16.0-dev.2(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.0-dev.2.zip)**

### Bug Fixes

- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper

### Features

- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles

## [4.16.0-dev.1] 2023-09-11

**Download: [4.16.0-dev.1(2.38 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.16.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): bundler watch has 60s cache

### Features

- feat(sdk): editor internal plugin link support

## [4.15.0-dev.3] 2023-08-29

**Download: [4.15.0-dev.3(2.34 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots

### Features

- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers

## [4.15.0-dev.2] 2023-08-25

**Download: [4.15.0-dev.2(2.34 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci

### Features

- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter

## [4.15.0-dev.1] 2023-08-17

**Download: [4.15.0-dev.1(1.45 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.15.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount

### Features

- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs

## [4.14.0-dev.2] 2023-08-09

**Download: [4.14.0-dev.2(1.45 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.14.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): customize component data not update when return a data getter

### Features

- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata

## [4.14.0-dev.1] 2023-08-01

**Download: [4.14.0-dev.1(1.46 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.14.0-dev.1.zip)**

### Bug Fixes

- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop

### Features

- feat(sdk): editor paste event props
- feat(sdk): echart component

## [4.13.1-dev.1] 2023-07-27

**Download: [4.13.1-dev.1(1.15 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor split figure bugs
- fix(sdk): object spread sytax error
- fix(sdk): add seqId to web input event

## [4.13.0-dev.2] 2023-07-26

**Download: [4.13.0-dev.2(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.0-dev.2.zip)**

### Bug Fixes

- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer

### Misc

- Revert "fix(sdk): iOS native component created failed when container is not visible "

## [4.13.0-dev.1] 2023-07-18

**Download: [4.13.0-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.13.0-dev.1.zip)**

### Bug Fixes

- fix(demo): editor toolbar bottom 0 when platform is not iOS
- fix(sdk): iOS native component created failed when container is not visible
- fix: cherry-pick from 4.12.1
- fix(sdk): cancel load-script when redirect
- fix(lib): add type of removeSkeleton

### Features

- feat(sdk): editor selectImage api
- feat(mpp-service) add released pr
- feat(sdk): support walletkit and init func
- feat(demo): add manual to web input public demo

## [4.12.0-dev.1] 2023-06-28

**Download: [4.12.0-dev.1(1.13 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.12.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs

### Features

- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image

### Performance Improvements

- perf: add filesystem cache

## [4.11.0-dev.3] 2023-06-09

**Download: [4.11.0-dev.3(1.13 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo

## [4.11.0-dev.2] 2023-06-07

**Download: [4.11.0-dev.2(1.12 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images

### Features

- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider

## [4.10.2-dev.1] 2023-06-06

**Download: [4.10.2-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix startCheckPageTimeline error

## [4.11.0-dev.1] 2023-05-29

**Download: [4.11.0-dev.1(1.11 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.11.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work

### Features

- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API

## [4.10.1-dev.1] 2023-05-25

**Download: [4.10.1-dev.1(1.14 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): renderer service compatitable with es5

## [4.10.0-dev.4] 2023-05-19

**Download: [4.10.0-dev.4(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend

### Features

- feat(demo): add prefetchRules

## [4.9.2-dev.1] 2023-05-19

**Download: [4.9.2-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params

## [4.10.0-dev.3] 2023-05-18

**Download: [4.10.0-dev.3(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack

### Features

- feat(sdk): getUserOpenId return token

## [4.9.1-dev.2] 2023-05-17

**Download: [4.9.1-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.1-dev.2.zip)**

## [4.10.0-dev.2] 2023-05-16

**Download: [4.10.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): load page frame after load base.bxml success

## [4.10.0-dev.1] 2023-05-15

**Download: [4.10.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.10.0-dev.1.zip)**

### Bug Fixes

- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found

### Features

- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs

## [4.9.1-dev.1] 2023-05-15

**Download: [4.9.1-dev.1(1.10 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): update load script error code

### Features

- feat(sdk): use appConfig after init appConfig & add appConfig detection & syncGetPage or
  asyncGetPage
- feat(host): set custom http headers for fetch requests

## [4.9.0-dev.3] 2023-04-26

**Download: [4.9.0-dev.3(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.3.zip)**

### Bug Fixes

- fix(demo): production convertToMPUrl usage

### Features

- feat(sdk): ut from plugin-location to plugin-request-subscribe-message

## [4.9.0-dev.2] 2023-04-25

**Download: [4.9.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise

### Features

- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo

## [4.9.0-dev.1] 2023-04-24

**Download: [4.9.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs

### Features

- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher

## [4.9.0-dev.1] 2023-04-24

**Download: [4.9.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.9.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs

### Features

- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher

## [4.8.0-dev.2] 2023-04-06

**Download: [4.8.0-dev.2(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.8.0-dev.2.zip)**

### Features

- feat(sdk): bids use monitorupload
- feat(demo): editor component demo

## [4.8.0-dev.1] 2023-04-04

**Download: [4.8.0-dev.1(1.09 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.8.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version

### Features

- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API

# Download Development Version

## [4.7.0-dev.6] 2023-03-17

**Download: [4.7.0-dev.6(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.6.zip)**

### Bug Fixes

- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources

## [4.7.0-dev.5] 2023-03-16

**Download: [4.7.0-dev.5(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue

## [4.7.0-dev.4] 2023-03-16

**Download: [4.7.0-dev.4(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel

## [4.7.0-dev.3] 2023-03-14

**Download: [4.7.0-dev.3(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus

### Features

- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation

## [4.7.0-dev.2] 2023-03-13

**Download: [4.7.0-dev.2(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): editor focus and mark

### Features

- feat(sdk): catch html
- feat(sdk): figure

## [4.7.0-dev.1] 2023-03-09

**Download: [4.7.0-dev.1(1.07 MB)](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.7.0-dev.1.zip)**

### Bug Fixes

- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue

### Features

- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly

## [4.6.0-dev.2] 2023-02-22

**Download: [SDK-4.6.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.6.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): add native-send-appLuanch timer
  ([532dde2e](https://git.toolsfdg.net/fe/mini-program/commit/532dde2e37e8c3ff48cbf655238b88a9a1ff0dcd))
  by finley.x@binance.com

### Internal

- chore: bump commit after write files
  ([9378fed1](https://git.toolsfdg.net/fe/mini-program/commit/9378fed122a9613f50aac333ff8543d12893bbbc))
  by dylan.z@binance.com

## [4.6.0-dev.1] 2023-02-21

**Download: [SDK-4.6.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.6.0-dev.1.zip)**

### Bug Fixes

- fix(bundler): css variables rpx to rem align with wechat
  ([5fcfd131](https://git.toolsfdg.net/fe/mini-program/commit/5fcfd1319437e3fd52389083be12f459cb53d243))
  by dylan.z@binance.com
- fix(sdk): mini game view port size
  ([fc6048f0](https://git.toolsfdg.net/fe/mini-program/commit/fc6048f03ed5b9cb7357654e8a5699124fa38898))
  by henry.w@binance.com
- fix(sdk): getChildrenNode util function
  ([7c5764b6](https://git.toolsfdg.net/fe/mini-program/commit/7c5764b60831fa1c194490a907a1ad10e7ded92b))
  by henry.w@binance.com
- fix(sdk): rendererId zero issue in native ui
  ([c3d9020b](https://git.toolsfdg.net/fe/mini-program/commit/c3d9020b10630ac6c12f71595fb3c80cd3e7d2cf))
  by dylan.z@binance.com
- fix(bundler): catchmove value should be an exp
  ([dc53e87f](https://git.toolsfdg.net/fe/mini-program/commit/dc53e87f6ccb59b859b0eb13171f5038c98910da))
  by lawrence.w@binance.com
- fix(sdk): swiper Item blank
  ([7981ff89](https://git.toolsfdg.net/fe/mini-program/commit/7981ff894557f9145b619a68c823252654826014))
  by finley.x@binance.com
- fix(demo): fix custom demo textarea maxlength
  ([c28c58aa](https://git.toolsfdg.net/fe/mini-program/commit/c28c58aa2556d9e8eb21ef3b46269461bcf308c4))
  by henry.w@binance.com

### Features

- feat(demo): control picker view demo
  ([b80c088c](https://git.toolsfdg.net/fe/mini-program/commit/b80c088cd6307f659af3fba713787becc824479c))
  by lawrence.w@binance.com
- feat(sdk): detect page timeline
  ([0b1381a4](https://git.toolsfdg.net/fe/mini-program/commit/0b1381a4406d0767f736836a8418aede38ccd44f))
  by finley.x@binance.com
- feat(host): support pageReadyCallback
  ([1339544e](https://git.toolsfdg.net/fe/mini-program/commit/1339544ec010a520efab2e822bfe15d4249fdc66))
  by dylan.z@binance.com

### Refactor

- refactor: remove any type in AppCommandMap
  ([9b2411bd](https://git.toolsfdg.net/fe/mini-program/commit/9b2411bde6250820403082572e38070d9c9fc443))
  by lucifer.l@binance.com

### Internal

- docs: add api comment for documentation
  ([7993a741](https://git.toolsfdg.net/fe/mini-program/commit/7993a741307a4049768fcfe771cfbb3ad6231723))
  by dylan.z@binance.com
- chore: update bump with git auto push
  ([e25b674f](https://git.toolsfdg.net/fe/mini-program/commit/e25b674f8ed8fd0638bc25122a9d8c6efb223d6d))
  by dylan.z@binance.com
- chore: change UT coverage scope and threshold
  ([50820980](https://git.toolsfdg.net/fe/mini-program/commit/50820980c6a0d517e0a19df8d2ed740965c36f40))
  by lucifer.l@binance.com
- docs: format issue
  ([05c3cc6e](https://git.toolsfdg.net/fe/mini-program/commit/05c3cc6e632ea84fc316a8db27fa7c9337d2ca24))
  by dylan.z@binance.com
- docs: update config
  ([aaae5561](https://git.toolsfdg.net/fe/mini-program/commit/aaae556164f3bd260fbed971c490f090b6327a25))
  by dylan.z@binance.com
- docs: excited features of the JSCore team 202302
  ([1b38cbfe](https://git.toolsfdg.net/fe/mini-program/commit/1b38cbfe6c2344120f532eed76bda7a6990a7fc8))
  by dylan.z@binance.com
- [WIP]fix(sdk): controlled picker view
  ([661aa89a](https://git.toolsfdg.net/fe/mini-program/commit/661aa89ad9c3289ce614f2b77995d4ebf6d08bfa))
  by lawrence.w@binance.com
- mpp service support binance us host app
  ([fb8edeb8](https://git.toolsfdg.net/fe/mini-program/commit/fb8edeb8c6840cc84ef840c6ca84dcfc3a51fd72))
  by leo.cc@binance.com

# [4.5.1-dev.1] 2023-02-14

**Download: [SDK-4.5.1-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([01449416](https://git.toolsfdg.net/fe/mini-program/commit/01449416c3989a0e9d2e89811987e30c8d40bdbd))
  by lawrence.w@binance.com

## [3.14.16-dev.1] 2023-02-10

**Download: [SDK-3.14.16-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.16-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([d9a10d59](https://git.toolsfdg.net/fe/mini-program/commit/d9a10d599fb2ab6d7c222c2204917dcd7511a888))
  by lawrence.w@binance.com

# [4.5.0-dev.2] 2023-02-01

**Download: [SDK-4.5.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix requestBinanceCardInfo error response & cicd
  ([b18093ab](https://git.toolsfdg.net/fe/mini-program/commit/b18093abab0f1aa938d804d91d93e6c55e2ba949))
  by lawrence.w@binance.com
- fix(bundler): compile optional chaining when using latest caniuse-lite
  ([771dc7af](https://git.toolsfdg.net/fe/mini-program/commit/771dc7af2ea7eb809d3c3834f5733052dfb6df27))
  by jolin.h@binance.com
- fix(sdk): android css transition native component
  ([a70840e6](https://git.toolsfdg.net/fe/mini-program/commit/a70840e6d95fd2488bfe0993377224da6defa855))
  by henry.w@binance.com

### Features

- feat(sdk): add binance-card-info api
  ([65680864](https://git.toolsfdg.net/fe/mini-program/commit/65680864e327d5b81eca872e11ca4db55039948e))
  by lawrence.w@binance.com
- feat(demo): migrate to pika
  ([8cdffe8c](https://git.toolsfdg.net/fe/mini-program/commit/8cdffe8c1f46bb9181a915b7f21fc9a512db2063))
  by dylan.z@binance.com
- feat(sdk): jssdk dashboard rename & calculate
  ([ea78ac01](https://git.toolsfdg.net/fe/mini-program/commit/ea78ac01e11f57278428b190b600e0e008e0fc53))
  by finley.x@binance.com
- feat(sdk): wallet connector use new wallet provider
  ([ca346f5d](https://git.toolsfdg.net/fe/mini-program/commit/ca346f5d4f9560ae2fb59c2c2fdbb251eb8f4a33))
  by zane.x@binance.com

### Refactor

- refactor: throw error for the non-supported apis in IDE
  ([62e2ad65](https://git.toolsfdg.net/fe/mini-program/commit/62e2ad659b2143dd6eac1567fb2016758a4294e6))
  by lucifer.l@binance.com

### Internal

- docs: remove the app.config.json issue since pika will support it
  ([747343ed](https://git.toolsfdg.net/fe/mini-program/commit/747343ed66a9de848d6399a9e9521a6ba5f883e1))
  by dylan.z@binance.com

## [4.5.0-dev.1] 2023-01-18

**Download: [SDK-4.5.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.5.0-dev.1.zip)**

### Features

- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react

### Internal

- docs: getCurrentInstance query incorrect

## [4.4.0-dev.5] 2023-01-12

**Download: [SDK-4.4.0-dev.5](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type

## [4.4.0-dev.4] 2023-01-11

**Download: [SDK-4.4.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): mpc method
- fix(lib): update types of bmp-react

### Features

- feat(sdk): webview component supports message

### Internal

- chore: update config for FAQ
- docs: faq about app.config.json

## [4.4.0-dev.3] 2023-01-10

**Download: [SDK-4.4.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): types of bn.call & add RootPortal to bmp-components

### Features

- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option

### Internal

- docs(sdk): darkmode

## [4.4.0-dev.2] 2023-01-06

**Download: [SDK-4.4.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.2.zip)**

### Bug Fixes

- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info

### Features

- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114

## [4.4.0-dev.1] 2023-01-04

**Download: [SDK-4.4.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.4.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes

### Features

- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal

### Internal

- chore(sdk): cherry pick update sdk loading
- test: add more unit tests for host

## [4.3.0-dev.4] 2022-12-22

**Download: [SDK-4.3.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): mini game keyboard event

### Features

- feat: integrate automator on CI

### Internal

- chore: remove `yarn playwright install --with-deps`

## [4.3.0-dev.3] 2022-12-21

**Download: [SDK-4.3.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.3.zip)**

### Bug Fixes

- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target

### Features

- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar

### Refactor

- refactor: rename host-mp-ide to host-ide

### Internal

- docs(sdk): integrate with doc-system
- chore(package.json): fix installing sqllite3 in macos

## [4.3.0-dev.2] 2022-12-19

**Download: [SDK-4.3.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.2.zip)**

### Bug Fixes

- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14

### Features

- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI

### Internal

- chore(package.json): add packageManager field
- chore: replace resolve with join
- chore(sdk): cherry-pick from 4.2.1
- chore: update version remote and pwd alias

## [4.3.0-dev.1] 2022-12-14

**Download: [SDK-4.3.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.3.0-dev.1.zip)**

### Bug Fixes

- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css

### Features

- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo

### Internal

- chore: bump local
- chore: update prefetch rule of component demo
- docs: demos readme

## [4.2.0-dev.4] 2022-11-30

**Download: [SDK-4.2.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.4.zip)**

### Bug Fixes

- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height

### Features

- feat(sdk): gcanvas optimazation

### Internal

- chore: remove useless message in changelog.md by 'bot'

## [4.2.0-dev.3] 2022-11-30

**Download: [SDK-4.2.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.3.zip)**

### Bug Fixes

- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces

### Features

- feat(demo): add a rendererId 0 issue test case

### Refactor

- refactor(sdk): plugins including show-leaderboard, storage and tab-bar

### Internal

- chore: redirect blank page issue

## [4.2.0-dev.2] 2022-11-24

**Download: [SDK-4.2.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.2.zip)**

### Bug Fixes

- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS

### Refactor

- refactor(sdk): native ui plugin
- refactor(sdk): replace enum with union type

### Internal

- chore(changelog): @mp/worker-mg@1.0.23
- chore(changelog): @mp/server-side-bundle@1.0.15
- chore(changelog): @mp/runtime-service-web@0.2.29
- chore(changelog): @mp/gen-sdk@1.0.25
- chore(changelog): @mp/host@0.2.58
- chore(changelog): @binance/mp-automator@2.0.7
- chore(changelog): @mp/remote-debug@1.0.25
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.24
- chore(changelog): @mp/runtime-plugin-user-info@1.0.16
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.15
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.13
- chore(changelog): @mp/plugins-mg@1.0.48
- chore(changelog): @mp/runtime-plugin-download-package@1.0.16
- chore(changelog): @mp/webview@1.0.16
- chore(changelog): @mp/runtime-plugin-performance@1.0.19
- chore(changelog): @mp/runtime-plugin-fps@1.0.9
- chore(changelog): @mp/app-command@1.0.18
- chore(changelog): @mp/runtime-plugin-create-intersection-observer@1.0.9
- chore(changelog): @mp/runtime-plugin-wallet-connector@1.0.5
- chore(changelog): @mp/runtime-plugin-current-ui-event@1.0.9
- chore(changelog): @mp/plugins-mp-internal@1.0.15
- chore(changelog): @mp/runtime-plugin-sensor-compass@1.0.8
- chore(changelog): @mp/runtime-plugin-app-lifecycle@1.0.8
- chore(changelog): @mp/runtime-plugin-system-info@1.0.13
- chore(changelog): @mp/runtime-plugin-sensor-gyroscope@1.0.8
- chore(changelog): @mp/runtime-plugin-keyboard@1.0.8
- chore(changelog): @mp/runtime-plugin-request-subscribe-message@1.0.6
- chore(changelog): @mp/runtime-plugin-sensor-accelerometer@1.0.8
- chore(changelog): @mp/runtime-plugin-app-internal@1.0.10
- chore(changelog): @mp/runtime-plugin-custom-plugin@1.0.13
- chore(changelog): @mp/runtime-plugin-ensure-logged-in@1.0.7
- chore(changelog): @mp/runtime-plugin-share-panel@1.0.11
- chore(changelog): @mp/runtime-plugin-inner-audio@1.0.7
- chore(changelog): @mp/runtime-plugin-update-manager@1.0.13
- chore(changelog): @mp/runtime-plugin-location@1.0.9
- chore(changelog): @mp/runtime-plugin-save-image-to-photos-album@1.0.8
- chore(changelog): @mp/runtime-plugin-audio-interruption@1.0.7
- chore(changelog): @mp/runtime-plugin-websocket@1.0.13
- chore(changelog): @mp/runtime-plugin-sensor-device-motion@1.0.8
- chore(changelog): @mp/runtime-plugin-upload-file@1.0.12
- chore(changelog): @mp/runtime-plugin-share-menu@1.0.5
- chore(changelog): @mp/runtime-plugin-scan-code@1.0.8
- chore(changelog): @mp/runtime-plugin-file-system-manager@1.0.8
- chore(changelog): @mp/runtime-plugin-create-webview@1.0.12
- chore(changelog): @mp/runtime-plugin-authorize@1.0.6
- chore(changelog): @mp/runtime-plugin-error-page@1.0.9
- chore(changelog): @mp/runtime-plugin-image-info@1.0.14
- chore(changelog): @mp/runtime-plugin-make-phone-call@1.0.6
- chore(changelog): @mp/runtime-plugin-can-use@1.0.14
- chore(changelog): @mp/bundler@3.0.9
- chore(changelog): @mp/runtime-plugin-framework-storage@1.0.4
- chore(changelog): @mp/runtime-plugin-choose-image@1.0.8
- chore(changelog): @mp/host-core@1.0.14
- chore(changelog): @binance/mp-cli@2.4.29
- chore(changelog): @mp/mpp-service@1.0.34
- chore(changelog): update changelog for version v4.2.0-dev.1
- chore(changelog): @binance/mp-web@0.0.34
- chore(changelog): @binance/mp-automator@2.0.5
- chore(changelog): @mp/runtime-sdk-electron@0.1.28
- chore(changelog): @mp/host@0.2.57
- chore(changelog): @mp/gen-sdk@1.0.24
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.23
- chore(changelog): @mp/runtime-service-web@0.2.28
- chore(changelog): @mp/remote-debug@1.0.24
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.12
- chore(changelog): @mp/plugins-mp@1.0.47
- chore(changelog): @mp/plugins-mg@1.0.47
- chore(changelog): @mp/runtime-worker-common@1.0.26
- chore(changelog): @mp/runtime-plugin-download-package@1.0.15
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.14

## [4.2.0-dev.1] 2022-11-23

**Download: [SDK-4.2.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.2.0-dev.1.zip)**

### Bug Fixes

- fix(automator): fix some bugs & add `.waitFor`
- fix(sdk): native component css
- fix(sdk): (cherry-pick) reduce the blank page
- fix(runtime): no need to add webview when open new page
- fix(demo): input style of storage pages & update privatePrefetchRules
- fix(sdk): cherry pick - load-script-progress event when mp background event to lead blank screen
- fix(sdk): cherry pick fix location plugin
- fix(cli): skip generation of unmatched tags
- fix(demo): request pages issue of component-demo
- fix(sdk): load \_\_app.js after $ready
- fix(sdk): remove generating worker-service-game.qjs
- fix(runtime): vibrate shifting bug
- fix(demo): show isPrefetch in request pages

### Features

- feat(sdk): demo update & delete appTimeline
- feat(sdk): native webview component
- feat(demo): runtime benchmark add getAppBaseInfo apis
- feat(sdk): (cherry-pick)support caretColor for Input and TextArea components
- feat(automator): automator added headless option & refactor `.launch` & demo page
- feat(demo): move sync-api-demo to component-demo & update prefetchRules
- feat(sdk): api on add to favorites
- feat(bundler): generate fileTree for analyzeSource
- feat(sdk): first render new fields
- feat(runtime): support selecting sdk

### Refactor

- refactor(host): plugin user-info
- refactor(host): plugin & remove twoFA demo

### Internal

- chore(changelog): @mp/runtime-service-web@0.2.27
- chore(changelog): @mp/server-side-bundle@1.0.13
- chore(changelog): @binance/mp-automator@2.0.4
- chore(changelog): @binance/mp-web@0.0.33
- chore(changelog): @mp/runtime-sdk-electron@0.1.27
- chore(changelog): @mp/gen-sdk@1.0.23
- chore(changelog): @mp/runtime-worker-common@1.0.25
- chore(changelog): @mp/worker-mg@1.0.21
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.22
- chore(changelog): @mp/remote-debug@1.0.23
- chore(changelog): @mp/host@0.2.56
- chore(changelog): @mp/runtime-plugin-load-subpackage@1.0.11
- chore(changelog): @mp/plugins-mg@1.0.46
- chore(changelog): @mp/runtime-plugin-ensure-resources@1.0.13
- chore(changelog): @mp/runtime-plugin-user-info@1.0.15
- chore(changelog): @mp/runtime-plugin-download-package@1.0.14
- chore(changelog): @mp/webview@1.0.15
- chore(changelog): @mp/runtime-plugin-performance@1.0.17
- chore(changelog): @mp/runtime-plugin-fps@1.0.8
- chore(changelog): @mp/app-command@1.0.17
- chore(changelog): @mp/runtime-plugin-create-selector-query@1.0.11
- chore(changelog): @mp/runtime-plugin-wallet-connector@1.0.4
- chore(changelog): @mp/runtime-plugin-create-intersection-observer@1.0.8
- chore(changelog): @mp/runtime-plugin-current-ui-event@1.0.8
- chore(changelog): @mp/runtime-plugin-request-subscribe-message@1.0.5
- chore(changelog): @mp/runtime-plugin-app-lifecycle@1.0.7
- chore(changelog): @mp/runtime-plugin-ensure-logged-in@1.0.6
- chore(changelog): @mp/plugins-mg-internal@1.0.13
- chore(changelog): @mp/runtime-plugin-update-manager@1.0.12
- chore(changelog): @mp/runtime-plugin-auth-capture@1.0.6
- chore(changelog): @mp/runtime-plugin-sensor-gyroscope@1.0.7
- chore(changelog): @mp/runtime-plugin-upload-file@1.0.11
- chore(changelog): @mp/runtime-plugin-web3@1.0.4
- chore(changelog): @mp/runtime-plugin-network@1.0.8
- chore(changelog): @mp/runtime-plugin-websocket@1.0.12
- chore(changelog): @mp/runtime-plugin-save-image-to-photos-album@1.0.7
- chore(changelog): @mp/runtime-plugin-sensor-compass@1.0.7
- chore(changelog): @mp/runtime-plugin-sensor-orientation@1.0.6
- chore(changelog): @mp/runtime-plugin-image-info@1.0.13
- chore(changelog): @mp/runtime-plugin-location@1.0.8
- chore(changelog): @mp/mpp-service@1.0.33
- chore(changelog): @mp/runtime-plugin-app-internal@1.0.9
- chore(changelog): @mp/runtime-plugin-keyboard@1.0.7
- chore(changelog): @mp/runtime-plugin-custom-plugin@1.0.12
- chore(changelog): @mp/runtime-plugin-share-panel@1.0.10
- chore(changelog): @mp/runtime-plugin-download-file@1.0.6
- chore(changelog): @mp/runtime-plugin-choose-image@1.0.7
- chore(changelog): @mp/runtime-plugin-make-phone-call@1.0.5
- chore(changelog): @mp/runtime-plugin-authorize@1.0.5
- chore(changelog): @mp/runtime-plugin-system-info@1.0.12
- chore(changelog): @mp/runtime-plugin-preview-image@1.0.8
- chore(changelog): @mp/runtime-plugin-scan-code@1.0.7
- chore(changelog): @mp/runtime-plugin-on-off@1.0.9
- chore(changelog): @mp/runtime-plugin-create-webview@1.0.11
- chore(changelog): @mp/runtime-plugin-can-use@1.0.13
- chore(changelog): @mp/runtime-plugin-clipboard@1.0.7
- chore(changelog): @mp/bundler@3.0.7
- chore(changelog): @mp/runtime-plugin-file-system-manager@1.0.7
- chore(changelog): @mp/runtime-plugin-favorite@1.0.2
- chore(changelog): @mp/runtime-shared@1.0.15
- chore(changelog): @mp/host-core@1.0.13
- chore(changelog): @binance/mp-cli@2.4.28
- chore(changelog): @binance/mp-web@0.0.32
- chore(changelog): @binance/mp-automator@2.0.3
- chore(changelog): @binance/mp-automator@2.0.2
- chore(changelog): @mp/runtime-sdk-electron@0.1.26
- chore(changelog): @mp/runtime-service-web@0.2.26
- chore(changelog): @binance/mp-web@0.0.31
- chore(changelog): @mp/host@0.2.55
- chore(changelog): @mp/worker-mg@1.0.20
- chore(changelog): @mp/remote-debug@1.0.22
- chore(changelog): @mp/plugins-mg@1.0.45
- chore(changelog): @mp/runtime-worker-common@1.0.24
- chore(changelog): @mp/runtime-plugin-download-package@1.0.13
- chore(changelog): @mp/runtime-plugin-performance@1.0.16
- chore(changelog): update changelog for version v3.14.8
- chore(changelog): @mp/runtime-service-web@0.2.25
- chore(changelog): @mp/gen-sdk@1.0.21
- chore(changelog): @binance/mp-web@0.0.30
- chore(changelog): @mp/runtime-worker-common@1.0.23
- chore(changelog): @mp/worker-mg@1.0.19
- chore(changelog): @mp/remote-debug@1.0.21
- chore(changelog): @mp/runtime-plugin-user-info@1.0.14
- chore(changelog): @mp/plugins-mp@1.0.44
- chore(changelog): update changelog for version v4.0.3
- chore(changelog): @mp/mpp-service@1.0.32
- chore(changelog): @binance/mp-automator@2.0.0
- chore(changelog): @mp/bundler@3.0.6
- chore(changelog): @mp/server-side-bundle@1.0.12
- chore(changelog): @binance/mp-web@0.0.29
- chore(changelog): @mp/runtime-service-web@0.2.24
- chore(changelog): @binance/mp-automator@1.0.14
- chore(changelog): @binance/mp-web@0.0.28
- chore(changelog): @mp/host@0.2.53
- chore(changelog): @mp/gen-sdk@1.0.20
- chore(changelog): @mp/worker-mg@1.0.18
- chore(changelog): @mp/mp-runtime-shared-plugins@1.1.19
- chore(changelog): @mp/plugins-mg@1.0.43
- chore(changelog): @mp/runtime-worker-common@1.0.22
- chore(changelog): @mp/remote-debug@1.0.20
- chore(changelog): @mp/plugins-mp@1.0.43
- ci: fix git push tag one by one
- chore(changelog): @mp/server-side-bundle@1.0.11
- chore(changelog): @mp/mpp-service@1.0.31
- chore(changelog): @mp/bundler@3.0.5
- chore(changelog): update changelog for version v3.14.7
- chore: add caretColor demo
- chore(changelog): update changelog for version v3.14.6
- chore(changelog): update changelog for version v4.1.0
- chore(changelog): update changelog for version v4.1.0
- chore(changelog): @binance/mp-cli@2.4.27
- chore(changelog): update changelog for version v4.0.2
- chore(changelog): @mp/gen-sdk@1.0.17
- chore(changelog): @mp/gen-sdk@1.0.16
- chore: gen-sdk local
- chore(changelog): @binance/mp-automator@1.0.9
- chore(changelog): @binance/mp-web@0.0.23
- chore(changelog): update changelog for version v4.1.0-dev.3

## [4.1.0-dev.3] 2022-11-10

**Download: [SDK-4.1.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.3.zip)**

### Bug Fixes

- fix(cli): mpService should support both function api and object api

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo

### Internal

- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2

## [4.1.0-dev.2] 2022-11-09

**Download: [SDK-4.1.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.2.zip)**

### Bug Fixes

- fix(mp-web): support absolute path
- fix(changelog): changelog bug: 3.14.5-dev.1 & 4.0.2-dev.1
- fix(sdk): add readme for deprecated usage
- fix(sdk): cherry pick - await load appJs
- fix(sdk): fix image style not work
- fix(cli): remove .npmrc and add npm token
- fix(cli): duplicate resolve issue of ConditionNamesPlugin
- fix(sdk): network service
- fix(sdk): ready replace uirenderserviceready
- fix(host): create webview files issue
- fix(host): support private-request command
- fix(runtime): download-file not work
- fix(sdk): env undefined
- fix(sdk): revoke native buffer issue
- fix(mp-web): fix sw.js ready timeline issue
- fix(sdk): native-image onload and image bug

### Features

- feat(sdk): load gcanvas on demand
- feat(sdk): add page-frame-resource points
- feat(automator): refactor mp-web & inject mp-web to automator
- feat(sdk): gcanvas createJSBuffer, less cpu cost
- feat(automator): support plugins service to fix service undefined issue
- feat(bundler): add **REPORT_POINTS** for renderer
- feat(sdk): nezhaRenderPageJs point
- feat(automator): allow reloading the mini-program
- feat(cli): update publish yml file
- feat(sdk): truncate long rpc logs limit length
- feat(sdk): shareAppMessage support fallback url
- feat(sdk): add debounce to navigator
- feat(cli): support conditional exports bmp
- feat(sdk): renderer to native page ready
- feat(sdk): add param usePrefetchCache to bn.request
- feat(demo): release component-demo PROD
- feat(sdk): getPerformance support entryType: loadPackage downloadPackage
- feat(sdk): scroll-view support showScrollbar
- feat(sdk): mg keyboard api
- feat(demo): taro version runtime benchmark

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore(changelog): @binance/mp-cli@2.4.24
- chore(demo): update prefetchRules of component-demo
- chore(changelog): @binance/mp-cli@2.4.23
- ci: fix bump exclude checked cache files
- chore(changelog): @mp/gen-sdk@1.0.12
- ci: fix wrong git tag versions for manifest and changelog
- chore(changelog): update changelog for version v3.14.5
- ci: pass the job if there is nothing to be validated
- chore(changelog): @binance/mp-web@0.0.18
- chore(changelog): @binance/mp-web@0.0.17
- docs: update how to fixed log when version validate failed
- chore(changelog): update changelog for version v3.14.5-dev.1
- docs(sdk): add docs about yarn bump
- chore(changelog): update changelog for version v4.0.2-dev.1
- chore: fix submodule error by removing temp file
- chore(changelog): @binance/mp-cli@2.4.22
- chore: bump version issue cause by cicd
- chore: local auto bump support
- chore(changelog): @binance/mp-cli@2.4.21
- chore: update ci
- chore(changelog): update changelog for version v4.0.1
- chore: version validate
- chore: rename pipeline name
- chore: update npm-publish job
- ci: fix release job for git fetch failed on CI
- chore: test new job success
- chore(changelog): update changelog for version v3.14.4
- chore: bump host deps chain
- chore(changelog): update changelog for version v4.0.1-dev.1
- ci: setup ci changelog & release automatically
- chore(sdk): bump plugins version
- chore(sdk): plugin bump version
- chore(sdk): bump versions
- chore(sdk): add mg adapter file
- chore(changelog): update changelog for version v4.1.0-dev.1

## [3.14.5-dev.1] 2022-11-08

**Download: [SDK-3.14.5-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.5-dev.1.zip)**

### Features

- feat(sdk): add page-frame-resource points

## [4.0.2-dev.1] 2022-11-08

**Download: [SDK-4.0.2-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.2-dev.1.zip)**

### Bug Fixes

- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs

## [4.0.1-dev.1] 2022-11-02

**Download: [SDK-4.0.1-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.1-dev.1.zip)**

### Bug Fixes

- fix(sdk): env undefined

### Internal

- chore(cicd): yaml files

## [4.1.0-dev.1] 2022-10-27

**Download: [SDK-4.1.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.1.0-dev.1.zip)**

### Bug Fixes

- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Internal

- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.0.0-dev.3] 2022-10-19

**Download: [SDK-4.0.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files

### Features

- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields

### Internal

- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2

## [4.0.0-dev.2] 2022-10-17

**Download: [SDK-4.0.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event

### Features

- feat(bundler): add monitor NEZHA_RENDER_PAGE_JS & update sorter of pkg
- feat(host): remove canvas useless dep
- feat(sdk): remove deprecated items for sdk4.0
- feat(sdk): getSystemInfo cache
- feat(server-side-bundle): compile & upload worker code into bytecode when enableBytecode
- feat(sdk): bump versions
- feat(sdk): bump version for ide deps
- feat(sdk): validate current page is tabBar page when call tabBar apis
- feat(demo): update prod demo
- feat(sdk): plugin createIntersectionObserver and fix selectorQuery setTimeout issue
- feat(sdk): detect darkmode for appBaseInfo
- feat(sdk): load app js advance after worker send $Ready

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1

## [4.0.0-dev.1] 2022-10-12

**Download: [SDK-4.0.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-4.0.0-dev.1.zip)**

### Bug Fixes

- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Internal

- chore(changelog): update changelog for version v3.14.1

## [3.14.0-dev.4] 2022-09-26

**Download: [SDK-3.14.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue

### Features

- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)

### Internal

- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3

## [3.14.0-dev.3] 2022-09-23

**Download: [SDK-3.14.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.3.zip)**

### Bug Fixes

- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue

### Features

- feat(sdk,demo): add private fps api and benchmark for render fps

### Internal

- chore(changelog): update changelog for version v3.14.0-dev.2

## [3.14.0-dev.2] 2022-09-22

**Download: [SDK-3.14.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.2.zip)**

### Bug Fixes

- fix(mpp-service): fix status api empty fail message

### Features

- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption

### Refactor

- refactor(sdk): remove locationReadyManager

### Internal

- chore(changelog): update changelog for version v3.14.0-dev.1

## [3.14.0-dev.1] 2022-09-21

**Download: [SDK-3.14.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.14.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): add properties on webgl context
- fix(sdk): fix timeOrigin 0 issues on IOS14
- fix(runtime): cannot resolve the font with url "bnshare://"
- fix(sdk): fix getperformance firstRender
- fix: cherry-pick cachePromise of getSystemInfo
- fix(sdk): use promise polyfill fix promise task order in ios12 - ios14
- fix(sdk): error code detection of remote debug
- fix(sdk): requestAnimationFrame NaN
- fix(automator): web cli core apis
- fix: add dependency to pass build job
- fix(sdk): performance init appLaunch payload
- fix: getPerformance first-render

### Features

- feat(sdk): gcanvas async method
- feat(server-side-bundle): use X-Mp-Open-Api-Token to authorize
- feat(sdk): add warn deprecated info for sdk 4.0
- feat(sdk): support injected prop in webview component
- feat(sdk): add experimental on walletconnector
- feat(bundler): support include options in project.config.json
- feat(sdk): error with stack
- feat(sdk): new render point NEZHA_INJECT_RENDERER_JS_END & update timeline point info
- feat(lib): use body class to control theme rather than prefers-color-scheme
- feat(lib): remote-debug route-change-done notify to render
- feat(cli): add props to webview
- feat(sdk): mpRuntimeLogger rename & add error code
- feat(sdk): webgl finish api
- feat(mpp-service): output version info to MPP_SERVICE_OUTPUT.json
- feat(sdk): time app check after app-launch
- feat(bundler): impl util-function analyzeSource & remove AddEntryAppJsPlugin

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Internal

- chore(changelog): update changelog for version v3.13.2
- chore(tools): remove cicd
- chore: fix dockerfile
- chore(changelog): update changelog for version v3.13.1
- docs(demo): update automator readme
- update cicd tool
- update cicd tool
- docs(docs): provide troubleshooting for canvas dependencies installing issue
- cicd tools
- docs: remove duplicated changelog for 3.13.0
- chore(changelog): update changelog for version v3.13.0
- chore(changelog): update changelog for version v3.13.0

## [3.13.0-dev.5] 2022-09-01

**Download: [SDK-3.13.0-dev.5](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.5.zip)**

### Bug Fixes

- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.4

## [3.13.0-dev.4] 2022-08-31

**Download: [SDK-3.13.0-dev.4](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.4.zip)**

### Bug Fixes

- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.3

## [3.13.0-dev.3] 2022-08-31

**Download: [SDK-3.13.0-dev.3](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.3.zip)**

### Features

- feat(sdk): sdk-loading

### Internal

- chore(changelog): update changelog for version v3.13.0-dev.2

## [3.13.0-dev.2] 2022-08-30

**Download: [SDK-3.13.0-dev.2](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.2.zip)**

### Bug Fixes

- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code

### Features

- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg

### Internal

- docs(sdk): components docs
- chore: changelog automation

## [3.13.0-dev.1] 2022-08-23

**Download: [SDK-3.13.0-dev.1](https://ftp.binance.com/mp-sdk/dev/mp-sdk-3.13.0-dev.1.zip)**

### Bug Fixes

- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register

### Features

- feat(sdk): setInterval 0 with warning
- feat(sdk): add api requestSubscribeMessage
- feat(sdk): make-phone-call
- feat(runtime): @mp/host catch error and send to parent window
- feat(sdk): canvas to temp file path api and demo
- feat(sdk): add FP/FCP/LCP entry for performance API
- feat(demo): add readfile api to benchmark
- feat(sdk): add route-change-done event to fix route entry negative duration
- feat(demo): add apiBenchmark at globalThis to run customize api benchmark
- feat(demo): add extended-libs page
- feat(demo): demo for webgl
- feat(cli): quick publish for dev & qa

### Refactor

- refactor(sdk): delete gcanvas useless code

### Internal

- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs