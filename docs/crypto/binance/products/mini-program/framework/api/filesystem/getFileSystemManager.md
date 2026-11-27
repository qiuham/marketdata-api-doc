---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/filesystem/getFileSystemManager
api_type: Guide
updated_at: 2026-11-27 18:45:54.634297
---

# bn.getFileSystemManager

▸ **getFileSystemManager**(): `FileSystemManager`

**`description`** Get the file system manager instance which is a singleton. On Android devices,
file system api will save file on external storage by default.- About filePath: filePath should
starts from root directory of source code bundle.Only supports absolute path like `/a/b` or
`a/b`.Files with extensions of `js,json,bxss,bxm` will be transformed into other files after
compilation, so they are not expected to be accessible.

- Valid value of encoding: utf-8, utf8

**`example`**

```ts
const manager = bn.getFileSystemManager();
manager.readFile({ filePath: "xxx" });
```

Returns

`FileSystemManager`

## Class: FileSystemManager

| Name                | Type                                                                                 | Description                                                |
| :------------------ | :----------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| rpc                 | `RPC`                                                                                |                                                            |
| readFileNative      | `undefined` \| (`options`: `ReadFileOption`) => `Promise`<`FSReadFileResult`\>       |                                                            |
| writeFileNative     | `undefined` \| (`options`: `WriteFileOption`) => `Promise`<`GeneralCallbackResult`\> |                                                            |
| readFileNativeSync  | `undefined` \| (`options`: `any`) => `any`                                           |                                                            |
| writeFileNativeSync | `undefined` \| (`options`: `any`) => `any`                                           |                                                            |
| readFile            | (`options`): `Promise`<`FSReadFileResult`\>                                          | **`description`** Read files in local directory.           |
| writeFile           | (`options`): `Promise`<`GeneralCallbackResult`\>                                     | **`description`** Write data into file in local directory. |
| removeSavedFile     | (`options`): `Promise`<`GeneralCallbackResult`\>                                     | **`description`** remove saved file.                       |
| mkdir               | (`options`): `Promise`<{}\>                                                          | **`description`** Create directory.                        |
| access              | (`options`): `Promise`<{}\>                                                          | **`description`** Try to access file/directory.            |
| unzip               | (`options`): `Promise`<{}\>                                                          | **`description`** Unzip file.                              |
| copyFile            | (`options`): `Promise`<{}\>                                                          | **`description`** Copy file to another path.               |
| readFileSync        | (`filePath`, `encoding?`, `position?`, `length?`): `FileData`                        | **`description`** Sync version of readFile.                |
| writeFileSync       | (`filePath`, `data`, `encoding?`): `any`                                             | **`description`** Sync version of writeFile.               |
| mkdirSync           | (`dirPath`, `recursive?`): `Object`                                                  | **`description`** Sync version of mkdir.                   |
| accessSync          | (`path`): `Object`                                                                   | **`description`** Sync version of access.                  |
| copyFileSync        | (`srcPath`, `destPath`): `Object`                                                    | **`description`** Sync version of copyFile.                |

### readFile

▸ **readFile**(`options`): `Promise`<`FSReadFileResult`\>

**`description`** Read files in local directory.

**`example`**

