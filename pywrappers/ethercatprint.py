from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libsoem.so'] = CDLL('libsoem.so')


EC_STATE_BOOT = 3
EC_STATE_SAFE_OP = 4
ECT_COES_SDORES = 3
EC_STATE_PRE_OP = 2
EC_STATE_INIT = 1
ECT_REG_DCCYCLE1 = 2468
ECT_REG_DCCYCLE0 = 2464
ECT_REG_DCSYNCACT = 2433
ECT_REG_DCSYSDIFF = 2348
ECT_REG_DCSYSTIME = 2320
ECT_SOE_WRITEREQ = 3
ECT_REG_SM1STAT = 2061
EC_BUF_COMPLETE = 4
EC_BUF_RCVD = 3
ECT_GET_OE_REQ = 5
ECT_REG_FMMU3 = 1584
ECT_GET_OD_REQ = 3
ECT_GET_ODLIST_RES = 2
ECT_REG_FMMU0 = 1536
ECT_SDO_ABORT = 128
ECT_SDO_SEG_UP_REQ = 96
ECT_REG_EEPSTAT = 1282
ECT_REG_EEPCTL = 1282
ECT_REG_EEPCFG = 1280
ECT_REG_RXERR = 768
ECT_REG_IRQMASK = 512
ECT_SII_SM = 41
ECT_REG_ALSTATCODE = 308
ECT_SII_GENERAL = 30
ECT_SII_STRING = 10
ECT_SII_MBXPROTO = 28
ECT_SII_TXMBXADR = 26
ECT_SII_REV = 12
EC_ECMD_RELOAD = 768
EC_ECMD_WRITE = 513
EC_ECMD_READ = 256
EC_ECMD_NOP = 0
ECT_MBXT_SOE = 5
ECT_REG_SM2 = 2064
ECT_REG_FMMU1 = 1552
ECT_REG_DCSTART0 = 2448
ECT_REG_DCCUC = 2432
ECT_REG_DCTIMEFILT = 2356
ECT_REG_DCSPEEDCNT = 2352
EC_ERR_TYPE_SOE_ERROR = 8
EC_ERR_TYPE_FOE_PACKETNUMBER = 7
EC_ERR_TYPE_FOE_BUF2SMALL = 6
EC_ERR_TYPE_FOE_ERROR = 5
EC_ERR_TYPE_SDOINFO_ERROR = 4
EC_ERR_TYPE_PACKET_ERROR = 3
EC_ERR_TYPE_EMERGENCY = 1
EC_ERR_TYPE_SDO_ERROR = 0
ECT_REG_DCSYSOFFSET = 2336
EC_ERR_NOK = 5
ITIMER_PROF = 2
ITIMER_VIRTUAL = 1
ECT_REG_DCTIME3 = 2316
ITIMER_REAL = 0
ECT_SOE_EMERGENCY = 6
ECT_SOE_NOTIFICATION = 5
ECT_SOE_WRITERES = 4
ECT_REG_SM1CONTR = 2063
ECT_SOE_READRES = 2
ECT_REG_FMMU2 = 1568
ECT_REG_DCSYSDELAY = 2344
ECT_REG_SM1ACT = 2062
ECT_SOE_READREQ = 1
EC_BUF_ALLOC = 1
ECT_REG_SM0STAT = 2053
EC_CMD_FRMW = 14
EC_CMD_ARMW = 13
ECT_REG_SM3 = 2072
EC_CMD_LRW = 12
EC_CMD_LWR = 11
EC_CMD_LRD = 10
EC_CMD_BRW = 9
EC_CMD_BWR = 8
EC_CMD_BRD = 7
ECT_SDOINFO_ERROR = 7
EC_CMD_FPRW = 6
EC_CMD_FPWR = 5
EC_CMD_FPRD = 4
EC_CMD_APRW = 3
EC_CMD_APWR = 2
EC_CMD_APRD = 1
ECT_REG_SM1 = 2056
EC_CMD_NOP = 0
ECT_REG_SM0 = 2048
ECT_GET_OD_RES = 4
EC_BUF_EMPTY = 0
ECT_REG_DCSOF = 2328
ECT_REG_ALSTAT = 304
ECT_REG_DLSTAT = 272
ECT_REG_DLALIAS = 259
ECT_REG_DLPORT = 257
ECT_REG_DLCTL = 256
ECT_REG_STADR = 16
ECT_REG_EEPDAT = 1288
ECT_REG_ESCSUP = 8
ECT_REG_PORTDES = 7
ECT_REG_TYPE = 0
ECT_FOE_ERROR = 5
ECT_FOE_ACK = 4
ECT_REG_EEPADR = 1284
ECT_FOE_DATA = 3
ECT_COES_SDOINFO = 8
ECT_COES_RXPDO_RR = 7
ECT_COES_TXPDO_RR = 6
ECT_SDO_UP_REQ_CA = 80
ECT_COES_RXPDO = 5
ECT_COES_TXPDO = 4
ECT_COES_SDOREQ = 2
ECT_COES_EMERGENCY = 1
ECT_MBXT_VOE = 15
ECT_SDO_UP_REQ = 64
ECT_MBXT_FOE = 4
ECT_MBXT_COE = 3
ECT_MBXT_EOE = 2
ECT_MBXT_AOE = 1
ECT_MBXT_ERR = 0
ECT_SDO_DOWN_INIT_CA = 49
ECT_SII_RXMBXADR = 24
ECT_SII_MBXSIZE = 25
ECT_SII_BOOTTXMBX = 22
ECT_SDO_DOWN_INIT = 33
ECT_SII_BOOTRXMBX = 20
ECT_SII_ID = 10
ECT_SII_MANUF = 8
ECT_SII_PDO = 50
ECT_REG_PDICTL = 320
ECT_SII_FMMU = 40
EC_ERR_NO_SLAVES = 4
EC_ERR_TIMEOUT = 3
EC_ERR_NOT_INITIALIZED = 2
EC_ERR_ALREADY_INITIALIZED = 1
EC_ERR_OK = 0
ECT_REG_ALCTL = 288
ECT_GET_OE_RES = 6
ECT_REG_DCTIME2 = 2312
ECT_INTEGER32 = 4
ECT_REG_ALIAS = 18
ECT_INTEGER8 = 2
ECT_REG_DCTIME1 = 2308
ECT_BIT8 = 55
ECT_BIT7 = 54
ECT_BIT6 = 53
ECT_BIT5 = 52
ECT_BIT4 = 51
ECT_FOE_BUSY = 6
ECT_BIT3 = 50
ECT_BIT2 = 49
ECT_BIT1 = 48
ECT_UNSIGNED64 = 27
ECT_UNSIGNED24 = 22
ECT_INTEGER64 = 21
ECT_REAL64 = 17
ECT_INTEGER24 = 16
ECT_DOMAIN = 15
ECT_TIME_DIFFERENCE = 13
ECT_TIME_OF_DAY = 12
ECT_UNICODE_STRING = 11
ECT_OCTET_STRING = 10
ECT_VISIBLE_STRING = 9
ECT_REG_DCTIME0 = 2304
ECT_REAL32 = 8
ECT_UNSIGNED32 = 7
ECT_UNSIGNED16 = 6
ECT_FOE_WRITE = 2
ECT_GET_ODLIST_REQ = 1
ECT_FOE_READ = 1
EC_BUF_TX = 2
ECT_UNSIGNED8 = 5
ECT_INTEGER16 = 3
ECT_BOOLEAN = 1
EC_STATE_ERROR = 16
EC_STATE_ACK = 16
EC_STATE_OPERATIONAL = 8
__time_t = c_long
time_t = __time_t
class timespec(Structure):
    pass
timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', c_long),
]
__sig_atomic_t = c_int
class __sigset_t(Structure):
    pass
__sigset_t._fields_ = [
    ('__val', c_ulong * 16),
]
class timeval(Structure):
    pass
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
__u_char = c_ubyte
__u_short = c_ushort
__u_int = c_uint
__u_long = c_ulong
__int8_t = c_byte
__uint8_t = c_ubyte
__int16_t = c_short
__uint16_t = c_ushort
__int32_t = c_int
__uint32_t = c_uint
__int64_t = c_long
__uint64_t = c_ulong
__quad_t = c_long
__u_quad_t = c_ulong
__dev_t = c_ulong
__uid_t = c_uint
__gid_t = c_uint
__ino_t = c_ulong
__ino64_t = c_ulong
__mode_t = c_uint
__nlink_t = c_ulong
__off_t = c_long
__off64_t = c_long
__pid_t = c_int
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    ('__val', c_int * 2),
]
__clock_t = c_long
__rlim_t = c_ulong
__rlim64_t = c_ulong
__id_t = c_uint
__useconds_t = c_uint
__daddr_t = c_int
__swblk_t = c_long
__key_t = c_int
__clockid_t = c_int
__timer_t = c_void_p
__blksize_t = c_long
__blkcnt_t = c_long
__blkcnt64_t = c_long
__fsblkcnt_t = c_ulong
__fsblkcnt64_t = c_ulong
__fsfilcnt_t = c_ulong
__fsfilcnt64_t = c_ulong
__ssize_t = c_long
__loff_t = __off64_t
__qaddr_t = POINTER(__quad_t)
__caddr_t = STRING
__intptr_t = c_long
__socklen_t = c_uint
sigset_t = __sigset_t
suseconds_t = __suseconds_t
__fd_mask = c_long
class fd_set(Structure):
    pass
