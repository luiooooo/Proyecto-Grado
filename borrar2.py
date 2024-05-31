import re

def clasificar_texto(texto):
    contenido_guardado = {
        "Original": texto,  
        "Texto": "",
        "DLLs": "",
        "Librerias": "",
        "Codigo": "",
        "Todo": texto,
        "Reporte": ""
    }
    
    # Patrones para identificar diferentes tipos de contenido
    patron_dll = re.compile(r'\b\w+\.dll\b', re.IGNORECASE)
    patron_librerias = re.compile(r'\b(io_|lib_|module_|core_|maxon_|cinema|c4d|rs256|up_)\w+', re.IGNORECASE)
    patron_codigo = re.compile(r'\b(if|else|while|for|return|int|float|bool|void|class|const|true|false|null)\b', re.IGNORECASE)
    
    # Líneas separadas del texto
    lineas = texto.splitlines()
    
    # Clasificación
    texto_plano = []
    dlls = []
    librerias = []
    codigo = []
    
    for linea in lineas:
        if patron_dll.search(linea):
            dlls.append(linea)
        elif patron_librerias.search(linea):
            librerias.append(linea)
        elif patron_codigo.search(linea):
            codigo.append(linea)
        else:
            texto_plano.append(linea)
    
    # Asignar los resultados al diccionario
    contenido_guardado["Texto"] = '\n'.join(texto_plano)
    contenido_guardado["DLLs"] = '\n'.join(dlls)
    contenido_guardado["Librerias"] = '\n'.join(librerias)
    contenido_guardado["Codigo"] = '\n'.join(codigo)
    
    return contenido_guardado