```ts
bn.getFileSystemManager().readFile({
  filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
  encoding: "utf-8",
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `ReadFileOption` |

Returns

`Promise`<`FSReadFileResult`\>

---

### writeFile

▸ **writeFile**(`options`): `Promise`<`GeneralCallbackResult`\>

**`description`** Write data into file in local directory.

**`example`**

```ts
bn.getFileSystemManager().writeFile({
  filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
  data: 'hello world'
  encoding: 'utf-8',
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type              |
| :-------- | :---------------- |
| `options` | `WriteFileOption` |

Returns

`Promise`<`GeneralCallbackResult`\>

---

### removeSavedFile

▸ **removeSavedFile**(`options`): `Promise`<`GeneralCallbackResult`\>

**`description`** remove saved file.

**`example`**

```ts
bn.getFileSystemManager()
 .removeSavedFile({
   filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
     success(removeRes) {
       console.log('remove file success', removeRes);
     },
     fail(removeErr) {
       console.error('remove file fail', removeErr);
     }
 })
})
```

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `options` | `RemoveSavedFileOptions` |

Returns

`Promise`<`GeneralCallbackResult`\>

---

### mkdir

▸ **mkdir**(`options`): `Promise`<{}\>

**`description`** Create directory.

**`example`**

```ts
bn.getFileSystemManager().mkdir({
  dirPath: "a/b/c/d",
  recursive: true,
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `FsMkdirOptions` |

Returns

`Promise`<{}\>

---

### access

▸ **access**(`options`): `Promise`<{}\>

**`description`** Try to access file/directory.

**`example`**

```ts
bn.getFileSystemManager().access({
  path: "a/b/c/d",
  success(res) {
    console.log(res);
  },
  fail(err) {},
});
```

Parameters

| Name      | Type              |
| :-------- | :---------------- |
| `options` | `FsAccessOptions` |

Returns

`Promise`<{}\>

---

### unzip

▸ **unzip**(`options`): `Promise`<{}\>

**`description`** Unzip file.

**`example`**

```ts
bn.getFileSystemManager().unzip({
  zipFilePath: 'foo.zip',
  targetPath: 'foo'
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `FsUnzipOptions` |

Returns

`Promise`<{}\>

---

### copyFile

▸ **copyFile**(`options`): `Promise`<{}\>

**`description`** Copy file to another path.

**`example`**

```ts
bn.getFileSystemManager().copyFile({
  destPath: 'a/foo',
  srcPath: 'a/bar'
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type            |
| :-------- | :-------------- |
| `options` | `FsCopyOptions` |

Returns

`Promise`<{}\>

---

### readFileSync

▸ **readFileSync**(`filePath`, `encoding?`, `position?`, `length?`): `FileData`

**`description`** Sync version of readFile.

**`example`**

```ts
bn.getFileSystemManager().readFileSync(`${bn.env.USER_DATA_PATH}/helloWorld.txt`,'utf-8')
})
```

Parameters

| Name        | Type                                                                                                                                            |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `filePath`  | `string`                                                                                                                                        |
| `encoding?` | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` |
| `position?` | `number`                                                                                                                                        |
| `length?`   | `number`                                                                                                                                        |

Returns

`FileData`

---

### writeFileSync

▸ **writeFileSync**(`filePath`, `data`, `encoding?`): `any`

**`description`** Sync version of writeFile.

**`example`**

```ts
bn.getFileSystemManager()
 .writeFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   'hello world',
   'utf-8'
 )
})
```

Parameters

| Name        | Type                                                                                                                                            |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `filePath`  | `string`                                                                                                                                        |
| `data`      | `FileData`                                                                                                                                      |
| `encoding?` | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` |

Returns

`any`

---

### mkdirSync

▸ **mkdirSync**(`dirPath`, `recursive?`): `Object`

**`description`** Sync version of mkdir.

**`example`**

```ts
bn.getFileSystemManager()
 .writeFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   'hello world',
   'utf-8'
 )
})
```

Parameters

| Name         | Type      |
| :----------- | :-------- |
| `dirPath`    | `string`  |
| `recursive?` | `boolean` |

Returns

`Object`

---

### accessSync

▸ **accessSync**(`path`): `Object`

**`description`** Sync version of access.

**`example`**

```ts
bn.getFileSystemManager()
 .accessSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`
 )
})
```

Parameters

| Name   | Type     |
| :----- | :------- |
| `path` | `string` |

Returns

`Object`

---

### copyFileSync

▸ **copyFileSync**(`srcPath`, `destPath`): `Object`

**`description`** Sync version of copyFile.

**`example`**

```ts
bn.getFileSystemManager()
 .copyFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   `${bn.env.USER_DATA_PATH}/foo.txt`
 )
})
```

Parameters

| Name       | Type     |
| :--------- | :------- |
| `srcPath`  | `string` |
| `destPath` | `string` |

Returns

`Object`

## Interface: FSReadFileResult

| Name   | Type       | Description     |
| :----- | :--------- | :-------------- |
| errMsg | `string`   | API call result |
| data?  | `FileData` | File content    |

## Interface: ReadFileOption

