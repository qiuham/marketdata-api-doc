---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/project-configuration
api_type: Guide
updated_at: 2026-11-26 18:38:46.202994
---

# Project Configuration File

You can configure your project using the `project.config.json` file found in the project's root
directory.

### Configuration Options

| Property        | Type     | Default Value | Required | Description                                                           |
| --------------- | -------- | ------------- | -------- | --------------------------------------------------------------------- |
| miniprogramRoot | `String` | -             | Yes      | Sets the directory (a relative path) for the Mini Program source code |
| packOptions     | `Object` | -             | No       | Sets the packaging configuration options                              |

### Packaging Options (packOptions)

`packOptions` helps manage the settings for project packaging. Packaging is an essential step for
previewing and uploading projects.

Using `packOptions.ignore` field, you can define filter rules. Files or folders that satisfy these
rules will be discarded during project packaging. They will not appear in the preview or the upload
outcomes.

`packOptions.ignore` is an array of objects, each containing:

| Property | Type | Default Value | Required | Description | | -------- | -------- | ------------- |
Yes | ------------- | | value | `String` | - | Yes | Path or value | | type | `String` | - | Yes |
Type |

Possible type values are `folder`, `file`, `suffix`, `prefix`, `regexp`, and `glob`, representing
folders, files, suffixes, prefixes, regular expressions, and Glob rules. Value comparison is
case-insensitive.

> Note: If the value of the value field designates a file or a folder path, the root directory is
> the Mini Program directory (`miniprogramRoot`).

Here's a sample configuration:

```json
// project.config.json

{
  "miniprogramRoot": "./dist",
  "packOptions": {
    "ignore": [
      {
        "type": "file",
        "value": "utils.bxs"
      },
      {
        "type": "folder",
        "value": "image"
      },
      {
        "type": "suffix",
        "value": ".LICENSE.txt"
      },
      {
        "type": "suffix",
        "value": ".css"
      },
      {
        "type": "prefix",
        "value": "rich-"
      },
      {
        "type": "glob",
        "value": "pages/API/**/*.js"
      },
      {
        "type": "regexp",
        "value": "index\\.js$"
      }
    ]
  }
  // ...
}
```

---

# Project Configuration File

You can configure your project using the `project.config.json` file found in the project's root
directory.

### Configuration Options

| Property        | Type     | Default Value | Required | Description                                                           |
| --------------- | -------- | ------------- | -------- | --------------------------------------------------------------------- |
| miniprogramRoot | `String` | -             | Yes      | Sets the directory (a relative path) for the Mini Program source code |
| packOptions     | `Object` | -             | No       | Sets the packaging configuration options                              |

### Packaging Options (packOptions)

`packOptions` helps manage the settings for project packaging. Packaging is an essential step for
previewing and uploading projects.

Using `packOptions.ignore` field, you can define filter rules. Files or folders that satisfy these
rules will be discarded during project packaging. They will not appear in the preview or the upload
outcomes.

`packOptions.ignore` is an array of objects, each containing:

| Property | Type | Default Value | Required | Description | | -------- | -------- | ------------- |
Yes | ------------- | | value | `String` | - | Yes | Path or value | | type | `String` | - | Yes |
Type |

Possible type values are `folder`, `file`, `suffix`, `prefix`, `regexp`, and `glob`, representing
folders, files, suffixes, prefixes, regular expressions, and Glob rules. Value comparison is
case-insensitive.

> Note: If the value of the value field designates a file or a folder path, the root directory is
> the Mini Program directory (`miniprogramRoot`).

Here's a sample configuration:

```json
// project.config.json

{
  "miniprogramRoot": "./dist",
  "packOptions": {
    "ignore": [
      {
        "type": "file",
        "value": "utils.bxs"
      },
      {
        "type": "folder",
        "value": "image"
      },
      {
        "type": "suffix",
        "value": ".LICENSE.txt"
      },
      {
        "type": "suffix",
        "value": ".css"
      },
      {
        "type": "prefix",
        "value": "rich-"
      },
      {
        "type": "glob",
        "value": "pages/API/**/*.js"
      },
      {
        "type": "regexp",
        "value": "index\\.js$"
      }
    ]
  }
  // ...
}
```