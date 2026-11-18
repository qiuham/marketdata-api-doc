---
exchange: kraken
source_url: https://docs.kraken.com/exchange/api-reference/drop-copy/logout
api_type: FIX
updated_at: 2026-11-18 01:44:48.189021
---

# Logout

> End a drop copy session

FIX
session: drop copy
35=5

Initiates or confirms the end of the session. On a failed logon the reason arrives here in Text. EncodedTextLen and EncodedText are the standard FIX 4.4 pair for carrying the same text in a non-ASCII encoding.

**Direction:** Either direction

***

**header** *required*

35=`5`

**58 - Text** `string`

Free-text description. Carries the reject reason, the logout reason, or other detail.

**Format:** Free text set by the sender.

**354 - EncodedTextLen** `Length`

Length in bytes of the EncodedText field that follows.

**Format:** Byte count.

Required: Conditional

**355 - EncodedText** `data`

Text repeated in a non-ASCII encoding, as named by MessageEncoding (347).

**Format:** Raw data; length given by EncodedTextLen (354).

Required: Conditional

**trailer** *required*