| Name      | Type                                                                                                                                            | Description                                                                                                                                                                                                       |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filePath  | `string`                                                                                                                                        | The file path to read.                                                                                                                                                                                            |
| encoding? | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` | File's character encoding. if not provided, read it in format of ArrayBuffer.; ;                                                                                                                                  |
| length?   | `number`                                                                                                                                        | Specify the length of file. If not provided, read until the end of file.Valid range: [1, fileLength].Unit: byte.                                                                                                  |
| position? | `number`                                                                                                                                        | Read file starting from specific position.If not provided, start from file head.The reading range should be left-closed and right-open, [position, position+length). Valid range: [0, fileLength - 1].Unit: byte. |
| complete? | (`res`): `void`                                                                                                                                 | Complete callback                                                                                                                                                                                                 |
| fail?     | (`err`): `void`                                                                                                                                 | Fail callback                                                                                                                                                                                                     |
| success?  | (`res`): `void`                                                                                                                                 | Success callback                                                                                                                                                                                                  |

### complete

▸ `Optional` **complete**(`res`): `void`

Complete callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`err`): `void`

Fail callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `GeneralCallbackResult` |

Returns

`void`

---

### success

▸ `Optional` **success**(`res`): `void`

Success callback

Parameters

| Name  | Type                            |
| :---- | :------------------------------ |
| `res` | `ReadFileSuccessCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name    | Type     | Description     |
| :------ | :------- | :-------------- |
| errMsg? | `string` | API call result |

## Interface: ReadFileSuccessCallbackResult

| Name    | Type       | Description     |
| :------ | :--------- | :-------------- |
| data    | `FileData` | File content    |
| errMsg? | `string`   | API call result |

## Interface: GeneralCallbackResult

| Name    | Type     | Description     |
| :------ | :------- | :-------------- |
| errMsg? | `string` | API call result |

## WriteFileOption

Ƭ **WriteFileOption**: `Object`

Type declaration

