import ctypes
import platform
from ctypes import Structure, c_long, c_int, c_wchar_p, c_ulong, c_float, WINFUNCTYPE
from ctypes.wintypes import DWORD, WORD, BYTE, HANDLE, LPCWSTR, ULONG, WCHAR, BOOL, LONG, PWCHAR
TCHAR = WCHAR

SDK_DLL = ctypes.WinDLL("x64\\SDKDLL.dll")

if platform.architecture()[0].startswith('64'):
    WIN_PACK = 8
else:
    WIN_PACK = 1


class GUID(ctypes.Structure):
    """GUID Windows OS Structure"""
    _pack_ = 1
    _fields_ = [("data1", DWORD),
                ("data2", WORD),
                ("data3", WORD),
                ("data4", BYTE * 8)]

    def __init__(self, data1=None, data2 = None, data3 = None, data4 = None):
        if data1 is not None:
            self.data1 = data1
        if data2 is not None:
            self.data2 = data2
        if data3 is not None:
            self.data3 = data3
        if data4 is not None:
            self.data4 = data4


_get_sdk_dll_ver_api_proto = WINFUNCTYPE(c_int)
_get_sdk_dll_ver_api = _get_sdk_dll_ver_api_proto(("GetCM_SDK_DllVer", SDK_DLL))


def get_sdk_dll_ver():
    return _get_sdk_dll_ver_api()


_get_now_time_api_proto = WINFUNCTYPE(c_wchar_p)
_get_now_time_api = _get_now_time_api_proto(("GetNowTime", SDK_DLL))


def get_now_time():
    return _get_now_time_api()


_get_now_cpu_usage_api_proto = WINFUNCTYPE(c_long)
_get_now_cpu_usage_api = _get_now_cpu_usage_api_proto(("GetNowCPUUsage", SDK_DLL))


def get_now_cpu_usage():
    return _get_now_cpu_usage_api()


_get_ram_usage_api_proto = WINFUNCTYPE(c_ulong)
_get_ram_usage_api = _get_ram_usage_api_proto(("GetRamUsage", SDK_DLL))


def get_ram_usage():
    return _get_ram_usage_api()


_get_now_volume_peek_value_api_proto = WINFUNCTYPE(c_float)
_get_now_volume_peek_value_api = _get_now_volume_peek_value_api_proto(("GetNowVolumePeekValue", SDK_DLL))


def get_now_volume_peek_value():
    return _get_now_volume_peek_value_api()

# # Set up prototype and parameters for the desired function call.
# # HLLAPI
#
# hllApiProto = ctypes.WINFUNCTYPE (
#     ctypes.c_int,      # Return type.
#     ctypes.c_void_p,   # Parameters 1 ...
#     ctypes.c_void_p,
#     ctypes.c_void_p,
#     ctypes.c_void_p)   # ... thru 4.
# hllApiParams = (1, "p1", 0), (1, "p2", 0), (1, "p3",0), (1, "p4",0),
#
# # Actually map the call ("HLLAPI(...)") to a Python name.
#
# hllApi = hllApiProto (("HLLAPI", hllDll), hllApiParams)
#
# # This is how you can actually call the DLL function.
# # Set up the variables and call the Python name with them.
#
# p1 = ctypes.c_int (1)
# p2 = ctypes.c_char_p (sessionVar)
# p3 = ctypes.c_int (1)
# p4 = ctypes.c_int (0)
# hllApi (ctypes.byref (p1), p2, ctypes.byref (p3), ctypes.byref (p4))


if __name__ == '__main__':
    print('test started')
    # print('get_sdk_dll_ver', get_sdk_dll_ver())
    # print('get_now_time', get_now_time())
    print('get_now_cpu_usage', get_now_cpu_usage())
    # print('get_ram_usage', get_ram_usage())
    print('get_now_volume_peek_value', get_now_volume_peek_value())
    print('test done')