fd_set._fields_ = [
    ('fds_bits', __fd_mask * 16),
]
fd_mask = __fd_mask
select = _libraries['libsoem.so'].select
select.restype = c_int
select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
pselect = _libraries['libsoem.so'].pselect
pselect.restype = c_int
pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
class timezone(Structure):
    pass
timezone._fields_ = [
    ('tz_minuteswest', c_int),
    ('tz_dsttime', c_int),
]
__timezone_ptr_t = POINTER(timezone)
gettimeofday = _libraries['libsoem.so'].gettimeofday
gettimeofday.restype = c_int
gettimeofday.argtypes = [POINTER(timeval), __timezone_ptr_t]
settimeofday = _libraries['libsoem.so'].settimeofday
settimeofday.restype = c_int
settimeofday.argtypes = [POINTER(timeval), POINTER(timezone)]
adjtime = _libraries['libsoem.so'].adjtime
adjtime.restype = c_int
adjtime.argtypes = [POINTER(timeval), POINTER(timeval)]

# values for enumeration '__itimer_which'
__itimer_which = c_int # enum
class itimerval(Structure):
    pass
itimerval._fields_ = [
    ('it_interval', timeval),
    ('it_value', timeval),
]
__itimer_which_t = c_int
getitimer = _libraries['libsoem.so'].getitimer
getitimer.restype = c_int
getitimer.argtypes = [__itimer_which_t, POINTER(itimerval)]
setitimer = _libraries['libsoem.so'].setitimer
setitimer.restype = c_int
setitimer.argtypes = [__itimer_which_t, POINTER(itimerval), POINTER(itimerval)]
utimes = _libraries['libsoem.so'].utimes
utimes.restype = c_int
utimes.argtypes = [STRING, POINTER(timeval)]
lutimes = _libraries['libsoem.so'].lutimes
lutimes.restype = c_int
lutimes.argtypes = [STRING, POINTER(timeval)]
futimes = _libraries['libsoem.so'].futimes
futimes.restype = c_int
futimes.argtypes = [c_int, POINTER(timeval)]
futimesat = _libraries['libsoem.so'].futimesat
futimesat.restype = c_int
futimesat.argtypes = [c_int, STRING, POINTER(timeval)]
uint16 = c_ushort
ec_sdoerror2string = _libraries['libsoem.so'].ec_sdoerror2string
ec_sdoerror2string.restype = STRING
ec_sdoerror2string.argtypes = [uint16]
ec_ALstatuscode2string = _libraries['libsoem.so'].ec_ALstatuscode2string
ec_ALstatuscode2string.restype = STRING
ec_ALstatuscode2string.argtypes = [uint16]
ec_soeerror2string = _libraries['libsoem.so'].ec_soeerror2string
ec_soeerror2string.restype = STRING
ec_soeerror2string.argtypes = [uint16]
ec_elist2string = _libraries['libsoem.so'].ec_elist2string
ec_elist2string.restype = STRING
ec_elist2string.argtypes = []
boolean = c_ubyte
int8 = c_byte
int16 = c_short
int32 = c_int
uint8 = c_ubyte
uint32 = c_uint
int64 = c_longlong
uint64 = c_ulonglong
ec_bufT = uint8 * 1518
class ec_etherheadert(Structure):
    pass