| Name        | Type                                                                                                                                                           | Description                                   |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| `complete`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `fail`      | `undefined` \| (`err`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `success`   | `undefined` \| (`res`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `data`      | `string` \| `ArrayBuffer`                                                                                                                                      | The data to write.                            |
| `filePath`  | `string`                                                                                                                                                       | The file path to write data in.               |
| `encoding?` | `undefined` \| `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` | Character encoding of the file to be written. |

---

## RemoveSavedFileOptions

Ƭ **RemoveSavedFileOptions**: `Object`

Type declaration

| Name       | Type                                                      | Description |
| :--------- | :-------------------------------------------------------- | :---------- |
| `complete` | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` | -           |
| `fail`     | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` | -           |
| `success`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` | -           |
| `filePath` | `string`                                                  | File path   |

---

## FsMkdirOptions

Ƭ **FsMkdirOptions**: `Object`

Type declaration

| Name        | Type                                                      |
| :---------- | :-------------------------------------------------------- |
| `dirPath`   | `string`                                                  |
| `recursive` | `undefined` \| `boolean`                                  |
| `complete`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`      | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`   | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsAccessOptions

Ƭ **FsAccessOptions**: `Object`

Type declaration

| Name       | Type                                                      |
| :--------- | :-------------------------------------------------------- |
| `path`     | `string`                                                  |
| `complete` | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`     | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsUnzipOptions

Ƭ **FsUnzipOptions**: `Object`

Type declaration

| Name          | Type                                                      |
| :------------ | :-------------------------------------------------------- |
| `zipFilePath` | `string`                                                  |
| `targetPath`  | `string`                                                  |
| `complete`    | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`        | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`     | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsCopyOptions

Ƭ **FsCopyOptions**: `Object`

Type declaration

| Name       | Type                    | Description     |
| :--------- | :---------------------- | :-------------- |
| `destPath` | `string`                | -               |
| `srcPath`  | `string`                | -               |
| `errMsg?`  | `undefined` \| `string` | API call result |

## FileData

Ƭ **FileData**: `string` \| `ArrayBuffer`

---

---

# bn.getFileSystemManager

▸ **getFileSystemManager**(): `FileSystemManager`

**`description`** Get the file system manager instance which is a singleton. On Android devices,
file system api will save file on external storage by default.- About filePath: filePath should
starts from root directory of source code bundle.Only supports absolute path like `/a/b` or
`a/b`.Files with extensions of `js,json,bxss,bxm` will be transformed into other files after
compilation, so they are not expected to be accessible.

- Valid value of encoding: utf-8, utf8

**`example`**

```ts
const manager = bn.getFileSystemManager();
manager.readFile({ filePath: "xxx" });
```

Returns

`FileSystemManager`

## Class: FileSystemManager

| Name                | Type                                                                                 | Description                                                |
| :------------------ | :----------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| rpc                 | `RPC`                                                                                |                                                            |
| readFileNative      | `undefined` \| (`options`: `ReadFileOption`) => `Promise`<`FSReadFileResult`\>       |                                                            |
| writeFileNative     | `undefined` \| (`options`: `WriteFileOption`) => `Promise`<`GeneralCallbackResult`\> |                                                            |
| readFileNativeSync  | `undefined` \| (`options`: `any`) => `any`                                           |                                                            |
| writeFileNativeSync | `undefined` \| (`options`: `any`) => `any`                                           |                                                            |
| readFile            | (`options`): `Promise`<`FSReadFileResult`\>                                          | **`description`** Read files in local directory.           |
| writeFile           | (`options`): `Promise`<`GeneralCallbackResult`\>                                     | **`description`** Write data into file in local directory. |
| removeSavedFile     | (`options`): `Promise`<`GeneralCallbackResult`\>                                     | **`description`** remove saved file.                       |
| mkdir               | (`options`): `Promise`<{}\>                                                          | **`description`** Create directory.                        |
| access              | (`options`): `Promise`<{}\>                                                          | **`description`** Try to access file/directory.            |
| unzip               | (`options`): `Promise`<{}\>                                                          | **`description`** Unzip file.                              |
| copyFile            | (`options`): `Promise`<{}\>                                                          | **`description`** Copy file to another path.               |
| readFileSync        | (`filePath`, `encoding?`, `position?`, `length?`): `FileData`                        | **`description`** Sync version of readFile.                |
| writeFileSync       | (`filePath`, `data`, `encoding?`): `any`                                             | **`description`** Sync version of writeFile.               |
| mkdirSync           | (`dirPath`, `recursive?`): `Object`                                                  | **`description`** Sync version of mkdir.                   |
| accessSync          | (`path`): `Object`                                                                   | **`description`** Sync version of access.                  |
| copyFileSync        | (`srcPath`, `destPath`): `Object`                                                    | **`description`** Sync version of copyFile.                |

### readFile

▸ **readFile**(`options`): `Promise`<`FSReadFileResult`\>

**`description`** Read files in local directory.

**`example`**

```ts
bn.getFileSystemManager().readFile({
  filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
  encoding: "utf-8",
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `ReadFileOption` |

Returns

`Promise`<`FSReadFileResult`\>

---

### writeFile

▸ **writeFile**(`options`): `Promise`<`GeneralCallbackResult`\>

**`description`** Write data into file in local directory.

**`example`**

```ts
bn.getFileSystemManager().writeFile({
  filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
  data: 'hello world'
  encoding: 'utf-8',
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type              |
| :-------- | :---------------- |
| `options` | `WriteFileOption` |

Returns

`Promise`<`GeneralCallbackResult`\>

---

### removeSavedFile

▸ **removeSavedFile**(`options`): `Promise`<`GeneralCallbackResult`\>

**`description`** remove saved file.

**`example`**

```ts
bn.getFileSystemManager()
 .removeSavedFile({
   filePath: `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
     success(removeRes) {
       console.log('remove file success', removeRes);
     },
     fail(removeErr) {
       console.error('remove file fail', removeErr);
     }
 })
})
```

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `options` | `RemoveSavedFileOptions` |

Returns

`Promise`<`GeneralCallbackResult`\>

---

### mkdir

▸ **mkdir**(`options`): `Promise`<{}\>

**`description`** Create directory.

**`example`**

```ts
bn.getFileSystemManager().mkdir({
  dirPath: "a/b/c/d",
  recursive: true,
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `FsMkdirOptions` |

Returns

`Promise`<{}\>

---

### access

▸ **access**(`options`): `Promise`<{}\>

**`description`** Try to access file/directory.

**`example`**

```ts
bn.getFileSystemManager().access({
  path: "a/b/c/d",
  success(res) {
    console.log(res);
  },
  fail(err) {},
});
```

Parameters

| Name      | Type              |
| :-------- | :---------------- |
| `options` | `FsAccessOptions` |

Returns

`Promise`<{}\>

---

### unzip

▸ **unzip**(`options`): `Promise`<{}\>

**`description`** Unzip file.

**`example`**

```ts
bn.getFileSystemManager().unzip({
  zipFilePath: 'foo.zip',
  targetPath: 'foo'
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type             |
| :-------- | :--------------- |
| `options` | `FsUnzipOptions` |

Returns

`Promise`<{}\>

---

### copyFile

▸ **copyFile**(`options`): `Promise`<{}\>

**`description`** Copy file to another path.

**`example`**

```ts
bn.getFileSystemManager().copyFile({
  destPath: 'a/foo',
  srcPath: 'a/bar'
  success(res) {
    console.log(res)
  },
})
```

Parameters

| Name      | Type            |
| :-------- | :-------------- |
| `options` | `FsCopyOptions` |

Returns

`Promise`<{}\>

---

### readFileSync

▸ **readFileSync**(`filePath`, `encoding?`, `position?`, `length?`): `FileData`

**`description`** Sync version of readFile.

**`example`**

```ts
bn.getFileSystemManager().readFileSync(`${bn.env.USER_DATA_PATH}/helloWorld.txt`,'utf-8')
})
```

Parameters

| Name        | Type                                                                                                                                            |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `filePath`  | `string`                                                                                                                                        |
| `encoding?` | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` |
| `position?` | `number`                                                                                                                                        |
| `length?`   | `number`                                                                                                                                        |

