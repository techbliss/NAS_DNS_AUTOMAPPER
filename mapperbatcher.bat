:S_CHECK
IF EXIST S:\NUL ECHO S: Drive Exists - [DNSADRESS]
ECHO S: Connecting Drive...
NET USE S: /DELETE
NET USE S: \\\DNSADRESS@SSL@PORT somepass /USER:someuser /PERSISTENT:YES

