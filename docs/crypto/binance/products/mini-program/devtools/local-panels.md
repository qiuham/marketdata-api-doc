---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/devtools/local-panels
api_type: Guide
updated_at: 2026-11-20 18:39:48.668080
---

# Local Panels

With the introduction of Binance devTools 2.19.0 came new features, specifically, the mock data
panel and audit panel.

## Audit

### Instructions

The audit panel reviews your mini app's implementations, delivering an estimation score indicative
of its adherence to best practices.

With the latest version of Binance DevTools, new tools have been introduced to assist developers in
applying best practices to their mini programs.

The Audit Panel can be used to measure just how closely your mini program adheres to suggested
methods for optimizing performance and user experience.

### Basic Usage

1. Click the **Run** button at the top-left (pictured below) and perform functions on the Mini
   Program interface. Upon running, the page will be scrutinized for "Experience Rating".

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/audits-panel-run.png)

2. Click **Stop** to cease the analysis, whereby an analysis report will appear, which you can use
   to refine your setup.
3. If you want to rerun the experience rating, click **Clear experience rating** at the top of the
   report to reset. Do bear in mind that the system doesn't currently support report storage
   services. Once experience ratings have been cleared, they are no longer viewable.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/audits-panel-clear.png)

## Mock

The mock data panel allows developers to mock all of the JS APIs of mini programs, making it
possible to debug all features, especially those requiring native capabilities on the devtools,
thereby saving significant development time.

In the interests of facilitating small program development, the developer tool offers API Mock
capability, simulating the calling results of some APIs.

### Instructions

### Basic Usage

Find the entry for Mock in the Tab at the top of the tool debug panel and click + New Rule.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-add.png)

Example rule:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-example-rule.png)

Result of hitting the rule above:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-resault.png)

### Rule Priority

When multiple rules are set up for an API, the first rule will be matched first. Once a rule is hit,
subsequent rules will not be executed.

### Data Templates

Complex simulated data needs can be served by data templates, designed for rapid generation of data
to your specifications.

_The syntax of the data template is from the open-source library
[Mock.js](https://github.com/nuysoft/Mock/wiki/Syntax-Specification). For detailed syntax, review
the project documentation._

Data previews are generated in real-time from the template in the template editor, aiding
confirmation of the template's accuracy.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-template-data.png)

### Rule Import and Export

If you need to share rules with other project members, you can export the rule configuration in
Mock, and then send the configuration file to other members for them to import. The operational
entry is shown below:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-share-rule.png)

#### Example

Here's a getSystemInfoSync example of the import & export feature. It consists of three steps:

- Create `getSystemInfoSync` mock Rules.
- Export the rules as a config file to a local folder.
- Import the local config file saved earlier in another project. You can use the append or cover
  mode to import the rules file.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-1.jpg)
![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-2.jpg)
![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-3.jpg)

## Code Quality

The latest version of Binance DevTools offers new tools designed to assist developers in applying
best practices to their mini programs.

The Code Quality Panel allows you to scan your mini-program project and receive suggestions about
resource sizing to improve performance.

![applog-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/analyze-tool.png)

## AppLog

The AppLog is designed to assist developers in fine-tuning the performance of their mini programs.
It lists all records from the framework, providing detailed insights into how the framework will
perform when rendering the mini program.

![applog-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/applog-panel.png)

## SourceMap

To address issues where SDK errors in mini programs can't be restored, a SourceMap panel has been
introduced.

Developers simply enter the row and column number where the copied and pasted error is located, then
select the version and the corresponding file, which will ensure the source code can be displayed.

![sourcemap-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/sourcemap-panel.png)

## Timeline

As we know, mini-programs need to run in specific containers, with the render and worker processes
separated. This separation creates significant challenges for diagnosing and analyzing issues. The
Timeline panel addresses this problem. By providing a complete log, it can display timelines for the
native, worker, and render modules for different app IDs and sessions. It also shows a waterfall of
resource and network requests, along with key performance data.

![Timeline Performance ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_panel.png)

As shown in the image, you can zoom into a specific module area by scrolling down. Following the
prompts, you can identify Long Task and memory warning situations. Clicking on a task will display
its original log, allowing you to review and analyze the source code at that time.

![Timeline Performance Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_panel_log.png)

### Performance Timeline

A simple panel for developers to see the key metrics such as FCP / LCP / FR and so on.