Returns

`FileData`

---

### writeFileSync

▸ **writeFileSync**(`filePath`, `data`, `encoding?`): `any`

**`description`** Sync version of writeFile.

**`example`**

```ts
bn.getFileSystemManager()
 .writeFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   'hello world',
   'utf-8'
 )
})
```

Parameters

| Name        | Type                                                                                                                                            |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `filePath`  | `string`                                                                                                                                        |
| `data`      | `FileData`                                                                                                                                      |
| `encoding?` | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` |

Returns

`any`

---

### mkdirSync

▸ **mkdirSync**(`dirPath`, `recursive?`): `Object`

**`description`** Sync version of mkdir.

**`example`**

```ts
bn.getFileSystemManager()
 .writeFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   'hello world',
   'utf-8'
 )
})
```

Parameters

| Name         | Type      |
| :----------- | :-------- |
| `dirPath`    | `string`  |
| `recursive?` | `boolean` |

Returns

`Object`

---

### accessSync

▸ **accessSync**(`path`): `Object`

**`description`** Sync version of access.

**`example`**

```ts
bn.getFileSystemManager()
 .accessSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`
 )
})
```

Parameters

| Name   | Type     |
| :----- | :------- |
| `path` | `string` |

Returns

`Object`

---

### copyFileSync

▸ **copyFileSync**(`srcPath`, `destPath`): `Object`

**`description`** Sync version of copyFile.

**`example`**

```ts
bn.getFileSystemManager()
 .copyFileSync(
   `${bn.env.USER_DATA_PATH}/helloWorld.txt`,
   `${bn.env.USER_DATA_PATH}/foo.txt`
 )
})
```

Parameters

| Name       | Type     |
| :--------- | :------- |
| `srcPath`  | `string` |
| `destPath` | `string` |

Returns

`Object`

## Interface: FSReadFileResult

| Name   | Type       | Description     |
| :----- | :--------- | :-------------- |
| errMsg | `string`   | API call result |
| data?  | `FileData` | File content    |

## Interface: ReadFileOption

| Name      | Type                                                                                                                                            | Description                                                                                                                                                                                                       |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filePath  | `string`                                                                                                                                        | The file path to read.                                                                                                                                                                                            |
| encoding? | `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` | File's character encoding. if not provided, read it in format of ArrayBuffer.; ;                                                                                                                                  |
| length?   | `number`                                                                                                                                        | Specify the length of file. If not provided, read until the end of file.Valid range: [1, fileLength].Unit: byte.                                                                                                  |
| position? | `number`                                                                                                                                        | Read file starting from specific position.If not provided, start from file head.The reading range should be left-closed and right-open, [position, position+length). Valid range: [0, fileLength - 1].Unit: byte. |
| complete? | (`res`): `void`                                                                                                                                 | Complete callback                                                                                                                                                                                                 |
| fail?     | (`err`): `void`                                                                                                                                 | Fail callback                                                                                                                                                                                                     |
| success?  | (`res`): `void`                                                                                                                                 | Success callback                                                                                                                                                                                                  |