ec_etherheadert._pack_ = 1
ec_etherheadert._fields_ = [
    ('da0', uint16),
    ('da1', uint16),
    ('da2', uint16),
    ('sa0', uint16),
    ('sa1', uint16),
    ('sa2', uint16),
    ('etype', uint16),
]
class ec_comt(Structure):
    pass
ec_comt._pack_ = 1
ec_comt._fields_ = [
    ('elength', uint16),
    ('command', uint8),
    ('index', uint8),
    ('ADP', uint16),
    ('ADO', uint16),
    ('dlength', uint16),
    ('irpt', uint16),
]

# values for enumeration 'ec_err'
ec_err = c_int # enum

# values for enumeration 'ec_state'
ec_state = c_int # enum

# values for enumeration 'ec_bufstate'
ec_bufstate = c_int # enum

# values for enumeration 'ec_datatype'
ec_datatype = c_int # enum

# values for enumeration 'ec_cmdtype'
ec_cmdtype = c_int # enum

# values for enumeration 'ec_ecmdtype'
ec_ecmdtype = c_int # enum

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for unnamed enumeration

# values for enumeration 'ec_err_type'
ec_err_type = c_int # enum
class N9ec_errort4DOT_22E(Union):
    pass
class N9ec_errort4DOT_224DOT_23E(Structure):
    pass
N9ec_errort4DOT_224DOT_23E._fields_ = [
    ('ErrorCode', uint16),
    ('ErrorReg', uint8),
    ('b1', uint8),
    ('w1', uint16),
    ('w2', uint16),
]
N9ec_errort4DOT_22E._anonymous_ = ['_0']
N9ec_errort4DOT_22E._fields_ = [
    ('AbortCode', int32),
    ('_0', N9ec_errort4DOT_224DOT_23E),
]
class ec_errort(Structure):
    pass