### Network and Resource Panel

For us to detect the resource download timing, such as \_\_app.js, worker.js. If you know how the
request happened on mini program, it will be very interesting to see the panel. Mostly the request
is created by worker then handle by native and response to worker handlers. When it send from worker
to native, it is handle by the rpc bridge, this step we call it as `queue`. After it will handle by
native, native will request and get the response like browser fetch api, we call it `request`.
Finally it will forward the response to worker, then developers can access the response, the whole
step we call it `response`. Under normal circumstances, there should be only a minimal duration
difference between the request and response steps. If not, worker is too busy and waiting a long
time to response it.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_network_timeline.png)

### Worker Timeline

The mostly important frame for developers, since code always run at the worker. It list all the
jssdk api function call and js engine sync task, such as timer. Additional, the custom log from
developers. The dangerous red color means it is
[long task](https://web.dev/articles/optimize-long-tasks), please try to optimize it if you consider
the better performance.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_worker.png)

### Custom Timeline log

We analyze logs on the framework side through a specific format. Additionally, we provide developers
with the ability to output custom logs to this timeline, as long as they adhere to the following log
format. Please parse the `sync` property to check the long task, it will be helpful for
optimization.

```txt


[NEZ_C(W|R)][timestamp(endTime)][timestamp(startTime)][name]stringifyPayload(JSONString | string)

```

### Timeline Usage

Pre-require:

- Binance App: >=2.87.0
- Binance App Type: Debug App
- SDK >= 4.\* (renderer detail log for be available for 4.31.0)
- IDE >= 2.49.0

#### iOS Logger

Collect your log via `console` application in macOS, make sure the log includes

- `Date and Time`
- `Category`
- `Message` **Make sure the log format endsWith `Message` body**.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_log.png)

After you start recording the log, please open the mini app to collect the log. Waiting for a few
second to get fully log once you finish the app operation. Then just save all the log to the `txt`
file.

#### Android Logger

For android, you enable the logcat.

After all the step already, open the binance app and terminal. Copy the shell command to your
terminal to write the log into the file.

```bash
adb logcat -> timeline.txt

```

Open your mini app now!

---

# Local Panels

With the introduction of Binance devTools 2.19.0 came new features, specifically, the mock data
panel and audit panel.

## Audit

### Instructions

The audit panel reviews your mini app's implementations, delivering an estimation score indicative
of its adherence to best practices.

With the latest version of Binance DevTools, new tools have been introduced to assist developers in
applying best practices to their mini programs.

The Audit Panel can be used to measure just how closely your mini program adheres to suggested
methods for optimizing performance and user experience.

### Basic Usage

1. Click the **Run** button at the top-left (pictured below) and perform functions on the Mini
   Program interface. Upon running, the page will be scrutinized for "Experience Rating".

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/audits-panel-run.png)

2. Click **Stop** to cease the analysis, whereby an analysis report will appear, which you can use
   to refine your setup.
3. If you want to rerun the experience rating, click **Clear experience rating** at the top of the
   report to reset. Do bear in mind that the system doesn't currently support report storage
   services. Once experience ratings have been cleared, they are no longer viewable.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/audits-panel-clear.png)

## Mock

The mock data panel allows developers to mock all of the JS APIs of mini programs, making it
possible to debug all features, especially those requiring native capabilities on the devtools,
thereby saving significant development time.

In the interests of facilitating small program development, the developer tool offers API Mock
capability, simulating the calling results of some APIs.

### Instructions

### Basic Usage

Find the entry for Mock in the Tab at the top of the tool debug panel and click + New Rule.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-add.png)

Example rule:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-example-rule.png)

Result of hitting the rule above:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-resault.png)

### Rule Priority

When multiple rules are set up for an API, the first rule will be matched first. Once a rule is hit,
subsequent rules will not be executed.

### Data Templates

Complex simulated data needs can be served by data templates, designed for rapid generation of data
to your specifications.