### complete

▸ `Optional` **complete**(`res`): `void`

Complete callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `res` | `GeneralCallbackResult` |

Returns

`void`

---

### fail

▸ `Optional` **fail**(`err`): `void`

Fail callback

Parameters

| Name  | Type                    |
| :---- | :---------------------- |
| `err` | `GeneralCallbackResult` |

Returns

`void`

---

### success

▸ `Optional` **success**(`res`): `void`

Success callback

Parameters

| Name  | Type                            |
| :---- | :------------------------------ |
| `res` | `ReadFileSuccessCallbackResult` |

Returns

`void`

## Interface: GeneralCallbackResult

| Name    | Type     | Description     |
| :------ | :------- | :-------------- |
| errMsg? | `string` | API call result |

## Interface: ReadFileSuccessCallbackResult

| Name    | Type       | Description     |
| :------ | :--------- | :-------------- |
| data    | `FileData` | File content    |
| errMsg? | `string`   | API call result |

## Interface: GeneralCallbackResult

| Name    | Type     | Description     |
| :------ | :------- | :-------------- |
| errMsg? | `string` | API call result |

## WriteFileOption

Ƭ **WriteFileOption**: `Object`

Type declaration

| Name        | Type                                                                                                                                                           | Description                                   |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| `complete`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `fail`      | `undefined` \| (`err`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `success`   | `undefined` \| (`res`: `GeneralCallbackResult`) => `void`                                                                                                      | -                                             |
| `data`      | `string` \| `ArrayBuffer`                                                                                                                                      | The data to write.                            |
| `filePath`  | `string`                                                                                                                                                       | The file path to write data in.               |
| `encoding?` | `undefined` \| `"ascii"` \| `"base64"` \| `"binary"` \| `"hex"` \| `"ucs2"` \| `"ucs-2"` \| `"utf16le"` \| `"utf-16le"` \| `"utf-8"` \| `"utf8"` \| `"latin1"` | Character encoding of the file to be written. |

---

## RemoveSavedFileOptions

Ƭ **RemoveSavedFileOptions**: `Object`

Type declaration

| Name       | Type                                                      | Description |
| :--------- | :-------------------------------------------------------- | :---------- |
| `complete` | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` | -           |
| `fail`     | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` | -           |
| `success`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` | -           |
| `filePath` | `string`                                                  | File path   |

---

## FsMkdirOptions

Ƭ **FsMkdirOptions**: `Object`

Type declaration

| Name        | Type                                                      |
| :---------- | :-------------------------------------------------------- |
| `dirPath`   | `string`                                                  |
| `recursive` | `undefined` \| `boolean`                                  |
| `complete`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`      | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`   | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsAccessOptions

Ƭ **FsAccessOptions**: `Object`

Type declaration

| Name       | Type                                                      |
| :--------- | :-------------------------------------------------------- |
| `path`     | `string`                                                  |
| `complete` | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`     | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`  | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsUnzipOptions

Ƭ **FsUnzipOptions**: `Object`

Type declaration

| Name          | Type                                                      |
| :------------ | :-------------------------------------------------------- |
| `zipFilePath` | `string`                                                  |
| `targetPath`  | `string`                                                  |
| `complete`    | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |
| `fail`        | `undefined` \| (`err`: `GeneralCallbackResult`) => `void` |
| `success`     | `undefined` \| (`res`: `GeneralCallbackResult`) => `void` |

---

## FsCopyOptions

Ƭ **FsCopyOptions**: `Object`

Type declaration

| Name       | Type                    | Description     |
| :--------- | :---------------------- | :-------------- |
| `destPath` | `string`                | -               |
| `srcPath`  | `string`                | -               |
| `errMsg?`  | `undefined` \| `string` | API call result |

## FileData

Ƭ **FileData**: `string` \| `ArrayBuffer`

---