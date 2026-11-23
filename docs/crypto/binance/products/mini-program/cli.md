---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/cli
api_type: Guide
updated_at: 2026-11-23 18:30:31.238392
---

# CLI

This document is a comprehensive guide on how to utilize the bmp Command Line Interface (CLI).

## CLI Download

Let's start by installing the CLI.

```bash
# optional
# Set the Binance npm registry (if not set already)
# npm config set @binance:registry https://npm.binance.com

# Install the CLI globally
$ npm install -g @binance/mp-cli
```

## CLI Usage

Breeze through the following commands to get used to the bmp CLI:

### Creating a New Project

```bash
$ bmp init [project-name]
```

Running the above command will conjure an initialized mini-program project brimming with potential!

For instance:

```bash
$ bmp init magnificent-mini-program
```

### Adding Support to an Existing React Project

```bash
# Navigate to the project root directory
$ cd [path-to-desirable-project-root]

# Run bmp bootstrap
$ bmp bootstrap
```

The above commands spin off a `.bmp` directory and add essential configurations to the existing
`tsconfig.json` file. This ensures support for importing @binance/\*, thereby enabling TypeScript
syntax support.

### Kicking Off with devServer

```bash
# Navigate to the project root directory
$ cd [path-to-project-root]

# Run bmp dev
$ npx bmp dev
```

Introducing the command that compiles your project and spins up `devServer`, listening on
`locahost:3000` by default. As you hop into the project and select the `dist` project, you will be
greeted by your running mini-program. With `liveReload` enabled on `devServer`, any changes to your
code will trigger an automatic rebuild and refreshes the page.

### Build and Compile

```bash
# Navigate to the project root directory
$ cd [path-to-project-root]

# Run bmp build
$ npx bmp build
```

Compiling the project code has never been easier! The above command renders mini-program files in
the project directory. With [Binance Devtools](download), developers can smoothly upload these files
to the management portal for release or swift online testing.

---

# CLI

This document is a comprehensive guide on how to utilize the bmp Command Line Interface (CLI).

## CLI Download

Let's start by installing the CLI.

```bash
# optional
# Set the Binance npm registry (if not set already)
# npm config set @binance:registry https://npm.binance.com

# Install the CLI globally
$ npm install -g @binance/mp-cli
```

## CLI Usage

Breeze through the following commands to get used to the bmp CLI:

### Creating a New Project

```bash
$ bmp init [project-name]
```

Running the above command will conjure an initialized mini-program project brimming with potential!

For instance:

```bash
$ bmp init magnificent-mini-program
```

### Adding Support to an Existing React Project

```bash
# Navigate to the project root directory
$ cd [path-to-desirable-project-root]

# Run bmp bootstrap
$ bmp bootstrap
```

The above commands spin off a `.bmp` directory and add essential configurations to the existing
`tsconfig.json` file. This ensures support for importing @binance/\*, thereby enabling TypeScript
syntax support.

### Kicking Off with devServer

```bash
# Navigate to the project root directory
$ cd [path-to-project-root]

# Run bmp dev
$ npx bmp dev
```

Introducing the command that compiles your project and spins up `devServer`, listening on
`locahost:3000` by default. As you hop into the project and select the `dist` project, you will be
greeted by your running mini-program. With `liveReload` enabled on `devServer`, any changes to your
code will trigger an automatic rebuild and refreshes the page.

### Build and Compile

```bash
# Navigate to the project root directory
$ cd [path-to-project-root]

# Run bmp build
$ npx bmp build
```

Compiling the project code has never been easier! The above command renders mini-program files in
the project directory. With [Binance Devtools](download), developers can smoothly upload these files
to the management portal for release or swift online testing.