_The syntax of the data template is from the open-source library
[Mock.js](https://github.com/nuysoft/Mock/wiki/Syntax-Specification). For detailed syntax, review
the project documentation._

Data previews are generated in real-time from the template in the template editor, aiding
confirmation of the template's accuracy.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-template-data.png)

### Rule Import and Export

If you need to share rules with other project members, you can export the rule configuration in
Mock, and then send the configuration file to other members for them to import. The operational
entry is shown below:

![img.png](https://bin.bnbstatic.com/image/julia/docs/mini-program/mock-panel-share-rule.png)

#### Example

Here's a getSystemInfoSync example of the import & export feature. It consists of three steps:

- Create `getSystemInfoSync` mock Rules.
- Export the rules as a config file to a local folder.
- Import the local config file saved earlier in another project. You can use the append or cover
  mode to import the rules file.

![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-1.jpg)
![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-2.jpg)
![img.png](https://bin.bnbstatic.com/image/julia/docs/mp-ide/mock-example-step-3.jpg)

## Code Quality

The latest version of Binance DevTools offers new tools designed to assist developers in applying
best practices to their mini programs.

The Code Quality Panel allows you to scan your mini-program project and receive suggestions about
resource sizing to improve performance.

![applog-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/analyze-tool.png)

## AppLog

The AppLog is designed to assist developers in fine-tuning the performance of their mini programs.
It lists all records from the framework, providing detailed insights into how the framework will
perform when rendering the mini program.

![applog-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/applog-panel.png)

## SourceMap

To address issues where SDK errors in mini programs can't be restored, a SourceMap panel has been
introduced.

Developers simply enter the row and column number where the copied and pasted error is located, then
select the version and the corresponding file, which will ensure the source code can be displayed.

![sourcemap-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/sourcemap-panel.png)

## Timeline

As we know, mini-programs need to run in specific containers, with the render and worker processes
separated. This separation creates significant challenges for diagnosing and analyzing issues. The
Timeline panel addresses this problem. By providing a complete log, it can display timelines for the
native, worker, and render modules for different app IDs and sessions. It also shows a waterfall of
resource and network requests, along with key performance data.

![Timeline Performance ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_panel.png)

As shown in the image, you can zoom into a specific module area by scrolling down. Following the
prompts, you can identify Long Task and memory warning situations. Clicking on a task will display
its original log, allowing you to review and analyze the source code at that time.

![Timeline Performance Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_panel_log.png)

### Performance Timeline

A simple panel for developers to see the key metrics such as FCP / LCP / FR and so on.

### Network and Resource Panel

For us to detect the resource download timing, such as \_\_app.js, worker.js. If you know how the
request happened on mini program, it will be very interesting to see the panel. Mostly the request
is created by worker then handle by native and response to worker handlers. When it send from worker
to native, it is handle by the rpc bridge, this step we call it as `queue`. After it will handle by
native, native will request and get the response like browser fetch api, we call it `request`.
Finally it will forward the response to worker, then developers can access the response, the whole
step we call it `response`. Under normal circumstances, there should be only a minimal duration
difference between the request and response steps. If not, worker is too busy and waiting a long
time to response it.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_network_timeline.png)

### Worker Timeline

The mostly important frame for developers, since code always run at the worker. It list all the
jssdk api function call and js engine sync task, such as timer. Additional, the custom log from
developers. The dangerous red color means it is
[long task](https://web.dev/articles/optimize-long-tasks), please try to optimize it if you consider
the better performance.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_worker.png)

### Custom Timeline log

We analyze logs on the framework side through a specific format. Additionally, we provide developers
with the ability to output custom logs to this timeline, as long as they adhere to the following log
format. Please parse the `sync` property to check the long task, it will be helpful for
optimization.

```txt


[NEZ_C(W|R)][timestamp(endTime)][timestamp(startTime)][name]stringifyPayload(JSONString | string)

```

### Timeline Usage

Pre-require:

- Binance App: >=2.87.0
- Binance App Type: Debug App
- SDK >= 4.\* (renderer detail log for be available for 4.31.0)
- IDE >= 2.49.0

#### iOS Logger

Collect your log via `console` application in macOS, make sure the log includes

- `Date and Time`
- `Category`
- `Message` **Make sure the log format endsWith `Message` body**.

![Timeline Network Log ](https://bin.bnbstatic.com/image/julia/docs/mp-ide/ide_timeline_log.png)

After you start recording the log, please open the mini app to collect the log. Waiting for a few
second to get fully log once you finish the app operation. Then just save all the log to the `txt`
file.

#### Android Logger

For android, you enable the logcat.

After all the step already, open the binance app and terminal. Copy the shell command to your
terminal to write the log into the file.

```bash
adb logcat -> timeline.txt

```

Open your mini app now!