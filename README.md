# type_listing
Python script to list and display Windows structures and enums from WinDBG (extraction from the json)

Exemple of usage:

```
paul@lab:~/type_listing$ python type_listing.py '_flt_' x86
List:
fltmgr!_FLT_OBJECT_FLAGS
fltmgr!_FLT_PREOP_CALLBACK_STATUS
fltmgr!_FLT_PARAMETERS
fltmgr!_FLT_GENERIC_WORKITEM
fltmgr!_FLT_REGISTRATION
fltmgr!_FLT_FILE_NAME_INFORMATION
fltmgr!_FLT_DEFERRED_IO_WORKITEM
fltmgr!_FLT_NAME_CONTROL
fltmgr!_FLT_VERIFIER_EXTENSION
fltmgr!_FLT_CALLBACK_DATA_QUEUE
fltmgr!_FLT_CCB
fltmgr!_FLT_MESSAGE_WAITER
fltmgr!_FLT_MUTEX_LIST_HEAD
fltmgr!_FLT_RELATED_CONTEXTS
fltmgr!_FLT_VERIFIER_EXTENSION_FLAGS
fltmgr!_FLT_INSTANCE
fltmgr!_FLT_VOLUME_PROPERTIES
fltmgr!_FLT_TAG_DATA_BUFFER
fltmgr!_FLT_CALLBACK_DATA
fltmgr!_FLT_OBJECT
fltmgr!_FLT_FILTER_FLAGS
fltmgr!_FLT_STATS
fltmgr!_FLT_VOLUME_FLAGS
fltmgr!_FLT_NPAGED_LOOKASIDE_NUMBER
fltmgr!_FLT_VERIFIER_OBJECT
fltmgr!_FLT_TYPE
fltmgr!_FLT_POSTOP_CALLBACK_STATUS
fltmgr!_FLT_RESOURCE_LIST_HEAD
fltmgr!_FLT_MESSAGE_WAITER_QUEUE
fltmgr!_FLT_PRCB
fltmgr!_FLT_RELATED_OBJECTS
fltmgr!_FLT_CONTEXT_REGISTRATION
fltmgr!_FLT_OPERATION_REGISTRATION
fltmgr!_FLT_FILTER
fltmgr!_FLT_VOLUME
fltmgr!_FLT_SERVER_PORT_OBJECT
fltmgr!_FLT_PORT_OBJECT
fltmgr!_FLT_IO_PARAMETER_BLOCK
fltmgr!_FLT_FILESYSTEM_TYPE
fltmgr!_FLT_INSTANCE_FLAGS

paul@lab:~/type_listing$ python type_listing.py 'fltmgr!_FLT_OPERATION_REGISTRATION' x86
List:
fltmgr!_FLT_OPERATION_REGISTRATION

fltmgr!_FLT_OPERATION_REGISTRATION
Description of fltmgr!_FLT_OPERATION_REGISTRATION
[[u'+0x000', u'MajorFunction', u' UChar'],
 [u'+0x004', u'Flags', u' Uint4B'],
 [u'+0x008', u'PreOperation', u' Ptr32     _FLT_PREOP_CALLBACK_STATUS '],
 [u'+0x00c', u'PostOperation', u' Ptr32     _FLT_POSTOP_CALLBACK_STATUS '],
 [u'+0x010', u'Reserved1', u' Ptr32 Void']]

paul@lab:~/type_listing$ python type_listing.py 'fltmgr!_FLT_OPERATION_REGISTRATION' x64
List:
FLTMGR!_FLT_OPERATION_REGISTRATION

FLTMGR!_FLT_OPERATION_REGISTRATION
Description of fltmgr!_FLT_OPERATION_REGISTRATION
[[u'+0x000', u'MajorFunction', u' UChar'],
 [u'+0x004', u'Flags', u' Uint4B'],
 [u'+0x008', u'PreOperation', u' Ptr64     _FLT_PREOP_CALLBACK_STATUS '],
 [u'+0x010', u'PostOperation', u' Ptr64     _FLT_POSTOP_CALLBACK_STATUS '],
 [u'+0x018', u'Reserved1', u' Ptr64 Void']]

```