ec_errort._anonymous_ = ['_0']
ec_errort._fields_ = [
    ('Time', timeval),
    ('Signal', boolean),
    ('Slave', uint16),
    ('Index', uint16),
    ('SubIdx', uint8),
    ('Etype', ec_err_type),
    ('_0', N9ec_errort4DOT_22E),
]
__all__ = ['__uint16_t', 'ECT_REG_DLSTAT',
           'N9ec_errort4DOT_224DOT_23E', '__int16_t',
           'ECT_COES_TXPDO_RR', 'EC_CMD_FPWR', 'ECT_SDO_DOWN_INIT',
           'ECT_SII_FMMU', 'settimeofday', 'EC_ERR_TYPE_SDO_ERROR',
           'ECT_REG_SM1STAT', 'ECT_REG_RXERR', 'ECT_SII_REV',
           'ECT_MBXT_AOE', 'EC_BUF_COMPLETE', 'timeval', '__uint32_t',
           'ECT_SDO_UP_REQ', 'ec_cmdtype', '__time_t',
           'ECT_UNSIGNED32', 'ec_elist2string', 'itimerval',
           'ECT_REG_SM0', 'N9ec_errort4DOT_22E', 'uint16',
           'ECT_REG_PDICTL', 'ECT_MBXT_COE', 'EC_STATE_PRE_OP',
           '__qaddr_t', 'ECT_SDO_ABORT', '__u_short', '__loff_t',
           'ECT_SII_MBXPROTO', 'ECT_GET_ODLIST_RES',
           'ECT_SOE_EMERGENCY', 'EC_CMD_ARMW', '__int32_t',
           'ECT_COES_SDOREQ', 'ECT_REG_ESCSUP', '__itimer_which_t',
           'ECT_DOMAIN', 'ECT_REG_DCTIMEFILT', 'ECT_REG_SM1',
           'ECT_SII_SM', 'ECT_REG_SM3', 'ECT_GET_OE_REQ',
           'ECT_SOE_NOTIFICATION', 'ECT_REG_IRQMASK', 'sigset_t',
           'ECT_MBXT_EOE', 'ECT_REG_FMMU0', 'ECT_REG_FMMU1',
           'ECT_REG_FMMU2', 'ECT_REG_FMMU3', 'ECT_GET_OD_RES',
           'ec_datatype', 'ECT_GET_OD_REQ', 'boolean',
           'ECT_REG_EEPADR', '__ssize_t', 'ECT_REG_SM1ACT',
           '__nlink_t', 'ECT_REAL32', 'ECT_MBXT_ERR',
           'EC_ERR_NO_SLAVES', 'futimes', '__uint64_t', 'fd_set',
           'ECT_BOOLEAN', 'ECT_REG_DCSYSDIFF', '__off64_t',
           'ECT_UNSIGNED8', '__fd_mask', 'int16', 'EC_ECMD_NOP',
           'ec_bufT', 'EC_ERR_TYPE_SOE_ERROR', 'ECT_REG_DLCTL',
           'ECT_SII_MANUF', 'getitimer', '__sigset_t', '__clockid_t',
           '__useconds_t', 'ECT_REG_DCSTART0', 'adjtime',
           'ECT_COES_TXPDO', '__timer_t', 'ECT_REG_DCCUC',
           'EC_ERR_TYPE_FOE_ERROR', 'ECT_SII_TXMBXADR', 'select',
           'ECT_INTEGER8', 'ec_bufstate', 'uint32',
           'ECT_REG_DCSYSTIME', 'EC_ERR_ALREADY_INITIALIZED',
           'EC_CMD_BRW', 'ec_err_type', 'ECT_SII_BOOTRXMBX',
           'ECT_INTEGER64', 'ECT_VISIBLE_STRING', 'EC_CMD_LRD',
           'ECT_FOE_BUSY', 'EC_CMD_BRD', 'ec_ALstatuscode2string',
           'ECT_REG_EEPSTAT', '__blkcnt64_t', 'ECT_SII_RXMBXADR',
           '__u_long', 'ECT_GET_OE_RES', 'EC_CMD_LRW',
           'EC_ERR_TYPE_PACKET_ERROR', 'ECT_COES_SDOINFO',
           'EC_STATE_INIT', '__fsfilcnt64_t', 'EC_CMD_APRD',
           '__blkcnt_t', 'ECT_BIT1', 'ECT_BIT2', 'ECT_BIT3',
           'ECT_BIT4', 'ECT_BIT5', 'ECT_BIT6', 'ECT_BIT7', 'ECT_BIT8',
           '__ino_t', 'ECT_REG_SM2', '__rlim64_t', 'EC_ERR_OK',
           'EC_CMD_APRW', 'ECT_MBXT_VOE', 'ECT_SII_ID', 'setitimer',
           'EC_BUF_RCVD', 'ECT_FOE_WRITE', 'EC_ERR_NOT_INITIALIZED',
           '__mode_t', 'futimesat', 'ECT_SII_STRING', 'ECT_INTEGER16',
           'ECT_REG_EEPDAT', '__blksize_t', 'ECT_SII_BOOTTXMBX',
           'ECT_COES_EMERGENCY', '__off_t', '__timezone_ptr_t',
           'ECT_REG_ALIAS', '__intptr_t', 'EC_ECMD_RELOAD',
           'ECT_REG_SM1CONTR', 'EC_ERR_TYPE_EMERGENCY', 'ec_state',
           'timespec', 'ECT_REG_EEPCTL', 'ECT_SDO_SEG_UP_REQ',
           'EC_ERR_NOK', '__suseconds_t', 'ECT_SII_GENERAL',
           'ECT_FOE_ERROR', 'EC_CMD_APWR', 'ECT_REG_ALCTL',
           'EC_STATE_SAFE_OP', 'ECT_SII_MBXSIZE', 'ECT_SII_PDO',
           'ECT_SOE_READREQ', 'ECT_SOE_READRES', 'EC_BUF_EMPTY',
           '__uint8_t', 'ECT_REAL64', 'EC_BUF_ALLOC', '__u_char',
           '__rlim_t', 'uint8', '__sig_atomic_t', 'gettimeofday',
           'EC_CMD_FPRD', 'ECT_REG_ALSTAT', 'ECT_TIME_DIFFERENCE',
           'pselect', 'int8', 'ECT_SDOINFO_ERROR', 'uint64',
           'ECT_REG_DLALIAS', 'EC_ERR_TYPE_FOE_BUF2SMALL',
           'ECT_FOE_READ', 'EC_ERR_TIMEOUT', 'ECT_REG_DLPORT',
           'ECT_REG_DCSOF', 'EC_BUF_TX', 'ECT_SDO_UP_REQ_CA',
           'ec_soeerror2string', 'ECT_FOE_ACK', '__socklen_t',
           'ECT_REG_DCSYSDELAY', 'fd_mask', 'ECT_FOE_DATA',
           'ec_sdoerror2string', 'EC_CMD_FPRW', 'ECT_INTEGER32',
           '__ino64_t', 'ECT_REG_EEPCFG', 'ec_etherheadert',
           'ECT_UNICODE_STRING', 'EC_CMD_BWR', 'ITIMER_REAL',
           '__caddr_t', 'ECT_REG_PORTDES', 'ECT_TIME_OF_DAY',
           '__u_int', '__clock_t', 'timezone', '__fsblkcnt_t',
           'ECT_SDO_DOWN_INIT_CA', 'EC_CMD_FRMW', 'ECT_REG_DCSYNCACT',
           'ECT_REG_DCSYSOFFSET', 'time_t', 'ECT_REG_STADR',
           'EC_STATE_BOOT', 'ECT_GET_ODLIST_REQ',
           'EC_STATE_OPERATIONAL', 'ECT_MBXT_SOE',
           'ECT_COES_RXPDO_RR', '__gid_t', '__fsid_t',
           'ECT_UNSIGNED64', 'ECT_REG_DCCYCLE1', 'ECT_REG_DCCYCLE0',
           '__u_quad_t', 'ECT_COES_SDORES', 'ECT_COES_RXPDO',
           'lutimes', 'EC_ECMD_WRITE', '__id_t', 'EC_ECMD_READ',
           'ec_comt', '__itimer_which', '__pid_t', 'ECT_INTEGER24',
           'ECT_REG_SM0STAT', 'ECT_SOE_WRITERES', '__fsblkcnt64_t',
           'ECT_SOE_WRITEREQ', 'EC_STATE_ACK', 'int32',
           'ECT_REG_TYPE', 'ECT_REG_DCTIME1', 'ECT_REG_DCTIME0',
           'ECT_REG_DCTIME3', 'ECT_REG_DCTIME2',
           'EC_ERR_TYPE_SDOINFO_ERROR', 'EC_CMD_NOP',
           'ECT_REG_DCSPEEDCNT', 'ECT_REG_ALSTATCODE', '__swblk_t',
           'ITIMER_PROF', 'ec_err', 'ECT_UNSIGNED16', 'EC_CMD_LWR',
           'ITIMER_VIRTUAL', 'EC_STATE_ERROR', 'ECT_MBXT_FOE',
           'ECT_OCTET_STRING', '__fsfilcnt_t', 'ECT_UNSIGNED24',
           'ec_errort', '__quad_t', '__int64_t', 'int64', '__key_t',
           'ec_ecmdtype', 'EC_ERR_TYPE_FOE_PACKETNUMBER', '__daddr_t',
           '__uid_t', 'utimes', '__int8_t', 'suseconds_t', '__dev_t']