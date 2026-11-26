---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/download-stable
api_type: Guide
updated_at: 2026-11-26 18:38:54.423574
---

# Download Stable Version

## [5.11.0] 2026-04-02

**Download: [5.11.0(2.76 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.11.0.zip)**

### Bug Fixes

- Fix/mp renderjs missing
- fix(sdk): add backward compatibility for ViewPager2 in SwiperView
- Fix/native cli preview UI layout
- Fix/type 0331
- fix(cli): bundle native-cli resources and resolve adb
- fix: showErrorPage for 600402 page_not_found error
- fix(sdk): mcp bin
- fix(lib): fix ide cli toolbar sync api
- fix(cli): ide cli node version match

### Features

- feat(sdk): add QJS bytecode compilation for renderer-service-hummer
- feat(sdk): support virtual appid for widget
- feat(sdk): add useNewWindow parameter to previewImage API
- feat(cli): native-cli & ide-cli-mcp-server recover capabilities improve
- Feat/ios orba
- feat(cli): mcp tool stability improve
- feat(sdk): screen cast
- feat(cli): ide cli mcp server sync
- feat(cli): add mobile screen viewer and simulator host capture

## [5.10.0] 2026-03-12

**Download: [5.10.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.10.0.zip)**

### Bug Fixes

- fix(sdk): fix video props type
- fix(native-cli): prevent host hang on Ctrl+C

### Features

- feat(cli): native cli mcp adjust
- feat(native-cli): add sync mp status mcp tool
- feat(sdk): support root portal to specific element
- Feat/hummer lcp
- feat(cli): sub mode default render path
- feat(cli): native cli UI bridge
- feat(cli): orba desktop mp side work
- feat(cli): make get_log_files as example
- feat(cli): native cli UI dev env
- feat(cli): init native-cli project

## [5.9.1] 2026-02-27

**Download: [5.9.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.9.1.zip)**

### Bug Fixes

- fix(sdk): renderer may never ready when route quickly

## [5.9.0] 2026-02-19

**Download: [5.9.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.9.0.zip)**

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

## [5.8.5] 2026-02-09

**Download: [5.8.5(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.5.zip)**

### Bug Fixes

- fix(sdk): <FlutterCustomNativeComponent/> dom update lead layout size abnormal

## [5.8.4] 2026-02-09

**Download: [5.8.4(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.4.zip)**

### Bug Fixes

- fix(sdk): routeChange type=switchTab and page isTabbarPage stack always be the rootTab

## [5.8.3] 2026-02-04

**Download: [5.8.3(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.3.zip)**

## [5.8.2] 2026-02-04

**Download: [5.8.2(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.2.zip)**

### Misc

- Revert " fix(sdk): sortable items when height changes " (#2522)

## [5.8.1] 2026-01-30

**Download: [5.8.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.1.zip)**

### Bug Fixes

- fix(sdk): navigate routeChanging defer ref issues

## [3.8.1] 2026-01-30

**Download: [3.8.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.8.1.zip)**

### Bug Fixes

- fix(sdk): navigate routeChanging defer ref issues
- fix(sdk): cherry pick 5.7.1
- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed
- fix(sdk): rm geature event listener binding
- fix(sdk): fix prerender inject data path
- fix(sdk,bundler): init nativeScrollNegotiation/enableBackToTop config
- fix(sdk): reuse page issue on ios platform
- fix(sdk): text dont filter nest components
- fix(sdk): chain routechange handler when receviced multiple routechange
- fix(lib): add missing code back to protect web import
- fix(sdk): add ut
- fix(lib): add comma to avoid MFA build error
- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android
- fix(cli): version sort
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
- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work
- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y
- fix(sdk): expose the error before app init
- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep
- fix(sdk): set scroll top not work / request support enableCache
- fix(sdk): `show-scrollbar` doesn't work
- fix(sdk): flutter getAttribute polyfill
- fix(sdk): fix input textarea type adjustPosition
- fix(cli): missing build start callback in bundleWatch
- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`
- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…
- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices
- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2
- fix(bmp): remove requestFullscreen param
- fix(sdk): flutter-video context issue
- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed
- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`
- fix(sdk): change handlePaste defaultValue
- fix(sdk): remove native component background color
- fix(sdk): flutter-image remove eventListener
- fix(sdk): support inlineLayout for skyline
- fix(sdk): flutter scroll refresher background color
- fix(sdk): android quickjs unsupport Unicode Property Escapes
- fix(sdk): cherry pick webview message issue
- fix(sdk): re-publish @mp/runtime-plugin-enable-sheet-gesture
- fix(sdk): fix cursor issue
- fix(runtime): premature return issue in ide enviroment's show-modal api
- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly
- fix(sdk): fix webview message action not work
- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator
- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop
- fix(sdk): fix component patch error messsage
- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type
- fix(sdk): vnode patch issues
- fix(sdk): navigate to type
- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory
- fix: add worker plugin
- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler
- fix(sdk): native component webview message
- fix(sdk): native event in worker
- fix(sdk): fix webview component
- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error
- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure
- fix(sdk): cursor is wired when editor tap keyboard enter
- fix: update render cache doc id
- fix(extended-lib): resolve path not a module
- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload
- fix(extended-lib): postpublish script throw error
- fix(host): support webassembly on host
- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions
- fix(extended-lib): add missing deps
- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type
- fix(sdk): revert readfile issue on ios
- fix(sdk): hotfix ios doesn't use native fs
- fix(sdk): when user delete all content web input may act unexpected
- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE
- fix(demo): icon size demo
- fix(sdk): label trigger itemClick event for radio and checkbox
- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter
- fix(bundler): fix IDE can not reload
- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value
- fix(sdk): support input focus and blur action by developers
- fix(sdk): END_FIRSTPAGE_APPLAUNCH send pid
- fix(sdk): clone data avoid reuse data object when reopen page
- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger
- fix(sdk): revert swiper located to wrong child when children updated
- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper
- fix(bundler): bundler watch has 60s cache
- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots
- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci
- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount
- fix(sdk): create webview api in mp cannot message
- fix(sdk): customize component data not update when return a data getter
- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop
- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer
- fix(demo): editor toolbar bottom 0 when platform is not iOS
- fix(sdk): iOS native component created failed when container is not visible
- fix: cherry-pick from 4.12.1
- fix(sdk): cancel load-script when redirect
- fix(lib): add type of removeSkeleton
- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs
- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo
- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images
- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work
- fix(mpp-service): set maxBodyLength & maxContentLength as Infinity wh…
- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend
- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack
- fix(sdk): load page frame after load base.bxml success
- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found
- fix(sdk): figure scrollIntoView should focus on the figure caption
- fix(demo): production convertToMPUrl usage
- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise
- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs
- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version
- fix(demo): bug in navigation demo
- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue
- fix(sdk): add native-send-appLuanch timer
- fix(bundler): css variables rpx to rem align with wechat
- fix(sdk): mini game view port size
- fix(sdk): getChildrenNode util function
- fix(sdk): rendererId zero issue in native ui
- fix(bundler): catchmove value should be an exp
- fix(sdk): swiper Item blank
- fix(demo): fix custom demo textarea maxlength
- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component
- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes
- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css
- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js
- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e(#NEZ-5634)
- fix(sdk): share-panel not working (#542)
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action

### Features

- feat(sdk): hummer gcanvas
- feat(sdk): load appjs when reload worker
- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool
- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId
- feat(sdk): add internal doc site
- feat(cli): auto perf
- feat(sdk): add extra type
- feat(sdk): support debug prefetch configuration
- feat(sdk): lottie comp support animationData props
- feat(bundler): update terser avoid bugs of old ver
- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve
- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum
- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev
- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion
- feat(bundler): support bundler version
- feat(sdk): support share v2 api
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(cli): support home page widget preview
- feat(mpp-service): update ai router payload
- feat(mpp-service): ai router solution
- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message
- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo
- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib
- feat(sdk): suspend & resume lifecycle
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
- feat(cli): rebundle while refresh
- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo
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
- feat(sdk): add disable-ios-embed props for ios native input
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
- feat(sdk): add showDiagnosticPage API
- feat(sdk): native-input cursor issue
- feat(sdk): add flutter-chart component
- feat(sdk): catch setTimeout callback error & Handle redundant `Uncaught` errors
- feat(cli): support debug mode flag
- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error
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
- feat(sdk): sortable support dark mode
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate
- feat(sdk): add switch tab options in api
- feat(sdk): add timeformat api
- feat(sdk): add showBackButton api
- feat(sdk): `native-textarea` add onPaste
- feat(sdk): `native-textarea` add `alwaysEmbed`
- feat(sdk): add the value of input type `decimals`
- feat(sdk): flutter-deprecated-textarea add `autoFocus`
- feat(sdk): new api page.updateRouteOptions
- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo
- feat(sdk): use tap for skyline
- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle
- feat(host): align response with native
- feat(sdk): flutter text component
- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18
- feat(demo): error handler demo
- feat(sdk): add deeplink target type
- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs
- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`
- feat(sdk): drawer component
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
- feat(sdk): choose image support compression threshold
- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode
- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components
- feat(sdk): webview component event api in queryselector
- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js
- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton
- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%
- feat(demo): add log for skyline debug & extended-lib should keep the built-in libs for cicd & ide
- feat(extended-lib): remove built-in upload and fix getUrl data not send
- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line
- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app
- feat(sdk): api hide back button
- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int
- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document
- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded
- feat(extended-lib): release to prod
- feat(sdk): custom native component
- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration
- feat(sdk): flutter can report lcp
- feat(host): support widget api
- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define
- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable
- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content
- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB
- feat(sdk): cherry-pick: add preloadflutterwebview api
- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event
- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor
- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection
- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list
- feat(sdk): editor support mention and hardBreak
- feat(bundler): use js-beautify replace prettier as formater of qjs
- feat(bundler): qjs compared from a formatted js code
- feat(lib): bmp-api openWidget add support for convention path
- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget
- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles
- feat(sdk): editor internal plugin link support
- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers
- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter
- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs
- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata
- feat(sdk): editor paste event props
- feat(sdk): echart component
- feat(sdk): editor selectImage api
- feat(mpp-service) add released pr
- feat(sdk): support walletkit and init func
- feat(demo): add manual to web input public demo
- feat(lib): add API removeSkeleton to bmp-react
- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image
- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider
- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API
- feat(demo): add prefetchRules
- feat(sdk): getUserOpenId return token
- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs
- feat(host): set custom http headers for fetch requests
- feat(sdk): ut from plugin-location to plugin-request-subscribe-message
- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo
- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher
- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API
- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly
- feat(demo): control picker view demo
- feat(sdk): detect page timeline
- feat(host): support pageReadyCallback
- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react
- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal
- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo
- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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
- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc
- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(cli): quick publish for dev & qa [NEZ-7388]
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target
- perf: add filesystem cache
- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "fix(sdk): export bmp component utils"
- Revert "chore: @mp/bundler dev"
- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)
- Revert "fix(sdk): iOS native component created failed when container is not visible "
- Revert "fix(sdk): env undefined"
- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)
- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action

## [5.8.0] 2026-01-30

**Download: [5.8.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.0.zip)**

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

## [5.7.4] 2026-01-26

**Download: [5.7.4(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.4.zip)**

### Misc

- revert: revert v5.7.2 and v5.7.3 which fix by native

## [5.7.3] 2026-01-16

**Download: [5.7.3(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.3.zip)**

### Bug Fixes

- fix(sdk): showErrorPage when setData unordered

## [5.7.2] 2026-01-15

**Download: [5.7.2(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.2.zip)**

### Features

- feat(sdk): showError page when node tree not matched

## [5.7.1] 2026-01-14

**Download: [5.7.1(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.1.zip)**

### Bug Fixes

- fix(sdk): fix route pending when page.js fails

## [5.6.1] 2026-01-14

**Download: [5.6.1(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.6.1.zip)**

### Bug Fixes

- fix(sdk): fix route pending when page.js fails

## [5.7.0] 2026-01-08

**Download: [5.7.0(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.0.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId
- feat(sdk): add internal doc site
- feat(cli): auto perf

## [5.5.3] 2025-12-29

**Download: [5.5.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.3.zip)**

## [5.4.2] 2025-12-29

**Download: [5.4.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.2.zip)**

## [5.2.10] 2025-12-29

**Download: [5.2.10(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.10.zip)**

## [5.6.0] 2025-12-19

**Download: [5.6.0(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.6.0.zip)**

### Bug Fixes

- fix(sdk): fix prerender inject data path
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

## [5.5.2] 2025-12-17

**Download: [5.5.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.2.zip)**

### Bug Fixes

- fix(sdk): add ut
- fix(lib): add comma to avoid MFA build error
- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android
- fix(cli): version sort
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

- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve
- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum
- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev
- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion

## [5.5.1] 2025-12-17

**Download: [5.5.1(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.1.zip)**

### Bug Fixes

- fix(libs); bmp-components imported unexpectedly by web project
- fix(sdk): usePageScroll hooks not work
- fix(bmp): pika ci error
- fix(sdk): fix resolve native comp & input update timestamp
- fix(sdk): render child node directly when component need children vnode
- fix(sdk): host mini app events and setData damaged by widget flow
- fix: revert comment
- fix(sdk): @binance/bmp-xx deps
- fix(sdk): scrollViewUpdate rendererId undefined
- fix(lib): define EMPTY_OBJ
- fix(sdk): fix build script
- fix(sdk): dep missing
- fix(sdk): plugins types issue
- fix(sdk): fake childnode
- fix(sdk): fix no text in child text
- fix(sdk): nested text node
- fix(sdk): remove capture event handler
- fix(cli): bundler function params missing
- fix(sdk): typo error
- fix(sdk): fix alias to avoid multiple event emit

### Features

- feat(bundler): fix bundler config
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
- feat(lib): use one reactMeta for context
- feat(sdk): update hummer webpack with production mode
- feat(sdk): update typo
- feat(lib): update useEffect
- feat(sdk): use pika **APPID**
- feat(lib): move context to bmp-react
- feat(lib): add context
- feat(cli): update bundler version
- feat(sdk): update widget
- feat(sdk): add log
- feat(sdk): add widget hummer
- feat(sdk): no cache for widget open event
- feat(sdk): remove global RuntimeMonitor
- feat(sdk): hummer send to worker pageready
- feat(sdk): track campatibility for app inst
- feat(sdk): support widget slot
- feat(sdk): widget plugin
- feat(sdk): support event & update
- feat(sdk): update widget
- feat(sdk): hummer event, context, widget update
- feat(sdk): add component render plugin
- feat(sdk): widget slot plugin
- feat(sdk): add page ready
- feat(sdk): export widget component
- feat(sdk): fix typo
- feat(sdk): add widgetOpen handler
- feat(sdk): widget plugin
- feat(sdk): remove app timeline check & loadApp directly
- feat(sdk): remove mg
- feat(sdk): draft widget
- feat(sdk): avoid event error of widget
- feat(sdk): mp lite support prerender
- feat(sdk): update 5.0 widget
- feat(sdk): remove app instance
- feat(bundler): init widget bundler
- feat(sdk): export methods for widget
- feat(sdk): worker not wait renderer ready
- feat(sdk): use vue render
- feat(sdk): add components alias
- feat(sdk): remove bxml render in worker
- feat(sdk): clean worker timeline
- feat(sdk): clean worker timeline
- feat(sdk): 5.0 add script to build renderer-service-hummer.js
- feat(sdk): remove vnode and patch on worker

### Misc

- Revert "Merge master"
- revert: root condition in setData

## [5.4.1] 2025-12-17

**Download: [5.4.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.1.zip)**

### Features

- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.3.5] 2025-12-17

**Download: [5.3.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.5.zip)**

## [5.2.9] 2025-12-15

**Download: [5.2.9(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.9.zip)**

### Bug Fixes

- fix(sdk): text dont filter nest components

## [5.5.0] 2025-11-27

**Download: [5.5.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.0.zip)**

### Features

- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.4.0] 2025-11-07

**Download: [5.4.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.0.zip)**

### Bug Fixes

- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android

### Features

- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum

## [5.2.8] 2025-11-04

**Download: [5.2.8(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.8.zip)**

### Bug Fixes

- fix(sdk): capacibility of document body
- fix(sdk): cp tab area scroll

## [5.3.4] 2025-11-04

**Download: [5.3.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.4.zip)**

### Bug Fixes

- fix(sdk): capacibility of document body
- fix(sdk): cp tab area scroll

## [5.3.4] 2025-11-04

**Download: [5.3.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.4.zip)**

### Bug Fixes

- fix(sdk): cp tab area scroll

## [5.2.8] 2025-11-04

**Download: [5.2.8(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.8.zip)**

### Bug Fixes

- fix(sdk): cp tab area scroll

## [4.51.4] 2025-11-03

**Download: [4.51.4(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.4.zip)**

### Bug Fixes

- Fix/tab move

## [5.3.3] 2025-11-02

**Download: [5.3.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.3.zip)**

### Bug Fixes

- fix(sdk): render data and prerender data independent to resolve flutter blink

## [5.2.7] 2025-11-02

**Download: [5.2.7(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.7.zip)**

### Bug Fixes

- fix(sdk): render data and prerender data independent to resolve flutter blink

## [4.51.3] 2025-10-30

**Download: [4.51.3(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.3.zip)**

### Features

- feat(sdk): editor chart UI revamp

## [5.3.2] 2025-10-30

**Download: [5.3.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.2.zip)**

### Bug Fixes

- fix(sdk): capacibility for prerender text

## [5.2.6] 2025-10-30

**Download: [5.2.6(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.6.zip)**

### Bug Fixes

- fix(sdk): capacibility for prerender text

## [4.51.2] 2025-10-29

**Download: [4.51.2(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.2.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [5.2.5] 2025-10-28

**Download: [5.2.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.5.zip)**

## [5.2.4] 2025-10-28

**Download: [5.2.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.4.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.3.1] 2025-10-28

**Download: [5.3.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.1.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.2.4] 2025-10-28

**Download: [5.2.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.4.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.3.0] 2025-10-17

**Download: [5.3.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.0.zip)**

### Features

- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [5.2.3] 2025-10-15

**Download: [5.2.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.3.zip)**

### Bug Fixes

- fix(sdk): nested text render

### Features

- feat(sdk): remove skeleton earlier to improve FCP

## [4.51.2] 2025-10-14

**Download: [4.51.2(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.2.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [4.51.1] 2025-10-13

**Download: [4.51.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.1.zip)**

### Features

- feat(sdk): flutter domToImage
- feat(mpp-service): update to junior

## [5.2.1] 2025-10-11

**Download: [5.2.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.1.zip)**

### Bug Fixes

- fix(sdk): render full attrs & buildin alias
- fix(cli): version sort

## [5.2.0] 2025-09-26

**Download: [5.2.0(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.0.zip)**

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

## [4.51.0] 2025-09-26

**Download: [4.51.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.0.zip)**

### Features

- Feat call all
- feat(sdk): sdk4.x support support formatter for all echart options

## [5.1.4] 2025-09-24

**Download: [5.1.4(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.4.zip)**

### Bug Fixes

- fix(sdk): usePageScroll hooks not work
- fix(sdk): hummer renderer support update single child

### Features

- feat(sdk): bn.removeWidgetSkeleton

## [5.1.3] 2025-09-17

**Download: [5.1.3(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.3.zip)**

### Bug Fixes

- fix(sdk): hummer render support update dom
- fix(sdk): fix hummer event not work because eventId not exist
- fix(sdk): comment log & debug log flag
- fix(sdk): remove duplicate worker module while hot-reload
- fix(sdk): fix render native webview

## [5.1.2] 2025-09-12

**Download: [5.1.2(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.2.zip)**

### Features

- feat(sdk): renderer mount do not wait worker rpc response

## [5.1.1] 2025-09-12

**Download: [5.1.1(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.1.zip)**

### Bug Fixes

- fix(sdk): fix widget FCP & LCP report
- fix(sdk): hotfix scrollview

### Features

- feat(sdk): sdk5.1 support formatter for all echart options

## [4.50.1] 2025-09-12

**Download: [4.50.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.50.1.zip)**

### Bug Fixes

- fix(sdk): hotfix scrollview

## [4.50.0] 2025-09-04

**Download: [4.50.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.50.0.zip)**

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

## [5.1.0] 2025-09-04

**Download: [5.1.0(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.0.zip)**

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

## [4.49.1] 2025-08-22

**Download: [4.49.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.49.1.zip)**

### Bug Fixes

- fix(sdk): nested scroll not work
- fix(sdk): menuBts props

## [5.0.0] 2025-08-15

**Download: [5.0.0(1.90 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.0.0.zip)**

### Bug Fixes

- fix(sdk): fix build script
- fix(sdk): dep missing
- fix(sdk): plugins types issue
- fix(sdk): fake childnode
- fix(sdk): fix no text in child text
- fix(sdk): nested text node
- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work
- fix(sdk): remove capture event handler
- fix(cli): bundler function params missing
- fix(sdk): typo error
- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- fix(sdk): fix alias to avoid multiple event emit
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y
- fix(sdk): expose the error before app init
- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(lib): use one reactMeta for context
- feat(sdk): update hummer webpack with production mode
- feat(sdk): update typo
- feat(lib): update useEffect
- feat(sdk): use pika **APPID**
- feat(lib): move context to bmp-react
- feat(lib): add context
- feat(cli): update bundler version
- feat(sdk): support share v2 api
- feat(sdk): update widget
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(sdk): add log
- feat(sdk): add widget hummer
- feat(sdk): no cache for widget open event
- feat(sdk): remove global RuntimeMonitor
- feat(sdk): hummer send to worker pageready
- feat(sdk): track campatibility for app inst
- feat(sdk): support widget slot
- feat(sdk): widget plugin
- feat(sdk): support event & update
- feat(sdk): update widget
- feat(sdk): hummer event, context, widget update
- feat(cli): support home page widget preview
- feat(sdk): add component render plugin
- feat(sdk): widget slot plugin
- feat(sdk): add page ready
- feat(sdk): export widget component
- feat(sdk): fix typo
- feat(sdk): add widgetOpen handler
- feat(sdk): widget plugin
- feat(sdk): remove app timeline check & loadApp directly
- feat(mpp-service): update ai router payload
- feat(sdk): remove mg
- feat(sdk): draft widget
- feat(mpp-service): ai router solution
- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(sdk): avoid event error of widget
- feat(cli): bundle watch process not exiting correctly
- feat(sdk): mp lite support prerender
- feat(sdk): update 5.0 widget
- feat(sdk): remove app instance
- feat(bundler): init widget bundler
- feat(sdk): export methods for widget
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message
- feat(sdk): worker not wait renderer ready
- feat(sdk): use vue render
- feat(sdk): add components alias
- feat(sdk): remove bxml render in worker
- feat(sdk): clean worker timeline
- feat(sdk): clean worker timeline
- feat(sdk): 5.0 add script to build renderer-service-hummer.js
- feat(sdk): remove vnode and patch on worker
- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo
- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib
- feat(sdk): suspend & resume lifecycle

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.49.0] 2025-08-14

**Download: [4.49.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.49.0.zip)**

### Bug Fixes

- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work

### Features

- feat(sdk): support share v2 api
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(cli): support home page widget preview
- feat(mpp-service): update ai router payload
- feat(mpp-service): ai router solution

## [4.48.1] 2025-08-04

**Download: [4.48.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.48.1.zip)**

### Bug Fixes

- fix(sdk): fix swiper loop mode & scroll view style

## [4.48.0] 2025-07-25

**Download: [4.48.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.48.0.zip)**

### Bug Fixes

- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y

### Features

- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.47.1] 2025-07-21

**Download: [4.47.1(1.84 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.47.1.zip)**

### Bug Fixes

- fix(sdk): scroll X in scroll Y (#2251)

## [4.47.0] 2025-07-07

**Download: [4.47.0(1.84 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.47.0.zip)**

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
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo

## [4.46.0] 2025-06-13

**Download: [4.46.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.46.0.zip)**

### Bug Fixes

- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.5] 2025-06-12

**Download: [4.45.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.5.zip)**

### Misc

- Revert "feat(sdk): remove set rem in flutter"

## [4.45.4] 2025-05-26

**Download: [4.45.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.4.zip)**

### Bug Fixes

- fix(sdk): add svg style filter
- fix(sdk): fix page-frame

### Features

- feat(sdk): remove set rem in flutter

## [4.45.3] 2025-05-23

**Download: [4.45.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.3.zip)**

### Bug Fixes

- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.3] 2025-05-23

**Download: [4.45.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.3.zip)**

### Features

- feat(sdk): remove set rem in flutter

## [4.45.2] 2025-05-21

**Download: [4.45.2(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.2.zip)**

### Bug Fixes

- fix(sdk): add svg style filter

## [4.45.1] 2025-05-19

**Download: [4.45.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.1.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.44.4] 2025-05-19

**Download: [4.44.4(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.4.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.45.1] 2025-05-19

**Download: [4.45.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.1.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.44.3] 2025-05-16

**Download: [4.44.3(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.3.zip)**

## [4.45.0] 2025-05-15

**Download: [4.45.0(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.0.zip)**

### Features

- feat(sdk): suspend & resume lifecycle

## [4.1043.1] 2025-05-12

**Download: [4.1043.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1043.1.zip)**

### Bug Fixes

- fix(sdk): support multiple chart instances with same chart id when work with swiper
- fix(sdk): observer doesn't work
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

## [4.44.2] 2025-05-12

**Download: [4.44.2(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.2.zip)**

### Bug Fixes

- fix(sdk): support multiple chart instances with same chart id when work with swiper

## [4.44.1] 2025-05-07

**Download: [4.44.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.1.zip)**

### Bug Fixes

- fix(sdk): observer doesn't work

## [4.44.0] 2025-05-02

**Download: [4.44.0(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.0.zip)**

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

## [4.1043.0] 2025-04-18

**Download: [4.1043.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1043.0.zip)**

## [4.43.1] 2025-04-16

**Download: [4.43.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.43.1.zip)**

### Bug Fixes

- fix(sdk): domtoimage image url corner cases

### Features

- feat(sdk): add dark_midnight support for prerender

## [4.43.0] 2025-04-10

**Download: [4.43.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.43.0.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill
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

## [4.42.2] 2025-04-02

**Download: [4.42.2(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.2.zip)**

## [4.42.1] 2025-03-25

**Download: [4.42.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.1.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill

## [4.42.0] 2025-03-21

**Download: [4.42.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.0.zip)**

### Bug Fixes

- fix(cli): missing build start callback in bundleWatch
- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`

### Features

- feat(cli): rebundle while refresh
- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo

## [4.41.7] 2025-03-20

**Download: [4.41.7(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.7.zip)**

### Bug Fixes

- fix(sdk): duplicated route change

## [4.41.6] 2025-03-19

**Download: [4.41.6(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.6.zip)**

### Bug Fixes

- fix(sdk): fix modal navigate on android 2.97(no cherry pick to master)

## [4.41.5] 2025-03-17

**Download: [4.41.5(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.5.zip)**

## [4.41.4] 2025-03-14

**Download: [4.41.4(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.4.zip)**

### Features

- feat(sdk): improve drag & sort behaviour

## [4.41.3] 2025-03-10

**Download: [4.41.3(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.3.zip)**

### Performance Improvements

- perf: optimize performance by remove rpc log
- perf: remove logger to fast lcp metric

## [4.41.3] 2025-03-10

**Download: [4.41.3(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.3.zip)**

### Performance Improvements

- perf: remove logger to fast lcp metric

## [4.41.2] 2025-03-07

**Download: [4.41.2(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.2.zip)**

### Bug Fixes

- fix(sdk): intersection Observer component undefined issue

## [4.41.1] 2025-03-06

**Download: [4.41.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.1.zip)**

### Bug Fixes

- fix(sdk): free mode sortable and highlight input rtl issue

## [4.41.0] 2025-03-03

**Download: [4.41.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.0.zip)**

### Bug Fixes

- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

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

## [4.41.0] 2025-02-28

**Download: [4.41.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.0.zip)**

### Bug Fixes

- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

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

## [4.40.2] 2025-02-21

**Download: [4.40.2(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.2.zip)**

### Bug Fixes

- fix(sdk): domToImage only disabled in flutter

## [4.40.1] 2025-02-19

**Download: [4.40.1(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.1.zip)**

### Bug Fixes

- fix(sdk): flutterTarget can not be converted directly

## [4.40.0] 2025-02-10

**Download: [4.40.0(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.0.zip)**

### Bug Fixes

- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices
- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2

### Features

- feat(sdk): add disable-ios-embed props for ios native input
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

## [4.39.8] 2025-01-29

**Download: [4.39.8(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.8.zip)**

### Bug Fixes

- fix(sdk): changelog script

## [4.39.7] 2025-01-27

**Download: [4.39.7(2.47 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.7.zip)**

### Bug Fixes

- fix(sdk): remove skyline sync ui command

## [4.38.7] 2025-01-24

**Download: [4.38.7(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.7.zip)**

### Bug Fixes

- fix(sdk): disable scrolling when scroll into view

## [4.37.11] 2025-01-24

**Download: [4.37.11(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.11.zip)**

### Bug Fixes

- fix(sdk): disable scrolling when scroll into view

## [4.39.6] 2025-01-24

**Download: [4.39.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.6.zip)**

### Features

- feat(sdk): disable scrolling when scroll into viewe

## [4.38.6] 2025-01-23

**Download: [4.38.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.6.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

### Features

- feat(sdk): native-input cursor issue

## [4.37.10] 2025-01-23

**Download: [4.37.10(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.10.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

### Features

- feat(sdk): native-input cursor issue

## [4.37.10] 2025-01-23

**Download: [4.37.10(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.10.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.38.6] 2025-01-23

**Download: [4.38.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.6.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.39.5] 2025-01-23

**Download: [4.39.5(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.5.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.39.4] 2025-01-21

**Download: [4.39.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.4.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.38.5] 2025-01-21

**Download: [4.38.5(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.5.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.37.9] 2025-01-21

**Download: [4.37.9(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.9.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.38.4] 2025-01-21

**Download: [4.38.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.4.zip)**

### Bug Fixes

- fix(sdk): 438 virtual list hotfix 0120

## [4.37.8] 2025-01-21

**Download: [4.37.8(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.8.zip)**

### Bug Fixes

- fix(sdk): virtual list hotfix 0120

## [4.39.3] 2025-01-20

**Download: [4.39.3(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.3.zip)**

### Bug Fixes

- fix(sdk): 439 virtual list hotfix 0120

## [4.38.4] 2025-01-20

**Download: [4.38.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.4.zip)**

### Bug Fixes

- fix(sdk): 438 virtual list hotfix 0120

## [4.37.8] 2025-01-20

**Download: [4.37.8(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.8.zip)**

### Bug Fixes

- fix(sdk): virtual list hotfix 0120

## [4.39.2] 2025-01-17

**Download: [4.39.2(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.2.zip)**

### Features

- feat(sdk): view component add events `onAppear&onIntersectionChange&o…

## [4.39.1] 2025-01-17

**Download: [4.39.1(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.1.zip)**

### Bug Fixes

- fix(sdk): 4.39 virtual list hotfix

## [4.38.3] 2025-01-17

**Download: [4.38.3(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.3.zip)**

## [4.37.7] 2025-01-17

**Download: [4.37.7(2.49 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.7.zip)**

## [4.39.0] 2025-01-16

**Download: [4.39.0(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.0.zip)**

### Bug Fixes

- fix(bmp): remove requestFullscreen param
- fix(sdk): flutter-video context issue

### Features

- feat(sdk): add showDiagnosticPage API
- feat(sdk): native-input cursor issue
- feat(sdk): add flutter-chart component
- feat(sdk): catch setTimeout callback error & Handle redundant `Uncaught` errors
- feat(cli): support debug mode flag

## [4.38.2] 2025-01-09

**Download: [4.38.2(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.2.zip)**

### Bug Fixes

- fix(sdk): flutter-video context issue
- fix(sdk): chart should be destroy after unmounted
- fix(sdk): enable placeholder for flutter

## [4.38.1] 2025-01-03

**Download: [4.38.1(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.1.zip)**

### Bug Fixes

- fix(sdk): chartActionQueue cache with id and monitor LCPElement payload

### Performance Improvements

- perf: remove getBoundingClientRect in flutter widget and nativeComp

## [4.38.0] 2024-12-26

**Download: [4.38.0(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.0.zip)**

### Bug Fixes

- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed

### Features

- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error
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

## [4.37.6] 2024-12-19

**Download: [4.37.6(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.6.zip)**

## [4.37.5] 2024-12-19

**Download: [4.37.5(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.5.zip)**

### Bug Fixes

- fix(sdk): svg object.hasown not found

## [4.37.4] 2024-12-17

**Download: [4.37.4(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.4.zip)**

### Features

- feat(sdk): svg improve inline tag support

## [4.37.3] 2024-12-12

**Download: [4.37.3(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.3.zip)**

### Bug Fixes

- fix(sdk): remove repeat effect when worker data update

## [4.36.3] 2024-12-12

**Download: [4.36.3(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.3.zip)**

### Features

- feat(sdk): add skeleton remove point

## [4.36.3] 2024-12-11

**Download: [4.36.3(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.3.zip)**

### Bug Fixes

- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): add remove skeleton point
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.37.2] 2024-12-10

**Download: [4.37.2(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.2.zip)**

### Bug Fixes

- fix(sdk): hotfix 4.37.2

## [4.37.1] 2024-12-09

**Download: [4.37.1(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.1.zip)**

### Bug Fixes

- fix(sdk): refresher event detail not provide the flutterTarget as expect

## [4.37.0] 2024-12-05

**Download: [4.37.0(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.0.zip)**

### Bug Fixes

- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): sortable support dark mode
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.36.2] 2024-11-27

**Download: [4.36.2(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.2.zip)**

### Bug Fixes

- fix(sdk): resolve IntersectionObserver is undefined issue

### Features

- feat(sdk): expose response for native component

## [4.36.1] 2024-11-20

**Download: [4.36.1(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.1.zip)**

### Bug Fixes

- fix(sdk): webview instance id should not repeat

## [4.36.0] 2024-11-15

**Download: [4.36.0(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.0.zip)**

### Bug Fixes

- fix(sdk): change handlePaste defaultValue
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

## [4.35.2] 2024-11-08

**Download: [4.35.2(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.2.zip)**

### Bug Fixes

- fix(sdk): check whether to use patch
- fix(sdk): release flutter image load
- fix(sdk): wrap inline element with bn-span for bn-markdown

### Misc

- Revert "chore: revert ui command"

## [4.35.1] 2024-10-31

**Download: [4.35.1(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.1.zip)**

### Bug Fixes

- fix(sdk): markdown paragraph use bn-view, strong/em use bn-text

## [4.35.0] 2024-10-25

**Download: [4.35.0(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.0.zip)**

### Bug Fixes

- fix(sdk): support inlineLayout for skyline
- fix(sdk): flutter scroll refresher background color
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

- feat(sdk): new api page.updateRouteOptions
- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo
- feat(sdk): use tap for skyline
- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.34.7] 2024-10-25

**Download: [4.34.7(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.7.zip)**

### Bug Fixes

- fix(sdk): support tap and inlineLayout for skyline

## [4.34.6] 2024-10-22

**Download: [4.34.6(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.6.zip)**

### Bug Fixes

- fix(sdk): android 7 quickjs not support Unicode Property Escapes

## [4.34.5] 2024-10-15

**Download: [4.34.5(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.5.zip)**

### Bug Fixes

- fix(sdk): `deprecated-textarea` support force update

## [4.34.4] 2024-10-11

**Download: [4.34.4(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.4.zip)**

### Features

- feat(sdk): web-view-post-message event handler

## [4.34.3] 2024-10-10

**Download: [4.34.3(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.3.zip)**

### Features

- feat(sdk): setup markdown on flutter

## [4.34.2] 2024-10-09

**Download: [4.34.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.2.zip)**

### Bug Fixes

- fix(sdk): message for createwebview api instance

## [4.33.3] 2024-10-09

**Download: [4.33.3(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.3.zip)**

### Bug Fixes

- fix(sdk): hotfix 4.33.3 deprecated textarea

## [4.34.1] 2024-10-09

**Download: [4.34.1(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.1.zip)**

### Bug Fixes

- fix(sdk): flutter deprecated textarea when composing
- fix(sdk): flutter deprecated textarea

## [4.34.0] 2024-10-07

**Download: [4.34.0(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.0.zip)**

### Bug Fixes

- fix(sdk): fix webview message action not work
- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(host): align response with native
- feat(sdk): flutter text component
- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.2] 2024-09-19

**Download: [4.33.2(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.2.zip)**

### Bug Fixes

- fix: add FlutterImage switch and remove FlutterSrollView type=list props

## [4.33.2] 2024-09-19

**Download: [4.33.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.2.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.1] 2024-09-17

**Download: [4.33.1(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.1.zip)**

## [4.33.0] 2024-09-13

**Download: [4.33.0(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.0.zip)**

### Bug Fixes

- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop
- fix(sdk): fix component patch error messsage
- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type

### Features

- feat(demo): error handler demo
- feat(sdk): add deeplink target type
- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs
- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)

## [4.32.1] 2024-08-30

**Download: [4.32.1(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.32.1.zip)**

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786)

## [4.32.0] 2024-08-23

**Download: [4.32.0(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.32.0.zip)**

### Bug Fixes

- fix(sdk): vnode patch issues
- fix(sdk): navigate to type
- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory

### Features

- feat(sdk): drawer component
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

## [4.31.1] 2024-08-02

**Download: [4.31.1(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.31.1.zip)**

### Bug Fixes

- fix: add worker plugin

## [4.31.0] 2024-08-02

**Download: [4.31.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.31.0.zip)**

### Bug Fixes

- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler

### Features

- feat(sdk): choose image support compression threshold
- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode
- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components

## [4.30.0] 2024-07-12

**Download: [4.30.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.30.0.zip)**

### Bug Fixes

- fix(sdk): native component webview message
- fix(sdk): native event in worker
- fix(sdk): fix webview component
- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error

### Features

- feat(sdk): webview component event api in queryselector
- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js

## [4.29.0] 2024-06-24

**Download: [4.29.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.29.0.zip)**

### Bug Fixes

- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure
- fix(sdk): cursor is wired when editor tap keyboard enter

### Features

- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton
- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%

## [4.28.0] 2024-05-31

**Download: [4.28.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.28.0.zip)**

### Bug Fixes

- fix: update render cache doc id
- fix(extended-lib): resolve path not a module

### Features

- feat(demo): add log for skyline debug & extended-lib should keep the built-in libs for cicd & ide
- feat(extended-lib): remove built-in upload and fix getUrl data not send
- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line

## [4.27.0] 2024-05-10

**Download: [4.27.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.27.0.zip)**

### Bug Fixes

- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload
- fix(extended-lib): postpublish script throw error

### Features

- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app
- feat(sdk): api hide back button
- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int

## [4.26.2] 2024-04-23

**Download: [4.26.2(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.2.zip)**

### Bug Fixes

- fix(sdk): wsw call id

## [4.26.1] 2024-04-22

**Download: [4.26.1(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.1.zip)**

### Features

- feat(sdk): web3 plugin use shell app (#1687)

## [4.26.0] 2024-04-19

**Download: [4.26.0(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.0.zip)**

### Bug Fixes

- fix(host): support webassembly on host
- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions

### Features

- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document
- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded

## [4.25.1] 2024-04-10

**Download: [4.25.1(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.25.1.zip)**

### Bug Fixes

- fix(sdk): echart no need delay
- fix(sdk): delay onReady for tarojs

### Features

- feat(sdk): add more error message info for appjs load

## [4.25.0] 2024-03-29

**Download: [4.25.0(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.25.0.zip)**

### Bug Fixes

- fix(extended-lib): add missing deps
- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type

### Features

- feat(extended-lib): release to prod
- feat(sdk): custom native component
- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration

## [4.23.1] 2024-02-21

**Download: [4.23.1(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.23.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick for hotfix

## [4.23.0] 2024-02-19

**Download: [4.23.0(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.23.0.zip)**

### Bug Fixes

- fix(sdk): when user delete all content web input may act unexpected
- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE

### Features

- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define

## [4.22.0] 2024-01-26

**Download: [4.22.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.22.0.zip)**

### Bug Fixes

- fix(demo): icon size demo
- fix(sdk): label trigger itemClick event for radio and checkbox

### Features

- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable
- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content

## [4.21.0] 2024-01-09

**Download: [4.21.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.21.0.zip)**

### Features

- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB

## [4.20.0] 2023-12-15

**Download: [4.20.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.20.0.zip)**

### Bug Fixes

- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter

## [4.19.0] 2023-11-24

**Download: [4.19.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.19.0.zip)**

### Bug Fixes

- fix(bundler): fix IDE can not reload

### Features

- feat(sdk): cherry-pick: add preloadflutterwebview api
- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event
- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor

## [4.18.1] 2023-11-22

**Download: [4.18.1(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.18.1.zip)**

### Features

- feat(sdk): add preloadflutterwebview api

## [4.18.0] 2023-11-03

**Download: [4.18.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.18.0.zip)**

### Bug Fixes

- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value
- fix(sdk): support input focus and blur action by developers

### Features

- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection
- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list
- feat(sdk): editor support mention and hardBreak

## [4.17.2] 2023-10-23

**Download: [4.17.2(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.2.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

## [4.17.1] 2023-10-18

**Download: [4.17.1(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.1.zip)**

### Bug Fixes

- fix(sdk): END_FIRSTPAGE_APPLAUNCH send pid

### Features

- feat(bundler): use js-beautify replace prettier as formater of qjs

## [4.16.3] 2023-10-13

**Download: [4.16.3(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.3.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.17.0] 2023-10-13

**Download: [4.17.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.0.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page
- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger

### Features

- feat(bundler): qjs compared from a formatted js code
- feat(lib): bmp-api openWidget add support for convention path
- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget

## [4.16.3] 2023-10-13

**Download: [4.16.3(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.3.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.16.2] 2023-09-27

**Download: [4.16.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.2.zip)**

### Bug Fixes

- fix(sdk): avoid crash when worker receive invalid tags

## [4.16.1] 2023-09-25

**Download: [4.16.1(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.1.zip)**

### Bug Fixes

- fix(sdk): editor link node

## [4.16.0] 2023-09-22

**Download: [4.16.0(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.0.zip)**

### Bug Fixes

- fix(sdk): revert swiper located to wrong child when children updated
- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper
- fix(bundler): bundler watch has 60s cache

### Features

- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles
- feat(sdk): editor internal plugin link support

## [4.15.1] 2023-09-07

**Download: [4.15.1(2.34 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.15.1.zip)**

### Bug Fixes

- fix(sdk): fix call plugin error code

## [4.15.0] 2023-08-31

**Download: [4.15.0(2.34 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.15.0.zip)**

### Bug Fixes

- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots
- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci
- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount

### Features

- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers
- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter
- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs

## [4.14.0] 2023-08-11

**Download: [4.14.0(1.45 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.14.0.zip)**

### Bug Fixes

- fix(sdk): create webview api in mp cannot message
- fix(sdk): customize component data not update when return a data getter
- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop

### Features

- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata
- feat(sdk): editor paste event props
- feat(sdk): echart component

## [4.13.1] 2023-07-28

**Download: [4.13.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.13.1.zip)**

### Bug Fixes

- fix(sdk): unicode regex issue
- fix(sdk): editor remove link and style recover
- fix(sdk): object spread syntax error
- fix(sdk): editor split figure bugs
- fix(sdk): object spread sytax error
- fix(sdk): add seqId to web input event

## [4.13.0] 2023-07-26

**Download: [4.13.0(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.13.0.zip)**

### Bug Fixes

- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer
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

### Misc

- Revert "fix(sdk): iOS native component created failed when container is not visible "

## [4.12.1] 2023-07-07

**Download: [4.12.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.12.1.zip)**

### Features

- feat: add mamual prop to web input

## [4.12.0] 2023-06-30

**Download: [4.12.0(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.12.0.zip)**

### Bug Fixes

- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs

### Features

- feat(lib): add API removeSkeleton to bmp-react
- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image

### Performance Improvements

- perf: add filesystem cache

## [4.11.1] 2023-06-27

**Download: [4.11.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.11.1.zip)**

### Bug Fixes

- fix(sdk): domtoimage svg base64 not have datatype (4.11)

## [4.11.0] 2023-06-16

**Download: [4.11.0(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.11.0.zip)**

### Bug Fixes

- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo
- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images
- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work

### Features

- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider
- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API

## [4.10.2] 2023-06-08

**Download: [4.10.2(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.2.zip)**

### Bug Fixes

- fix(sdk): fix startCheckPageTimeline error

## [4.10.1] 2023-05-25

**Download: [4.10.1(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.1.zip)**

### Bug Fixes

- fix(sdk): renderer service compatitable with es5

## [4.10.0] 2023-05-23

**Download: [4.10.0(1.10 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.0.zip)**

### Bug Fixes

- fix(mpp-service): set maxBodyLength & maxContentLength as Infinity wh…
- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend
- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack
- fix(sdk): load page frame after load base.bxml success
- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found

### Features

- feat(demo): add prefetchRules
- feat(sdk): getUserOpenId return token
- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs

## [4.9.2] 2023-05-19

**Download: [4.9.2(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.2.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params

## [4.9.1] 2023-05-17

**Download: [4.9.1(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.1.zip)**

### Bug Fixes

- fix(sdk): update load script error code

### Features

- feat(sdk): use appConfig after init appConfig & add appConfig detection & syncGetPage or
  asyncGetPage
- feat(host): set custom http headers for fetch requests

## [4.9.0] 2023-04-28

**Download: [4.9.0(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.0.zip)**

### Bug Fixes

- fix(sdk): figure scrollIntoView should focus on the figure caption
- fix(demo): production convertToMPUrl usage
- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise
- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs
- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version
- fix(demo): bug in navigation demo
- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue
- fix(sdk): add native-send-appLuanch timer
- fix(bundler): css variables rpx to rem align with wechat
- fix(sdk): mini game view port size
- fix(sdk): getChildrenNode util function
- fix(sdk): rendererId zero issue in native ui
- fix(bundler): catchmove value should be an exp
- fix(sdk): swiper Item blank
- fix(demo): fix custom demo textarea maxlength
- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component
- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes
- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css
- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): ut from plugin-location to plugin-request-subscribe-message
- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo
- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher
- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API
- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly
- feat(demo): control picker view demo
- feat(sdk): detect page timeline
- feat(host): support pageReadyCallback
- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react
- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal
- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo
- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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
- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc
- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "fix(sdk): env undefined"
- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

## [4.8.1] 2023-04-13

**Download: [4.8.1(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.8.1.zip)**

### Bug Fixes

- fix(sdk): fix load page.js error to report 603505 when webview is destroyed

## [4.8.0] 2023-04-07

**Download: [4.8.0(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.8.0.zip)**

### Bug Fixes

- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version

### Features

- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API

## [4.7.1] 2023-03-23

**Download: [4.7.1(NaN MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.7.1.zip)**

### Bug Fixes

- fix(sdk): startuptimeout & try catch getpage & add get page info
- fix(demo): bug in navigation demo

### Features

- feat(sdk): catch html
- feat(sdk): figure

## [4.7.0] 2023-03-17

**Download: [4.7.0(1.1 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.7.0.zip)**

### Bug Fixes

- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue

### Features

- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly

## [3.14.16] 2023-02-24

**Download: [SDK-3.14.16](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.16.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([d9a10d59](https://git.toolsfdg.net/fe/mini-program/commit/d9a10d599fb2ab6d7c222c2204917dcd7511a888))
  by lawrence.w@binance.com

## [4.6.0] 2023-02-24

**Download: [SDK-4.6.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.6.0.zip)**

### Bug Fixes

- fix(sdk): add native-send-appLuanch timer
  ([532dde2e](https://git.toolsfdg.net/fe/mini-program/commit/532dde2e37e8c3ff48cbf655238b88a9a1ff0dcd))
  by finley.x@binance.com
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
- fix(sdk): controlled picker view
  ([661aa89a](https://git.toolsfdg.net/fe/mini-program/commit/661aa89ad9c3289ce614f2b77995d4ebf6d08bfa))
  by lawrence.w@binance.com

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

- chore: bump commit after write files
  ([9378fed1](https://git.toolsfdg.net/fe/mini-program/commit/9378fed122a9613f50aac333ff8543d12893bbbc))
  by dylan.z@binance.com
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
- mpp service support binance us host app
  ([fb8edeb8](https://git.toolsfdg.net/fe/mini-program/commit/fb8edeb8c6840cc84ef840c6ca84dcfc3a51fd72))
  by leo.cc@binance.com

## [4.5.0] 2023-02-03

**Download: [SDK-4.5.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.5.0.zip)**

### Bug Fixes

- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component

### Features

- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react

### Refactor

- refactor: throw error for the non-supported apis in IDE

### Internal

- chore: update component demo
- docs: remove the app.config.json issue since pika will support it
- docs: getCurrentInstance query incorrect

## [4.4.0] 2023-01-13

**Download: [SDK-4.4.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.4.0.zip)**

### Bug Fixes

- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes

### Features

- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal

### Internal

- chore: update config for FAQ
- docs: faq about app.config.json
- docs(sdk): darkmode
- chore(sdk): cherry pick update sdk loading
- test: add more unit tests for host

## [3.14.15] 2023-01-10

**Download: [SDK-3.14.15](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.15.zip)**

### Bug Fixes

- fix(sdk): cherry pick from native component css

### Internal

- cherry-pick(sdk): swiper

## [3.14.14] 2023-01-04

**Download: [SDK-3.14.14](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.14.zip)**

### Bug Fixes

- fix(sdk): picker view component

### Features

- feat(sdk): add applaunch pid & new point from pageJsEnd to pageReady
- feat(sdk): cherry-pick - add error log for 603114

## [3.14.13] 2022-12-29

**Download: [SDK-3.14.13](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.13.zip)**

### Bug Fixes

- fix(sdk): image style not work when set mode to aspectFill

## [3.14.12] 2022-12-26

**Download: [SDK-3.14.12](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.12.zip)**

### Bug Fixes

- fix(sdk): update sdk loading

## [4.3.0] 2022-12-22

**Download: [SDK-4.3.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.3.0.zip)**

### Bug Fixes

- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css

### Features

- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo

### Refactor

- refactor: rename host-mp-ide to host-ide

### Internal

- chore: remove `yarn playwright install --with-deps`
- docs(sdk): integrate with doc-system
- chore(package.json): fix installing sqllite3 in macos
- chore(package.json): add packageManager field
- chore: replace resolve with join
- chore(sdk): cherry-pick from 4.2.1
- chore: update version remote and pwd alias
- chore: bump local
- chore: update prefetch rule of component demo
- docs: demos readme

## [3.14.11] 2022-12-19

**Download: [SDK-3.14.11](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.11.zip)**

### Bug Fixes

- fix(sdk): appConfig bug in ios while open worker pool

## [4.2.1] 2022-12-15

**Download: [SDK-4.2.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.2.1.zip)**

### Features

- feat(sdk): add mg page-ready

## [3.14.10] 2022-12-07

**Download: [SDK-3.14.10](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.10.zip)**

### Bug Fixes

- fix(sdk): fix renderer-defer lead to blank screen

## [4.2.0] 2022-12-02

**Download: [SDK-4.2.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.2.0.zip)**

### Bug Fixes

- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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

- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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

- refactor(sdk): plugins including show-leaderboard, storage and tab-bar
- refactor(sdk): native ui plugin
- refactor(sdk): replace enum with union type
- refactor(host): plugin user-info
- refactor(host): plugin & remove twoFA demo

### Internal

- chore: remove useless message in changelog.md by 'bot'
- chore: redirect blank page issue
- ci: fix git push tag one by one
- chore: add caretColor demo
- chore: gen-sdk local

## [3.14.9] 2022-12-01

**Download: [SDK-3.14.9](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.9.zip)**

### Features

- feat(sdk): support navigateTo an external link - cherry pick

## [3.14.8] 2022-11-22

**Download: [SDK-3.14.8](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.8.zip)**

### Bug Fixes

- fix(sdk): fix native delay app-launch after background and load \_\_app.js fail to lead blank
  screen

### Features

- feat(sdk): nezha render js point

## [4.0.3] 2022-11-18

**Download: [SDK-4.0.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.3.zip)**

### Bug Fixes

- fix(sdk): rendererId start with zero
- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs
- fix(sdk): env undefined
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1

## [3.14.7] 2022-11-17

**Download: [SDK-3.14.7](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.7.zip)**

### Features

- feat(sdk): add support caretColor style for Input and TextArea components

## [3.14.6] 2022-11-16

**Download: [SDK-3.14.6](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.6.zip)**

### Bug Fixes

- fix(sdk): load-script-progress event when mp background event to lead blank screen
- fix(sdk): remove generating worker-service-game.qjs

### Internal

- chore: add checker for 3.14
- chore: gen-sdk script
- chore: update changelog.js

## [4.1.0] 2022-11-16

**Download: [SDK-4.1.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1.0.zip)**

### Bug Fixes

- fix(cli): skip generation of unmatched tags
- fix(sdk): read-file demo, location api
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin
- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore: 4.1 pr checker
- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2
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
- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.1.0] 2022-11-16

**Download: [SDK-4.1.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1.0.zip)**

### Bug Fixes

- fix(sdk): read-file demo, location api
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin
- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore: 4.1 pr checker
- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2
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
- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.0.2] 2022-11-14)

**Download: [SDK-4.0.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.2.zip)**

### Bug Fixes

- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs
- fix(sdk): env undefined
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js
- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e
- fix(sdk): share-panel not working
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action
- fix(sdk): fix timeline order error
- fix(sdk): remove global wx, fix getOpenDataContext placeholder
- fix(sdk): timeline appJs error
- fix(sdk): timeline-update
- fix(cli): debugReact with react-reconciler not works
- fix(sdk): increase gas limit when estiamte gas failed
- fix(runtime): postMessage should wait for ready
- fix(cli): resolve taro presets from installation dir of bmp
- fix(cli): support node 15
- fix(sdk): can-i-use types & injectPrivateApi
- fix(rumtime): support tmp/store/usr http request
- fix(bundler): source-map OOM & repeated refresh in watch mode issues
- fix(sdk): fix onOffManager memory leak for task-style apis
- fix(demo): fix demo for fileSystemManager
- fix(runtime): add Math.ceil when populate gas
- fix(sdk): canvas plugin
- fix(bundler): adjust the order of loading script in page-frame
- fix(bundler): load base.bxml.js earlier than renderer-service.js
- fix(sdk): plugin write file
- fix(sdk): blank page when relaunch in old ios device
- fix(sdk): support cocos
- fix(sdk): app-rpc-logger judge from or to & delete extra log
- fix(sdk): monitor d change to dt & update RuntimeLogger monitor-upload
- fix(sdk): webview not working for the webview using node-bridge
- fix(bundler): load base.bxml.js in head element of page-frame
- fix(sdk): plugin-private-request command
- fix(sdk): add dataset to MPEventTarget
- fix(runtime): onNativeApiRequest able to listen all actions
- fix(sdk): radio and checkbox components
- fix(sdk): ios not support bigint 64
- fix(sdk): sentry + vconsole cause oom
- fix(sdk): fix Android need to tap input twice to focus
- fix(sdk): fix the issue that slider wrap with position: relative container
- fix(mp): fix request cookie setting
- fix(sdk): fix reportEvent with keyword to error
- fix(sdk): timeline startup del loadAppJs
- fix(sdk): DeprecatedInput auto-fill not emit input event
- fix(sdk): fix native input color with autoFocus props
- fix(runtime): storage plugin api not work
- fix(sdk): fix Image style width:100%
- fix(sdk): remove header filed with null value
- fix: add defer for webview context in the node-bridge demo
- fix: create a empty webview if src not provied
- fix(mp): fix tab bar css, red dot api error message
- fix(sdk): fix Image style being overridden and comments using English
- fix(sdk): image can not use width/height: auto with div-bgImg
- fix(sdk): onAppShow not working
- fix(sdk): remove the error of webivew-sdk Unknown Action $ready
- fix(sdk): update image component from img to div with background-image
- fix: framework-load-script has been registed
- fix(sdk): fix View component touchstart twice (#295)
- fix(lib,sdk): fix deprecated-input onInput not working
- fix(runtime): show & hide ToastContainer
- fix(sdk): plugin create native buffer
- fix(sdk): Image and IDECoverImage onload & onerror
- fix(sdk): timelogger error add time
- fix(sdk): debounce update state for native input
- fix(sdk): fix re-launch page not found issue
- fix(runtime): fix storage plugin
- fix(sdk): disable the JS timer for blank page detection
- fix(lib): make bundler generate component code that not override comp…
- fix(runtime): prevent app.js load twice
- fix(sdk): polyfill IntersectionObserver for iOS 12.1 (#237)
- fix: add commit hash to branch name
- Fix: release script
- fix: unexport subscribeLocationChange
- fix: sdk build
- fix the problem that bundler still work when in h5 mode
- fix some dependencies of project template
- fix: use path.resolve
- fix: make form component soft controlled & add missing component map
- fix: use -o
- fix the problem after last commit which make bundle script not work
- fix: normalize page url
- fix: 🐛 overwrite template files
- fix for debugger
- fix: 🐛 add http-proxy-middleware@0.19 in runtime-render
- Fix/fix the request with correct parameters and all other things for mvp2
- fix: send body only for post and put method
- fix: prevent user from scaling view
- fix: remove useless code
- fix(runtime-renderer): fix multiple event binding on same event
- fix: get props and data from parent & rename api
- fix: typo
- fix: use Object.assign
- fix: reduce payload size
- fix: Resolve events from attrs and separate two rpc events
- fix: use eventNames to tell the different if it is a event name or a normal props name
- fix: watch $props
- fix: rename
- fix: watch all props changed
- fix: remove bind props interface
- fix: remove useless code
- fix the problem invoked by packange name changed of taro plugin
- fix: prevent capture event trigger twice
- fix: 🐛 use e.currentTarget
- fix: 🐛 renderTaro and updateData
- fix: 🐛 renderTaro
- fix: keep compatible with taro
- fix: add tapCapture
- fix: add capture event
- fix: update props naming
- fix: remove console.log
- fix: Non-function value encountered for default slot. Prefer function slots for better
  performance.
- fix: remove console.log
- fix: types
- fix: update sdk
- fix: response.data typing
- fix: 🐛 enableCSSModule
- fix: call ready before navigation-push
- fix: typo
- fix: typo
- fix: typo
- fix: change data type
- fix: 🐛 back to list page
- fix: rpc
- fix(runner): rpc message format
- fix(runner): rpc message format
- fix: pass query to page.oLoad
- fix: fix ready and push action order
- fix: page component created twice
- fix: fix page hooks
- fix: 🐛 support page-hide and page-show
- fix: 🐛 not parse querystring when method is GET or HEAD
- fix: 🐛 createAndSavePage params
- fix: 🐛 init lifecycle and method
- fix: 🐛 only create page when \_\_pageConfig exist
- fix: 🐛 create page on worker runtime
- fix: build
- fix: disable webpack-dev-server host check
- fix: improve js compatibility
- fix: improve js compatibility
- fix: prefix component instance id with page id
- fix(rpc): change rpc interface
- fix: 🐛 add recordInstanceBoundEffect
- fix: 🐛 remove effect
- fix: 🐛 computed bind to ctx
- fix: change defualt build format to esm-bundler
- fix: change defualt build format to esm-bundler
- fix(project): fix default format
- fix(project): format package.json
- fix(project): rm .gitkeep & fix deps
- fix: typo
- fix: COMPONENT_TYPE_ID is undefined
- fix: 🐛 build script

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …
- feat(bundler & mpp-service): add bundler-cli & support output .pkg files
- feat(sdk): clear detection when hidden
- feat(demo): update runtime-web-host bundleAll params
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(sdk): framework-storage plugin
- feat(bundler,cli): update bundler log info
- feat(mpp-service): add package mpp-service to tools
- feat(sdk): hotfix-3.7.3-onerror-monitor-upload
- feat(sdk): try catch error in App lifecycle
- feat(sdk): add load pageJS info in timeline logger
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(bundler): move page logic to page.worker.js
- feat(sdk): add startAppLaunch handleAppLaunchCallback in runtimeloger
- feat(demo): preloadRule demo app
- feat(sdk,runtime): file system manger access api sdk,runtime,demo
- feat(cli): add button open-type getUserProfile & getEmailAddress
- feat(sdk): canIUse plugin
- feat(demo): handle error demo
- feat(runtime): remove native-ui
- feat(sdk): add Button open-type attribute getUserProfile
- feat(sdk): add Button open-type attribute openSetting
- feat(sdk): add wallet-connector plugin
- feat(lib): add binary-pkg to bundler
- feat(sdk): add API isLoggedIn & add custom plugin ensure-logged-in
- feat(demo): private-request demo
- feat(runtime): filesystem permission
- feat(sdk): plugin device-orientation-change
- feat: add disableBounces page to demo app
- feat(mp,sdk): file system plugins
- feat: private-request plugin
- feat(sdk): app-rpc logger add event
- feat(mp): buffer-url mp plugin
- feat(sdk): timeLogger-startup add loadAppJs and appLoad
- feat(sdk): native-rpc-logger supprot event
- feat(cli): add support autocomplete feature for DeprecatedInput
- feat(sdk): support confirm event for web input
- feat(sdk,mp): mp,sdk plugin tab bar red dot
- feat(cli & bundler): provide source-map in prod mode
- feat: update blank-page demo with navigate to a new page
- feat: update blank page demo with input
- feat(runtime): on-off plugin
- feat(sdk): add system log label
- feat(sdk): plugins show-leaderboard, cloud-storage
- feat(mp): plugin background-fetch
- feat(runtime): save image to photos album plugin
- feat(bundler): extract base.bxml
- feat(sdk): plugin beforeAppClose api and demo
- feat: add blank-page demo
- feat(sdk): add direction RTL support for native components include native-input
- feat(runtime): clipboard plugin
- feat(sdk): optimize vconsole, lazy load, split log and system panel
- feat(sdk): report plugin
- feat(mp-runtime): add webview plugin
- feat: sync with mono 3.5.0
- feat:
  test([32d06ace](https://git.toolsfdg.net/fe/mini-program/commit/32d06aceb8d95036bc2f28bd72ea4f7347db3db2))
  by ka
- feat: test
- feat: trigger
- feat: failed trigger and do it one more time
- feat: test publish
- feat: modify release script
- feat(Slider): add mp-slider component
- feat: add fallback action handler
- feat: add bn.login
- feat(cli): archive bundle to zip file
- feat(cli): do bundle after taro build
- feat: add downloadFile and requestPayment
- feat: add base component Radio and RadioGroup & fix wrong onChange target id
- feat: add dist -d option
- feat: add bn apis
- feat(taro-plugin): 🎸 add bn typings for taro
- feat(build): add build command in @mp/cli
- feat: 🎸 add cli-init react template
- feat: implement WorkerService with iframe
- feat: add mp-checkbox & mp-checkbox-group
- feat: add action defintions
- feat: 🎸 add options to dev cli
- feat: 🎸 init @mp/cli
- feat: support api cors
- feat: expose rpcworker on dev
- feat: add toast action
- feat: 🎸 change page in app.json from object to array
- feat: enhance request taro
- feat: enhance request taro
- feat: enhance request taro
- feat: 🎸 add set method
- Feature/bundler
- feat(runtime-render): connect mp event to taro event
- feat: enhance request
- feat: add icon
- feat: add mp-text & fix input event
- feat: 🎸 add entry html and update taro plugin
- feat: 🎸 add **cid and **pageConfig to Page function
- feature/bundle
- feat: 🎸 remove isPage logic and add test cases
- feat: 🎸 defineApp and defineComponent
- feat: 🎸 _.config.json => _.json
- feat: 🎸 add \_\_cid to components
- feat: 🎸 add bundleAll method
- feat: 🎸 add merge-page-config-plugin
- feat: 🎸 return empty style and import pages
- feat: 🎸 add bundleApp function
- feat: export renderTaro
- feat: output sdk manifest
- feat: 🎸 add mp-tpl-loader and complete mp-bjs-loader
- feat: 🎸 use mp-bjs-loader
- feat: add mp-switch
- feat: add mp-textarea
- feat: add mp-label
- feat: runner-web-cli
- feat: add onTap
- feat: add mp-input
- feat: 🎸 add @babel/runtime
- feat: 🎸 support css module and scss
- feat: 🎸 clean memfs dir before run each test
- feat: 🎸 set config.optimization and add test cases
- feat: 🎸 extract css files
- feat: 🎸 add webpack-chain and support css files
- feat: 🎸 bundle single page
- feat: 🎸 invoke AppShow before first page loaded
- feat: 🎸 runner: support app-hide & app-show
- feat: 🎸 bn.api
- feat: 🎸 `runner` support navigate-pop and navigate-redirect
- feat: add navigator.redirect
- feat(public-api): init bn
- feat(rpc): add callback error
- feat: add app.js
- feat: 🎸 add multi pages and remove app-launch / page-load event
- feat: 🎸 add page2 and import worker.js on demand
- feat: 🎸 set navigation bar title
- feat: 🎸 add bn.request function
- feat: 🎸 mock native functions
- feat: navigator
- feat: add App and Page
- feat: navigator
- feat(runtime-render): add mp- prefix
- feat(runtime-render): add comments
- feat(runtime-render): update text
- feat(runtime-render): add tap event
- feat: add load and unload method
- feat: 🎸 support tsconfig.json in packages
- feat: 🎸 add @vue/compiler
- feat: multipage runner
- feat: 🎸 compiler init
- feat: add cmd typings
- feat: add runner-web
- feat: queue msg before ready
- feat(event): add event support
- feat: desctroy component when unmounted
- feat: add build watch option and add methods and computed function
- feat: 🎸 support methods and computed functionality
- feat(compiler): add base compile functions
- feat(project): add `dev:all` script
- feat(project): add `dev:all` script
- feat(project): specify format
- feat(project): update `dev:app` scripts
- feat(project): add owners
- feat: add dev script
- feat: use single rpc implementation
- feat: counter demo
- feat: first commit for runtime-\*
- feat: 🎸 add rollup to build runtime bundle
- feat: 🎸 minify code
- feat: 🎸 add rollup to build runtime bundle
- feat(rpc): add webwork rpc & native rpc
- feat(rpc): change names
- feat(rpc): add nativeBridge
- feat(rpc): add nativeBridge
- feat(rpc): fix issue
- feat(rpc): fix issue
- feat(rpc): add createRpcFromWorkerToView
- feat(rpc): add result
- feat(rpc): add createRpcFromViewToWorkder for dev
- feat: define rpc interface

### Refactor

- refactor(sdk): remove locationReadyManager
- refactor(sdk): delete gcanvas useless code
- refactor(demo): move component
- refactor: websocket hostplugin and text-line-height
- refactor: ide plugin login, location, download-package
- refactor: sensor plugin migration
- refactor: move plugins to runtime-plugins
- refactor(demo): mp-web
- refactor: ide plugin migration(error page, preview-image)
- refactor(sdk): optimize logger
- refactor: ide-host plugin migration
- refactor(runtime): redefine definePlugin to support service
- refactor(sdk): refactor plugins
- refactor: plugins migration
- refactor: clean dist of @mp/host
- refactor(runtime): re-export by host itself
- refactor(demo): component transform page
- refactor(sdk): fix plugin migration types errors
- refactor: new DSL demo page - tabbar
- refactor(demo): new component demo based on bxml
- refactor(sdk): migrate choose-image clipboard cloud-storage
- refactor(sdk): migrate plugin-canvas
- refactor(runtime): migrate plugins
- refactor(plugins): plugins -> runtime-plugins
- refactor(sdk): rename directories & fix watch mode
- refactor: remove @mp/runtime-host
- refactor(runtime): migrate plugins from to runtime-plugins
- refactor(sdk): plugins -> runtime-plugins
- refactor(runtime): code quality
- refactor(plugin): migrate internal-plugins
- refactor(runtime): add new desgin for plugin service
- refactor(sdk,runtime): extract internal plugins & fix types for mp-ide
- refactor(sdk,runtime): colocate host plugin & extract @mp/host-core
- refactor: restructure folders
- refactor: unit test of mp runtime
- refactor: rename deviceInfo to viewportInfo
- refactor(runtime): re-export @mp/plugins-mp
- refactor(sdk): add new runtime-core and move plugins to runtime-plugins
- refactor(runtime): rename runtime api
- refactor: runtime re-export
- refactor(runtime): add watch mode
- refactor(runtime): export resolvePublicAsset instead of dirs
- refactor(runtime): remove jump plugin effect
- refactor(runtime): jump plugin
- refactor(runtime): plugin performance-test and fix a bug cause by defaultTargetId is zero
- refactor(runtime): mp-runtime dev mode
- refactor(sdk,runtime): remove rollup warnings and prevent it
- refactor(sdk): use disableBuiltInPlugins options instead of setIsMG
- refactor(mp runtime): mp runtime api
- refactor(runtime): remove useless service
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(sdk): monitor-upload service and plugin
- refactor: update-manager
- refactor(sdk): performance plugin
- refactor: extract fs
- refactor(sdk): share-panel plugin for mp & mg
- refactor: navigation-bar plugin
- refactor: rollup build
- refactor: split action and event
- refactor: separate action and event
- refactor: events -> listeners
- refactor: use cache & proxy
- refactor: bind props with relation
- refactor: rename customevent -> events & emitEvents
- refactor: separate component props into normal props and custom events
- refactor: using async setup to init instance
- refactor: 💡 add webpack utils.ts
- refactor: use $emit event
- refactor: 💡 addStyleRule
- refactor: change action to string from object
- refactor: 💡 ViewManager.\_destroyView
- refactor: remove render.js suffix
- refactor: change page url
- refactor: 💡 change name
- refactor: pass rendererId by context
- refactor: change ready process
- refactor: change native bridge interface
- refactor: 💡 @compiler -> @mp/compiler
- refactor: use single bridge
- refactor: rpc init process
- refactor: update rpc message struct
- refactor: use two bridge to communicate
- refactor: change rpc interface
- refactor: change rpc interface

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)
- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action
- Revert "fix(sdk): update image component from img to div with background-image " (#309)
- Revert "feat(mp-runtime): add webview plugin"
- Revert "feat: 🎸 change page in app.json from object to array " (#119)
- Revert "feat(project): add `dev:all` script " (#21)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1
- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4
- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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
- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs
- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app
- chore(sdk): debug log
- chore(demo): bump qa demo version for radio-issue
- style(demo): add style of public
- docs(bundler): add how to use pkg-cli
- chore: webstudio release public-demo on prod
- build: sync webview demo
- build: sync-demos
- chore: build with bump version from hotfix or local
- chore: webstudio release public-demo on prod
- chore: webstudio release public demo to prod
- chore: rebuild webstudio public-demo
- chore: prepare demo app release
- chore: webstudio test disabledSubpackage
- chore: webstudio test subPackage
- chore: bump version
- docs: mp-host overview
- chore: bump version
- chore: webstudio
- chore: release component-demo
- chore(sdk): delete RendererReady
- Chore/webstudio
- chore: test-webstudio
- chore: add service.ts to files field
- chore(sdk): update local gen-sdk mainfest.json version
- chore: webstudio
- chore: hide migrated pages for testing purpose
- chore: webstudio config
- chore: webstudio config
- chore: webstudio config
- chore: bump version
- chore(sdk): cherrypick 3.10.1 to master
- chore(release): mp-sdk v3.10.0
- chore: bump versions
- chore: image url
- build: issue template
- chore: test webstudio auto submit
- chore: studio publish mp-sdk
- chore: test webstudio
- chore: webstudio demo
- chore: webstudio
- chore: add 1st version of issue templates
- chore(lib): bump versions cause by router query parameter feature
- docs: update documents about how to test plugin
- chore(sdk): cherry pick - delay 30s check app temporary
- chore(sdk): cherry pick 3.9.2 to master
- Merge branch 'master' into release/3.9
- docs: format readme
- chore(sdk): cherry pick 3.9.2 to master
- chore(sdk): cherry pick 3.9.2 to master
- chore: add concurrency script
- chore(release): mp-sdk v3.9.0
- chore: forgot to add .cjs suffix
- chore: fix yarn release script
- chore(demo): migrate component-demo to use cli 2.4.9
- chore: bump npm versions
- chore: add @tarojs/react to dependencies of babel-preset-bmp
- chore(cli): remove useless webpack alias
- docs(runtime): added migration plugin
- chore: bump version
- docs(demo): how to add new feature on new demo app
- chore: bump npm versions
- chore: bump npm versions
- chore: trigger packages republish
- chore(sdk): drop compatibility code isLegacyAppJsLoaded
- chore(doc): update mp-runtime doc troubleshooting
- chore: update automator README & puppeteer package
- docs(sdk): add special cases description
- docs(runtime): test host plugin
- Merge pull request #471 from finley-x/release/3.8
- Merge branch 'master' into release/3.8
- chore: bump npm versions
- chore(release): mp-sdk v3.8.0
- docs: plugin integrate with IDE & release
- chore: add wallet created action
- docs: how to development mp runtime
- docs: add plugin docs
- chore: set --unhandled-rejections=warn with jest to fix unit-test on node16
- chore: add @mp/mp-runtime-shared-plugins
- chore: bump versions
- chore: throw typescript check error
- chore: bump mp-runtime version
- chore: pre commit disallow empty files
- Merge pull request #423 from finley-x/release/3.7.4
- chore(cli): re-trigger bump CLI v2.3.3
- chore: organize mono workspaces
- chore(sdk): release/3.7.3 -> master
- chore(sdk): restore yml
- chore(sdk): restore yml
- test(sdk): logger test update
- chore(release): mp-sdk v3.7.2
- test(runtime): add inner audio unit tests
- chore(sdk): canvas plugins
- test(lib): improve logger unit tests
- ci: commitlint allow multiple scopes
- test(lib): add logger unit tests
- chore(sdk): fix fs plugin demos
- ci: fix commit-lint issue
- chore(sdk): demo for fs and orientation plugin
- chore: bump version to 1.1.0
- chore(sdk): fix Circular dependencies
- chore(cli): downgrade Taro to 3.2.13
- chore(bundler & sdk): move patches to root of workspace
- chore(bundler): add compiler-dom.d.ts
- chore(bundler): use tsc to build bundler
- build: fix cli build & render dev mode
- test: remove jest errors
- build(lib): update runtime-worker-common build script
- test(sdk): fix report test error
- test(sdk): fix report test error
- chore: use tsc to build cli
- chore: logger error caused by navigation-bar
- build: fix validate sdk output & add runtime-worker-common as deps of MP_ONLY
- chore: merge release/3.6
- chore: integrate v3.5.2
- Merge pull request #168 from kami-c/feature/test-ci-5
- Merge pull request #167 from
  fe/\_\_release-mp-sdk_prod_1.0.1_c7aa75d45e4516e684e941c544935c32a862b2ca_1646900584973
- release mp-sdk v1.0.1
- Merge pull request #154 from henry-w/mono-sdk-3.4.0
- moved from mono 3.4.0, add prowjob + config
- Merge pull request #152 from michael-xu/feature/mp-slider
- Merge pull request #151 from myron-li/dev
- Merge pull request #150 from myron-li/dev
- Merge pull request #148 from chengfan-lin/mp-cli-build-bundle-zip
- Merge pull request #149 from myron-li/dev
- Merge pull request #147 from myron-li/dev
- Merge pull request #146 from michael-xu/feature/radio
- update
- Merge pull request #145 from myron-li/refactor-build
- Merge pull request #144 from myron-li/fix-build
- Merge pull request #143 from james-l/feat/patches
- unit the style of module import
- use cross-spwan instead of child_process
- add livereload for dev server
- clean up package.json of cli
- added a link cmd to make it easy to install cli added cli related document
- Merge pull request #142 from michael-xu/fix/origin-bundler-with-path
- do patches before build
- Merge pull request #139 from myron-li/work
- chore: 🤖 update yarn.lock
- Merge pull request #136 from myron-li/html-worker-container
- Merge pull request #135 from luffy-wang/fix-for-debugger
- Merge pull request #131 from myron-li/add-actions
- Merge pull request #126 from myron-li/refactor-rpc
- Merge pull request #125 from myron-li/MYRON-1
- Merge pull request #124 from myron-li/dev
- Merge pull request #97 from michael-xu/feature/custom-event
- Merge pull request #120 from james-l/Feature/watch-mode-bundler
- added exception catching in bundle script of watch mode
- test: 💍 add cid equal test case
- complete w -> watch as watch mode argument
- chore: upgrade vue
- Merge pull request #121 from myron-li/toast
- added the bundler usage to README.md
- add watching mode for bundler
- Merge pull request #117 from myron-li/action
- Merge pull request #109 from luffy-wang/enhance-request
- chore: 🤖 update service assets
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #115 from chengfan-lin/api-taro
- Merge branch 'master' into feature/custom-event
- Merge pull request #114 from bowen-zhu/feature/bundler
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #113 from myron-li/MYRON-1
- chore: fix typo
- Merge pull request #111 from chengfan-lin/api-taro
- Merge pull request #112 from james-l/simplify-taro-plugin
- make bxss generate correct sourcemap when is in development
- simplify taro plugin and make it work as an npm package
- Merge pull request #108 from luffy-wang/add-icon
- Merge pull request #107 from james-l/fix/yarn-command-of-build-taro-plugin
- Merge pull request #106 from myron-li/batch-updated
- optimize: batch setData call
- Merge pull request #105 from michael-xu/feature/components
- Merge pull request #104 from myron-li/optimize
- chore: optimize build
- Merge pull request #103 from bowen-zhu/fix/bunlder
- Merge pull request #102 from james-l/fix/sourcemap-of-css
- dont let bxss generate sourcemap
- Merge pull request #101 from james-l/change-output-of-taro-plugin
- Merge branch 'master' into change-output-of-taro-plugin
- added components definitions of uikit requirements
- test: 💍 add test cases
- use tsc instead of rollup as the packer
- Merge pull request #95 from myron-li/refactor
- add sourcemap to bjs files
- use a modified app loader instead of origin one
- let page's code export via umd
- make output of the page scripts ends with .bjs
- Merge pull request #87 from bowen-zhu/feature/app-bundler
- chore: 🤖 remove bundled files
- chore: 🤖 add todos
- chore: 🤖 rename .tpl -> .bxml
- chore: 🤖 update package.json
- test: 💍 update test cases
- test: 💍 update test cases
- Merge pull request #90 from james-l/Feature/taro-integration
- add components
- Merge pull request #91 from myron-li/custom-event
- chore: custom component
- add code to support lifecycle callback of taro for Page object
- added REDME to taro plugin package
- add taro platform plugin into repository
- Merge pull request #89 from myron-li/bundle-demo
- chore: add example
- Merge pull request #88 from myron-li/rename
- chore: rename
- Merge pull request #84 from myron-li/taro
- chore: 🤖 build bundler by tsc
- Merge pull request #79 from michael-xu/feature/mp-components
- chore: 🤖 split bundler
- Merge pull request #77 from bowen-zhu/feature/bundler
- test: 💍 remove useless test fixtures
- test: 💍 add basic fixtures
- Merge pull request #78 from myron-li/runner
- chore: 🤖 remove unused example
- Merge pull request #74 from bowen-zhu/feature/loader
- test: 💍 add runInDom test function
- chore: 🤖 rename and remove useless code
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- chore: 🤖 setup bundler
- chore: 🤖 add compiler example
- merge upstream master
- chore: update example
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- add weather app demo
- Merge pull request #71 from myron-li/fix-page-hooks
- chore: 🤖 rename types
- Merge pull request #69 from bowen-zhu/feature/runner
- chore: 🤖 types
- chore: 🤖 navigate in worker
- chore: renemae variable
- chore: update example
- chore: rename variables
- Merge pull request #68 from myron-li/navigator-redirect
- Merge pull request #66 from bowen-zhu/fix/runner
- Merge pull request #65 from myron-li/page-url
- Merge pull request #64 from myron-li/app-js
- Merge pull request #60 from bowen-zhu/feature/runner-navigation
- chore: 🤖 remove redundant code
- chore: 🤖 rename function names
- chore: 🤖 add response interface
- chore: 🤖 update types and ui
- Merge pull request #63 from myron-li/integrate-app-and-page
- Merge pull request #57 from myron-li/navigator
- Merge pull request #54 from luffy-wang/add-app
- enhance
- create once only
- Merge pull request #52 from sora-liu/master
- typos
- add createApp and interfaces
- chore: rename pageid to rendererid
- chore: 🤖 update compiler fixture
- Merge pull request #51 from myron-li/init-process
- chore: 🤖 build prod version
- Merge pull request #48 from bowen-zhu/feature/compiler
- chore: 🤖 compiler dir structure
- Merge pull request #46 from myron-li/single-bridge
- Merge pull request #45 from myron-li/multi-page
- refacotr: change rpc message definition
- Merge pull request #44 from myron-li/test
- test: add component test
- Merge pull request #43 from myron-li/setup-test
- chore: setup jest
- Merge pull request #40 from myron-li/fix-compatibility
- Merge pull request #39 from myron-li/format
- Merge pull request #38 from myron-li/compiler-helper
- Merge pull request #37 from myron-li/worker-render-protocol
- Merge pull request #36 from myron-li/update-rpc
- change rpc
- Merge pull request #34 from myron-li/mock-service
- Merge pull request #32 from myron-li/bridge-ready
- Merge pull request #31 from myron-li/multi-bridge
- Merge pull request #30 from luffy-wang/change-rpc
- Merge pull request #27 from myron-li/build-sdk
- chore: add command to generate sdk
- Merge pull request #26 from myron-li/cleanup
- Merge pull request #25 from shenxiang-feng/master
- Merge pull request #23 from luffy-wang/add-compile-functions
- Merge pull request #19 from myron-li/patch
- chore: update readme
- chore: update readme
- Merge pull request #10 from myron-li/dev-script
- chore: 🤖 add todo
- chore: rename packages
- chore: 🤖 project setup
- chore: 🤖 add @types/node
- chore: 🤖 add eslint and prettier
- chore: 🤖 build ts files
- chore: 🤖 add lerna
- init
- wip
- init

## [3.14.5] 2022-11-10

**Download: [SDK-3.14.5](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.5.zip)**

### Bug Fixes

- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e
- fix(sdk): share-panel not working (#542)
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action
- fix(sdk): fix timeline order error
- fix(sdk): remove global wx, fix getOpenDataContext placeholder
- fix(sdk): timeline appJs error
- fix(sdk): timeline-update
- fix(cli): debugReact with react-reconciler not works
- fix(sdk): increase gas limit when estiamte gas failed
- fix(runtime): postMessage should wait for ready
- fix(cli): resolve taro presets from installation dir of bmp
- fix(cli): support node 15
- fix(sdk): can-i-use types & injectPrivateApi
- fix(rumtime): support tmp/store/usr http request
- fix(bundler): source-map OOM & repeated refresh in watch mode issues
- fix(sdk): fix onOffManager memory leak for task-style apis
- fix(demo): fix demo for fileSystemManager
- fix(runtime): add Math.ceil when populate gas
- fix(sdk): canvas plugin
- fix(bundler): adjust the order of loading script in page-frame
- fix(bundler): load base.bxml.js earlier than renderer-service.js
- fix(sdk): plugin write file
- fix(sdk): blank page when relaunch in old ios device
- fix(sdk): support cocos
- fix(sdk): app-rpc-logger judge from or to & delete extra log
- fix(sdk): monitor d change to dt & update RuntimeLogger monitor-upload
- fix(sdk): webview not working for the webview using node-bridge
- fix(bundler): load base.bxml.js in head element of page-frame
- fix(sdk): plugin-private-request command
- fix(sdk): add dataset to MPEventTarget
- fix(runtime): onNativeApiRequest able to listen all actions
- fix(sdk): radio and checkbox components
- fix(sdk): ios not support bigint 64
- fix(sdk): sentry + vconsole cause oom
- fix(sdk): fix Android need to tap input twice to focus
- fix(sdk): fix the issue that slider wrap with position: relative container
- fix(mp): fix request cookie setting
- fix(sdk): fix reportEvent with keyword to error
- fix(sdk): timeline startup del loadAppJs
- fix(sdk): DeprecatedInput auto-fill not emit input event
- fix(sdk): fix native input color with autoFocus props
- fix(runtime): storage plugin api not work
- fix(sdk): fix Image style width:100%
- fix(sdk): remove header filed with null value
- fix: add defer for webview context in the node-bridge demo
- fix: create a empty webview if src not provied
- fix(mp): fix tab bar css, red dot api error message
- fix(sdk): fix Image style being overridden and comments using English
- fix(sdk): image can not use width/height: auto with div-bgImg
- fix(sdk): onAppShow not working
- fix(sdk): remove the error of webivew-sdk Unknown Action $ready
- fix(sdk): update image component from img to div with background-image
- fix: framework-load-script has been registed
- fix(sdk): fix View component touchstart twice (#295)
- fix(lib,sdk): fix deprecated-input onInput not working
- fix(runtime): show & hide ToastContainer
- fix(sdk): plugin create native buffer
- fix(sdk): Image and IDECoverImage onload & onerror
- fix(sdk): timelogger error add time
- fix(sdk): debounce update state for native input
- fix(sdk): fix re-launch page not found issue
- fix(runtime): fix storage plugin
- fix(sdk): disable the JS timer for blank page detection
- fix(lib): make bundler generate component code that not override comp…
- fix(runtime): prevent app.js load twice
- fix(sdk): polyfill IntersectionObserver for iOS 12.1 (#237)
- fix: add commit hash to branch name
- Fix: release script
- fix: unexport subscribeLocationChange
- fix: sdk build
- fix the problem that bundler still work when in h5 mode
- fix some dependencies of project template
- fix: use path.resolve
- fix: make form component soft controlled & add missing component map
- fix: use -o
- fix the problem after last commit which make bundle script not work
- fix: normalize page url
- fix: 🐛 overwrite template files
- fix for debugger
- fix: 🐛 add http-proxy-middleware@0.19 in runtime-render
- Fix/fix the request with correct parameters and all other things for mvp2
- fix: send body only for post and put method
- fix: prevent user from scaling view
- fix: remove useless code
- fix(runtime-renderer): fix multiple event binding on same event
- fix: get props and data from parent & rename api
- fix: typo
- fix: use Object.assign
- fix: reduce payload size
- fix: Resolve events from attrs and separate two rpc events
- fix: use eventNames to tell the different if it is a event name or a normal props name
- fix: watch $props
- fix: rename
- fix: watch all props changed
- fix: remove bind props interface
- fix: remove useless code
- fix the problem invoked by packange name changed of taro plugin
- fix: prevent capture event trigger twice
- fix: 🐛 use e.currentTarget
- fix: 🐛 renderTaro and updateData
- fix: 🐛 renderTaro
- fix: keep compatible with taro
- fix: add tapCapture
- fix: add capture event
- fix: update props naming
- fix: remove console.log
- fix: Non-function value encountered for default slot. Prefer function slots for better
  performance.
- fix: remove console.log
- fix: types
- fix: update sdk
- fix: response.data typing
- fix: 🐛 enableCSSModule
- fix: call ready before navigation-push
- fix: typo
- fix: typo
- fix: typo
- fix: change data type
- fix: 🐛 back to list page
- fix: rpc
- fix(runner): rpc message format
- fix(runner): rpc message format
- fix: pass query to page.oLoad
- fix: fix ready and push action order
- fix: page component created twice
- fix: fix page hooks
- fix: 🐛 support page-hide and page-show
- fix: 🐛 not parse querystring when method is GET or HEAD
- fix: 🐛 createAndSavePage params
- fix: 🐛 init lifecycle and method
- fix: 🐛 only create page when \_\_pageConfig exist
- fix: 🐛 create page on worker runtime
- fix: build
- fix: disable webpack-dev-server host check
- fix: improve js compatibility
- fix: improve js compatibility
- fix: prefix component instance id with page id
- fix(rpc): change rpc interface
- fix: 🐛 add recordInstanceBoundEffect
- fix: 🐛 remove effect
- fix: 🐛 computed bind to ctx
- fix: change defualt build format to esm-bundler
- fix: change defualt build format to esm-bundler
- fix(project): fix default format
- fix(project): format package.json
- fix(project): rm .gitkeep & fix deps
- fix: typo
- fix: COMPONENT_TYPE_ID is undefined
- fix: 🐛 build script

### Features

- feat(sdk): add page-frame-resource points
- feat(sdk): shareAppMessage support fallback url
- feat(sdk): generate bytecode for worker-service
- feat(sdk): toDataURL and getuserprofile
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …
- feat(bundler & mpp-service): add bundler-cli & support output .pkg files
- feat(sdk): clear detection when hidden
- feat(demo): update runtime-web-host bundleAll params
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(sdk): framework-storage plugin
- feat(bundler,cli): update bundler log info
- feat(mpp-service): add package mpp-service to tools
- feat(sdk): hotfix-3.7.3-onerror-monitor-upload
- feat(sdk): try catch error in App lifecycle
- feat(sdk): add load pageJS info in timeline logger
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(bundler): move page logic to page.worker.js
- feat(sdk): add startAppLaunch handleAppLaunchCallback in runtimeloger
- feat(demo): preloadRule demo app
- feat(sdk,runtime): file system manger access api sdk,runtime,demo
- feat(cli): add button open-type getUserProfile & getEmailAddress
- feat(sdk): canIUse plugin
- feat(demo): handle error demo
- feat(runtime): remove native-ui
- feat(sdk): add Button open-type attribute getUserProfile
- feat(sdk): add Button open-type attribute openSetting
- feat(sdk): add wallet-connector plugin
- feat(lib): add binary-pkg to bundler
- feat(sdk): add API isLoggedIn & add custom plugin ensure-logged-in
- feat(demo): private-request demo
- feat(runtime): filesystem permission
- feat(sdk): plugin device-orientation-change
- feat: add disableBounces page to demo app
- feat(mp,sdk): file system plugins
- feat: private-request plugin
- feat(sdk): app-rpc logger add event
- feat(mp): buffer-url mp plugin
- feat(sdk): timeLogger-startup add loadAppJs and appLoad
- feat(sdk): native-rpc-logger supprot event
- feat(cli): add support autocomplete feature for DeprecatedInput
- feat(sdk): support confirm event for web input
- feat(sdk,mp): mp,sdk plugin tab bar red dot
- feat(cli & bundler): provide source-map in prod mode
- feat: update blank-page demo with navigate to a new page
- feat: update blank page demo with input
- feat(runtime): on-off plugin
- feat(sdk): add system log label
- feat(sdk): plugins show-leaderboard, cloud-storage
- feat(mp): plugin background-fetch
- feat(runtime): save image to photos album plugin
- feat(bundler): extract base.bxml
- feat(sdk): plugin beforeAppClose api and demo
- feat: add blank-page demo
- feat(sdk): add direction RTL support for native components include native-input
- feat(runtime): clipboard plugin
- feat(sdk): optimize vconsole, lazy load, split log and system panel
- feat(sdk): report plugin
- feat(mp-runtime): add webview plugin
- feat: sync with mono 3.5.0
- feat:
  test([32d06ace](https://git.toolsfdg.net/fe/mini-program/commit/32d06aceb8d95036bc2f28bd72ea4f7347db3db2))
  by ka
- feat: test
- feat: trigger
- feat: failed trigger and do it one more time
- feat: test publish
- feat: modify release script
- feat(Slider): add mp-slider component
- feat: add fallback action handler
- feat: add bn.login
- feat(cli): archive bundle to zip file
- feat(cli): do bundle after taro build
- feat: add downloadFile and requestPayment
- feat: add base component Radio and RadioGroup & fix wrong onChange target id
- feat: add dist -d option
- feat: add bn apis
- feat(taro-plugin): 🎸 add bn typings for taro
- feat(build): add build command in @mp/cli
- feat: 🎸 add cli-init react template
- feat: implement WorkerService with iframe
- feat: add mp-checkbox & mp-checkbox-group
- feat: add action defintions
- feat: 🎸 add options to dev cli
- feat: 🎸 init @mp/cli
- feat: support api cors
- feat: expose rpcworker on dev
- feat: add toast action
- feat: 🎸 change page in app.json from object to array
- feat: enhance request taro
- feat: enhance request taro
- feat: enhance request taro
- feat: 🎸 add set method
- Feature/bundler
- feat(runtime-render): connect mp event to taro event
- feat: enhance request
- feat: add icon
- feat: add mp-text & fix input event
- feat: 🎸 add entry html and update taro plugin
- feat: 🎸 add **cid and **pageConfig to Page function
- feature/bundle
- feat: 🎸 remove isPage logic and add test cases
- feat: 🎸 defineApp and defineComponent
- feat: 🎸 _.config.json => _.json
- feat: 🎸 add \_\_cid to components
- feat: 🎸 add bundleAll method
- feat: 🎸 add merge-page-config-plugin
- feat: 🎸 return empty style and import pages
- feat: 🎸 add bundleApp function
- feat: export renderTaro
- feat: output sdk manifest
- feat: 🎸 add mp-tpl-loader and complete mp-bjs-loader
- feat: 🎸 use mp-bjs-loader
- feat: add mp-switch
- feat: add mp-textarea
- feat: add mp-label
- feat: runner-web-cli
- feat: add onTap
- feat: add mp-input
- feat: 🎸 add @babel/runtime
- feat: 🎸 support css module and scss
- feat: 🎸 clean memfs dir before run each test
- feat: 🎸 set config.optimization and add test cases
- feat: 🎸 extract css files
- feat: 🎸 add webpack-chain and support css files
- feat: 🎸 bundle single page
- feat: 🎸 invoke AppShow before first page loaded
- feat: 🎸 runner: support app-hide & app-show
- feat: 🎸 bn.api
- feat: 🎸 `runner` support navigate-pop and navigate-redirect
- feat: add navigator.redirect
- feat(public-api): init bn
- feat(rpc): add callback error
- feat: add app.js
- feat: 🎸 add multi pages and remove app-launch / page-load event
- feat: 🎸 add page2 and import worker.js on demand
- feat: 🎸 set navigation bar title
- feat: 🎸 add bn.request function
- feat: 🎸 mock native functions
- feat: navigator
- feat: add App and Page
- feat: navigator
- feat(runtime-render): add mp- prefix
- feat(runtime-render): add comments
- feat(runtime-render): update text
- feat(runtime-render): add tap event
- feat: add load and unload method
- feat: 🎸 support tsconfig.json in packages
- feat: 🎸 add @vue/compiler
- feat: multipage runner
- feat: 🎸 compiler init
- feat: add cmd typings
- feat: add runner-web
- feat: queue msg before ready
- feat(event): add event support
- feat: desctroy component when unmounted
- feat: add build watch option and add methods and computed function
- feat: 🎸 support methods and computed functionality
- feat(compiler): add base compile functions
- feat(project): add `dev:all` script
- feat(project): add `dev:all` script
- feat(project): specify format
- feat(project): update `dev:app` scripts
- feat(project): add owners
- feat: add dev script
- feat: use single rpc implementation
- feat: counter demo
- feat: first commit for runtime-\*
- feat: 🎸 add rollup to build runtime bundle
- feat: 🎸 minify code
- feat: 🎸 add rollup to build runtime bundle
- feat(rpc): add webwork rpc & native rpc
- feat(rpc): change names
- feat(rpc): add nativeBridge
- feat(rpc): add nativeBridge
- feat(rpc): fix issue
- feat(rpc): fix issue
- feat(rpc): add createRpcFromWorkerToView
- feat(rpc): add result
- feat(rpc): add createRpcFromViewToWorkder for dev
- feat: define rpc interface

### Refactor

- refactor(sdk): remove locationReadyManager
- refactor(sdk): delete gcanvas useless code
- refactor(demo): move component
- refactor: websocket hostplugin and text-line-height
- refactor: ide plugin login, location, download-package
- refactor: sensor plugin migration
- refactor: move plugins to runtime-plugins
- refactor(demo): mp-web
- refactor: ide plugin migration(error page, preview-image)
- refactor(sdk): optimize logger
- refactor: ide-host plugin migration
- refactor(runtime): redefine definePlugin to support service
- refactor(sdk): refactor plugins
- refactor: plugins migration
- refactor: clean dist of @mp/host
- refactor(runtime): re-export by host itself
- refactor(demo): component transform page
- refactor(sdk): fix plugin migration types errors
- refactor: new DSL demo page - tabbar
- refactor(demo): new component demo based on bxml
- refactor(sdk): migrate choose-image clipboard cloud-storage
- refactor(sdk): migrate plugin-canvas
- refactor(runtime): migrate plugins
- refactor(plugins): plugins -> runtime-plugins
- refactor(sdk): rename directories & fix watch mode
- refactor: remove @mp/runtime-host
- refactor(runtime): migrate plugins from to runtime-plugins
- refactor(sdk): plugins -> runtime-plugins
- refactor(runtime): code quality
- refactor(plugin): migrate internal-plugins
- refactor(runtime): add new desgin for plugin service
- refactor(sdk,runtime): extract internal plugins & fix types for mp-ide
- refactor(sdk,runtime): colocate host plugin & extract @mp/host-core
- refactor: restructure folders
- refactor: unit test of mp runtime
- refactor: rename deviceInfo to viewportInfo
- refactor(runtime): re-export @mp/plugins-mp
- refactor(sdk): add new runtime-core and move plugins to runtime-plugins
- refactor(runtime): rename runtime api
- refactor: runtime re-export
- refactor(runtime): add watch mode
- refactor(runtime): export resolvePublicAsset instead of dirs
- refactor(runtime): remove jump plugin effect
- refactor(runtime): jump plugin
- refactor(runtime): plugin performance-test and fix a bug cause by defaultTargetId is zero
- refactor(runtime): mp-runtime dev mode
- refactor(sdk,runtime): remove rollup warnings and prevent it
- refactor(sdk): use disableBuiltInPlugins options instead of setIsMG
- refactor(mp runtime): mp runtime api
- refactor(runtime): remove useless service
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(sdk): monitor-upload service and plugin
- refactor: update-manager
- refactor(sdk): performance plugin
- refactor: extract fs
- refactor(sdk): share-panel plugin for mp & mg
- refactor: navigation-bar plugin
- refactor: rollup build
- refactor: split action and event
- refactor: separate action and event
- refactor: events -> listeners
- refactor: use cache & proxy
- refactor: bind props with relation
- refactor: rename customevent -> events & emitEvents
- refactor: separate component props into normal props and custom events
- refactor: using async setup to init instance
- refactor: 💡 add webpack utils.ts
- refactor: use $emit event
- refactor: 💡 addStyleRule
- refactor: change action to string from object
- refactor: 💡 ViewManager.\_destroyView
- refactor: remove render.js suffix
- refactor: change page url
- refactor: 💡 change name
- refactor: pass rendererId by context
- refactor: change ready process
- refactor: change native bridge interface
- refactor: 💡 @compiler -> @mp/compiler
- refactor: use single bridge
- refactor: rpc init process
- refactor: update rpc message struct
- refactor: use two bridge to communicate
- refactor: change rpc interface
- refactor: change rpc interface

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action
- Revert "fix(sdk): update image component from img to div with background-image " (#309)
- Revert "feat(mp-runtime): add webview plugin"
- Revert "feat: 🎸 change page in app.json from object to array " (#119)
- Revert "feat(project): add `dev:all` script " (#21)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4
- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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
- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs
- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app
- chore(sdk): debug log
- chore(demo): bump qa demo version for radio-issue
- style(demo): add style of public
- docs(bundler): add how to use pkg-cli
- chore: webstudio release public-demo on prod
- build: sync webview demo
- build: sync-demos
- chore: build with bump version from hotfix or local
- chore: webstudio release public-demo on prod
- chore: webstudio release public demo to prod
- chore: rebuild webstudio public-demo
- chore: prepare demo app release
- chore: webstudio test disabledSubpackage
- chore: webstudio test subPackage
- chore: bump version
- docs: mp-host overview
- chore: bump version
- chore: webstudio
- chore: release component-demo
- chore(sdk): delete RendererReady
- Chore/webstudio
- chore: test-webstudio
- chore: add service.ts to files field
- chore(sdk): update local gen-sdk mainfest.json version
- chore: webstudio
- chore: hide migrated pages for testing purpose
- chore: webstudio config
- chore: webstudio config
- chore: webstudio config
- chore: bump version
- chore(sdk): cherrypick 3.10.1 to master
- chore(release): mp-sdk v3.10.0
- chore: bump versions
- chore: image url
- build: issue template
- chore: test webstudio auto submit
- chore: studio publish mp-sdk
- chore: test webstudio
- chore: webstudio demo
- chore: webstudio
- chore: add 1st version of issue templates
- chore(lib): bump versions cause by router query parameter feature
- docs: update documents about how to test plugin
- chore(sdk): cherry pick - delay 30s check app temporary
- chore(sdk): cherry pick 3.9.2 to master
- Merge branch 'master' into release/3.9
- docs: format readme
- chore(sdk): cherry pick 3.9.2 to master
- chore(sdk): cherry pick 3.9.2 to master
- chore: add concurrency script
- chore(release): mp-sdk v3.9.0
- chore: forgot to add .cjs suffix
- chore: fix yarn release script
- chore(demo): migrate component-demo to use cli 2.4.9
- chore: bump npm versions
- chore: add @tarojs/react to dependencies of babel-preset-bmp
- chore(cli): remove useless webpack alias
- docs(runtime): added migration plugin
- chore: bump version
- docs(demo): how to add new feature on new demo app
- chore: bump npm versions
- chore: bump npm versions
- chore: trigger packages republish
- chore(sdk): drop compatibility code isLegacyAppJsLoaded
- chore(doc): update mp-runtime doc troubleshooting
- chore: update automator README & puppeteer package
- docs(sdk): add special cases description
- docs(runtime): test host plugin
- Merge pull request #471 from finley-x/release/3.8
- Merge branch 'master' into release/3.8
- chore: bump npm versions
- chore(release): mp-sdk v3.8.0
- docs: plugin integrate with IDE & release
- chore: add wallet created action
- docs: how to development mp runtime
- docs: add plugin docs
- chore: set --unhandled-rejections=warn with jest to fix unit-test on node16
- chore: add @mp/mp-runtime-shared-plugins
- chore: bump versions
- chore: throw typescript check error
- chore: bump mp-runtime version
- chore: pre commit disallow empty files
- Merge pull request #423 from finley-x/release/3.7.4
- chore(cli): re-trigger bump CLI v2.3.3
- chore: organize mono workspaces
- chore(sdk): release/3.7.3 -> master
- chore(sdk): restore yml
- chore(sdk): restore yml
- test(sdk): logger test update
- chore(release): mp-sdk v3.7.2
- test(runtime): add inner audio unit tests
- chore(sdk): canvas plugins
- test(lib): improve logger unit tests
- ci: commitlint allow multiple scopes
- test(lib): add logger unit tests
- chore(sdk): fix fs plugin demos
- ci: fix commit-lint issue
- chore(sdk): demo for fs and orientation plugin
- chore: bump version to 1.1.0
- chore(sdk): fix Circular dependencies
- chore(cli): downgrade Taro to 3.2.13
- chore(bundler & sdk): move patches to root of workspace
- chore(bundler): add compiler-dom.d.ts
- chore(bundler): use tsc to build bundler
- build: fix cli build & render dev mode
- test: remove jest errors
- build(lib): update runtime-worker-common build script
- test(sdk): fix report test error
- test(sdk): fix report test error
- chore: use tsc to build cli
- chore: logger error caused by navigation-bar
- build: fix validate sdk output & add runtime-worker-common as deps of MP_ONLY
- chore: merge release/3.6
- chore: integrate v3.5.2
- Merge pull request #168 from kami-c/feature/test-ci-5
- Merge pull request #167 from
  fe/\_\_release-mp-sdk_prod_1.0.1_c7aa75d45e4516e684e941c544935c32a862b2ca_1646900584973
- release mp-sdk v1.0.1
- Merge pull request #154 from henry-w/mono-sdk-3.4.0
- moved from mono 3.4.0, add prowjob + config
- Merge pull request #152 from michael-xu/feature/mp-slider
- Merge pull request #151 from myron-li/dev
- Merge pull request #150 from myron-li/dev
- Merge pull request #148 from chengfan-lin/mp-cli-build-bundle-zip
- Merge pull request #149 from myron-li/dev
- Merge pull request #147 from myron-li/dev
- Merge pull request #146 from michael-xu/feature/radio
- update
- Merge pull request #145 from myron-li/refactor-build
- Merge pull request #144 from myron-li/fix-build
- Merge pull request #143 from james-l/feat/patches
- unit the style of module import
- use cross-spwan instead of child_process
- add livereload for dev server
- clean up package.json of cli
- added a link cmd to make it easy to install cli added cli related document
- Merge pull request #142 from michael-xu/fix/origin-bundler-with-path
- do patches before build
- Merge pull request #139 from myron-li/work
- chore: 🤖 update yarn.lock
- Merge pull request #136 from myron-li/html-worker-container
- Merge pull request #135 from luffy-wang/fix-for-debugger
- Merge pull request #131 from myron-li/add-actions
- Merge pull request #126 from myron-li/refactor-rpc
- Merge pull request #125 from myron-li/MYRON-1
- Merge pull request #124 from myron-li/dev
- Merge pull request #97 from michael-xu/feature/custom-event
- Merge pull request #120 from james-l/Feature/watch-mode-bundler
- added exception catching in bundle script of watch mode
- test: 💍 add cid equal test case
- complete w -> watch as watch mode argument
- chore: upgrade vue
- Merge pull request #121 from myron-li/toast
- added the bundler usage to README.md
- add watching mode for bundler
- Merge pull request #117 from myron-li/action
- Merge pull request #109 from luffy-wang/enhance-request
- chore: 🤖 update service assets
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #115 from chengfan-lin/api-taro
- Merge branch 'master' into feature/custom-event
- Merge pull request #114 from bowen-zhu/feature/bundler
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #113 from myron-li/MYRON-1
- chore: fix typo
- Merge pull request #111 from chengfan-lin/api-taro
- Merge pull request #112 from james-l/simplify-taro-plugin
- make bxss generate correct sourcemap when is in development
- simplify taro plugin and make it work as an npm package
- Merge pull request #108 from luffy-wang/add-icon
- Merge pull request #107 from james-l/fix/yarn-command-of-build-taro-plugin
- Merge pull request #106 from myron-li/batch-updated
- optimize: batch setData call
- Merge pull request #105 from michael-xu/feature/components
- Merge pull request #104 from myron-li/optimize
- chore: optimize build
- Merge pull request #103 from bowen-zhu/fix/bunlder
- Merge pull request #102 from james-l/fix/sourcemap-of-css
- dont let bxss generate sourcemap
- Merge pull request #101 from james-l/change-output-of-taro-plugin
- Merge branch 'master' into change-output-of-taro-plugin
- added components definitions of uikit requirements
- test: 💍 add test cases
- use tsc instead of rollup as the packer
- Merge pull request #95 from myron-li/refactor
- add sourcemap to bjs files
- use a modified app loader instead of origin one
- let page's code export via umd
- make output of the page scripts ends with .bjs
- Merge pull request #87 from bowen-zhu/feature/app-bundler
- chore: 🤖 remove bundled files
- chore: 🤖 add todos
- chore: 🤖 rename .tpl -> .bxml
- chore: 🤖 update package.json
- test: 💍 update test cases
- test: 💍 update test cases
- Merge pull request #90 from james-l/Feature/taro-integration
- add components
- Merge pull request #91 from myron-li/custom-event
- chore: custom component
- add code to support lifecycle callback of taro for Page object
- added REDME to taro plugin package
- add taro platform plugin into repository
- Merge pull request #89 from myron-li/bundle-demo
- chore: add example
- Merge pull request #88 from myron-li/rename
- chore: rename
- Merge pull request #84 from myron-li/taro
- chore: 🤖 build bundler by tsc
- Merge pull request #79 from michael-xu/feature/mp-components
- chore: 🤖 split bundler
- Merge pull request #77 from bowen-zhu/feature/bundler
- test: 💍 remove useless test fixtures
- test: 💍 add basic fixtures
- Merge pull request #78 from myron-li/runner
- chore: 🤖 remove unused example
- Merge pull request #74 from bowen-zhu/feature/loader
- test: 💍 add runInDom test function
- chore: 🤖 rename and remove useless code
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- chore: 🤖 setup bundler
- chore: 🤖 add compiler example
- merge upstream master
- chore: update example
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- add weather app demo
- Merge pull request #71 from myron-li/fix-page-hooks
- chore: 🤖 rename types
- Merge pull request #69 from bowen-zhu/feature/runner
- chore: 🤖 types
- chore: 🤖 navigate in worker
- chore: renemae variable
- chore: update example
- chore: rename variables
- Merge pull request #68 from myron-li/navigator-redirect
- Merge pull request #66 from bowen-zhu/fix/runner
- Merge pull request #65 from myron-li/page-url
- Merge pull request #64 from myron-li/app-js
- Merge pull request #60 from bowen-zhu/feature/runner-navigation
- chore: 🤖 remove redundant code
- chore: 🤖 rename function names
- chore: 🤖 add response interface
- chore: 🤖 update types and ui
- Merge pull request #63 from myron-li/integrate-app-and-page
- Merge pull request #57 from myron-li/navigator
- Merge pull request #54 from luffy-wang/add-app
- enhance
- create once only
- Merge pull request #52 from sora-liu/master
- typos
- add createApp and interfaces
- chore: rename pageid to rendererid
- chore: 🤖 update compiler fixture
- Merge pull request #51 from myron-li/init-process
- chore: 🤖 build prod version
- Merge pull request #48 from bowen-zhu/feature/compiler
- chore: 🤖 compiler dir structure
- Merge pull request #46 from myron-li/single-bridge
- Merge pull request #45 from myron-li/multi-page
- refacotr: change rpc message definition
- Merge pull request #44 from myron-li/test
- test: add component test
- Merge pull request #43 from myron-li/setup-test
- chore: setup jest
- Merge pull request #40 from myron-li/fix-compatibility
- Merge pull request #39 from myron-li/format
- Merge pull request #38 from myron-li/compiler-helper
- Merge pull request #37 from myron-li/worker-render-protocol
- Merge pull request #36 from myron-li/update-rpc
- change rpc
- Merge pull request #34 from myron-li/mock-service
- Merge pull request #32 from myron-li/bridge-ready
- Merge pull request #31 from myron-li/multi-bridge
- Merge pull request #30 from luffy-wang/change-rpc
- Merge pull request #27 from myron-li/build-sdk
- chore: add command to generate sdk
- Merge pull request #26 from myron-li/cleanup
- Merge pull request #25 from shenxiang-feng/master
- Merge pull request #23 from luffy-wang/add-compile-functions
- Merge pull request #19 from myron-li/patch
- chore: update readme
- chore: update readme
- Merge pull request #10 from myron-li/dev-script
- chore: 🤖 add todo
- chore: rename packages
- chore: 🤖 project setup
- chore: 🤖 add @types/node
- chore: 🤖 add eslint and prettier
- chore: 🤖 build ts files
- chore: 🤖 add lerna
- init
- wip
- init

## [3.14.5] 2022-11-09

**Download: [SDK-3.14.5](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.5.zip)**

### Features

- feat(sdk): add page-frame-resource points

## [4.0.1] 2022-11-04

**Download: [SDK-4.0.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.1.zip)**

### Bug Fixes

- fix(sdk): env undefined

### Internal

- chore(cicd): yaml files

## [3.14.4] 2022-11-03

**Download: [SDK-3.14.4](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.4.zip)**

### Features

- feat(sdk): shareAppMessage support fallback url

### Internal

- chore(cicd): yaml files

## [4.0.0] 2022-10-25

**Download: [SDK-4.0.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.0.zip)**

### Bug Fixes

- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1

## [3.14.3] 2022-10-24

**Download: [SDK-3.14.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.3.zip)**

### Features

- feat(sdk): generate bytecode for worker-service

## [3.14.2] 2022-10-17

**Download: [SDK-3.14.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.2.zip)**

### Features

- feat(sdk): toDataURL and getuserprofile

## [3.14.1] 2022-10-05

**Download: [SDK-3.14.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.1.zip)**

### Bug Fixes

- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works

### Features

- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class

### Internal

- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4

## [3.14.0] 2022-09-29

**Download: [SDK-3.14.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.0.zip)**

### Bug Fixes

- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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

- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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

### Refactor

- refactor(sdk): remove locationReadyManager

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)

### Internal

- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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

## [3.13.3] 2022-09-26

**Download: [SDK-3.13.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.3.zip)**

### Features

- feat(sdk): android cache promise

## [3.13.2] 2022-09-20

**Download: [SDK-3.13.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.2.zip)**

### Misc

- Revert "fix(sdk): cache promise for getSystemInfo " (#866)

## [3.13.1] 2022-09-16

**Download: [SDK-3.13.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.1.zip)**

### Bug Fixes

- fix(sdk): cache promise for getSystemInfo
- fix(sdk): requestAnimationFrame NaN

## [3.13.0] 2022-09-02

**Download: [SDK-3.13.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.0.zip)**

### Bug Fixes

- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register

### Features

- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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

- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs

## [3.12.3] 2022-09-01

**Download: [SDK-3.12.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.3.zip)**

### Bug Fixes

- fix(sdk): iOS 13.8 promise eventloop issue

### Internal

- chore: changelog automation (#808)

## [3.12.2] 2022-08-31

**Download: [SDK-3.12.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.2.zip)**

### Bug Fixes

- fix(sdk): fix taskify cache fail

## [3.12.1] 2022-08-12

**Download: [SDK-3.12.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.1.zip)**

### Bug Fixes

- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type

### Features

- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins

### Internal

- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app

---

# Download Stable Version

## [5.11.0] 2026-04-02

**Download: [5.11.0(2.76 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.11.0.zip)**

### Bug Fixes

- Fix/mp renderjs missing
- fix(sdk): add backward compatibility for ViewPager2 in SwiperView
- Fix/native cli preview UI layout
- Fix/type 0331
- fix(cli): bundle native-cli resources and resolve adb
- fix: showErrorPage for 600402 page_not_found error
- fix(sdk): mcp bin
- fix(lib): fix ide cli toolbar sync api
- fix(cli): ide cli node version match

### Features

- feat(sdk): add QJS bytecode compilation for renderer-service-hummer
- feat(sdk): support virtual appid for widget
- feat(sdk): add useNewWindow parameter to previewImage API
- feat(cli): native-cli & ide-cli-mcp-server recover capabilities improve
- Feat/ios orba
- feat(cli): mcp tool stability improve
- feat(sdk): screen cast
- feat(cli): ide cli mcp server sync
- feat(cli): add mobile screen viewer and simulator host capture

## [5.10.0] 2026-03-12

**Download: [5.10.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.10.0.zip)**

### Bug Fixes

- fix(sdk): fix video props type
- fix(native-cli): prevent host hang on Ctrl+C

### Features

- feat(cli): native cli mcp adjust
- feat(native-cli): add sync mp status mcp tool
- feat(sdk): support root portal to specific element
- Feat/hummer lcp
- feat(cli): sub mode default render path
- feat(cli): native cli UI bridge
- feat(cli): orba desktop mp side work
- feat(cli): make get_log_files as example
- feat(cli): native cli UI dev env
- feat(cli): init native-cli project

## [5.9.1] 2026-02-27

**Download: [5.9.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.9.1.zip)**

### Bug Fixes

- fix(sdk): renderer may never ready when route quickly

## [5.9.0] 2026-02-19

**Download: [5.9.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.9.0.zip)**

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

## [5.8.5] 2026-02-09

**Download: [5.8.5(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.5.zip)**

### Bug Fixes

- fix(sdk): <FlutterCustomNativeComponent/> dom update lead layout size abnormal

## [5.8.4] 2026-02-09

**Download: [5.8.4(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.4.zip)**

### Bug Fixes

- fix(sdk): routeChange type=switchTab and page isTabbarPage stack always be the rootTab

## [5.8.3] 2026-02-04

**Download: [5.8.3(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.3.zip)**

## [5.8.2] 2026-02-04

**Download: [5.8.2(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.2.zip)**

### Misc

- Revert " fix(sdk): sortable items when height changes " (#2522)

## [5.8.1] 2026-01-30

**Download: [5.8.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.1.zip)**

### Bug Fixes

- fix(sdk): navigate routeChanging defer ref issues

## [3.8.1] 2026-01-30

**Download: [3.8.1(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.8.1.zip)**

### Bug Fixes

- fix(sdk): navigate routeChanging defer ref issues
- fix(sdk): cherry pick 5.7.1
- fix(sdk): sortable items when height changes
- fix(sdkl): wallet prerender failed
- fix(sdk): rm geature event listener binding
- fix(sdk): fix prerender inject data path
- fix(sdk,bundler): init nativeScrollNegotiation/enableBackToTop config
- fix(sdk): reuse page issue on ios platform
- fix(sdk): text dont filter nest components
- fix(sdk): chain routechange handler when receviced multiple routechange
- fix(lib): add missing code back to protect web import
- fix(sdk): add ut
- fix(lib): add comma to avoid MFA build error
- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android
- fix(cli): version sort
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
- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work
- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y
- fix(sdk): expose the error before app init
- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep
- fix(sdk): set scroll top not work / request support enableCache
- fix(sdk): `show-scrollbar` doesn't work
- fix(sdk): flutter getAttribute polyfill
- fix(sdk): fix input textarea type adjustPosition
- fix(cli): missing build start callback in bundleWatch
- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`
- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…
- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices
- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2
- fix(bmp): remove requestFullscreen param
- fix(sdk): flutter-video context issue
- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed
- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`
- fix(sdk): change handlePaste defaultValue
- fix(sdk): remove native component background color
- fix(sdk): flutter-image remove eventListener
- fix(sdk): support inlineLayout for skyline
- fix(sdk): flutter scroll refresher background color
- fix(sdk): android quickjs unsupport Unicode Property Escapes
- fix(sdk): cherry pick webview message issue
- fix(sdk): re-publish @mp/runtime-plugin-enable-sheet-gesture
- fix(sdk): fix cursor issue
- fix(runtime): premature return issue in ide enviroment's show-modal api
- fix(sdk): editor pos nodeBefore return real textContent if node is nonTextNode
- fix(sdk): `deprecated-textarea` support force update
- fix(sdk): deprecated input does not update when is composing
- fix(sdk): jarvis input does not update correctly
- fix(sdk): fix webview message action not work
- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator
- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop
- fix(sdk): fix component patch error messsage
- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type
- fix(sdk): vnode patch issues
- fix(sdk): navigate to type
- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory
- fix: add worker plugin
- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler
- fix(sdk): native component webview message
- fix(sdk): native event in worker
- fix(sdk): fix webview component
- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error
- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure
- fix(sdk): cursor is wired when editor tap keyboard enter
- fix: update render cache doc id
- fix(extended-lib): resolve path not a module
- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload
- fix(extended-lib): postpublish script throw error
- fix(host): support webassembly on host
- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions
- fix(extended-lib): add missing deps
- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type
- fix(sdk): revert readfile issue on ios
- fix(sdk): hotfix ios doesn't use native fs
- fix(sdk): when user delete all content web input may act unexpected
- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE
- fix(demo): icon size demo
- fix(sdk): label trigger itemClick event for radio and checkbox
- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter
- fix(bundler): fix IDE can not reload
- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value
- fix(sdk): support input focus and blur action by developers
- fix(sdk): END_FIRSTPAGE_APPLAUNCH send pid
- fix(sdk): clone data avoid reuse data object when reopen page
- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger
- fix(sdk): revert swiper located to wrong child when children updated
- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper
- fix(bundler): bundler watch has 60s cache
- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots
- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci
- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount
- fix(sdk): create webview api in mp cannot message
- fix(sdk): customize component data not update when return a data getter
- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop
- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer
- fix(demo): editor toolbar bottom 0 when platform is not iOS
- fix(sdk): iOS native component created failed when container is not visible
- fix: cherry-pick from 4.12.1
- fix(sdk): cancel load-script when redirect
- fix(lib): add type of removeSkeleton
- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs
- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo
- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images
- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work
- fix(mpp-service): set maxBodyLength & maxContentLength as Infinity wh…
- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend
- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack
- fix(sdk): load page frame after load base.bxml success
- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found
- fix(sdk): figure scrollIntoView should focus on the figure caption
- fix(demo): production convertToMPUrl usage
- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise
- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs
- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version
- fix(demo): bug in navigation demo
- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue
- fix(sdk): add native-send-appLuanch timer
- fix(bundler): css variables rpx to rem align with wechat
- fix(sdk): mini game view port size
- fix(sdk): getChildrenNode util function
- fix(sdk): rendererId zero issue in native ui
- fix(bundler): catchmove value should be an exp
- fix(sdk): swiper Item blank
- fix(demo): fix custom demo textarea maxlength
- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component
- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes
- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css
- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js
- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e(#NEZ-5634)
- fix(sdk): share-panel not working (#542)
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action

### Features

- feat(sdk): hummer gcanvas
- feat(sdk): load appjs when reload worker
- feat(sdk): enhance native event channel for CustomNativeComponent
- feat(cli): miniprogram mcp server
- feat(cli): more function in devtool
- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId
- feat(sdk): add internal doc site
- feat(cli): auto perf
- feat(sdk): add extra type
- feat(sdk): support debug prefetch configuration
- feat(sdk): lottie comp support animationData props
- feat(bundler): update terser avoid bugs of old ver
- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve
- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum
- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev
- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion
- feat(bundler): support bundler version
- feat(sdk): support share v2 api
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(cli): support home page widget preview
- feat(mpp-service): update ai router payload
- feat(mpp-service): ai router solution
- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message
- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo
- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib
- feat(sdk): suspend & resume lifecycle
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
- feat(cli): rebundle while refresh
- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo
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
- feat(sdk): add disable-ios-embed props for ios native input
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
- feat(sdk): add showDiagnosticPage API
- feat(sdk): native-input cursor issue
- feat(sdk): add flutter-chart component
- feat(sdk): catch setTimeout callback error & Handle redundant `Uncaught` errors
- feat(cli): support debug mode flag
- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error
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
- feat(sdk): sortable support dark mode
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate
- feat(sdk): add switch tab options in api
- feat(sdk): add timeformat api
- feat(sdk): add showBackButton api
- feat(sdk): `native-textarea` add onPaste
- feat(sdk): `native-textarea` add `alwaysEmbed`
- feat(sdk): add the value of input type `decimals`
- feat(sdk): flutter-deprecated-textarea add `autoFocus`
- feat(sdk): new api page.updateRouteOptions
- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo
- feat(sdk): use tap for skyline
- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle
- feat(host): align response with native
- feat(sdk): flutter text component
- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18
- feat(demo): error handler demo
- feat(sdk): add deeplink target type
- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs
- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`
- feat(sdk): drawer component
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
- feat(sdk): choose image support compression threshold
- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode
- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components
- feat(sdk): webview component event api in queryselector
- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js
- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton
- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%
- feat(demo): add log for skyline debug & extended-lib should keep the built-in libs for cicd & ide
- feat(extended-lib): remove built-in upload and fix getUrl data not send
- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line
- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app
- feat(sdk): api hide back button
- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int
- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document
- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded
- feat(extended-lib): release to prod
- feat(sdk): custom native component
- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration
- feat(sdk): flutter can report lcp
- feat(host): support widget api
- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define
- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable
- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content
- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB
- feat(sdk): cherry-pick: add preloadflutterwebview api
- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event
- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor
- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection
- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list
- feat(sdk): editor support mention and hardBreak
- feat(bundler): use js-beautify replace prettier as formater of qjs
- feat(bundler): qjs compared from a formatted js code
- feat(lib): bmp-api openWidget add support for convention path
- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget
- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles
- feat(sdk): editor internal plugin link support
- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers
- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter
- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs
- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata
- feat(sdk): editor paste event props
- feat(sdk): echart component
- feat(sdk): editor selectImage api
- feat(mpp-service) add released pr
- feat(sdk): support walletkit and init func
- feat(demo): add manual to web input public demo
- feat(lib): add API removeSkeleton to bmp-react
- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image
- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider
- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API
- feat(demo): add prefetchRules
- feat(sdk): getUserOpenId return token
- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs
- feat(host): set custom http headers for fetch requests
- feat(sdk): ut from plugin-location to plugin-request-subscribe-message
- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo
- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher
- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API
- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly
- feat(demo): control picker view demo
- feat(sdk): detect page timeline
- feat(host): support pageReadyCallback
- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react
- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal
- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo
- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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
- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc
- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(cli): quick publish for dev & qa [NEZ-7388]
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target
- perf: add filesystem cache
- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "fix(sdk): export bmp component utils"
- Revert "chore: @mp/bundler dev"
- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)
- Revert "fix(sdk): iOS native component created failed when container is not visible "
- Revert "fix(sdk): env undefined"
- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)
- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action

## [5.8.0] 2026-01-30

**Download: [5.8.0(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.8.0.zip)**

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

## [5.7.4] 2026-01-26

**Download: [5.7.4(2.21 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.4.zip)**

### Misc

- revert: revert v5.7.2 and v5.7.3 which fix by native

## [5.7.3] 2026-01-16

**Download: [5.7.3(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.3.zip)**

### Bug Fixes

- fix(sdk): showErrorPage when setData unordered

## [5.7.2] 2026-01-15

**Download: [5.7.2(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.2.zip)**

### Features

- feat(sdk): showError page when node tree not matched

## [5.7.1] 2026-01-14

**Download: [5.7.1(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.1.zip)**

### Bug Fixes

- fix(sdk): fix route pending when page.js fails

## [5.6.1] 2026-01-14

**Download: [5.6.1(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.6.1.zip)**

### Bug Fixes

- fix(sdk): fix route pending when page.js fails

## [5.7.0] 2026-01-08

**Download: [5.7.0(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.7.0.zip)**

### Bug Fixes

- fix(sdk): rm geature event listener binding

### Features

- feat(sdk): hummer button functions
- feat(sdk): support createContext with customNativeComponent widget rendererId
- feat(sdk): add internal doc site
- feat(cli): auto perf

## [5.5.3] 2025-12-29

**Download: [5.5.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.3.zip)**

## [5.4.2] 2025-12-29

**Download: [5.4.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.2.zip)**

## [5.2.10] 2025-12-29

**Download: [5.2.10(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.10.zip)**

## [5.6.0] 2025-12-19

**Download: [5.6.0(1.87 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.6.0.zip)**

### Bug Fixes

- fix(sdk): fix prerender inject data path
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

## [5.5.2] 2025-12-17

**Download: [5.5.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.2.zip)**

### Bug Fixes

- fix(sdk): add ut
- fix(lib): add comma to avoid MFA build error
- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android
- fix(cli): version sort
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

- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve
- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum
- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev
- feat(sdk): call all api
- feat(sdk): preload font
- feat(mpp-service): add widget qrcode request logic
- feat(bundler): update widgetConfigs
- feat(cli): dynamic bundle version support
- feat(sdk): video class name
- feat(cli): clean code & fix no-qjs flag & fix fs-extra copy failed
- feat: add preload-worker
- feat(cli): use libversion

## [5.5.1] 2025-12-17

**Download: [5.5.1(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.1.zip)**

### Bug Fixes

- fix(libs); bmp-components imported unexpectedly by web project
- fix(sdk): usePageScroll hooks not work
- fix(bmp): pika ci error
- fix(sdk): fix resolve native comp & input update timestamp
- fix(sdk): render child node directly when component need children vnode
- fix(sdk): host mini app events and setData damaged by widget flow
- fix: revert comment
- fix(sdk): @binance/bmp-xx deps
- fix(sdk): scrollViewUpdate rendererId undefined
- fix(lib): define EMPTY_OBJ
- fix(sdk): fix build script
- fix(sdk): dep missing
- fix(sdk): plugins types issue
- fix(sdk): fake childnode
- fix(sdk): fix no text in child text
- fix(sdk): nested text node
- fix(sdk): remove capture event handler
- fix(cli): bundler function params missing
- fix(sdk): typo error
- fix(sdk): fix alias to avoid multiple event emit

### Features

- feat(bundler): fix bundler config
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
- feat(lib): use one reactMeta for context
- feat(sdk): update hummer webpack with production mode
- feat(sdk): update typo
- feat(lib): update useEffect
- feat(sdk): use pika **APPID**
- feat(lib): move context to bmp-react
- feat(lib): add context
- feat(cli): update bundler version
- feat(sdk): update widget
- feat(sdk): add log
- feat(sdk): add widget hummer
- feat(sdk): no cache for widget open event
- feat(sdk): remove global RuntimeMonitor
- feat(sdk): hummer send to worker pageready
- feat(sdk): track campatibility for app inst
- feat(sdk): support widget slot
- feat(sdk): widget plugin
- feat(sdk): support event & update
- feat(sdk): update widget
- feat(sdk): hummer event, context, widget update
- feat(sdk): add component render plugin
- feat(sdk): widget slot plugin
- feat(sdk): add page ready
- feat(sdk): export widget component
- feat(sdk): fix typo
- feat(sdk): add widgetOpen handler
- feat(sdk): widget plugin
- feat(sdk): remove app timeline check & loadApp directly
- feat(sdk): remove mg
- feat(sdk): draft widget
- feat(sdk): avoid event error of widget
- feat(sdk): mp lite support prerender
- feat(sdk): update 5.0 widget
- feat(sdk): remove app instance
- feat(bundler): init widget bundler
- feat(sdk): export methods for widget
- feat(sdk): worker not wait renderer ready
- feat(sdk): use vue render
- feat(sdk): add components alias
- feat(sdk): remove bxml render in worker
- feat(sdk): clean worker timeline
- feat(sdk): clean worker timeline
- feat(sdk): 5.0 add script to build renderer-service-hummer.js
- feat(sdk): remove vnode and patch on worker

### Misc

- Revert "Merge master"
- revert: root condition in setData

## [5.4.1] 2025-12-17

**Download: [5.4.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.1.zip)**

### Features

- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.3.5] 2025-12-17

**Download: [5.3.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.5.zip)**

## [5.2.9] 2025-12-15

**Download: [5.2.9(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.9.zip)**

### Bug Fixes

- fix(sdk): text dont filter nest components

## [5.5.0] 2025-11-27

**Download: [5.5.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.5.0.zip)**

### Features

- feat(sdk): support closest AnchorElement tap
- feat(sdk): add private api getVisibilityState
- feat(sdk): input support force-decimal-dot
- feat(sdk): fliter standalone chunk js for bytecode pkg
- feat(sdk): support webview markdown list style
- feat(cli): release 1.0.0 stable version
- feat(cli): dx improve

## [5.4.0] 2025-11-07

**Download: [5.4.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.4.0.zip)**

### Bug Fixes

- fix(sdk): cp view based sdk 5.0 issue
- fix(sdk): cp tab area scroll
- fix(sdk): render data and prerender data independent to resolve flutter blink
- fix(sdk): ignore preload font on flutter
- fix(bundler): compatibility for old android

### Features

- feat(sdk): page timeline add check point
- feat(sdk): editor chart UI revamp
- feat(sdk,bundler): customize renderer components
- feat(sdk): add debug
- feat(sdk): b8 widget custom lifecycle
- feat(extendedLib): extended lib ci and checksum

## [5.2.8] 2025-11-04

**Download: [5.2.8(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.8.zip)**

### Bug Fixes

- fix(sdk): capacibility of document body
- fix(sdk): cp tab area scroll

## [5.3.4] 2025-11-04

**Download: [5.3.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.4.zip)**

### Bug Fixes

- fix(sdk): capacibility of document body
- fix(sdk): cp tab area scroll

## [5.3.4] 2025-11-04

**Download: [5.3.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.4.zip)**

### Bug Fixes

- fix(sdk): cp tab area scroll

## [5.2.8] 2025-11-04

**Download: [5.2.8(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.8.zip)**

### Bug Fixes

- fix(sdk): cp tab area scroll

## [4.51.4] 2025-11-03

**Download: [4.51.4(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.4.zip)**

### Bug Fixes

- Fix/tab move

## [5.3.3] 2025-11-02

**Download: [5.3.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.3.zip)**

### Bug Fixes

- fix(sdk): render data and prerender data independent to resolve flutter blink

## [5.2.7] 2025-11-02

**Download: [5.2.7(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.7.zip)**

### Bug Fixes

- fix(sdk): render data and prerender data independent to resolve flutter blink

## [4.51.3] 2025-10-30

**Download: [4.51.3(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.3.zip)**

### Features

- feat(sdk): editor chart UI revamp

## [5.3.2] 2025-10-30

**Download: [5.3.2(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.2.zip)**

### Bug Fixes

- fix(sdk): capacibility for prerender text

## [5.2.6] 2025-10-30

**Download: [5.2.6(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.6.zip)**

### Bug Fixes

- fix(sdk): capacibility for prerender text

## [4.51.2] 2025-10-29

**Download: [4.51.2(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.2.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [5.2.5] 2025-10-28

**Download: [5.2.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.5.zip)**

## [5.2.4] 2025-10-28

**Download: [5.2.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.4.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.3.1] 2025-10-28

**Download: [5.3.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.1.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.2.4] 2025-10-28

**Download: [5.2.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.4.zip)**

### Bug Fixes

- fix(sdk): viewbased mp issue

## [5.3.0] 2025-10-17

**Download: [5.3.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.3.0.zip)**

### Features

- feat(sdk): update value for input
- feat(script): add dev tag for publish-dev
- feat(sdk): add scrollOffset for pageScrollTo
- feat(sdk): support access node in SelectQuery
- feat(sdk): flutterToImage and nativeComponent for iOS webview renderer
- feat(sdk): remove root style 100%
- feat(mpp-service): use label as rev

## [5.2.3] 2025-10-15

**Download: [5.2.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.3.zip)**

### Bug Fixes

- fix(sdk): nested text render

### Features

- feat(sdk): remove skeleton earlier to improve FCP

## [4.51.2] 2025-10-14

**Download: [4.51.2(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.2.zip)**

### Features

- feat(sdk): support custom native component in iOS

## [4.51.1] 2025-10-13

**Download: [4.51.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.1.zip)**

### Features

- feat(sdk): flutter domToImage
- feat(mpp-service): update to junior

## [5.2.1] 2025-10-11

**Download: [5.2.1(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.1.zip)**

### Bug Fixes

- fix(sdk): render full attrs & buildin alias
- fix(cli): version sort

## [5.2.0] 2025-09-26

**Download: [5.2.0(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.2.0.zip)**

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

## [4.51.0] 2025-09-26

**Download: [4.51.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.51.0.zip)**

### Features

- Feat call all
- feat(sdk): sdk4.x support support formatter for all echart options

## [5.1.4] 2025-09-24

**Download: [5.1.4(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.4.zip)**

### Bug Fixes

- fix(sdk): usePageScroll hooks not work
- fix(sdk): hummer renderer support update single child

### Features

- feat(sdk): bn.removeWidgetSkeleton

## [5.1.3] 2025-09-17

**Download: [5.1.3(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.3.zip)**

### Bug Fixes

- fix(sdk): hummer render support update dom
- fix(sdk): fix hummer event not work because eventId not exist
- fix(sdk): comment log & debug log flag
- fix(sdk): remove duplicate worker module while hot-reload
- fix(sdk): fix render native webview

## [5.1.2] 2025-09-12

**Download: [5.1.2(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.2.zip)**

### Features

- feat(sdk): renderer mount do not wait worker rpc response

## [5.1.1] 2025-09-12

**Download: [5.1.1(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.1.zip)**

### Bug Fixes

- fix(sdk): fix widget FCP & LCP report
- fix(sdk): hotfix scrollview

### Features

- feat(sdk): sdk5.1 support formatter for all echart options

## [4.50.1] 2025-09-12

**Download: [4.50.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.50.1.zip)**

### Bug Fixes

- fix(sdk): hotfix scrollview

## [4.50.0] 2025-09-04

**Download: [4.50.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.50.0.zip)**

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

## [5.1.0] 2025-09-04

**Download: [5.1.0(1.81 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.1.0.zip)**

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

## [4.49.1] 2025-08-22

**Download: [4.49.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.49.1.zip)**

### Bug Fixes

- fix(sdk): nested scroll not work
- fix(sdk): menuBts props

## [5.0.0] 2025-08-15

**Download: [5.0.0(1.90 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-5.0.0.zip)**

### Bug Fixes

- fix(sdk): fix build script
- fix(sdk): dep missing
- fix(sdk): plugins types issue
- fix(sdk): fake childnode
- fix(sdk): fix no text in child text
- fix(sdk): nested text node
- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work
- fix(sdk): remove capture event handler
- fix(cli): bundler function params missing
- fix(sdk): typo error
- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- fix(sdk): fix alias to avoid multiple event emit
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y
- fix(sdk): expose the error before app init
- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(lib): use one reactMeta for context
- feat(sdk): update hummer webpack with production mode
- feat(sdk): update typo
- feat(lib): update useEffect
- feat(sdk): use pika **APPID**
- feat(lib): move context to bmp-react
- feat(lib): add context
- feat(cli): update bundler version
- feat(sdk): support share v2 api
- feat(sdk): update widget
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(sdk): add log
- feat(sdk): add widget hummer
- feat(sdk): no cache for widget open event
- feat(sdk): remove global RuntimeMonitor
- feat(sdk): hummer send to worker pageready
- feat(sdk): track campatibility for app inst
- feat(sdk): support widget slot
- feat(sdk): widget plugin
- feat(sdk): support event & update
- feat(sdk): update widget
- feat(sdk): hummer event, context, widget update
- feat(cli): support home page widget preview
- feat(sdk): add component render plugin
- feat(sdk): widget slot plugin
- feat(sdk): add page ready
- feat(sdk): export widget component
- feat(sdk): fix typo
- feat(sdk): add widgetOpen handler
- feat(sdk): widget plugin
- feat(sdk): remove app timeline check & loadApp directly
- feat(mpp-service): update ai router payload
- feat(sdk): remove mg
- feat(sdk): draft widget
- feat(mpp-service): ai router solution
- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(sdk): avoid event error of widget
- feat(cli): bundle watch process not exiting correctly
- feat(sdk): mp lite support prerender
- feat(sdk): update 5.0 widget
- feat(sdk): remove app instance
- feat(bundler): init widget bundler
- feat(sdk): export methods for widget
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message
- feat(sdk): worker not wait renderer ready
- feat(sdk): use vue render
- feat(sdk): add components alias
- feat(sdk): remove bxml render in worker
- feat(sdk): clean worker timeline
- feat(sdk): clean worker timeline
- feat(sdk): 5.0 add script to build renderer-service-hummer.js
- feat(sdk): remove vnode and patch on worker
- feat(sdk): support nested scroll view
- feat(sdk): blank detector
- feat(sdk): support typewriter effect for flutter markdown
- feat(sdk): support playsinline for video
- feat(sdk): use \_\_mp_runtime_config.screenWidth for set rem
- feat(mpp-service): add report file size functions
- feat(extended-lib): mpp runtime vendor
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo
- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib
- feat(sdk): suspend & resume lifecycle

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.49.0] 2025-08-14

**Download: [4.49.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.49.0.zip)**

### Bug Fixes

- fix(sdk): fix swiper loop mode & scroll view style
- fix(sdk): fix intersection observer relative info not work

### Features

- feat(sdk): support share v2 api
- feat(sdk): add formatter attribute
- feat(sdk): menuBts for flutter markdown
- feat(sdk): video poster
- feat(sdk): support locked config for sortableitem
- feat(cli): support home page widget preview
- feat(mpp-service): update ai router payload
- feat(mpp-service): ai router solution

## [4.48.1] 2025-08-04

**Download: [4.48.1(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.48.1.zip)**

### Bug Fixes

- fix(sdk): fix swiper loop mode & scroll view style

## [4.48.0] 2025-07-25

**Download: [4.48.0(1.85 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.48.0.zip)**

### Bug Fixes

- fix(sdk): relaunch deeplink issue
- fix(sdk): fix swiper autoplay
- Fix/swiper 0708
- fix(sdk): deeplink with data loader issue
- fix(sdk): exports utils
- fix(sdk): export bmp component utils
- fix(sdk): scroll X in scroll Y

### Features

- feat(sdk): revert autoheight default value to false
- feat(sdk): swiper autoHeight
- feat(sdk): mp plugin support AbortSignal
- feat(sdk): add require error log
- feat(cli): bundle watch process not exiting correctly
- feat(cli): add error handler for ios debug target query
- feat(cli): support inspect webview/webf with native devtool protocol message

### Misc

- Revert "fix(sdk): export bmp component utils"

## [4.47.1] 2025-07-21

**Download: [4.47.1(1.84 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.47.1.zip)**

### Bug Fixes

- fix(sdk): scroll X in scroll Y (#2251)

## [4.47.0] 2025-07-07

**Download: [4.47.0(1.84 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.47.0.zip)**

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
- feat(sdk): new api bn.addPhoneCalendar & bn.addPhoneRepeatCalendar
- feat(cli): add meta info indicator and every day tip
- feat(sdk): add new svg component demo

## [4.46.0] 2025-06-13

**Download: [4.46.0(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.46.0.zip)**

### Bug Fixes

- fix(sdk): hide home button api
- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): not set dataurl on style change
- feat(sdk): w3w timeline monitor
- feat(sdk): flutter svg class support
- feat(sdk): add ios timeline log fit regexp
- feat(sdk): virtualList support size by function
- feat(sdk): remove set rem in flutter
- feat(sdk): add createEventSource support for IDE
- feat(sdk): add `max-lines` for text-span
- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.5] 2025-06-12

**Download: [4.45.5(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.5.zip)**

### Misc

- Revert "feat(sdk): remove set rem in flutter"

## [4.45.4] 2025-05-26

**Download: [4.45.4(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.4.zip)**

### Bug Fixes

- fix(sdk): add svg style filter
- fix(sdk): fix page-frame

### Features

- feat(sdk): remove set rem in flutter

## [4.45.3] 2025-05-23

**Download: [4.45.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.3.zip)**

### Bug Fixes

- fix(server-side-bundle): add bundler as dep

### Features

- feat(sdk): support page preload
- feat(sdk): negotiation scroll with native on Android
- feat(extended-lib): use dynamicExtendedLib for all the libs and remove upload builtIn lib

## [4.45.3] 2025-05-23

**Download: [4.45.3(1.80 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.3.zip)**

### Features

- feat(sdk): remove set rem in flutter

## [4.45.2] 2025-05-21

**Download: [4.45.2(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.2.zip)**

### Bug Fixes

- fix(sdk): add svg style filter

## [4.45.1] 2025-05-19

**Download: [4.45.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.1.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.44.4] 2025-05-19

**Download: [4.44.4(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.4.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.45.1] 2025-05-19

**Download: [4.45.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.1.zip)**

### Bug Fixes

- fix(sdk): fix page-frame

## [4.44.3] 2025-05-16

**Download: [4.44.3(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.3.zip)**

## [4.45.0] 2025-05-15

**Download: [4.45.0(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.45.0.zip)**

### Features

- feat(sdk): suspend & resume lifecycle

## [4.1043.1] 2025-05-12

**Download: [4.1043.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1043.1.zip)**

### Bug Fixes

- fix(sdk): support multiple chart instances with same chart id when work with swiper
- fix(sdk): observer doesn't work
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

## [4.44.2] 2025-05-12

**Download: [4.44.2(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.2.zip)**

### Bug Fixes

- fix(sdk): support multiple chart instances with same chart id when work with swiper

## [4.44.1] 2025-05-07

**Download: [4.44.1(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.1.zip)**

### Bug Fixes

- fix(sdk): observer doesn't work

## [4.44.0] 2025-05-02

**Download: [4.44.0(1.73 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.44.0.zip)**

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

## [4.1043.0] 2025-04-18

**Download: [4.1043.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1043.0.zip)**

## [4.43.1] 2025-04-16

**Download: [4.43.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.43.1.zip)**

### Bug Fixes

- fix(sdk): domtoimage image url corner cases

### Features

- feat(sdk): add dark_midnight support for prerender

## [4.43.0] 2025-04-10

**Download: [4.43.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.43.0.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill
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

## [4.42.2] 2025-04-02

**Download: [4.42.2(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.2.zip)**

## [4.42.1] 2025-03-25

**Download: [4.42.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.1.zip)**

### Bug Fixes

- fix(sdk): flutter getAttribute polyfill

## [4.42.0] 2025-03-21

**Download: [4.42.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.42.0.zip)**

### Bug Fixes

- fix(cli): missing build start callback in bundleWatch
- fix(sdk): add LCP report target
- fix(sdk): drawer component visible when mounted
- fix(mpp-service): fix qjs build for Andriod
- fix(demo): pika no longer support `independent`

### Features

- feat(cli): rebundle while refresh
- feat(cli): improve achieve stability
- feat(cli): adjust glob params
- feat(cli): manual update qjsc version
- feat(cli): add syncPackInclude flag
- feat(bmp): add direction type for sortable
- feat(runtime): add api `fs.removeSavedFile`
- feat(demo): add more chose file or media demo

## [4.41.7] 2025-03-20

**Download: [4.41.7(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.7.zip)**

### Bug Fixes

- fix(sdk): duplicated route change

## [4.41.6] 2025-03-19

**Download: [4.41.6(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.6.zip)**

### Bug Fixes

- fix(sdk): fix modal navigate on android 2.97(no cherry pick to master)

## [4.41.5] 2025-03-17

**Download: [4.41.5(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.5.zip)**

## [4.41.4] 2025-03-14

**Download: [4.41.4(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.4.zip)**

### Features

- feat(sdk): improve drag & sort behaviour

## [4.41.3] 2025-03-10

**Download: [4.41.3(1.71 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.3.zip)**

### Performance Improvements

- perf: optimize performance by remove rpc log
- perf: remove logger to fast lcp metric

## [4.41.3] 2025-03-10

**Download: [4.41.3(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.3.zip)**

### Performance Improvements

- perf: remove logger to fast lcp metric

## [4.41.2] 2025-03-07

**Download: [4.41.2(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.2.zip)**

### Bug Fixes

- fix(sdk): intersection Observer component undefined issue

## [4.41.1] 2025-03-06

**Download: [4.41.1(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.1.zip)**

### Bug Fixes

- fix(sdk): free mode sortable and highlight input rtl issue

## [4.41.0] 2025-03-03

**Download: [4.41.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.0.zip)**

### Bug Fixes

- fix(sdk): page frame await syntax error
- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

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

## [4.41.0] 2025-02-28

**Download: [4.41.0(1.72 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.41.0.zip)**

### Bug Fixes

- fix op_line_number size increased and get_label_pos not changed on node-qjsc
- fix(mp-service): fix track line and column numbers for expressions on…

### Features

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

## [4.40.2] 2025-02-21

**Download: [4.40.2(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.2.zip)**

### Bug Fixes

- fix(sdk): domToImage only disabled in flutter

## [4.40.1] 2025-02-19

**Download: [4.40.1(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.1.zip)**

### Bug Fixes

- fix(sdk): flutterTarget can not be converted directly

## [4.40.0] 2025-02-10

**Download: [4.40.0(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.40.0.zip)**

### Bug Fixes

- fix(bundler): loadScriptSync issue on android
- fix(sdk): svg data url regexp missing text wrap
- fix(sdk): fix cursor flashing on devices
- fix(sdk): handle non-enumerable CustomEvent properties type and detail
- fix(sdk): cherry-pick virtual list hotfix
- fix(sdk): clear unreachable rpc promise
- fix(sdk): remove skyline sync ui command (#2058)
- fix(sdk): mitigate the risk of memory leak
- fix(host): loadScriptSync issue
- fix(cli): change @shoelace-style/shoelace version to 2

### Features

- feat(sdk): add disable-ios-embed props for ios native input
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

## [4.39.8] 2025-01-29

**Download: [4.39.8(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.8.zip)**

### Bug Fixes

- fix(sdk): changelog script

## [4.39.7] 2025-01-27

**Download: [4.39.7(2.47 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.7.zip)**

### Bug Fixes

- fix(sdk): remove skyline sync ui command

## [4.38.7] 2025-01-24

**Download: [4.38.7(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.7.zip)**

### Bug Fixes

- fix(sdk): disable scrolling when scroll into view

## [4.37.11] 2025-01-24

**Download: [4.37.11(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.11.zip)**

### Bug Fixes

- fix(sdk): disable scrolling when scroll into view

## [4.39.6] 2025-01-24

**Download: [4.39.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.6.zip)**

### Features

- feat(sdk): disable scrolling when scroll into viewe

## [4.38.6] 2025-01-23

**Download: [4.38.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.6.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

### Features

- feat(sdk): native-input cursor issue

## [4.37.10] 2025-01-23

**Download: [4.37.10(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.10.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

### Features

- feat(sdk): native-input cursor issue

## [4.37.10] 2025-01-23

**Download: [4.37.10(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.10.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.38.6] 2025-01-23

**Download: [4.38.6(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.6.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.39.5] 2025-01-23

**Download: [4.39.5(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.5.zip)**

### Bug Fixes

- fix(sdk): clear unreachable rpc promise

## [4.39.4] 2025-01-21

**Download: [4.39.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.4.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.38.5] 2025-01-21

**Download: [4.38.5(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.5.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.37.9] 2025-01-21

**Download: [4.37.9(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.9.zip)**

### Bug Fixes

- fix(sdk): mitigate the risk of memory leak

## [4.38.4] 2025-01-21

**Download: [4.38.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.4.zip)**

### Bug Fixes

- fix(sdk): 438 virtual list hotfix 0120

## [4.37.8] 2025-01-21

**Download: [4.37.8(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.8.zip)**

### Bug Fixes

- fix(sdk): virtual list hotfix 0120

## [4.39.3] 2025-01-20

**Download: [4.39.3(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.3.zip)**

### Bug Fixes

- fix(sdk): 439 virtual list hotfix 0120

## [4.38.4] 2025-01-20

**Download: [4.38.4(2.57 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.4.zip)**

### Bug Fixes

- fix(sdk): 438 virtual list hotfix 0120

## [4.37.8] 2025-01-20

**Download: [4.37.8(2.56 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.8.zip)**

### Bug Fixes

- fix(sdk): virtual list hotfix 0120

## [4.39.2] 2025-01-17

**Download: [4.39.2(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.2.zip)**

### Features

- feat(sdk): view component add events `onAppear&onIntersectionChange&o…

## [4.39.1] 2025-01-17

**Download: [4.39.1(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.1.zip)**

### Bug Fixes

- fix(sdk): 4.39 virtual list hotfix

## [4.38.3] 2025-01-17

**Download: [4.38.3(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.3.zip)**

## [4.37.7] 2025-01-17

**Download: [4.37.7(2.49 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.7.zip)**

## [4.39.0] 2025-01-16

**Download: [4.39.0(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.39.0.zip)**

### Bug Fixes

- fix(bmp): remove requestFullscreen param
- fix(sdk): flutter-video context issue

### Features

- feat(sdk): add showDiagnosticPage API
- feat(sdk): native-input cursor issue
- feat(sdk): add flutter-chart component
- feat(sdk): catch setTimeout callback error & Handle redundant `Uncaught` errors
- feat(cli): support debug mode flag

## [4.38.2] 2025-01-09

**Download: [4.38.2(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.2.zip)**

### Bug Fixes

- fix(sdk): flutter-video context issue
- fix(sdk): chart should be destroy after unmounted
- fix(sdk): enable placeholder for flutter

## [4.38.1] 2025-01-03

**Download: [4.38.1(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.1.zip)**

### Bug Fixes

- fix(sdk): chartActionQueue cache with id and monitor LCPElement payload

### Performance Improvements

- perf: remove getBoundingClientRect in flutter widget and nativeComp

## [4.38.0] 2024-12-26

**Download: [4.38.0(2.50 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.38.0.zip)**

### Bug Fixes

- fix(sdk): adjust unload timming
- fix(sdk): native input with number type issue
- fix(cli): ide-cli pnpm dep package.json resolve failed

### Features

- feat(sdk): `MP.onError` message format & `MP.lifecycle` throw error
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

## [4.37.6] 2024-12-19

**Download: [4.37.6(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.6.zip)**

## [4.37.5] 2024-12-19

**Download: [4.37.5(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.5.zip)**

### Bug Fixes

- fix(sdk): svg object.hasown not found

## [4.37.4] 2024-12-17

**Download: [4.37.4(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.4.zip)**

### Features

- feat(sdk): svg improve inline tag support

## [4.37.3] 2024-12-12

**Download: [4.37.3(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.3.zip)**

### Bug Fixes

- fix(sdk): remove repeat effect when worker data update

## [4.36.3] 2024-12-12

**Download: [4.36.3(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.3.zip)**

### Features

- feat(sdk): add skeleton remove point

## [4.36.3] 2024-12-11

**Download: [4.36.3(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.3.zip)**

### Bug Fixes

- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): add remove skeleton point
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.37.2] 2024-12-10

**Download: [4.37.2(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.2.zip)**

### Bug Fixes

- fix(sdk): hotfix 4.37.2

## [4.37.1] 2024-12-09

**Download: [4.37.1(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.1.zip)**

### Bug Fixes

- fix(sdk): refresher event detail not provide the flutterTarget as expect

## [4.37.0] 2024-12-05

**Download: [4.37.0(2.48 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.37.0.zip)**

### Bug Fixes

- fix(sdk): widget load timeline
- fix(sdk): flutter deprecated-textarea autoheight style error
- fix(sdk): trigger renderEffect before componentinit to fix patch issues
- fix(sdk): fix page stack update timing
- fix(sdk): run setdata callback after vue nexttick
- fix(bmp): update type `BnInputProps&BnTextareaProps`

### Features

- feat(sdk): sortable support dark mode
- feat: sortable component
- feat(sdk): flutter-scrollview add `refresher` props
- feat:(sdk): builtin svg component
- feat(sdk): deprecated textarea autoHeight support
- feat(ide-cli): preview functions for binance devtool
- feat(sdk): create chart context support options params
- feat(sdk): DeprecatedTextarea add `autocorrect` & `autocapitalize`
- feat(sdk): add scrollstart scrollend to scrollview
- feat(sdk): add `flutter-container`
- feat(sdk): add `option.url` in applyUpdate

### Performance Improvements

- perf: enhance scroll performance by reduce binding getter from event target

### Misc

- Revert "chore: @mp/bundler dev"

## [4.36.2] 2024-11-27

**Download: [4.36.2(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.2.zip)**

### Bug Fixes

- fix(sdk): resolve IntersectionObserver is undefined issue

### Features

- feat(sdk): expose response for native component

## [4.36.1] 2024-11-20

**Download: [4.36.1(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.1.zip)**

### Bug Fixes

- fix(sdk): webview instance id should not repeat

## [4.36.0] 2024-11-15

**Download: [4.36.0(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.36.0.zip)**

### Bug Fixes

- fix(sdk): change handlePaste defaultValue
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

## [4.35.2] 2024-11-08

**Download: [4.35.2(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.2.zip)**

### Bug Fixes

- fix(sdk): check whether to use patch
- fix(sdk): release flutter image load
- fix(sdk): wrap inline element with bn-span for bn-markdown

### Misc

- Revert "chore: revert ui command"

## [4.35.1] 2024-10-31

**Download: [4.35.1(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.1.zip)**

### Bug Fixes

- fix(sdk): markdown paragraph use bn-view, strong/em use bn-text

## [4.35.0] 2024-10-25

**Download: [4.35.0(2.43 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.35.0.zip)**

### Bug Fixes

- fix(sdk): support inlineLayout for skyline
- fix(sdk): flutter scroll refresher background color
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

- feat(sdk): new api page.updateRouteOptions
- feat(sdk): `DeprecatedTextarea` support `cursor/autoFocus/selection-start/selection-end`
- feat(demo): add error handler bot modal demo
- feat(sdk): use tap for skyline
- feat(sdk): add tab-switched api
- feat(sdk): update caniuse api
- feat(sdk): support multi pages in tabbar
- feat(sdk): webview clearScrollStatus, invoke api
- feat(sdk): add sticky-header & stick-section
- feat(sdk): add `<FlutterSwiper />`
- feat(sdk): setup markdown on flutter
- feat(sdk): new api enable enableSheetGesture
- feat(extended-lib): expose buildIn libs for server side bundle

## [4.34.7] 2024-10-25

**Download: [4.34.7(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.7.zip)**

### Bug Fixes

- fix(sdk): support tap and inlineLayout for skyline

## [4.34.6] 2024-10-22

**Download: [4.34.6(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.6.zip)**

### Bug Fixes

- fix(sdk): android 7 quickjs not support Unicode Property Escapes

## [4.34.5] 2024-10-15

**Download: [4.34.5(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.5.zip)**

### Bug Fixes

- fix(sdk): `deprecated-textarea` support force update

## [4.34.4] 2024-10-11

**Download: [4.34.4(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.4.zip)**

### Features

- feat(sdk): web-view-post-message event handler

## [4.34.3] 2024-10-10

**Download: [4.34.3(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.3.zip)**

### Features

- feat(sdk): setup markdown on flutter

## [4.34.2] 2024-10-09

**Download: [4.34.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.2.zip)**

### Bug Fixes

- fix(sdk): message for createwebview api instance

## [4.33.3] 2024-10-09

**Download: [4.33.3(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.3.zip)**

### Bug Fixes

- fix(sdk): hotfix 4.33.3 deprecated textarea

## [4.34.1] 2024-10-09

**Download: [4.34.1(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.1.zip)**

### Bug Fixes

- fix(sdk): flutter deprecated textarea when composing
- fix(sdk): flutter deprecated textarea

## [4.34.0] 2024-10-07

**Download: [4.34.0(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.34.0.zip)**

### Bug Fixes

- fix(sdk): fix webview message action not work
- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(host): align response with native
- feat(sdk): flutter text component
- feat(sdk): update markdown & pika version update
- feat(sdk): support readme feature
- feat(sdk): add 2 components `ContextMenu` & `ContextMenuItem`
- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.2] 2024-09-19

**Download: [4.33.2(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.2.zip)**

### Bug Fixes

- fix: add FlutterImage switch and remove FlutterSrollView type=list props

## [4.33.2] 2024-09-19

**Download: [4.33.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.2.zip)**

### Bug Fixes

- fix(sdk): native list view conflict with sliver style
- fix(automator): add timeout when run automator

### Features

- feat(sdk): add `<Lottie />` component & lottie-context
- feat(bundler): emit handlePageBundled when skeleton build finish
- feat(bundler): upgrade webpack to support Node >=18

## [4.33.1] 2024-09-17

**Download: [4.33.1(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.1.zip)**

## [4.33.0] 2024-09-13

**Download: [4.33.0(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.33.0.zip)**

### Bug Fixes

- fix(sdk): fix catchmove not work
- fix(sdk): add textarea placeholder class prop
- fix(sdk): fix component patch error messsage
- fix(sdk): fix drawer error and support accelaration
- fix(lib): fix event channel type
- fix(bundler): bundle watch mode should copy ignore files
- fix(sdk): scroll y on scrollView is not works
- fix(sdk): fix textarea props and type

### Features

- feat(demo): error handler demo
- feat(sdk): add deeplink target type
- feat(sdk): hack textarea with **BN_IGNORE_IS_COMPOSING** id
- feat(extended-lib): update react qjs
- feat(sdk): add component `flutter-image`
- feat(demo): add style inject demo page
- feat(sdk): add component flutter-scroll-view
- feat(sdk): add plugin `runtime-plugin-update-page-query`
- feat(sdk): add type `injected` for bmp-component
- feat(sdk): add plugin `runtime-plugin-control-button`

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786) (#1796)

## [4.32.1] 2024-08-30

**Download: [4.32.1(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.32.1.zip)**

### Misc

- Revert "fix(sdk): vnode patch issues " (#1786)

## [4.32.0] 2024-08-23

**Download: [4.32.0(2.20 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.32.0.zip)**

### Bug Fixes

- fix(sdk): vnode patch issues
- fix(sdk): navigate to type
- fix(sdk): delay page set to make sure buforeRouteChange done
- fix(bundler): disable sourcemap to reduce memory

### Features

- feat(sdk): drawer component
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

## [4.31.1] 2024-08-02

**Download: [4.31.1(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.31.1.zip)**

### Bug Fixes

- fix: add worker plugin

## [4.31.0] 2024-08-02

**Download: [4.31.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.31.0.zip)**

### Bug Fixes

- fix(lib): fix bmp component types
- fix(bundler): fix expression bundler

### Features

- feat(sdk): choose image support compression threshold
- feat(sdk): webview scrollChange event
- feat(sdk): add logger for timeline log analyze
- feat(sdk): scrollView skyline type list property support
- feat(sdk): input prop disablePaste
- feat(bundler): support bns in base.bxml and pika compile mode
- feat(sdk): editor chart ui revamp
- feat(sdk): support create worker
- feat(lib): add type of Script to bmp-components

## [4.30.0] 2024-07-12

**Download: [4.30.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.30.0.zip)**

### Bug Fixes

- fix(sdk): native component webview message
- fix(sdk): native event in worker
- fix(sdk): fix webview component
- fix(sdk): intersectionObserver margin
- fix(sdk): eventhandler of chart component
- fix(extended-lib): ethers Event identifier duplicated and getGlobal function error

### Features

- feat(sdk): webview component event api in queryselector
- feat(sdk): support navigate api with animated
- feat(sdk): bn.onCopy Api on Android
- feat(host): export workerEnvCode for host
- feat(extended-lib): upload bitcoinjs-lib & solana/web3.js
- feat(extended-lib): upload ethers-5.5.4.js

## [4.29.0] 2024-06-24

**Download: [4.29.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.29.0.zip)**

### Bug Fixes

- fix(sdk): webview sdk only send invoke message
- fix(sdk): image to figure will insert a new paragraph before the figure
- fix(sdk): cursor is wired when editor tap keyboard enter

### Features

- feat(sdk): new api for webview component
- feat(sdk): api show setting
- feat(sdk): support fontFamily for native-input and native-textarea
- feat(extended-lib): upload react-dom 18.2.0
- feat(sdk): remove load skeleton
- feat(sdk): add onCopy event for text component
- feat: mini program performance babel plugin
- feat(sdk): add ut coverage 98%

## [4.28.0] 2024-05-31

**Download: [4.28.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.28.0.zip)**

### Bug Fixes

- fix: update render cache doc id
- fix(extended-lib): resolve path not a module

### Features

- feat(demo): add log for skyline debug & extended-lib should keep the built-in libs for cicd & ide
- feat(extended-lib): remove built-in upload and fix getUrl data not send
- feat(extended-lib): support web3 libs
- feat(sdk): richtext support a href
- feat(sdk): add page name to performance point
- feat(sdk): widget props support functions in deeper obj
- feat(sdk): webview status and invoke api
- feat(sdk): add ut and increase coverage to 96.88%
- feat(sdk): support dynamic rendering cache
- feat(sdk): defer for taro useReady
- feat(sdk): editor chart insert should focus next line

## [4.27.0] 2024-05-10

**Download: [4.27.0(2.42 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.27.0.zip)**

### Bug Fixes

- fix(sdk): image should not add appid for bn protocal src in widget
- fix(sdk): page query not ready when onload
- fix(extended-lib): postpublish script throw error

### Features

- feat(sdk): api getrandomvalues
- feat(sdk): widgetslot props can use functions start with 'on'
- feat(plugin): sdk support w3w evm configurable
- feat(sdk): add flutter input comp
- feat(lib): add getWidgetId and try get ctx from current.widget
- feat(sdk): widget can load base.bxml in target app
- feat(sdk): api hide back button
- feat(sdk): editor echart card
- feat(sdk): cross app rpc support sync action
- feat(sdk): bump
- feat(host): support big int

## [4.26.2] 2024-04-23

**Download: [4.26.2(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.2.zip)**

### Bug Fixes

- fix(sdk): wsw call id

## [4.26.1] 2024-04-22

**Download: [4.26.1(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.1.zip)**

### Features

- feat(sdk): web3 plugin use shell app (#1687)

## [4.26.0] 2024-04-19

**Download: [4.26.0(2.41 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.26.0.zip)**

### Bug Fixes

- fix(host): support webassembly on host
- fix(sdk): hover class not disappear
- fix(sdk): create webview support widget
- fix(host): widget ref not works and webview size not correct
- fix(sdk): chart component need delay to setOptions

### Features

- feat(demo): host shell app add basebxml & preload
- feat(server-side-bundle): add bytecode full
- feat(sdk): api open document
- feat(sdk): cross app rpc api
- feat(demo): native component demo update
- feat(bundler): support widget extended lib
- feat(sdk): bns can work on exp
- feat(sdk): cherry-pick: delay onReady for tarojs & add more error message info for appjs load
- feat(cli): webf lint add new rules
- feat(lib): check media query in webf
- feat(sdk): taro page await app loaded

## [4.25.1] 2024-04-10

**Download: [4.25.1(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.25.1.zip)**

### Bug Fixes

- fix(sdk): echart no need delay
- fix(sdk): delay onReady for tarojs

### Features

- feat(sdk): add more error message info for appjs load

## [4.25.0] 2024-03-29

**Download: [4.25.0(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.25.0.zip)**

### Bug Fixes

- fix(extended-lib): add missing deps
- fix(sdk): fix createwebview node-bridge issu
- fix(sdk): fix bmp-component type

### Features

- feat(extended-lib): release to prod
- feat(sdk): custom native component
- feat(sdk): improve doc 0325
- feat(sdk): add new prop webPreferences
- feat(bundler): add solution for dynamic lib
- feat(sdk): render earlier for pages with static template configuration

## [4.23.1] 2024-02-21

**Download: [4.23.1(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.23.1.zip)**

### Bug Fixes

- fix(sdk): cherry-pick for hotfix

## [4.23.0] 2024-02-19

**Download: [4.23.0(2.40 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.23.0.zip)**

### Bug Fixes

- fix(sdk): when user delete all content web input may act unexpected
- fix(sdk): remote-debug env update
- fix(sdk): remote debugger resend ready to IDE

### Features

- feat(sdk): add error code for widget when renderer destroy during init
- feat(sdk): widget can get props without properties define

## [4.22.0] 2024-01-26

**Download: [4.22.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.22.0.zip)**

### Bug Fixes

- fix(demo): icon size demo
- fix(sdk): label trigger itemClick event for radio and checkbox

### Features

- feat(sdk): webf lint adjustment
- feat(sdk): add api setPageScrollable
- feat(sdk): limit data point max length
- feat(sdk): closeWidget can close native opend widget
- feat(sdk): editor support \n inside paste content

## [4.21.0] 2024-01-09

**Download: [4.21.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.21.0.zip)**

### Features

- feat(sdk): editor link paste with strick whitelist validator
- feat(bundler): increase SOURCEMAP_SIZE_LIMIT to 10MB

## [4.20.0] 2023-12-15

**Download: [4.20.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.20.0.zip)**

### Bug Fixes

- fix(sdk): flutter gradient issue
- fix(bundler): using prettier as formatter

## [4.19.0] 2023-11-24

**Download: [4.19.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.19.0.zip)**

### Bug Fixes

- fix(bundler): fix IDE can not reload

### Features

- feat(sdk): cherry-pick: add preloadflutterwebview api
- feat(sdk): add error code to show error page
- feat(sdk): add renderer Type in getCurrentPages api
- feat(sdk): createSelectorQuery select support rootPortal options
- feat(sdk): add latest version to update event
- feat(sdk): editor enter event
- feat(sdk): enableCursor for developers to use native cursor

## [4.18.1] 2023-11-22

**Download: [4.18.1(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.18.1.zip)**

### Features

- feat(sdk): add preloadflutterwebview api

## [4.18.0] 2023-11-03

**Download: [4.18.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.18.0.zip)**

### Bug Fixes

- fix(sdk): fix webview sdk to compatible with node bridget
- fix(cli): fix scroll-speed-limit default value
- fix(cli): fix scroll-speed-limit default value
- fix(sdk): support input focus and blur action by developers

### Features

- feat(sdk): hold atom selection
- feat(sdk): web input support inputmode and pattern
- feat(bundler): merge widgetconfig to appconfig
- feat(sdk): support atom selection
- feat(sdk): add scrollSpeedLimit to avoid blank frame of virtual list
- feat(sdk): editor support mention and hardBreak

## [4.17.2] 2023-10-23

**Download: [4.17.2(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.2.zip)**

### Bug Fixes

- fix(sdk): support input focus and blur action by developers

## [4.17.1] 2023-10-18

**Download: [4.17.1(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.1.zip)**

### Bug Fixes

- fix(sdk): END_FIRSTPAGE_APPLAUNCH send pid

### Features

- feat(bundler): use js-beautify replace prettier as formater of qjs

## [4.16.3] 2023-10-13

**Download: [4.16.3(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.3.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.17.0] 2023-10-13

**Download: [4.17.0(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.17.0.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page
- fix(sdk): cherry pick 4.16.2 + try catch instance update
- fix(sdk): using show-scrollbar disable scrollbar
- fix(sdk): iOS cursor always at the edge of the word, selection update event not trigger

### Features

- feat(bundler): qjs compared from a formatted js code
- feat(lib): bmp-api openWidget add support for convention path
- feat(sdk): report error during renderer launching process
- feat(sdk): scroll view support scrollWithAnimation and scrollIntoViewAlignment
- feat(sdk): support swiper rtl props
- feat(sdk): widget support open dialog
- feat(tools): webf style linter
- feat(sdk): report LCP only after user interacts
- feat(sdk): set tab bar list api
- feat(lib): refactor WidgetSlot as react component
- feat(lib): bmp-react & bmp-component add support for widget

## [4.16.3] 2023-10-13

**Download: [4.16.3(2.39 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.3.zip)**

### Bug Fixes

- fix(sdk): clone data avoid reuse data object when reopen page

## [4.16.2] 2023-09-27

**Download: [4.16.2(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.2.zip)**

### Bug Fixes

- fix(sdk): avoid crash when worker receive invalid tags

## [4.16.1] 2023-09-25

**Download: [4.16.1(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.1.zip)**

### Bug Fixes

- fix(sdk): editor link node

## [4.16.0] 2023-09-22

**Download: [4.16.0(2.38 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.16.0.zip)**

### Bug Fixes

- fix(sdk): revert swiper located to wrong child when children updated
- fix(demo): component-demo use built-in chart
- fix(sdk): decode extra data without appid
- fix(sdk): swiper located to wrong child when children updated
- fix(bundler): fix expression not work on tag in `bn:for`
- fix(demo): independent package config
- fix(demo): private-close-app require shouldClose payload
- fix(bundler): decompress replace unzipper
- fix(bundler): bundler watch has 60s cache

### Features

- feat(sdk): echarts tooltip support basic dom
- feat(sdk): widget in widgetslot support lifecycles
- feat(sdk): editor internal plugin link support

## [4.15.1] 2023-09-07

**Download: [4.15.1(2.34 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.15.1.zip)**

### Bug Fixes

- fix(sdk): fix call plugin error code

## [4.15.0] 2023-08-31

**Download: [4.15.0(2.34 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.15.0.zip)**

### Bug Fixes

- fix(sdk): enbale flutter qjs
- fix(sdk): swiper may throw error when disable indicatorDots
- fix(sdk): widget props can get in worker
- fix(sdk): cursor always jump to the first position when value change from an empty string
- fix(sdk): check demo page ci
- fix(bundler): source-map issue of swc-loader
- fix(sdk): reset transform when refresher unmount

### Features

- feat(sdk): add more info to showErrorPage and add widget error report
- feat(sdk): export standard error to developers
- feat(sdk): bump version
- feat(sdk): dynamic widget support props and add openWidget API
- feat(sdk): sdk ut to 95%
- feat(bundler): build qjs for renderer in flutter
- feat(demo): enable flutter
- feat(bundler): server side bundle add more files into qjs

## [4.14.0] 2023-08-11

**Download: [4.14.0(1.45 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.14.0.zip)**

### Bug Fixes

- fix(sdk): create webview api in mp cannot message
- fix(sdk): customize component data not update when return a data getter
- fix(cli): webview component onmessage event
- fix(sdk): cherry-pick fix web input seqId
- fix(sdk): cherry-pick editor remove link and style recover (#1515)
- fix(sdk): cherry-pick editor split figure bugs
- fix(sdk): object spread syntax error
- fix(cli): add webview component, webpack chain error
- fix(bundler): lock unzipper version cause new version may lost file
- fix(host): block TextEncoder prop

### Features

- feat(sdk): editor transform pasted content
- feat(demo): pika extendedlib
- feat(sdk): scroll-view supports scroll-anchor
- feat(sdk): api bn.preloadWebContent to preload webview content advance
- Feat/metadata
- feat(sdk): editor paste event props
- feat(sdk): echart component

## [4.13.1] 2023-07-28

**Download: [4.13.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.13.1.zip)**

### Bug Fixes

- fix(sdk): unicode regex issue
- fix(sdk): editor remove link and style recover
- fix(sdk): object spread syntax error
- fix(sdk): editor split figure bugs
- fix(sdk): object spread sytax error
- fix(sdk): add seqId to web input event

## [4.13.0] 2023-07-26

**Download: [4.13.0(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.13.0.zip)**

### Bug Fixes

- fix(demo): intersection observer usage
- fix(sdk): bundler remove touchmove prevent modifer
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

### Misc

- Revert "fix(sdk): iOS native component created failed when container is not visible "

## [4.12.1] 2023-07-07

**Download: [4.12.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.12.1.zip)**

### Features

- feat: add mamual prop to web input

## [4.12.0] 2023-06-30

**Download: [4.12.0(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.12.0.zip)**

### Bug Fixes

- fix(sdk): font-family should go with system font-family
- fix(sdk): domtoimage svg base64 not have datatype
- fix(sdk): add export type
- fix(demo): fix canvas toTempFilePath
- fix(server-side-bundle): remove subpackage prefix of sourceURL
- fix(server-side-bundle): sourceURL issue of qjs

### Features

- feat(lib): add API removeSkeleton to bmp-react
- feat(sdk): control input
- feat(server-side-bundle): add sentry project name and releaseid
- feat(sdk): split figure into fig-caption and image

### Performance Improvements

- perf: add filesystem cache

## [4.11.1] 2023-06-27

**Download: [4.11.1(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.11.1.zip)**

### Bug Fixes

- fix(sdk): domtoimage svg base64 not have datatype (4.11)

## [4.11.0] 2023-06-16

**Download: [4.11.0(1.13 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.11.0.zip)**

### Bug Fixes

- fix(sdk): domtoImage local image support for android
- fix(demo): fix share demo
- fix(sdk): video fullscreenchange on IOS
- fix(cli): hack taro catch event
- fix(demo): update prefetch image path
- fix(mpp-service): newVersionFromServer might be null issue
- fix(demo): reset zoom ref when toggle camera position
- fix(sdk): dom to image support private static server images
- fix(sdk): editorContext insertCoin not works
- fix(mpp-service): min versoin should not replace the input version
- fix(mpp-service): set min upload version as 0.0.1
- fix(automator): read route of undefined issue
- fix(mpp-service): disable contentType when getUploadFileKey
- fix(demo): websocket url not work

### Features

- feat(server-side-bundle): use file path as sourceURL of qjs
- feat(sdk): support udpsocket api
- feat(sdk): 🎸 [plugin] add universal web3 provider
- feat(sdk): dom to image support native canvas
- feat(sdk): editor extension link
- feat(sdk,bundler,demo): support skeleton
- feat(sdk,bundler,demo): add camera component & createCameraContext API

## [4.10.2] 2023-06-08

**Download: [4.10.2(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.2.zip)**

### Bug Fixes

- fix(sdk): fix startCheckPageTimeline error

## [4.10.1] 2023-05-25

**Download: [4.10.1(1.14 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.1.zip)**

### Bug Fixes

- fix(sdk): renderer service compatitable with es5

## [4.10.0] 2023-05-23

**Download: [4.10.0(1.10 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.10.0.zip)**

### Bug Fixes

- fix(mpp-service): set maxBodyLength & maxContentLength as Infinity wh…
- fix(sdk): canIUseCustom support string params
- fix(cli): support catch touchend
- fix(sdk): fix ths issue about get appConfig & getPage
- fix(sdk): callbackify error no stack
- fix(sdk): load page frame after load base.bxml success
- fix(mpp-service): add contentType filed when upload for security
- fix(host): download support put
- fix(demo): add private send transaction demo
- fix(cli): webview injected not work
- fix(demo): webview page not found

### Features

- feat(demo): add prefetchRules
- feat(sdk): getUserOpenId return token
- feat(sdk): editor coin
- feat(sdk): editor image scrollIntoView
- feat(sdk): editor image default spinner
- feat(sdk): Mini Game touch event optimization
- feat(bundler): support bxs

## [4.9.2] 2023-05-19

**Download: [4.9.2(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.2.zip)**

### Bug Fixes

- fix(sdk): canIUseCustom support string params

## [4.9.1] 2023-05-17

**Download: [4.9.1(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.1.zip)**

### Bug Fixes

- fix(sdk): update load script error code

### Features

- feat(sdk): use appConfig after init appConfig & add appConfig detection & syncGetPage or
  asyncGetPage
- feat(host): set custom http headers for fetch requests

## [4.9.0] 2023-04-28

**Download: [4.9.0(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.9.0.zip)**

### Bug Fixes

- fix(sdk): figure scrollIntoView should focus on the figure caption
- fix(demo): production convertToMPUrl usage
- fix(sdk): editor caption selection and image keyboard handler
- fix(host): definitions for bn.env
- fix(sdk): unhandleRejection support polyfilled promise
- fix(sdk): fix edtior editing image error
- fix(sdk): init performance observer after worker ready
- fix(sdk): editor delete image event stopropagation
- fix(sdk): fix load page.js error to report 603505 when webview is des…
- fix(demo): fix event-channel demo
- fix(demo): on/off pairs
- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version
- fix(demo): bug in navigation demo
- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue
- fix(sdk): add native-send-appLuanch timer
- fix(bundler): css variables rpx to rem align with wechat
- fix(sdk): mini game view port size
- fix(sdk): getChildrenNode util function
- fix(sdk): rendererId zero issue in native ui
- fix(bundler): catchmove value should be an exp
- fix(sdk): swiper Item blank
- fix(demo): fix custom demo textarea maxlength
- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component
- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes
- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css
- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): ut from plugin-location to plugin-request-subscribe-message
- feat(sdk): file method support put method
- feat(demo): add beforeRouteChange usage to component-demo
- feat(sdk,bundler): add show confirm bar for input
- feat(sdk): srcollview pulldown refresher
- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API
- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly
- feat(demo): control picker view demo
- feat(sdk): detect page timeline
- feat(host): support pageReadyCallback
- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react
- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal
- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo
- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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
- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc
- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "fix(sdk): env undefined"
- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

## [4.8.1] 2023-04-13

**Download: [4.8.1(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.8.1.zip)**

### Bug Fixes

- fix(sdk): fix load page.js error to report 603505 when webview is destroyed

## [4.8.0] 2023-04-07

**Download: [4.8.0(1.09 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.8.0.zip)**

### Bug Fixes

- fix(sdk): editor image selection and focus
- fix(mpp-service): print the old and new version

### Features

- feat(sdk): bids use monitorupload
- feat(demo): editor component demo
- feat(sdk): remove settimeout for page.show
- feat(sdk): page-not-found
- feat(sdk): add page-frame-html in sdk
- feat(sdk): chooseMedia & chooseFile API

## [4.7.1] 2023-03-23

**Download: [4.7.1(NaN MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.7.1.zip)**

### Bug Fixes

- fix(sdk): startuptimeout & try catch getpage & add get page info
- fix(demo): bug in navigation demo

### Features

- feat(sdk): catch html
- feat(sdk): figure

## [4.7.0] 2023-03-17

**Download: [4.7.0(1.1 MB)](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.7.0.zip)**

### Bug Fixes

- fix(sdk): editor image cursor position and delete use touchend event
- fix(sdk): update report data object & cancel startupTimeout when load resources
- fix(sdk): editor image support update and deletable, hashtag keyboard key unexpected issue
- fix(sdk): update load-script payload to ensure the cache is loaded
- fix(sdk): update event channel if page init before eventChannel
- fix(sdk): fix native input color issues on ios13
- fix(demo): update pika to fix input issue
- fix(sdk): update dom to image scale impl and fix image / font issues
- fix(sdk): rename getUserOpenId & doc-api - getUserOpenId/getUserKycStatus
- fix(host): get-image-info is broken on IDE
- fix(host): bn.request support arraybuffer body
- fix(demo): radio page issue

### Features

- feat(sdk): editor focus and mark
- feat(sdk): add startupTimeout & restore time compensation
- feat(sdk): editor extension update and docs
- feat(sdk): loading progress animation
- feat(host): createBufferUrl support svg
- feat(demo): add dom to image demo
- feat(sdk): method domToImage
- feat(sdk): exitMiniProgram support force close
- feat(sdk): new api - getuseropenid getuserkycstatus
- feat(sdk): editor component & editorContext api
- feat(sdk): load resource fail or slowly

## [3.14.16] 2023-02-24

**Download: [SDK-3.14.16](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.16.zip)**

### Bug Fixes

- fix(sdk): cherry-pick - picker view control mode
  ([d9a10d59](https://git.toolsfdg.net/fe/mini-program/commit/d9a10d599fb2ab6d7c222c2204917dcd7511a888))
  by lawrence.w@binance.com

## [4.6.0] 2023-02-24

**Download: [SDK-4.6.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.6.0.zip)**

### Bug Fixes

- fix(sdk): add native-send-appLuanch timer
  ([532dde2e](https://git.toolsfdg.net/fe/mini-program/commit/532dde2e37e8c3ff48cbf655238b88a9a1ff0dcd))
  by finley.x@binance.com
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
- fix(sdk): controlled picker view
  ([661aa89a](https://git.toolsfdg.net/fe/mini-program/commit/661aa89ad9c3289ce614f2b77995d4ebf6d08bfa))
  by lawrence.w@binance.com

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

- chore: bump commit after write files
  ([9378fed1](https://git.toolsfdg.net/fe/mini-program/commit/9378fed122a9613f50aac333ff8543d12893bbbc))
  by dylan.z@binance.com
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
- mpp service support binance us host app
  ([fb8edeb8](https://git.toolsfdg.net/fe/mini-program/commit/fb8edeb8c6840cc84ef840c6ca84dcfc3a51fd72))
  by leo.cc@binance.com

## [4.5.0] 2023-02-03

**Download: [SDK-4.5.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.5.0.zip)**

### Bug Fixes

- fix(lib): remove optional chaining from bmp-react
- fix(sdk): fix requestBinanceCardInfo error response & cicd
- fix(bundler): compile optional chaining when using latest caniuse-lite
- fix(sdk): android css transition native component

### Features

- feat(sdk): add binance-card-info api
- feat(demo): migrate to pika
- feat(sdk): jssdk dashboard rename & calculate
- feat(sdk): wallet connector use new wallet provider
- feat(lib): add WebViewComponent to @binance/bmp-components
- feat(demo): add English desc to image mode demo
- feat(sdk): remove window info cache for view-base mode
- feat(lib): add getCurrentInstance & getTabBar to @binance/bmp-react

### Refactor

- refactor: throw error for the non-supported apis in IDE

### Internal

- chore: update component demo
- docs: remove the app.config.json issue since pika will support it
- docs: getCurrentInstance query incorrect

## [4.4.0] 2023-01-13

**Download: [SDK-4.4.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.4.0.zip)**

### Bug Fixes

- fix(sdk): fit audio platform api getters/setters on Andriod
- fix(sdk): add RootPortal type
- fix(sdk): mpc method
- fix(lib): update types of bmp-react
- fix(sdk): types of bn.call & add RootPortal to bmp-components
- fix(demo): caret-color
- fix(lib): virtual-list use new bmp packages
- fix(sdk): update canIuse info
- fix(sdk): cherry pick fix picker view component
- fix(lib): @binance/mp-components don't import @tarojs/components
- fix(sdk): image reload after src changes

### Features

- feat(sdk): webview component supports message
- feat(sdk): add runtime-plugin-mpc
- feat(automator): impove `setupProxyMethod` & add test
- feat(sdk): create buffer url supports extension option
- feat(demo): add audio and write file benchemark
- feat(sdk): swiper support previousMargin/nextMargin/snapToEdge
- feat(automator): add mock api for automator
- feat(lib): bmp-api & bmp-components & bmp-react
- feat(sdk): add error log for 603114
- feat(sdk): View support prop: catchMove
- feat(demo): images add mode & readFile add length & position config
- feat(lib): generate types for @binance/mp-service
- feat(sdk): root-portal

### Internal

- chore: update config for FAQ
- docs: faq about app.config.json
- docs(sdk): darkmode
- chore(sdk): cherry pick update sdk loading
- test: add more unit tests for host

## [3.14.15] 2023-01-10

**Download: [SDK-3.14.15](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.15.zip)**

### Bug Fixes

- fix(sdk): cherry pick from native component css

### Internal

- cherry-pick(sdk): swiper

## [3.14.14] 2023-01-04

**Download: [SDK-3.14.14](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.14.zip)**

### Bug Fixes

- fix(sdk): picker view component

### Features

- feat(sdk): add applaunch pid & new point from pageJsEnd to pageReady
- feat(sdk): cherry-pick - add error log for 603114

## [3.14.13] 2022-12-29

**Download: [SDK-3.14.13](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.13.zip)**

### Bug Fixes

- fix(sdk): image style not work when set mode to aspectFill

## [3.14.12] 2022-12-26

**Download: [SDK-3.14.12](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.12.zip)**

### Bug Fixes

- fix(sdk): update sdk loading

## [4.3.0] 2022-12-22

**Download: [SDK-4.3.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.3.0.zip)**

### Bug Fixes

- fix(sdk): mini game keyboard event
- fix(demo): fix demo navigation bar page
- fix(bundler): fix babel env target
- fix(demo): api navigation bar input element
- fix(sdk): cherry-pick from release/3.14
- fix(runtime): network service setupServices multiple times
- fix(automator): update @binance/mp-web for fix some issue and add `sdkPath` option
- fix(bundler): launch MP with page of independent subpackage
- fix(sdk): Image widthfix/heightFix mode can update size automatically
- fix(demo): fix universal-share css

### Features

- feat: integrate automator on CI
- feat(sdk): loadFontFace
- feat(sdk): file system api use platform api
- feat(sdk): expose navigateBackMiniProgram, add mpModalType prop to navigateToMiniProgram
- feat(sdk): webview bounce and loading bar
- feat(lib): fork implement from @tarojs/components to @binance/mp-components
- feat(sdk): create buffer url use platformAPI
- feat(sdk): createInnerAudioContext use platform api
- feat(demo): fix create buffer url demo

### Refactor

- refactor: rename host-mp-ide to host-ide

### Internal

- chore: remove `yarn playwright install --with-deps`
- docs(sdk): integrate with doc-system
- chore(package.json): fix installing sqllite3 in macos
- chore(package.json): add packageManager field
- chore: replace resolve with join
- chore(sdk): cherry-pick from 4.2.1
- chore: update version remote and pwd alias
- chore: bump local
- chore: update prefetch rule of component demo
- docs: demos readme

## [3.14.11] 2022-12-19

**Download: [SDK-3.14.11](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.11.zip)**

### Bug Fixes

- fix(sdk): appConfig bug in ios while open worker pool

## [4.2.1] 2022-12-15

**Download: [SDK-4.2.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.2.1.zip)**

### Features

- feat(sdk): add mg page-ready

## [3.14.10] 2022-12-07

**Download: [SDK-3.14.10](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.10.zip)**

### Bug Fixes

- fix(sdk): fix renderer-defer lead to blank screen

## [4.2.0] 2022-12-02

**Download: [SDK-4.2.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.2.0.zip)**

### Bug Fixes

- fix(bundler): reorder files in pkg - renderer files first
- fix(sdk): fix web canvas width and height
- fix(automator): replace parcel with http server to fix the installation issue from BIDS
- fix(sdk): selectorQuery return empty when error
- fix(runtime): remove BXML spaces
- fix(bundler): remove setImmediate polyfill to fix pika MP white screen on iOS
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

- feat(sdk): gcanvas optimazation
- feat(demo): add a rendererId 0 issue test case
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

- refactor(sdk): plugins including show-leaderboard, storage and tab-bar
- refactor(sdk): native ui plugin
- refactor(sdk): replace enum with union type
- refactor(host): plugin user-info
- refactor(host): plugin & remove twoFA demo

### Internal

- chore: remove useless message in changelog.md by 'bot'
- chore: redirect blank page issue
- ci: fix git push tag one by one
- chore: add caretColor demo
- chore: gen-sdk local

## [3.14.9] 2022-12-01

**Download: [SDK-3.14.9](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.9.zip)**

### Features

- feat(sdk): support navigateTo an external link - cherry pick

## [3.14.8] 2022-11-22

**Download: [SDK-3.14.8](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.8.zip)**

### Bug Fixes

- fix(sdk): fix native delay app-launch after background and load \_\_app.js fail to lead blank
  screen

### Features

- feat(sdk): nezha render js point

## [4.0.3] 2022-11-18

**Download: [SDK-4.0.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.3.zip)**

### Bug Fixes

- fix(sdk): rendererId start with zero
- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs
- fix(sdk): env undefined
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1

## [3.14.7] 2022-11-17

**Download: [SDK-3.14.7](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.7.zip)**

### Features

- feat(sdk): add support caretColor style for Input and TextArea components

## [3.14.6] 2022-11-16

**Download: [SDK-3.14.6](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.6.zip)**

### Bug Fixes

- fix(sdk): load-script-progress event when mp background event to lead blank screen
- fix(sdk): remove generating worker-service-game.qjs

### Internal

- chore: add checker for 3.14
- chore: gen-sdk script
- chore: update changelog.js

## [4.1.0] 2022-11-16

**Download: [SDK-4.1.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1.0.zip)**

### Bug Fixes

- fix(cli): skip generation of unmatched tags
- fix(sdk): read-file demo, location api
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin
- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore: 4.1 pr checker
- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2
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
- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.1.0] 2022-11-16

**Download: [SDK-4.1.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.1.0.zip)**

### Bug Fixes

- fix(sdk): read-file demo, location api
- fix(cli): mpService should support both function api and object api
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
- fix(runtime): width of scroll-bar should be zero
- fix(automator): support download-package rpc
- fix(cli): update web host cli

### Features

- feat(sdk): web canvas component
- feat(demo): mini game system info demo
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
- feat(demo): virtual list
- feat(runtime): support bn.env.USER_DATA_PATH
- feat(sdk): remove monitor because native didn't support the commands
- feat(sdk): loadScriptSync rpc

### Refactor

- refactor(sdk): migrate wallet-connector plugin
- refactor(host): share-menu(sdk & host)and network
- refactor(sdk): migrate toast plugin
- refactor(host): update manager and webview plugin
- refactor(sdk): migrate web3 plugin

### Misc

- Revert "fix(sdk): env undefined"

### Internal

- chore: 4.1 pr checker
- chore(changelog): @binance/mp-cli@2.4.26
- chore(changelog): @binance/mp-automator@1.0.7
- chore(changelog): @binance/mp-web@0.0.21
- chore(mp-web): update start script
- chore(changelog): update changelog for version v3.14.5
- chore(changelog): @binance/mp-cli@2.4.25
- chore: fix changelog.md
- chore(changelog): update changelog for version v4.1.0-dev.2
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
- chore(cicd): migrate prowjobs
- chore(changelog): update changelog for version v4.0.0
- chore: noopify commands

## [4.0.2] 2022-11-14)

**Download: [SDK-4.0.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.2.zip)**

### Bug Fixes

- fix(sdk): cherry pick - fix image style not work
- fix(sdk): await load appJs
- fix(sdk): env undefined
- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js
- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e
- fix(sdk): share-panel not working
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action
- fix(sdk): fix timeline order error
- fix(sdk): remove global wx, fix getOpenDataContext placeholder
- fix(sdk): timeline appJs error
- fix(sdk): timeline-update
- fix(cli): debugReact with react-reconciler not works
- fix(sdk): increase gas limit when estiamte gas failed
- fix(runtime): postMessage should wait for ready
- fix(cli): resolve taro presets from installation dir of bmp
- fix(cli): support node 15
- fix(sdk): can-i-use types & injectPrivateApi
- fix(rumtime): support tmp/store/usr http request
- fix(bundler): source-map OOM & repeated refresh in watch mode issues
- fix(sdk): fix onOffManager memory leak for task-style apis
- fix(demo): fix demo for fileSystemManager
- fix(runtime): add Math.ceil when populate gas
- fix(sdk): canvas plugin
- fix(bundler): adjust the order of loading script in page-frame
- fix(bundler): load base.bxml.js earlier than renderer-service.js
- fix(sdk): plugin write file
- fix(sdk): blank page when relaunch in old ios device
- fix(sdk): support cocos
- fix(sdk): app-rpc-logger judge from or to & delete extra log
- fix(sdk): monitor d change to dt & update RuntimeLogger monitor-upload
- fix(sdk): webview not working for the webview using node-bridge
- fix(bundler): load base.bxml.js in head element of page-frame
- fix(sdk): plugin-private-request command
- fix(sdk): add dataset to MPEventTarget
- fix(runtime): onNativeApiRequest able to listen all actions
- fix(sdk): radio and checkbox components
- fix(sdk): ios not support bigint 64
- fix(sdk): sentry + vconsole cause oom
- fix(sdk): fix Android need to tap input twice to focus
- fix(sdk): fix the issue that slider wrap with position: relative container
- fix(mp): fix request cookie setting
- fix(sdk): fix reportEvent with keyword to error
- fix(sdk): timeline startup del loadAppJs
- fix(sdk): DeprecatedInput auto-fill not emit input event
- fix(sdk): fix native input color with autoFocus props
- fix(runtime): storage plugin api not work
- fix(sdk): fix Image style width:100%
- fix(sdk): remove header filed with null value
- fix: add defer for webview context in the node-bridge demo
- fix: create a empty webview if src not provied
- fix(mp): fix tab bar css, red dot api error message
- fix(sdk): fix Image style being overridden and comments using English
- fix(sdk): image can not use width/height: auto with div-bgImg
- fix(sdk): onAppShow not working
- fix(sdk): remove the error of webivew-sdk Unknown Action $ready
- fix(sdk): update image component from img to div with background-image
- fix: framework-load-script has been registed
- fix(sdk): fix View component touchstart twice (#295)
- fix(lib,sdk): fix deprecated-input onInput not working
- fix(runtime): show & hide ToastContainer
- fix(sdk): plugin create native buffer
- fix(sdk): Image and IDECoverImage onload & onerror
- fix(sdk): timelogger error add time
- fix(sdk): debounce update state for native input
- fix(sdk): fix re-launch page not found issue
- fix(runtime): fix storage plugin
- fix(sdk): disable the JS timer for blank page detection
- fix(lib): make bundler generate component code that not override comp…
- fix(runtime): prevent app.js load twice
- fix(sdk): polyfill IntersectionObserver for iOS 12.1 (#237)
- fix: add commit hash to branch name
- Fix: release script
- fix: unexport subscribeLocationChange
- fix: sdk build
- fix the problem that bundler still work when in h5 mode
- fix some dependencies of project template
- fix: use path.resolve
- fix: make form component soft controlled & add missing component map
- fix: use -o
- fix the problem after last commit which make bundle script not work
- fix: normalize page url
- fix: 🐛 overwrite template files
- fix for debugger
- fix: 🐛 add http-proxy-middleware@0.19 in runtime-render
- Fix/fix the request with correct parameters and all other things for mvp2
- fix: send body only for post and put method
- fix: prevent user from scaling view
- fix: remove useless code
- fix(runtime-renderer): fix multiple event binding on same event
- fix: get props and data from parent & rename api
- fix: typo
- fix: use Object.assign
- fix: reduce payload size
- fix: Resolve events from attrs and separate two rpc events
- fix: use eventNames to tell the different if it is a event name or a normal props name
- fix: watch $props
- fix: rename
- fix: watch all props changed
- fix: remove bind props interface
- fix: remove useless code
- fix the problem invoked by packange name changed of taro plugin
- fix: prevent capture event trigger twice
- fix: 🐛 use e.currentTarget
- fix: 🐛 renderTaro and updateData
- fix: 🐛 renderTaro
- fix: keep compatible with taro
- fix: add tapCapture
- fix: add capture event
- fix: update props naming
- fix: remove console.log
- fix: Non-function value encountered for default slot. Prefer function slots for better
  performance.
- fix: remove console.log
- fix: types
- fix: update sdk
- fix: response.data typing
- fix: 🐛 enableCSSModule
- fix: call ready before navigation-push
- fix: typo
- fix: typo
- fix: typo
- fix: change data type
- fix: 🐛 back to list page
- fix: rpc
- fix(runner): rpc message format
- fix(runner): rpc message format
- fix: pass query to page.oLoad
- fix: fix ready and push action order
- fix: page component created twice
- fix: fix page hooks
- fix: 🐛 support page-hide and page-show
- fix: 🐛 not parse querystring when method is GET or HEAD
- fix: 🐛 createAndSavePage params
- fix: 🐛 init lifecycle and method
- fix: 🐛 only create page when \_\_pageConfig exist
- fix: 🐛 create page on worker runtime
- fix: build
- fix: disable webpack-dev-server host check
- fix: improve js compatibility
- fix: improve js compatibility
- fix: prefix component instance id with page id
- fix(rpc): change rpc interface
- fix: 🐛 add recordInstanceBoundEffect
- fix: 🐛 remove effect
- fix: 🐛 computed bind to ctx
- fix: change defualt build format to esm-bundler
- fix: change defualt build format to esm-bundler
- fix(project): fix default format
- fix(project): format package.json
- fix(project): rm .gitkeep & fix deps
- fix: typo
- fix: COMPONENT_TYPE_ID is undefined
- fix: 🐛 build script

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …
- feat(bundler & mpp-service): add bundler-cli & support output .pkg files
- feat(sdk): clear detection when hidden
- feat(demo): update runtime-web-host bundleAll params
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(sdk): framework-storage plugin
- feat(bundler,cli): update bundler log info
- feat(mpp-service): add package mpp-service to tools
- feat(sdk): hotfix-3.7.3-onerror-monitor-upload
- feat(sdk): try catch error in App lifecycle
- feat(sdk): add load pageJS info in timeline logger
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(bundler): move page logic to page.worker.js
- feat(sdk): add startAppLaunch handleAppLaunchCallback in runtimeloger
- feat(demo): preloadRule demo app
- feat(sdk,runtime): file system manger access api sdk,runtime,demo
- feat(cli): add button open-type getUserProfile & getEmailAddress
- feat(sdk): canIUse plugin
- feat(demo): handle error demo
- feat(runtime): remove native-ui
- feat(sdk): add Button open-type attribute getUserProfile
- feat(sdk): add Button open-type attribute openSetting
- feat(sdk): add wallet-connector plugin
- feat(lib): add binary-pkg to bundler
- feat(sdk): add API isLoggedIn & add custom plugin ensure-logged-in
- feat(demo): private-request demo
- feat(runtime): filesystem permission
- feat(sdk): plugin device-orientation-change
- feat: add disableBounces page to demo app
- feat(mp,sdk): file system plugins
- feat: private-request plugin
- feat(sdk): app-rpc logger add event
- feat(mp): buffer-url mp plugin
- feat(sdk): timeLogger-startup add loadAppJs and appLoad
- feat(sdk): native-rpc-logger supprot event
- feat(cli): add support autocomplete feature for DeprecatedInput
- feat(sdk): support confirm event for web input
- feat(sdk,mp): mp,sdk plugin tab bar red dot
- feat(cli & bundler): provide source-map in prod mode
- feat: update blank-page demo with navigate to a new page
- feat: update blank page demo with input
- feat(runtime): on-off plugin
- feat(sdk): add system log label
- feat(sdk): plugins show-leaderboard, cloud-storage
- feat(mp): plugin background-fetch
- feat(runtime): save image to photos album plugin
- feat(bundler): extract base.bxml
- feat(sdk): plugin beforeAppClose api and demo
- feat: add blank-page demo
- feat(sdk): add direction RTL support for native components include native-input
- feat(runtime): clipboard plugin
- feat(sdk): optimize vconsole, lazy load, split log and system panel
- feat(sdk): report plugin
- feat(mp-runtime): add webview plugin
- feat: sync with mono 3.5.0
- feat:
  test([32d06ace](https://git.toolsfdg.net/fe/mini-program/commit/32d06aceb8d95036bc2f28bd72ea4f7347db3db2))
  by ka
- feat: test
- feat: trigger
- feat: failed trigger and do it one more time
- feat: test publish
- feat: modify release script
- feat(Slider): add mp-slider component
- feat: add fallback action handler
- feat: add bn.login
- feat(cli): archive bundle to zip file
- feat(cli): do bundle after taro build
- feat: add downloadFile and requestPayment
- feat: add base component Radio and RadioGroup & fix wrong onChange target id
- feat: add dist -d option
- feat: add bn apis
- feat(taro-plugin): 🎸 add bn typings for taro
- feat(build): add build command in @mp/cli
- feat: 🎸 add cli-init react template
- feat: implement WorkerService with iframe
- feat: add mp-checkbox & mp-checkbox-group
- feat: add action defintions
- feat: 🎸 add options to dev cli
- feat: 🎸 init @mp/cli
- feat: support api cors
- feat: expose rpcworker on dev
- feat: add toast action
- feat: 🎸 change page in app.json from object to array
- feat: enhance request taro
- feat: enhance request taro
- feat: enhance request taro
- feat: 🎸 add set method
- Feature/bundler
- feat(runtime-render): connect mp event to taro event
- feat: enhance request
- feat: add icon
- feat: add mp-text & fix input event
- feat: 🎸 add entry html and update taro plugin
- feat: 🎸 add **cid and **pageConfig to Page function
- feature/bundle
- feat: 🎸 remove isPage logic and add test cases
- feat: 🎸 defineApp and defineComponent
- feat: 🎸 _.config.json => _.json
- feat: 🎸 add \_\_cid to components
- feat: 🎸 add bundleAll method
- feat: 🎸 add merge-page-config-plugin
- feat: 🎸 return empty style and import pages
- feat: 🎸 add bundleApp function
- feat: export renderTaro
- feat: output sdk manifest
- feat: 🎸 add mp-tpl-loader and complete mp-bjs-loader
- feat: 🎸 use mp-bjs-loader
- feat: add mp-switch
- feat: add mp-textarea
- feat: add mp-label
- feat: runner-web-cli
- feat: add onTap
- feat: add mp-input
- feat: 🎸 add @babel/runtime
- feat: 🎸 support css module and scss
- feat: 🎸 clean memfs dir before run each test
- feat: 🎸 set config.optimization and add test cases
- feat: 🎸 extract css files
- feat: 🎸 add webpack-chain and support css files
- feat: 🎸 bundle single page
- feat: 🎸 invoke AppShow before first page loaded
- feat: 🎸 runner: support app-hide & app-show
- feat: 🎸 bn.api
- feat: 🎸 `runner` support navigate-pop and navigate-redirect
- feat: add navigator.redirect
- feat(public-api): init bn
- feat(rpc): add callback error
- feat: add app.js
- feat: 🎸 add multi pages and remove app-launch / page-load event
- feat: 🎸 add page2 and import worker.js on demand
- feat: 🎸 set navigation bar title
- feat: 🎸 add bn.request function
- feat: 🎸 mock native functions
- feat: navigator
- feat: add App and Page
- feat: navigator
- feat(runtime-render): add mp- prefix
- feat(runtime-render): add comments
- feat(runtime-render): update text
- feat(runtime-render): add tap event
- feat: add load and unload method
- feat: 🎸 support tsconfig.json in packages
- feat: 🎸 add @vue/compiler
- feat: multipage runner
- feat: 🎸 compiler init
- feat: add cmd typings
- feat: add runner-web
- feat: queue msg before ready
- feat(event): add event support
- feat: desctroy component when unmounted
- feat: add build watch option and add methods and computed function
- feat: 🎸 support methods and computed functionality
- feat(compiler): add base compile functions
- feat(project): add `dev:all` script
- feat(project): add `dev:all` script
- feat(project): specify format
- feat(project): update `dev:app` scripts
- feat(project): add owners
- feat: add dev script
- feat: use single rpc implementation
- feat: counter demo
- feat: first commit for runtime-\*
- feat: 🎸 add rollup to build runtime bundle
- feat: 🎸 minify code
- feat: 🎸 add rollup to build runtime bundle
- feat(rpc): add webwork rpc & native rpc
- feat(rpc): change names
- feat(rpc): add nativeBridge
- feat(rpc): add nativeBridge
- feat(rpc): fix issue
- feat(rpc): fix issue
- feat(rpc): add createRpcFromWorkerToView
- feat(rpc): add result
- feat(rpc): add createRpcFromViewToWorkder for dev
- feat: define rpc interface

### Refactor

- refactor(sdk): remove locationReadyManager
- refactor(sdk): delete gcanvas useless code
- refactor(demo): move component
- refactor: websocket hostplugin and text-line-height
- refactor: ide plugin login, location, download-package
- refactor: sensor plugin migration
- refactor: move plugins to runtime-plugins
- refactor(demo): mp-web
- refactor: ide plugin migration(error page, preview-image)
- refactor(sdk): optimize logger
- refactor: ide-host plugin migration
- refactor(runtime): redefine definePlugin to support service
- refactor(sdk): refactor plugins
- refactor: plugins migration
- refactor: clean dist of @mp/host
- refactor(runtime): re-export by host itself
- refactor(demo): component transform page
- refactor(sdk): fix plugin migration types errors
- refactor: new DSL demo page - tabbar
- refactor(demo): new component demo based on bxml
- refactor(sdk): migrate choose-image clipboard cloud-storage
- refactor(sdk): migrate plugin-canvas
- refactor(runtime): migrate plugins
- refactor(plugins): plugins -> runtime-plugins
- refactor(sdk): rename directories & fix watch mode
- refactor: remove @mp/runtime-host
- refactor(runtime): migrate plugins from to runtime-plugins
- refactor(sdk): plugins -> runtime-plugins
- refactor(runtime): code quality
- refactor(plugin): migrate internal-plugins
- refactor(runtime): add new desgin for plugin service
- refactor(sdk,runtime): extract internal plugins & fix types for mp-ide
- refactor(sdk,runtime): colocate host plugin & extract @mp/host-core
- refactor: restructure folders
- refactor: unit test of mp runtime
- refactor: rename deviceInfo to viewportInfo
- refactor(runtime): re-export @mp/plugins-mp
- refactor(sdk): add new runtime-core and move plugins to runtime-plugins
- refactor(runtime): rename runtime api
- refactor: runtime re-export
- refactor(runtime): add watch mode
- refactor(runtime): export resolvePublicAsset instead of dirs
- refactor(runtime): remove jump plugin effect
- refactor(runtime): jump plugin
- refactor(runtime): plugin performance-test and fix a bug cause by defaultTargetId is zero
- refactor(runtime): mp-runtime dev mode
- refactor(sdk,runtime): remove rollup warnings and prevent it
- refactor(sdk): use disableBuiltInPlugins options instead of setIsMG
- refactor(mp runtime): mp runtime api
- refactor(runtime): remove useless service
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(sdk): monitor-upload service and plugin
- refactor: update-manager
- refactor(sdk): performance plugin
- refactor: extract fs
- refactor(sdk): share-panel plugin for mp & mg
- refactor: navigation-bar plugin
- refactor: rollup build
- refactor: split action and event
- refactor: separate action and event
- refactor: events -> listeners
- refactor: use cache & proxy
- refactor: bind props with relation
- refactor: rename customevent -> events & emitEvents
- refactor: separate component props into normal props and custom events
- refactor: using async setup to init instance
- refactor: 💡 add webpack utils.ts
- refactor: use $emit event
- refactor: 💡 addStyleRule
- refactor: change action to string from object
- refactor: 💡 ViewManager.\_destroyView
- refactor: remove render.js suffix
- refactor: change page url
- refactor: 💡 change name
- refactor: pass rendererId by context
- refactor: change ready process
- refactor: change native bridge interface
- refactor: 💡 @compiler -> @mp/compiler
- refactor: use single bridge
- refactor: rpc init process
- refactor: update rpc message struct
- refactor: use two bridge to communicate
- refactor: change rpc interface
- refactor: change rpc interface

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)
- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action
- Revert "fix(sdk): update image component from img to div with background-image " (#309)
- Revert "feat(mp-runtime): add webview plugin"
- Revert "feat: 🎸 change page in app.json from object to array " (#119)
- Revert "feat(project): add `dev:all` script " (#21)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1
- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4
- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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
- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs
- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app
- chore(sdk): debug log
- chore(demo): bump qa demo version for radio-issue
- style(demo): add style of public
- docs(bundler): add how to use pkg-cli
- chore: webstudio release public-demo on prod
- build: sync webview demo
- build: sync-demos
- chore: build with bump version from hotfix or local
- chore: webstudio release public-demo on prod
- chore: webstudio release public demo to prod
- chore: rebuild webstudio public-demo
- chore: prepare demo app release
- chore: webstudio test disabledSubpackage
- chore: webstudio test subPackage
- chore: bump version
- docs: mp-host overview
- chore: bump version
- chore: webstudio
- chore: release component-demo
- chore(sdk): delete RendererReady
- Chore/webstudio
- chore: test-webstudio
- chore: add service.ts to files field
- chore(sdk): update local gen-sdk mainfest.json version
- chore: webstudio
- chore: hide migrated pages for testing purpose
- chore: webstudio config
- chore: webstudio config
- chore: webstudio config
- chore: bump version
- chore(sdk): cherrypick 3.10.1 to master
- chore(release): mp-sdk v3.10.0
- chore: bump versions
- chore: image url
- build: issue template
- chore: test webstudio auto submit
- chore: studio publish mp-sdk
- chore: test webstudio
- chore: webstudio demo
- chore: webstudio
- chore: add 1st version of issue templates
- chore(lib): bump versions cause by router query parameter feature
- docs: update documents about how to test plugin
- chore(sdk): cherry pick - delay 30s check app temporary
- chore(sdk): cherry pick 3.9.2 to master
- Merge branch 'master' into release/3.9
- docs: format readme
- chore(sdk): cherry pick 3.9.2 to master
- chore(sdk): cherry pick 3.9.2 to master
- chore: add concurrency script
- chore(release): mp-sdk v3.9.0
- chore: forgot to add .cjs suffix
- chore: fix yarn release script
- chore(demo): migrate component-demo to use cli 2.4.9
- chore: bump npm versions
- chore: add @tarojs/react to dependencies of babel-preset-bmp
- chore(cli): remove useless webpack alias
- docs(runtime): added migration plugin
- chore: bump version
- docs(demo): how to add new feature on new demo app
- chore: bump npm versions
- chore: bump npm versions
- chore: trigger packages republish
- chore(sdk): drop compatibility code isLegacyAppJsLoaded
- chore(doc): update mp-runtime doc troubleshooting
- chore: update automator README & puppeteer package
- docs(sdk): add special cases description
- docs(runtime): test host plugin
- Merge pull request #471 from finley-x/release/3.8
- Merge branch 'master' into release/3.8
- chore: bump npm versions
- chore(release): mp-sdk v3.8.0
- docs: plugin integrate with IDE & release
- chore: add wallet created action
- docs: how to development mp runtime
- docs: add plugin docs
- chore: set --unhandled-rejections=warn with jest to fix unit-test on node16
- chore: add @mp/mp-runtime-shared-plugins
- chore: bump versions
- chore: throw typescript check error
- chore: bump mp-runtime version
- chore: pre commit disallow empty files
- Merge pull request #423 from finley-x/release/3.7.4
- chore(cli): re-trigger bump CLI v2.3.3
- chore: organize mono workspaces
- chore(sdk): release/3.7.3 -> master
- chore(sdk): restore yml
- chore(sdk): restore yml
- test(sdk): logger test update
- chore(release): mp-sdk v3.7.2
- test(runtime): add inner audio unit tests
- chore(sdk): canvas plugins
- test(lib): improve logger unit tests
- ci: commitlint allow multiple scopes
- test(lib): add logger unit tests
- chore(sdk): fix fs plugin demos
- ci: fix commit-lint issue
- chore(sdk): demo for fs and orientation plugin
- chore: bump version to 1.1.0
- chore(sdk): fix Circular dependencies
- chore(cli): downgrade Taro to 3.2.13
- chore(bundler & sdk): move patches to root of workspace
- chore(bundler): add compiler-dom.d.ts
- chore(bundler): use tsc to build bundler
- build: fix cli build & render dev mode
- test: remove jest errors
- build(lib): update runtime-worker-common build script
- test(sdk): fix report test error
- test(sdk): fix report test error
- chore: use tsc to build cli
- chore: logger error caused by navigation-bar
- build: fix validate sdk output & add runtime-worker-common as deps of MP_ONLY
- chore: merge release/3.6
- chore: integrate v3.5.2
- Merge pull request #168 from kami-c/feature/test-ci-5
- Merge pull request #167 from
  fe/\_\_release-mp-sdk_prod_1.0.1_c7aa75d45e4516e684e941c544935c32a862b2ca_1646900584973
- release mp-sdk v1.0.1
- Merge pull request #154 from henry-w/mono-sdk-3.4.0
- moved from mono 3.4.0, add prowjob + config
- Merge pull request #152 from michael-xu/feature/mp-slider
- Merge pull request #151 from myron-li/dev
- Merge pull request #150 from myron-li/dev
- Merge pull request #148 from chengfan-lin/mp-cli-build-bundle-zip
- Merge pull request #149 from myron-li/dev
- Merge pull request #147 from myron-li/dev
- Merge pull request #146 from michael-xu/feature/radio
- update
- Merge pull request #145 from myron-li/refactor-build
- Merge pull request #144 from myron-li/fix-build
- Merge pull request #143 from james-l/feat/patches
- unit the style of module import
- use cross-spwan instead of child_process
- add livereload for dev server
- clean up package.json of cli
- added a link cmd to make it easy to install cli added cli related document
- Merge pull request #142 from michael-xu/fix/origin-bundler-with-path
- do patches before build
- Merge pull request #139 from myron-li/work
- chore: 🤖 update yarn.lock
- Merge pull request #136 from myron-li/html-worker-container
- Merge pull request #135 from luffy-wang/fix-for-debugger
- Merge pull request #131 from myron-li/add-actions
- Merge pull request #126 from myron-li/refactor-rpc
- Merge pull request #125 from myron-li/MYRON-1
- Merge pull request #124 from myron-li/dev
- Merge pull request #97 from michael-xu/feature/custom-event
- Merge pull request #120 from james-l/Feature/watch-mode-bundler
- added exception catching in bundle script of watch mode
- test: 💍 add cid equal test case
- complete w -> watch as watch mode argument
- chore: upgrade vue
- Merge pull request #121 from myron-li/toast
- added the bundler usage to README.md
- add watching mode for bundler
- Merge pull request #117 from myron-li/action
- Merge pull request #109 from luffy-wang/enhance-request
- chore: 🤖 update service assets
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #115 from chengfan-lin/api-taro
- Merge branch 'master' into feature/custom-event
- Merge pull request #114 from bowen-zhu/feature/bundler
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #113 from myron-li/MYRON-1
- chore: fix typo
- Merge pull request #111 from chengfan-lin/api-taro
- Merge pull request #112 from james-l/simplify-taro-plugin
- make bxss generate correct sourcemap when is in development
- simplify taro plugin and make it work as an npm package
- Merge pull request #108 from luffy-wang/add-icon
- Merge pull request #107 from james-l/fix/yarn-command-of-build-taro-plugin
- Merge pull request #106 from myron-li/batch-updated
- optimize: batch setData call
- Merge pull request #105 from michael-xu/feature/components
- Merge pull request #104 from myron-li/optimize
- chore: optimize build
- Merge pull request #103 from bowen-zhu/fix/bunlder
- Merge pull request #102 from james-l/fix/sourcemap-of-css
- dont let bxss generate sourcemap
- Merge pull request #101 from james-l/change-output-of-taro-plugin
- Merge branch 'master' into change-output-of-taro-plugin
- added components definitions of uikit requirements
- test: 💍 add test cases
- use tsc instead of rollup as the packer
- Merge pull request #95 from myron-li/refactor
- add sourcemap to bjs files
- use a modified app loader instead of origin one
- let page's code export via umd
- make output of the page scripts ends with .bjs
- Merge pull request #87 from bowen-zhu/feature/app-bundler
- chore: 🤖 remove bundled files
- chore: 🤖 add todos
- chore: 🤖 rename .tpl -> .bxml
- chore: 🤖 update package.json
- test: 💍 update test cases
- test: 💍 update test cases
- Merge pull request #90 from james-l/Feature/taro-integration
- add components
- Merge pull request #91 from myron-li/custom-event
- chore: custom component
- add code to support lifecycle callback of taro for Page object
- added REDME to taro plugin package
- add taro platform plugin into repository
- Merge pull request #89 from myron-li/bundle-demo
- chore: add example
- Merge pull request #88 from myron-li/rename
- chore: rename
- Merge pull request #84 from myron-li/taro
- chore: 🤖 build bundler by tsc
- Merge pull request #79 from michael-xu/feature/mp-components
- chore: 🤖 split bundler
- Merge pull request #77 from bowen-zhu/feature/bundler
- test: 💍 remove useless test fixtures
- test: 💍 add basic fixtures
- Merge pull request #78 from myron-li/runner
- chore: 🤖 remove unused example
- Merge pull request #74 from bowen-zhu/feature/loader
- test: 💍 add runInDom test function
- chore: 🤖 rename and remove useless code
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- chore: 🤖 setup bundler
- chore: 🤖 add compiler example
- merge upstream master
- chore: update example
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- add weather app demo
- Merge pull request #71 from myron-li/fix-page-hooks
- chore: 🤖 rename types
- Merge pull request #69 from bowen-zhu/feature/runner
- chore: 🤖 types
- chore: 🤖 navigate in worker
- chore: renemae variable
- chore: update example
- chore: rename variables
- Merge pull request #68 from myron-li/navigator-redirect
- Merge pull request #66 from bowen-zhu/fix/runner
- Merge pull request #65 from myron-li/page-url
- Merge pull request #64 from myron-li/app-js
- Merge pull request #60 from bowen-zhu/feature/runner-navigation
- chore: 🤖 remove redundant code
- chore: 🤖 rename function names
- chore: 🤖 add response interface
- chore: 🤖 update types and ui
- Merge pull request #63 from myron-li/integrate-app-and-page
- Merge pull request #57 from myron-li/navigator
- Merge pull request #54 from luffy-wang/add-app
- enhance
- create once only
- Merge pull request #52 from sora-liu/master
- typos
- add createApp and interfaces
- chore: rename pageid to rendererid
- chore: 🤖 update compiler fixture
- Merge pull request #51 from myron-li/init-process
- chore: 🤖 build prod version
- Merge pull request #48 from bowen-zhu/feature/compiler
- chore: 🤖 compiler dir structure
- Merge pull request #46 from myron-li/single-bridge
- Merge pull request #45 from myron-li/multi-page
- refacotr: change rpc message definition
- Merge pull request #44 from myron-li/test
- test: add component test
- Merge pull request #43 from myron-li/setup-test
- chore: setup jest
- Merge pull request #40 from myron-li/fix-compatibility
- Merge pull request #39 from myron-li/format
- Merge pull request #38 from myron-li/compiler-helper
- Merge pull request #37 from myron-li/worker-render-protocol
- Merge pull request #36 from myron-li/update-rpc
- change rpc
- Merge pull request #34 from myron-li/mock-service
- Merge pull request #32 from myron-li/bridge-ready
- Merge pull request #31 from myron-li/multi-bridge
- Merge pull request #30 from luffy-wang/change-rpc
- Merge pull request #27 from myron-li/build-sdk
- chore: add command to generate sdk
- Merge pull request #26 from myron-li/cleanup
- Merge pull request #25 from shenxiang-feng/master
- Merge pull request #23 from luffy-wang/add-compile-functions
- Merge pull request #19 from myron-li/patch
- chore: update readme
- chore: update readme
- Merge pull request #10 from myron-li/dev-script
- chore: 🤖 add todo
- chore: rename packages
- chore: 🤖 project setup
- chore: 🤖 add @types/node
- chore: 🤖 add eslint and prettier
- chore: 🤖 build ts files
- chore: 🤖 add lerna
- init
- wip
- init

## [3.14.5] 2022-11-10

**Download: [SDK-3.14.5](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.5.zip)**

### Bug Fixes

- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works
- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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
- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register
- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type
- fix(sdk): fetch remote tags with force arg when tag conflict
- fix(demo): textarea maxlength caused display issue
- fix(sdk): access methods defined within methods property
- fix(sdk): fix this problem for '\_setDataMaxSize' of undefined
- fix(cli & runtime): useExtendedLib issue
- fix(demo): public-demo textarea bug
- fix(bundler): if directive not work as non-first attribute
- fix(sdk): revert removing of setTimeout hack because of useDidShow issues on IOS
- fix(server-side-bundle): set default value of versionSetting
- fix(runtime): plainText body not supported
- fix(demo): fix crash caused by private request demo
- fix(sdk): bug in OnOffManager and add test
- fix(sdk): revert changes of performance entry name
- fix(demo): callback should not inside function component
- fix(bundler): nested component with directive "for"
- fix(runtime): set different left for title on different lefticon
- fix(mpp-service): remove request body of getApplicationVersions
- fix(sdk): request-timeout
- fix: webstudio qa test
- fix(sdk): tmpl_0_undefined bug lead to a blank page
- fix(sdk): remove 120ms timeout of page show, make sure onShow is before onReady
- fix(sdk): use logger to enable warn log visible
- fix(bundler): disable autoloading postcss config of MP project
- fix(sdk): tmpl_0_undefined issue
- fix(demo): component-demo-public head component click fix
- fix(demo): get appid from systemInfo
- fix(runtime): set title when route-changed
- fix(sdk): add missing @mp/runtime-plugin-sensor-orientation depenedncies
- fix(sdk): page instance option property update
- fix(sdk): from render to worker UIRendererServiceReady
- fix(sdk): use log.error instead of filter text nest component
- fix(demo): route query parameter different handler with encode64
- fix(runtime): load extended lib of specific version
- fix(bundler): require relative path for cocos game
- fix(sdk): reject the previous defer when reLaunch too early
- fix(sdk): adjust MPRunTimeLogger
- fix(sdk): routing api should wait app launched
- fix(automator): api is undefined during first lauch of e2e
- fix(sdk): share-panel not working (#542)
- fix(bundler): copy non-existent files issue
- fix(demo): how to use custom tabbar
- fix(cli): resolve path of react
- fix(sdk): rename package
- fix(runtime): add getBridgeCode to files array
- fix(runtime): remove dependency cycle
- fix(runtime): align fail behaviour of request plugin with wechat
- fix(sdk): cherry pick - timeline check app & hotfix 3.8.2
- fix(bundler): common.bxss is imported twice & release factory after jsModule is required
- fix(sdk): empty subpackages force download action
- fix(runtime): add service.d.ts to npm pack
- fix(cli): update vendors to support node 16
- fix: catch downloadFile fail and remove --unhandled-rejections=warn
- fix(sdk): mg add devicePixelRatio into getSystemInfo api
- fix(sdk): mp canvastouche event payload
- fix(bundler): add globalThis polyfill to page-frame
- fix(sdk): setData in onLoad not working
- fix(cli): fix tarojs version can not found in yarn global action
- fix(sdk): fix timeline order error
- fix(sdk): remove global wx, fix getOpenDataContext placeholder
- fix(sdk): timeline appJs error
- fix(sdk): timeline-update
- fix(cli): debugReact with react-reconciler not works
- fix(sdk): increase gas limit when estiamte gas failed
- fix(runtime): postMessage should wait for ready
- fix(cli): resolve taro presets from installation dir of bmp
- fix(cli): support node 15
- fix(sdk): can-i-use types & injectPrivateApi
- fix(rumtime): support tmp/store/usr http request
- fix(bundler): source-map OOM & repeated refresh in watch mode issues
- fix(sdk): fix onOffManager memory leak for task-style apis
- fix(demo): fix demo for fileSystemManager
- fix(runtime): add Math.ceil when populate gas
- fix(sdk): canvas plugin
- fix(bundler): adjust the order of loading script in page-frame
- fix(bundler): load base.bxml.js earlier than renderer-service.js
- fix(sdk): plugin write file
- fix(sdk): blank page when relaunch in old ios device
- fix(sdk): support cocos
- fix(sdk): app-rpc-logger judge from or to & delete extra log
- fix(sdk): monitor d change to dt & update RuntimeLogger monitor-upload
- fix(sdk): webview not working for the webview using node-bridge
- fix(bundler): load base.bxml.js in head element of page-frame
- fix(sdk): plugin-private-request command
- fix(sdk): add dataset to MPEventTarget
- fix(runtime): onNativeApiRequest able to listen all actions
- fix(sdk): radio and checkbox components
- fix(sdk): ios not support bigint 64
- fix(sdk): sentry + vconsole cause oom
- fix(sdk): fix Android need to tap input twice to focus
- fix(sdk): fix the issue that slider wrap with position: relative container
- fix(mp): fix request cookie setting
- fix(sdk): fix reportEvent with keyword to error
- fix(sdk): timeline startup del loadAppJs
- fix(sdk): DeprecatedInput auto-fill not emit input event
- fix(sdk): fix native input color with autoFocus props
- fix(runtime): storage plugin api not work
- fix(sdk): fix Image style width:100%
- fix(sdk): remove header filed with null value
- fix: add defer for webview context in the node-bridge demo
- fix: create a empty webview if src not provied
- fix(mp): fix tab bar css, red dot api error message
- fix(sdk): fix Image style being overridden and comments using English
- fix(sdk): image can not use width/height: auto with div-bgImg
- fix(sdk): onAppShow not working
- fix(sdk): remove the error of webivew-sdk Unknown Action $ready
- fix(sdk): update image component from img to div with background-image
- fix: framework-load-script has been registed
- fix(sdk): fix View component touchstart twice (#295)
- fix(lib,sdk): fix deprecated-input onInput not working
- fix(runtime): show & hide ToastContainer
- fix(sdk): plugin create native buffer
- fix(sdk): Image and IDECoverImage onload & onerror
- fix(sdk): timelogger error add time
- fix(sdk): debounce update state for native input
- fix(sdk): fix re-launch page not found issue
- fix(runtime): fix storage plugin
- fix(sdk): disable the JS timer for blank page detection
- fix(lib): make bundler generate component code that not override comp…
- fix(runtime): prevent app.js load twice
- fix(sdk): polyfill IntersectionObserver for iOS 12.1 (#237)
- fix: add commit hash to branch name
- Fix: release script
- fix: unexport subscribeLocationChange
- fix: sdk build
- fix the problem that bundler still work when in h5 mode
- fix some dependencies of project template
- fix: use path.resolve
- fix: make form component soft controlled & add missing component map
- fix: use -o
- fix the problem after last commit which make bundle script not work
- fix: normalize page url
- fix: 🐛 overwrite template files
- fix for debugger
- fix: 🐛 add http-proxy-middleware@0.19 in runtime-render
- Fix/fix the request with correct parameters and all other things for mvp2
- fix: send body only for post and put method
- fix: prevent user from scaling view
- fix: remove useless code
- fix(runtime-renderer): fix multiple event binding on same event
- fix: get props and data from parent & rename api
- fix: typo
- fix: use Object.assign
- fix: reduce payload size
- fix: Resolve events from attrs and separate two rpc events
- fix: use eventNames to tell the different if it is a event name or a normal props name
- fix: watch $props
- fix: rename
- fix: watch all props changed
- fix: remove bind props interface
- fix: remove useless code
- fix the problem invoked by packange name changed of taro plugin
- fix: prevent capture event trigger twice
- fix: 🐛 use e.currentTarget
- fix: 🐛 renderTaro and updateData
- fix: 🐛 renderTaro
- fix: keep compatible with taro
- fix: add tapCapture
- fix: add capture event
- fix: update props naming
- fix: remove console.log
- fix: Non-function value encountered for default slot. Prefer function slots for better
  performance.
- fix: remove console.log
- fix: types
- fix: update sdk
- fix: response.data typing
- fix: 🐛 enableCSSModule
- fix: call ready before navigation-push
- fix: typo
- fix: typo
- fix: typo
- fix: change data type
- fix: 🐛 back to list page
- fix: rpc
- fix(runner): rpc message format
- fix(runner): rpc message format
- fix: pass query to page.oLoad
- fix: fix ready and push action order
- fix: page component created twice
- fix: fix page hooks
- fix: 🐛 support page-hide and page-show
- fix: 🐛 not parse querystring when method is GET or HEAD
- fix: 🐛 createAndSavePage params
- fix: 🐛 init lifecycle and method
- fix: 🐛 only create page when \_\_pageConfig exist
- fix: 🐛 create page on worker runtime
- fix: build
- fix: disable webpack-dev-server host check
- fix: improve js compatibility
- fix: improve js compatibility
- fix: prefix component instance id with page id
- fix(rpc): change rpc interface
- fix: 🐛 add recordInstanceBoundEffect
- fix: 🐛 remove effect
- fix: 🐛 computed bind to ctx
- fix: change defualt build format to esm-bundler
- fix: change defualt build format to esm-bundler
- fix(project): fix default format
- fix(project): format package.json
- fix(project): rm .gitkeep & fix deps
- fix: typo
- fix: COMPONENT_TYPE_ID is undefined
- fix: 🐛 build script

### Features

- feat(sdk): add page-frame-resource points
- feat(sdk): shareAppMessage support fallback url
- feat(sdk): generate bytecode for worker-service
- feat(sdk): toDataURL and getuserprofile
- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class
- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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
- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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
- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins
- feat(sdk): improve web3 api
- feat(demo): Standard Benchmark DSL Mini Program for runtimes
- feat(demo): migrate component-demo api to component-demo-public
- feat(sdk): cache promise api until it resolved
- feat(bundler): add file hash to pkg
- feat(sdk): filesystem api - copyfile, unzip
- feat(demo): update radio example code as wechat example
- feat(runtime): assign path to render iframe name
- feat(demo): form view media public demo components
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(demo): release demos in QA env
- feat(cli): support taro prerender
- feat(mpp-service): intergate server-side-bundle
- feat(sdk): open-type getEmailAddress / getPhoneNumber
- feat(demo): share app demo
- feat(sdk): universal link
- feat(extended-lib): export libs info
- feat(bundler): add analyse mode to pkg-cli
- feat(extended-lib): add new package @mp/extended-lib
- feat(bundler): add pkg-cli
- feat(sdk): monitorupload NEZHA_RENDER_PAGE_JS with data-eb
- feat(sdk): setData payload size & remove cocos
- feat(sdk): check TIME_APP by heartbeat scheme
- feat(lib): preload styles bug fix
- feat(demo): migrate theme-context
- feat(bundler): bundler-cli add disabledSubpackages
- feat(mpp-service): upload pkg of mini-program
- feat(sdk): refactor framework-load-script
- feat(demo): update custome event demo
- feat(sdk): ide clipboard plugin migrate
- feat(demo): add getEmailAddress getPhoneNumber demo
- feat(server-side-bundle): upload source-map & source-code
- feat(lib): preload html core
- feat(mpp-service): support auto increase version code & improve error…
- feat(runtime): simulator navigator title left align
- feat(sdk): custom event on/off
- feat(sdk): open-type button support getPhoneNumber, getEmail
- feat(demo): expose base64_encode method example for developers
- feat(sdk): native send event to worker with time
- feat(sdk): renderer send RendererReady to Native
- feat(demo): standalone webview demo
- feat(sdk): add create offscreen canvas api
- feat(sdk): warn if developer call sync api in app & page lifecycle
- feat(runtime,sdk): handle page-not-found and fix onPageNotFound not working
- feat(server-side-bundle): add new package @mp/server-side-bundle
- feat(demo): implement 5 api to component-demo
- feat(demo): component-demo for dsl
- feat(sdk): route query parameters updates
- feat(demo): migrate e2e test
- feat(mpp-service): submit the MiniProgram in audit step
- feat(demo): enterkeyhint of search
- feat(sdk): remote debug support sync rpc
- feat(sdk): remove cocos runtime script from sdk package
- feat(automator): replace puppeteer wiht playwright
- feat(sdk): wallet-connector issue fix
- feat(sdk): text component support decode and space
- feat(sdk): add new rpc action RendererServiceReady
- feat(sdk): add fullyDownloaded to FrameworkDownloadPackage
- feat(demo): webview custom nav demo
- feat(lib): host getImageInfo plugin
- feat(sdk): getImageInfo support relative path
- feat(sdk): add wallet-connector plugin
- feat(bundler) : bxml support relative path
- feat(cli): update deprecated input props
- feat(demo): public demo component migrate
- feat(demo): update wallet connector demo
- feat(demo): include get-image-info demo image files
- feat(demo): component demo public
- feat(runtime): deprecated input support confirm event
- feat(demo): update wallet connector demo
- feat(demo): getImageInfo support absolute path and short path
- feat(demo): add more cases in wallet-connector demo
- feat(cli,doc): modify bundler info for useExtendedLib and update doc troubleshooting
- feat(bundler & runtime): support useExtendedLib
- feat(demo): update the unsupported domain test
- feat: e2e-test
- feat(sdk): hotfix 3.8.1 cherry pick master & restore yml
- feat(sdk): redesign timeline
- feat(sdk): startlocationupdate type
- feat(sdk): image-info plugin
- feat(demo): get-image-info demo
- feat(sdk): add plugin user-info & migrate getUserProfile to action get-user-info-profile
- feat(cli): support externals lib
- feat(playground): add wallet-connector context api
- feat(cli): upgrade tarojs to 3.4.4
- feat(sdk): expose esmoudle of plugin submodule with .mjs
- feat(bundler): empty app.js for drop compatibility & fix independent …
- feat(bundler & mpp-service): add bundler-cli & support output .pkg files
- feat(sdk): clear detection when hidden
- feat(demo): update runtime-web-host bundleAll params
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): hotfix-3.7.6-cherry-pick-to-master timeline update
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(sdk): framework-storage plugin
- feat(bundler,cli): update bundler log info
- feat(mpp-service): add package mpp-service to tools
- feat(sdk): hotfix-3.7.3-onerror-monitor-upload
- feat(sdk): try catch error in App lifecycle
- feat(sdk): add load pageJS info in timeline logger
- feat(sdk): add more info about AppLaunch in runtimeloger
- feat(bundler): move page logic to page.worker.js
- feat(sdk): add startAppLaunch handleAppLaunchCallback in runtimeloger
- feat(demo): preloadRule demo app
- feat(sdk,runtime): file system manger access api sdk,runtime,demo
- feat(cli): add button open-type getUserProfile & getEmailAddress
- feat(sdk): canIUse plugin
- feat(demo): handle error demo
- feat(runtime): remove native-ui
- feat(sdk): add Button open-type attribute getUserProfile
- feat(sdk): add Button open-type attribute openSetting
- feat(sdk): add wallet-connector plugin
- feat(lib): add binary-pkg to bundler
- feat(sdk): add API isLoggedIn & add custom plugin ensure-logged-in
- feat(demo): private-request demo
- feat(runtime): filesystem permission
- feat(sdk): plugin device-orientation-change
- feat: add disableBounces page to demo app
- feat(mp,sdk): file system plugins
- feat: private-request plugin
- feat(sdk): app-rpc logger add event
- feat(mp): buffer-url mp plugin
- feat(sdk): timeLogger-startup add loadAppJs and appLoad
- feat(sdk): native-rpc-logger supprot event
- feat(cli): add support autocomplete feature for DeprecatedInput
- feat(sdk): support confirm event for web input
- feat(sdk,mp): mp,sdk plugin tab bar red dot
- feat(cli & bundler): provide source-map in prod mode
- feat: update blank-page demo with navigate to a new page
- feat: update blank page demo with input
- feat(runtime): on-off plugin
- feat(sdk): add system log label
- feat(sdk): plugins show-leaderboard, cloud-storage
- feat(mp): plugin background-fetch
- feat(runtime): save image to photos album plugin
- feat(bundler): extract base.bxml
- feat(sdk): plugin beforeAppClose api and demo
- feat: add blank-page demo
- feat(sdk): add direction RTL support for native components include native-input
- feat(runtime): clipboard plugin
- feat(sdk): optimize vconsole, lazy load, split log and system panel
- feat(sdk): report plugin
- feat(mp-runtime): add webview plugin
- feat: sync with mono 3.5.0
- feat:
  test([32d06ace](https://git.toolsfdg.net/fe/mini-program/commit/32d06aceb8d95036bc2f28bd72ea4f7347db3db2))
  by ka
- feat: test
- feat: trigger
- feat: failed trigger and do it one more time
- feat: test publish
- feat: modify release script
- feat(Slider): add mp-slider component
- feat: add fallback action handler
- feat: add bn.login
- feat(cli): archive bundle to zip file
- feat(cli): do bundle after taro build
- feat: add downloadFile and requestPayment
- feat: add base component Radio and RadioGroup & fix wrong onChange target id
- feat: add dist -d option
- feat: add bn apis
- feat(taro-plugin): 🎸 add bn typings for taro
- feat(build): add build command in @mp/cli
- feat: 🎸 add cli-init react template
- feat: implement WorkerService with iframe
- feat: add mp-checkbox & mp-checkbox-group
- feat: add action defintions
- feat: 🎸 add options to dev cli
- feat: 🎸 init @mp/cli
- feat: support api cors
- feat: expose rpcworker on dev
- feat: add toast action
- feat: 🎸 change page in app.json from object to array
- feat: enhance request taro
- feat: enhance request taro
- feat: enhance request taro
- feat: 🎸 add set method
- Feature/bundler
- feat(runtime-render): connect mp event to taro event
- feat: enhance request
- feat: add icon
- feat: add mp-text & fix input event
- feat: 🎸 add entry html and update taro plugin
- feat: 🎸 add **cid and **pageConfig to Page function
- feature/bundle
- feat: 🎸 remove isPage logic and add test cases
- feat: 🎸 defineApp and defineComponent
- feat: 🎸 _.config.json => _.json
- feat: 🎸 add \_\_cid to components
- feat: 🎸 add bundleAll method
- feat: 🎸 add merge-page-config-plugin
- feat: 🎸 return empty style and import pages
- feat: 🎸 add bundleApp function
- feat: export renderTaro
- feat: output sdk manifest
- feat: 🎸 add mp-tpl-loader and complete mp-bjs-loader
- feat: 🎸 use mp-bjs-loader
- feat: add mp-switch
- feat: add mp-textarea
- feat: add mp-label
- feat: runner-web-cli
- feat: add onTap
- feat: add mp-input
- feat: 🎸 add @babel/runtime
- feat: 🎸 support css module and scss
- feat: 🎸 clean memfs dir before run each test
- feat: 🎸 set config.optimization and add test cases
- feat: 🎸 extract css files
- feat: 🎸 add webpack-chain and support css files
- feat: 🎸 bundle single page
- feat: 🎸 invoke AppShow before first page loaded
- feat: 🎸 runner: support app-hide & app-show
- feat: 🎸 bn.api
- feat: 🎸 `runner` support navigate-pop and navigate-redirect
- feat: add navigator.redirect
- feat(public-api): init bn
- feat(rpc): add callback error
- feat: add app.js
- feat: 🎸 add multi pages and remove app-launch / page-load event
- feat: 🎸 add page2 and import worker.js on demand
- feat: 🎸 set navigation bar title
- feat: 🎸 add bn.request function
- feat: 🎸 mock native functions
- feat: navigator
- feat: add App and Page
- feat: navigator
- feat(runtime-render): add mp- prefix
- feat(runtime-render): add comments
- feat(runtime-render): update text
- feat(runtime-render): add tap event
- feat: add load and unload method
- feat: 🎸 support tsconfig.json in packages
- feat: 🎸 add @vue/compiler
- feat: multipage runner
- feat: 🎸 compiler init
- feat: add cmd typings
- feat: add runner-web
- feat: queue msg before ready
- feat(event): add event support
- feat: desctroy component when unmounted
- feat: add build watch option and add methods and computed function
- feat: 🎸 support methods and computed functionality
- feat(compiler): add base compile functions
- feat(project): add `dev:all` script
- feat(project): add `dev:all` script
- feat(project): specify format
- feat(project): update `dev:app` scripts
- feat(project): add owners
- feat: add dev script
- feat: use single rpc implementation
- feat: counter demo
- feat: first commit for runtime-\*
- feat: 🎸 add rollup to build runtime bundle
- feat: 🎸 minify code
- feat: 🎸 add rollup to build runtime bundle
- feat(rpc): add webwork rpc & native rpc
- feat(rpc): change names
- feat(rpc): add nativeBridge
- feat(rpc): add nativeBridge
- feat(rpc): fix issue
- feat(rpc): fix issue
- feat(rpc): add createRpcFromWorkerToView
- feat(rpc): add result
- feat(rpc): add createRpcFromViewToWorkder for dev
- feat: define rpc interface

### Refactor

- refactor(sdk): remove locationReadyManager
- refactor(sdk): delete gcanvas useless code
- refactor(demo): move component
- refactor: websocket hostplugin and text-line-height
- refactor: ide plugin login, location, download-package
- refactor: sensor plugin migration
- refactor: move plugins to runtime-plugins
- refactor(demo): mp-web
- refactor: ide plugin migration(error page, preview-image)
- refactor(sdk): optimize logger
- refactor: ide-host plugin migration
- refactor(runtime): redefine definePlugin to support service
- refactor(sdk): refactor plugins
- refactor: plugins migration
- refactor: clean dist of @mp/host
- refactor(runtime): re-export by host itself
- refactor(demo): component transform page
- refactor(sdk): fix plugin migration types errors
- refactor: new DSL demo page - tabbar
- refactor(demo): new component demo based on bxml
- refactor(sdk): migrate choose-image clipboard cloud-storage
- refactor(sdk): migrate plugin-canvas
- refactor(runtime): migrate plugins
- refactor(plugins): plugins -> runtime-plugins
- refactor(sdk): rename directories & fix watch mode
- refactor: remove @mp/runtime-host
- refactor(runtime): migrate plugins from to runtime-plugins
- refactor(sdk): plugins -> runtime-plugins
- refactor(runtime): code quality
- refactor(plugin): migrate internal-plugins
- refactor(runtime): add new desgin for plugin service
- refactor(sdk,runtime): extract internal plugins & fix types for mp-ide
- refactor(sdk,runtime): colocate host plugin & extract @mp/host-core
- refactor: restructure folders
- refactor: unit test of mp runtime
- refactor: rename deviceInfo to viewportInfo
- refactor(runtime): re-export @mp/plugins-mp
- refactor(sdk): add new runtime-core and move plugins to runtime-plugins
- refactor(runtime): rename runtime api
- refactor: runtime re-export
- refactor(runtime): add watch mode
- refactor(runtime): export resolvePublicAsset instead of dirs
- refactor(runtime): remove jump plugin effect
- refactor(runtime): jump plugin
- refactor(runtime): plugin performance-test and fix a bug cause by defaultTargetId is zero
- refactor(runtime): mp-runtime dev mode
- refactor(sdk,runtime): remove rollup warnings and prevent it
- refactor(sdk): use disableBuiltInPlugins options instead of setIsMG
- refactor(mp runtime): mp runtime api
- refactor(runtime): remove useless service
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(runtime): move service plugin to IDE
- refactor(sdk): monitor-upload service and plugin
- refactor: update-manager
- refactor(sdk): performance plugin
- refactor: extract fs
- refactor(sdk): share-panel plugin for mp & mg
- refactor: navigation-bar plugin
- refactor: rollup build
- refactor: split action and event
- refactor: separate action and event
- refactor: events -> listeners
- refactor: use cache & proxy
- refactor: bind props with relation
- refactor: rename customevent -> events & emitEvents
- refactor: separate component props into normal props and custom events
- refactor: using async setup to init instance
- refactor: 💡 add webpack utils.ts
- refactor: use $emit event
- refactor: 💡 addStyleRule
- refactor: change action to string from object
- refactor: 💡 ViewManager.\_destroyView
- refactor: remove render.js suffix
- refactor: change page url
- refactor: 💡 change name
- refactor: pass rendererId by context
- refactor: change ready process
- refactor: change native bridge interface
- refactor: 💡 @compiler -> @mp/compiler
- refactor: use single bridge
- refactor: rpc init process
- refactor: update rpc message struct
- refactor: use two bridge to communicate
- refactor: change rpc interface
- refactor: change rpc interface

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)
- revert(sdk): revert getPhoneNumber/getEmailAddress feature because IOS not ready yet
- revert(sdk): rollback to use the old get-user-profile action
- Revert "fix(sdk): update image component from img to div with background-image " (#309)
- Revert "feat(mp-runtime): add webview plugin"
- Revert "feat: 🎸 change page in app.json from object to array " (#119)
- Revert "feat(project): add `dev:all` script " (#21)

### Internal

- chore(cicd): yaml files
- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4
- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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
- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs
- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app
- chore(sdk): debug log
- chore(demo): bump qa demo version for radio-issue
- style(demo): add style of public
- docs(bundler): add how to use pkg-cli
- chore: webstudio release public-demo on prod
- build: sync webview demo
- build: sync-demos
- chore: build with bump version from hotfix or local
- chore: webstudio release public-demo on prod
- chore: webstudio release public demo to prod
- chore: rebuild webstudio public-demo
- chore: prepare demo app release
- chore: webstudio test disabledSubpackage
- chore: webstudio test subPackage
- chore: bump version
- docs: mp-host overview
- chore: bump version
- chore: webstudio
- chore: release component-demo
- chore(sdk): delete RendererReady
- Chore/webstudio
- chore: test-webstudio
- chore: add service.ts to files field
- chore(sdk): update local gen-sdk mainfest.json version
- chore: webstudio
- chore: hide migrated pages for testing purpose
- chore: webstudio config
- chore: webstudio config
- chore: webstudio config
- chore: bump version
- chore(sdk): cherrypick 3.10.1 to master
- chore(release): mp-sdk v3.10.0
- chore: bump versions
- chore: image url
- build: issue template
- chore: test webstudio auto submit
- chore: studio publish mp-sdk
- chore: test webstudio
- chore: webstudio demo
- chore: webstudio
- chore: add 1st version of issue templates
- chore(lib): bump versions cause by router query parameter feature
- docs: update documents about how to test plugin
- chore(sdk): cherry pick - delay 30s check app temporary
- chore(sdk): cherry pick 3.9.2 to master
- Merge branch 'master' into release/3.9
- docs: format readme
- chore(sdk): cherry pick 3.9.2 to master
- chore(sdk): cherry pick 3.9.2 to master
- chore: add concurrency script
- chore(release): mp-sdk v3.9.0
- chore: forgot to add .cjs suffix
- chore: fix yarn release script
- chore(demo): migrate component-demo to use cli 2.4.9
- chore: bump npm versions
- chore: add @tarojs/react to dependencies of babel-preset-bmp
- chore(cli): remove useless webpack alias
- docs(runtime): added migration plugin
- chore: bump version
- docs(demo): how to add new feature on new demo app
- chore: bump npm versions
- chore: bump npm versions
- chore: trigger packages republish
- chore(sdk): drop compatibility code isLegacyAppJsLoaded
- chore(doc): update mp-runtime doc troubleshooting
- chore: update automator README & puppeteer package
- docs(sdk): add special cases description
- docs(runtime): test host plugin
- Merge pull request #471 from finley-x/release/3.8
- Merge branch 'master' into release/3.8
- chore: bump npm versions
- chore(release): mp-sdk v3.8.0
- docs: plugin integrate with IDE & release
- chore: add wallet created action
- docs: how to development mp runtime
- docs: add plugin docs
- chore: set --unhandled-rejections=warn with jest to fix unit-test on node16
- chore: add @mp/mp-runtime-shared-plugins
- chore: bump versions
- chore: throw typescript check error
- chore: bump mp-runtime version
- chore: pre commit disallow empty files
- Merge pull request #423 from finley-x/release/3.7.4
- chore(cli): re-trigger bump CLI v2.3.3
- chore: organize mono workspaces
- chore(sdk): release/3.7.3 -> master
- chore(sdk): restore yml
- chore(sdk): restore yml
- test(sdk): logger test update
- chore(release): mp-sdk v3.7.2
- test(runtime): add inner audio unit tests
- chore(sdk): canvas plugins
- test(lib): improve logger unit tests
- ci: commitlint allow multiple scopes
- test(lib): add logger unit tests
- chore(sdk): fix fs plugin demos
- ci: fix commit-lint issue
- chore(sdk): demo for fs and orientation plugin
- chore: bump version to 1.1.0
- chore(sdk): fix Circular dependencies
- chore(cli): downgrade Taro to 3.2.13
- chore(bundler & sdk): move patches to root of workspace
- chore(bundler): add compiler-dom.d.ts
- chore(bundler): use tsc to build bundler
- build: fix cli build & render dev mode
- test: remove jest errors
- build(lib): update runtime-worker-common build script
- test(sdk): fix report test error
- test(sdk): fix report test error
- chore: use tsc to build cli
- chore: logger error caused by navigation-bar
- build: fix validate sdk output & add runtime-worker-common as deps of MP_ONLY
- chore: merge release/3.6
- chore: integrate v3.5.2
- Merge pull request #168 from kami-c/feature/test-ci-5
- Merge pull request #167 from
  fe/\_\_release-mp-sdk_prod_1.0.1_c7aa75d45e4516e684e941c544935c32a862b2ca_1646900584973
- release mp-sdk v1.0.1
- Merge pull request #154 from henry-w/mono-sdk-3.4.0
- moved from mono 3.4.0, add prowjob + config
- Merge pull request #152 from michael-xu/feature/mp-slider
- Merge pull request #151 from myron-li/dev
- Merge pull request #150 from myron-li/dev
- Merge pull request #148 from chengfan-lin/mp-cli-build-bundle-zip
- Merge pull request #149 from myron-li/dev
- Merge pull request #147 from myron-li/dev
- Merge pull request #146 from michael-xu/feature/radio
- update
- Merge pull request #145 from myron-li/refactor-build
- Merge pull request #144 from myron-li/fix-build
- Merge pull request #143 from james-l/feat/patches
- unit the style of module import
- use cross-spwan instead of child_process
- add livereload for dev server
- clean up package.json of cli
- added a link cmd to make it easy to install cli added cli related document
- Merge pull request #142 from michael-xu/fix/origin-bundler-with-path
- do patches before build
- Merge pull request #139 from myron-li/work
- chore: 🤖 update yarn.lock
- Merge pull request #136 from myron-li/html-worker-container
- Merge pull request #135 from luffy-wang/fix-for-debugger
- Merge pull request #131 from myron-li/add-actions
- Merge pull request #126 from myron-li/refactor-rpc
- Merge pull request #125 from myron-li/MYRON-1
- Merge pull request #124 from myron-li/dev
- Merge pull request #97 from michael-xu/feature/custom-event
- Merge pull request #120 from james-l/Feature/watch-mode-bundler
- added exception catching in bundle script of watch mode
- test: 💍 add cid equal test case
- complete w -> watch as watch mode argument
- chore: upgrade vue
- Merge pull request #121 from myron-li/toast
- added the bundler usage to README.md
- add watching mode for bundler
- Merge pull request #117 from myron-li/action
- Merge pull request #109 from luffy-wang/enhance-request
- chore: 🤖 update service assets
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #115 from chengfan-lin/api-taro
- Merge branch 'master' into feature/custom-event
- Merge pull request #114 from bowen-zhu/feature/bundler
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program into enhance-request
- Merge pull request #113 from myron-li/MYRON-1
- chore: fix typo
- Merge pull request #111 from chengfan-lin/api-taro
- Merge pull request #112 from james-l/simplify-taro-plugin
- make bxss generate correct sourcemap when is in development
- simplify taro plugin and make it work as an npm package
- Merge pull request #108 from luffy-wang/add-icon
- Merge pull request #107 from james-l/fix/yarn-command-of-build-taro-plugin
- Merge pull request #106 from myron-li/batch-updated
- optimize: batch setData call
- Merge pull request #105 from michael-xu/feature/components
- Merge pull request #104 from myron-li/optimize
- chore: optimize build
- Merge pull request #103 from bowen-zhu/fix/bunlder
- Merge pull request #102 from james-l/fix/sourcemap-of-css
- dont let bxss generate sourcemap
- Merge pull request #101 from james-l/change-output-of-taro-plugin
- Merge branch 'master' into change-output-of-taro-plugin
- added components definitions of uikit requirements
- test: 💍 add test cases
- use tsc instead of rollup as the packer
- Merge pull request #95 from myron-li/refactor
- add sourcemap to bjs files
- use a modified app loader instead of origin one
- let page's code export via umd
- make output of the page scripts ends with .bjs
- Merge pull request #87 from bowen-zhu/feature/app-bundler
- chore: 🤖 remove bundled files
- chore: 🤖 add todos
- chore: 🤖 rename .tpl -> .bxml
- chore: 🤖 update package.json
- test: 💍 update test cases
- test: 💍 update test cases
- Merge pull request #90 from james-l/Feature/taro-integration
- add components
- Merge pull request #91 from myron-li/custom-event
- chore: custom component
- add code to support lifecycle callback of taro for Page object
- added REDME to taro plugin package
- add taro platform plugin into repository
- Merge pull request #89 from myron-li/bundle-demo
- chore: add example
- Merge pull request #88 from myron-li/rename
- chore: rename
- Merge pull request #84 from myron-li/taro
- chore: 🤖 build bundler by tsc
- Merge pull request #79 from michael-xu/feature/mp-components
- chore: 🤖 split bundler
- Merge pull request #77 from bowen-zhu/feature/bundler
- test: 💍 remove useless test fixtures
- test: 💍 add basic fixtures
- Merge pull request #78 from myron-li/runner
- chore: 🤖 remove unused example
- Merge pull request #74 from bowen-zhu/feature/loader
- test: 💍 add runInDom test function
- chore: 🤖 rename and remove useless code
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- chore: 🤖 setup bundler
- chore: 🤖 add compiler example
- merge upstream master
- chore: update example
- Merge branch 'master' of https://git.toolsfdg.net/fe/mini-program
- add weather app demo
- Merge pull request #71 from myron-li/fix-page-hooks
- chore: 🤖 rename types
- Merge pull request #69 from bowen-zhu/feature/runner
- chore: 🤖 types
- chore: 🤖 navigate in worker
- chore: renemae variable
- chore: update example
- chore: rename variables
- Merge pull request #68 from myron-li/navigator-redirect
- Merge pull request #66 from bowen-zhu/fix/runner
- Merge pull request #65 from myron-li/page-url
- Merge pull request #64 from myron-li/app-js
- Merge pull request #60 from bowen-zhu/feature/runner-navigation
- chore: 🤖 remove redundant code
- chore: 🤖 rename function names
- chore: 🤖 add response interface
- chore: 🤖 update types and ui
- Merge pull request #63 from myron-li/integrate-app-and-page
- Merge pull request #57 from myron-li/navigator
- Merge pull request #54 from luffy-wang/add-app
- enhance
- create once only
- Merge pull request #52 from sora-liu/master
- typos
- add createApp and interfaces
- chore: rename pageid to rendererid
- chore: 🤖 update compiler fixture
- Merge pull request #51 from myron-li/init-process
- chore: 🤖 build prod version
- Merge pull request #48 from bowen-zhu/feature/compiler
- chore: 🤖 compiler dir structure
- Merge pull request #46 from myron-li/single-bridge
- Merge pull request #45 from myron-li/multi-page
- refacotr: change rpc message definition
- Merge pull request #44 from myron-li/test
- test: add component test
- Merge pull request #43 from myron-li/setup-test
- chore: setup jest
- Merge pull request #40 from myron-li/fix-compatibility
- Merge pull request #39 from myron-li/format
- Merge pull request #38 from myron-li/compiler-helper
- Merge pull request #37 from myron-li/worker-render-protocol
- Merge pull request #36 from myron-li/update-rpc
- change rpc
- Merge pull request #34 from myron-li/mock-service
- Merge pull request #32 from myron-li/bridge-ready
- Merge pull request #31 from myron-li/multi-bridge
- Merge pull request #30 from luffy-wang/change-rpc
- Merge pull request #27 from myron-li/build-sdk
- chore: add command to generate sdk
- Merge pull request #26 from myron-li/cleanup
- Merge pull request #25 from shenxiang-feng/master
- Merge pull request #23 from luffy-wang/add-compile-functions
- Merge pull request #19 from myron-li/patch
- chore: update readme
- chore: update readme
- Merge pull request #10 from myron-li/dev-script
- chore: 🤖 add todo
- chore: rename packages
- chore: 🤖 project setup
- chore: 🤖 add @types/node
- chore: 🤖 add eslint and prettier
- chore: 🤖 build ts files
- chore: 🤖 add lerna
- init
- wip
- init

## [3.14.5] 2022-11-09

**Download: [SDK-3.14.5](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.5.zip)**

### Features

- feat(sdk): add page-frame-resource points

## [4.0.1] 2022-11-04

**Download: [SDK-4.0.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.1.zip)**

### Bug Fixes

- fix(sdk): env undefined

### Internal

- chore(cicd): yaml files

## [3.14.4] 2022-11-03

**Download: [SDK-3.14.4](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.4.zip)**

### Features

- feat(sdk): shareAppMessage support fallback url

### Internal

- chore(cicd): yaml files

## [4.0.0] 2022-10-25

**Download: [SDK-4.0.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-4.0.0.zip)**

### Bug Fixes

- fix(demo): update webgl demo with rgba
- fix(demo): payment request use success callback instead
- fix(sdk): useNativeImage
- fix(mpp-service): copy source-code ignore node_module & hidden files
- fix(sdk): fix image and keep **MP_WARN_DEPRECATED**
- fix(sdk): gcanvas toDataURL and audio time update event
- fix(server-side-bundle): upload bytecode pkg issue
- fix(sdk): getUserProfile mini game doesn't need check tap event
- fix(demo): native input width zero in android when container is a flex box
- fix(sdk): reuqest text no response
- fix(bundler): update dependencies to fix pkg-cli
- fix(bundler): support error stack link jump of dev mode page.worker.js

### Features

- feat(sdk): support multiple intersectionObserver
- feat(sdk): navigateTo add target external
- feat(sdk): update canIUse for new api
- feat(runtime): downloa-package add two fields
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
- feat(sdk): generate bytecode for worker-service
- feat(sdk): gcanvas buffer data optimize
- feat: native image
- feat(bundler): add new package node-qjsc
- feat(sdk): getAppBaseInfo & getWindowInfo & getDeviceInfo
- feat(runtime): expose updateBackground of create webview service for ide
- feat(sdk): $renderer-ready action
- feat(sdk): loadScriptSync method

### Misc

- Revert "Revert "refactor(sdk): remove locationReadyManager " (#888)" (#929)

### Internal

- chore(changelog): update changelog for version v3.14.3
- chore(changelog): update changelog for version v4.0.0-dev.3
- chore(runtime): add currentSize filed
- chore: update public demo
- chore(sdk): automator package rename
- chore(changelog): update changelog for version v4.0.0-dev.2
- chore(changelog): update changelog for version v3.14.2
- chore: update public demo
- chore: component-demo
- chore: bump npm versions
- chore(changelog): update changelog for version v4.0.0-dev.1
- chore(changelog): update changelog for version v3.14.1

## [3.14.3] 2022-10-24

**Download: [SDK-3.14.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.3.zip)**

### Features

- feat(sdk): generate bytecode for worker-service

## [3.14.2] 2022-10-17

**Download: [SDK-3.14.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.2.zip)**

### Features

- feat(sdk): toDataURL and getuserprofile

## [3.14.1] 2022-10-05

**Download: [SDK-3.14.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.1.zip)**

### Bug Fixes

- fix(demo): fix benchmark
- fix(sdk, demo): check promise polyfill by using \_\_\_mp_polyfill
- fix(demo): public demo read file
- fix(sdk): native-cover-view not work when using taro
- fix(demo): two-fa demo scene data is undefined
- fix(demo): pull down refresh not works

### Features

- feat(sdk): chainId should be number when pass to native
- feat(demo): add promise polyfill demo for QA regression
- feat: web host cli
- feat(demo): release demo on QA env
- feat(cli): cover-view support hover-class

### Internal

- chore(changelog): update changelog for version v3.14.0
- chore(changelog): update changelog for version v3.14.0-dev.4

## [3.14.0] 2022-09-29

**Download: [SDK-3.14.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.14.0.zip)**

### Bug Fixes

- fix(sdk): cache promise online with polyfill
- fix(sdk): mini game audio adapter
- fix: disable ed and add @deprecated flag
- fix(sdk): changelog issue
- fix(sdk): callbackId could be zero
- fix(sdk): input scrollbar css issue on android
- fix(sdk): isCache undefined issue
- fix(mpp-service): fix status api empty fail message
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

- feat(demo): improve twoFa demo
- feat(demo): remove webauthn demo
- feat(bundler): add statistics mode to pkg-cli & feat(mpp-service): support config msv
- feat(sdk,demo): add private fps api and benchmark for render fps
- feat(sdk): cache promise reject handler
- feat(sdk): getperformance-evaluateScript
- feat(lib): add promise polyfill source code and descreption
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

### Refactor

- refactor(sdk): remove locationReadyManager

### Performance Improvements

- perf: app-rpc msg encoder
- perf: pre-create worker
- perf(sdk): use local js-sha3

### Misc

- Revert "refactor(sdk): remove locationReadyManager " (#888)
- Revert "fix: cherry-pick cachePromise of getSystemInfo " (#867)

### Internal

- chore(changelog): update changelog for version v3.13.3
- chore(changelog): update changelog for version v3.14.0-dev.3
- chore(changelog): update changelog for version v3.14.0-dev.2
- chore(changelog): update changelog for version v3.14.0-dev.1
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

## [3.13.3] 2022-09-26

**Download: [SDK-3.13.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.3.zip)**

### Features

- feat(sdk): android cache promise

## [3.13.2] 2022-09-20

**Download: [SDK-3.13.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.2.zip)**

### Misc

- Revert "fix(sdk): cache promise for getSystemInfo " (#866)

## [3.13.1] 2022-09-16

**Download: [SDK-3.13.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.1.zip)**

### Bug Fixes

- fix(sdk): cache promise for getSystemInfo
- fix(sdk): requestAnimationFrame NaN

## [3.13.0] 2022-09-02

**Download: [SDK-3.13.0](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.13.0.zip)**

### Bug Fixes

- fix(sdk): delete useless report
- fix(sdk): loading when expect route-change type
- fix(sdk): remove cachePromise to fix ios 13 eventloop issue
- fix(sdk): fix: fix to signature error when include specific data struct issue
- fix(sdk): remove type check in wallet-connect plugin
- fix(sdk): gcanvas texImage2D flushnative
- fix(sdk): fix taskify cache fail
- fix(sdk): remove canvas service code
- fix(sdk): fix applaunch-getPerformance
- fix(sdk): fix webview sdk
- fix(mpp-service): publish issue
- fix(sdk): fix mg api host register

### Features

- feat(mpp-service): output hostQrcode to a file
- feat(sdk): sdk-loading
- feat(lib): remote-debug new action & ignore native side delay error
- feat(sdk): create webview sdk & demo
- feat(runtime): disable click when loading display
- feat(sdk): gcanvas supports cocos
- feat(bundler): use zlib to compress pkg
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

- docs: changelog for hotfix 3.12.2
- chore(changelog): update changelog for version v3.12.3
- chore(changelog): update changelog for version v3.13.0-dev.5
- chore(changelog): update changelog for version v3.13.0-dev.4
- chore(changelog): update changelog for version v3.13.0-dev.3
- chore(changelog): update changelog for version v3.13.0-dev.2
- docs(sdk): components docs
- chore: changelog automation
- docs(sdk): view & text components docs
- chore(sdk): getperformance update
- test: taskify-unit-test
- chore: deploy extended-lib to prod env
- docs: add typedoc doc to generate plugin docs

## [3.12.3] 2022-09-01

**Download: [SDK-3.12.3](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.3.zip)**

### Bug Fixes

- fix(sdk): iOS 13.8 promise eventloop issue

### Internal

- chore: changelog automation (#808)

## [3.12.2] 2022-08-31

**Download: [SDK-3.12.2](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.2.zip)**

### Bug Fixes

- fix(sdk): fix taskify cache fail

## [3.12.1] 2022-08-12

**Download: [SDK-3.12.1](https://ftp.binance.com/mp-sdk/prod/mp-sdk-3.12.1.zip)**

### Bug Fixes

- fix(sdk): navigateBackMiniProgram extra data should transform to string
- fix(sdk): fix blank screen issue when relaunch because of taskify
- fix(demo): public demo
- fix(sdk): getCurrentPages error handler
- fix(demo): textarea confirm-type

### Features

- feat(sdk): add mt_start when monitorupload setdata
- feat(extended-lib): integrate distribution API (test on dev env)
- feat(cli): support plugins

### Internal

- chore: test publish @mp/extended-lib on QA env
- chore(demo): release prod demos
- chore: publish @mp/extended-lib
- chore(demo): bump component-demo-public prod version
- chore(demo): release improve web3 api feature with component-demo app