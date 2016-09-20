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

Description of fltmgr!_FLT_OPERATION_REGISTRATION
[[u'+0x000', u'MajorFunction', u' UChar'],
 [u'+0x004', u'Flags', u' Uint4B'],
 [u'+0x008', u'PreOperation', u' Ptr32     _FLT_PREOP_CALLBACK_STATUS '],
 [u'+0x00c', u'PostOperation', u' Ptr32     _FLT_POSTOP_CALLBACK_STATUS '],
 [u'+0x010', u'Reserved1', u' Ptr32 Void']]

paul@lab:~/type_listing$ python type_listing.py 'fltmgr!_FLT_OPERATION_REGISTRATION' x64
List:
FLTMGR!_FLT_OPERATION_REGISTRATION

Description of fltmgr!_FLT_OPERATION_REGISTRATION
[[u'+0x000', u'MajorFunction', u' UChar'],
 [u'+0x004', u'Flags', u' Uint4B'],
 [u'+0x008', u'PreOperation', u' Ptr64     _FLT_PREOP_CALLBACK_STATUS '],
 [u'+0x010', u'PostOperation', u' Ptr64     _FLT_POSTOP_CALLBACK_STATUS '],
 [u'+0x018', u'Reserved1', u' Ptr64 Void']]

paul@lab:~/type_listing$ python type_listing.py 'fltmgr!_FLT_OPERATION_REGISTRATION' x64 680002020000000000000000000000001082010000000000f013010000000000b014010000000000d014010000000000f014010000000000f014010000000000
List:
FLTMGR!_FLT_REGISTRATION

Description of FLTMGR!_FLT_REGISTRATION
[[u'+0x000', u'Size', u' Uint2B'],
 [u'+0x002', u'Version', u' Uint2B'],
 [u'+0x004', u'Flags', u' Uint4B'],
 [u'+0x008', u'ContextRegistration', u' Ptr64 _FLT_CONTEXT_REGISTRATION'],
 [u'+0x010', u'OperationRegistration', u' Ptr64 _FLT_OPERATION_REGISTRATION'],
 [u'+0x018', u'FilterUnloadCallback', u' Ptr64     long '],
 [u'+0x020', u'InstanceSetupCallback', u' Ptr64     long '],
 [u'+0x028', u'InstanceQueryTeardownCallback', u' Ptr64     long '],
 [u'+0x030', u'InstanceTeardownStartCallback', u' Ptr64     void '],
 [u'+0x038', u'InstanceTeardownCompleteCallback', u' Ptr64     void '],
 [u'+0x040', u'GenerateFileNameCallback', u' Ptr64     long '],
 [u'+0x048', u'NormalizeNameComponentCallback', u' Ptr64     long '],
 [u'+0x050', u'NormalizeContextCleanupCallback', u' Ptr64     void '],
 [u'+0x058', u'TransactionNotificationCallback', u' Ptr64     long '],
 [u'+0x060', u'NormalizeNameComponentExCallback', u' Ptr64     long '],
 [u'+0x068', u'SectionNotificationCallback', u' Ptr64     long ']]

+0x000 = 0x68 (Size  Uint2B)
+0x002 = 0x202 (Version  Uint2B)
+0x004 = 0x0 (Flags  Uint4B)
+0x008 = 0x0 (ContextRegistration  Ptr64 _FLT_CONTEXT_REGISTRATION)
+0x010 = 0x18210 (OperationRegistration  Ptr64 _FLT_OPERATION_REGISTRATION)
+0x018 = 0x113f0 (FilterUnloadCallback  Ptr64     long )
+0x020 = 0x114b0 (InstanceSetupCallback  Ptr64     long )
+0x028 = 0x114d0 (InstanceQueryTeardownCallback  Ptr64     long )
+0x030 = 0x114f0 (InstanceTeardownStartCallback  Ptr64     void )
+0x038 = 0x114f0 (InstanceTeardownCompleteCallback  Ptr64     void )
+0x040 = 0x00 (GenerateFileNameCallback  Ptr64     long )
+0x048 = 0x00 (NormalizeNameComponentCallback  Ptr64     long )
+0x050 = 0x00 (NormalizeContextCleanupCallback  Ptr64     void )
+0x058 = 0x00 (TransactionNotificationCallback  Ptr64     long )
+0x060 = 0x00 (NormalizeNameComponentExCallback  Ptr64     long )

```