# Ejemplo de uso con el texto proporcionado
texto = """
.text
.pdata
.rsrc
CRITICALH
true1
lite1
confH
lite3
t2H9_
fals3E
taH9s
gfffffffH
t6H9N
tnH9q
tSL9Y
y1HcA
t3Hc@
tLL9X
tXL9P
t7H9Z
w2IcD
ex*rY
AVVWUSH
tEH9p
Bx2H9y
@ 0t4H
tVL9f
BQRAPAQH
gfffffffH
Job QueuH
tMI9H
tfL9Z
tqL9X
        H
gfffffffH
F  t*H
x0uNf.
tXL9k
txL9R
xcI9_
gfffffffL
xfI9_
ol. f
oM fE
H3KXH3CPH
AVVWUSH
tUL9g
AVVWUSH
UPu@H
F tpH
oTU0f
xbtlD
fTarget
N uNH
pMutex_
MaxonAppH
Q8H9Q v
Main ThrE1
ead QueuH1
Thread QH1
Main Thr
UUUUUU
Set the memory model.
MAXON
'*-036
filor
@CFIL
adgjmpsvy
input path is empty
Allow setting of thread group affinity
log all output to a file
if no path is specified the log file will be created in the temporary directory
shortcut does not link to a file or directory
File member @ is a different datatype in file and memory
category
library
.c4dpy
JobDummy
_array
isArray
Must use UInt32 for the index
io_fbx
Expected scaling would be about @ x
context
helpText
no valid path is set in the shortcut
 const
Directory @ does not exist
for pipeline test
Memory Block Start Corrupt
can't go higher in hierarchy than root
_content
different content
Datatype doesn't match file content
command line argument
Cinema 4D Team Render Client
.cpuidinit
a value of 0 disables it
redshift
Group not finished yet
Job not finished yet
asset
preset
project
Cineware arguments
_bits
_errors
Server 2008 without Hyper-V for Windows Essential Server Solutions
Standard Server Solutions
sections
plugins
symbols
Length of backtrace for Spinlocks
 bytes
Classes
set the number of threads used
note that the number can be higher than the actual number of cores
a value of 0 will utilize the real number of available cores
Data types
volumes
Loading Modules
branches
c4d_nodes
Alien Threads
corelibs
operator
leaklayer
Windows Essential Business Server Security Server
Small Business Server
Cinema 4D Team Render Server
Windows Essential Business Server Messaging Server
Windows Home Server
Solution Embedded Server
Microsoft Hyper-V Server
Pointer
could not auto-detect a delimiter
leaks from the same location will be grouped together
wait after launch for the debugger
Fixed @ events with wrong order
No binding to start folder
shader
Illegal file header
Illegal or wrong file header
Wrong file header
Expected no number
utf16char
utf32char
group
JobGroup
scopedump
timestamp
--help
io_skp
_hashMap
Leak graph written to
_info
	unknown
Unknown
g_maxon
Maxon
Storage Server Express Edition
Server for Small Business Edition
Cluster Server Edition
Home Premium Server Edition
Home Server Edition
Web Server Edition
Compute Cluster Edition
Starter Edition
Small Business Server Premium Edition
Home Premium Edition
Ultimate Edition
Home Edition
Storage Server Standard Edition
Home Basic Edition
Web Edition
Standard x64 Edition
dbversion
Compiler Version
-listen
g_openurl
g_openUrl
moduleUrl
_impl
ProxyImpl
UnitImpl
ClassImpl
TimerImpl
UrlImpl
DllImpl
UuidImpl
MiscImpl
RCUImpl
 symbol
Only one Write allowed at the top level
Only one Read allowed at the top level
global
don't ask
Array access does not work
file is too short to contain a link
Number of spins when to suspect a potential deadlock
Double free of memory block
NoStack
io_obj
-nogui
_path
override the default temporary path
baseUrl not part of path
English
mograph
authority mismatch
scheme mismatch
Cinebench
io_dwg
If statement missing
Delayed statement missing
Input stream missing
void datatype missing
Expected no string
Expected string
sleeping
g_warning
Illegal 32-Bit encoding
Illegal UTF-16 encoding
config
io_gltf
remove
_value
not a hex value
not a bool value
HasValue
Default Queue
Execution Queue
Reuse Resource Queue
Main Thread Queue
Job Queue
ServiceIO Queue
 magic byte
attribute
Cinema 4D Lite
NoCause
False
release
c4d_base
_type
Illegal reference type
_keyType
dataType
no scope
rootScope
NoMachine
_time
startTime
endTime
_scheme
fullname
Invalid language name
Expected node name
hen an error prevents loading part of a module
g_console
Not a valid json file
Not a binary MAXON file
Illegal file header - no XML file
g_logFile
method table
not available
ment variable
Value out of range
volume id out of range
Single Language
_message
Function @ has no virtual function callee
_mode
 mode
_code
unknown UTF8 code
_fastMode
Unknown stride
perforce
R-Reference
_trace
warn if a module uses an outdated method table of a non-virtual interface
Error creating interface
io_usd
xdl64_upd
Datatype of @ not found
Database id '@' not found
...debugger found
Module path @ couldn't be found
per second
_uuid
delayed
Group is already enqueued
Job is already enqueued
Newer file structure detected
string or closing curly bracket expected
comma expected
generated
Main thread allocator key has been set before main thread has been updated
Too many datatypes used
Caller was cancelled
Console output failed
Startup path setup failed
Command line scan failed
logger is disabled
Timers are disabled
Thread list is currently locked
End of file reached
Main thread pointer was already changed
Embedded
No observers were added
no logger outputs available added
g_alloc
assetdb
nulldata
_data
missing '.' in jwt data
_fastData
China
g_dna
Expected comma
exchangeW
Server Standard Edition without Hyper-V
Cluster Server V
en-US
Core N
Launch Cinema 4D
  @ with module@
MAXON_@
clang @.@.@
Registry @
const @
Module @ uses an outdated method table for @
Writing API summary to @
Couldn't write to @
Skipping module @ for better matching version @
Seek error in @
Function @ not found in @
Skip failed in @
  uses framework @
Resolving module @ of @
  could not resolve @
Could not create log file @
Couldn't close file @
Skipping module @ because its core framework is newer than supported @
RS256
Vector4
upd_win64
xdl64
Windows Storage Server 2003
Vector2
Url path is empty.
The name is empty.
Url is not a directory.
Object already contained in hierarchy.
Could not acquire crypt context.
Invalid hex input.
Url does not exist.
No handler present.
Only the enqueuing job is allowed to wait.
Registry for entry @ doesn't exist yet.
.preset.
Temp path not set.
SetData is not allowed for const object.
EraseData is not allowed for const object.
Path does not contain valid address.
You can't add more than @ class proxies to a class.
Once a group has been enqueued only its jobs can add further groups.
Show DataType leaks.
True to not save missing string databases.
File buffer size in kB for writing files.
File buffer size in kB for reading files.
Once a group has been enqueued only its jobs can add further jobs.
Factory is nullptr.
parent is nullptr.
Cannot store pointer to type @ to a nullptr.
Cannot store object of type @ to a nullptr.
.error.
cannot write to read-only buffer.
writes the temp file into ram instead temp folder.
You tried to start a job which is part of a group.
Illegal if condition.
Else condition broken.
End condition broken.
.enum.
 input stream.
Cannot open stream.
"""

# Ejecutar la función con el texto de ejemplo
resultado = clasificar_texto(texto)

# Mostrar el resultado
for categoria, contenido in resultado.items():
    print(f"{categoria}:\n{contenido}\n{'-'*40}\n")
