DMP_EVENTS = {
    'Za': 'Zone Alarm',
    'Zb': 'Zone Force Alarm',
    'Zc': 'Device Status',
    'Zd': 'Wireless Low Battery',
    'Ze': 'Equipment',
    'Zf': 'Walk Test Fail',
    'Zg': 'Holidays',
    'Zh': 'Wireless Zone Missing',
    'Zj': 'Zone Access',
    'Zk': 'Walk Test Verify',
    'Zl': 'Schedules',
    'Zm': 'Service Code',
    'Zq': 'Arming Status',
    'Zr': 'Zone Restore',
    'Zs': 'System Message',
    'Zt': 'Zone Trouble',
    'Zu': 'User Codes',
    'Zw': 'Zone Fault',
    'Zx': 'Zone Bypass',
    'Zy': 'Zone Reset',
}

DMP_TYPES = {
    #Zones
    'BL': 'Blank',
    'FI': 'Fire',
    'BU': 'Burglary',
    'SV': 'Supervisory',
    'PN': 'Panic',
    'EM': 'Emergency',
    'A1': 'Auxiliary 1',
    'A2': 'Auxiliary 2',
    #Access
    'DA': 'Door Access Granted',
    'AA': 'Door Access Denied: Armed Area',
    'IA': 'Door Access Denied: Invalid Area',
    'IT': 'Door Access Denied: Invalid Time',
    'AP': 'Door Access Denied: Previous Access',
    'IC': 'Door Access Denied: Invalid Code',
    'IL': 'Door Access Denied: Invalid Level',
    #Status
    'DO': 'Door Status: Open',
    'DC': 'Door Status: Closed',
    'HO': 'Door Status: Held Open',
    'FO': 'Door Status: Forced Open',
    'ON': 'Output Status: On',
    'OF': 'Output Status: Off',
    'PL': 'Output Status: Pulse',
    'TP': 'Output Status: Temporal',
    #Equipment
    'RP': 'Equipment: Repair',
    'RL': 'Equipment: Replace',
    'AD': 'Equipment: Add',
    'RM': 'Equipment: Remove',
    'AJ': 'Equipment: Adjust',
    'TS': 'Equipment: Test',
    #Qualifier
    'DT': 'Service',
    'AC': 'All Areas Armed',
    #Arming
    'OP': 'Area Disarmed',
    'CL': 'Area Armed',
    'LA': 'Area Late to Arm',
    #Schedule
    'PE': 'Permanent Schedule',
    'TE': 'Temporary Schedule',
    'PR': 'Primary Schedule',
    'SE': 'Secondary Schedule',
    'S1': 'Shift 1',
    'S2': 'Shift 2',
    'S3': 'Shift 3',
    'S4': 'Shift 4',
    #System Messages
    '000': 'AC Power Restored',
    '001': 'Standby Battery Restored',
    '002': 'Communications Line Restored',
    '003': 'Panel Tamper Restored',
    '004': 'Backup Communications Restored',
    '005': 'Panel Ground Restored',
    '006': 'System Not Armed by Scheduled Time',
    '007': 'Automatic Communication Test',
    '008': 'AC Power Failure',
    '009': 'Low Standby Battery',
    '010': 'Low Communications Signal',
    '011': 'Panel Tamper',
    '012': 'Backup Communications Failure',
    '013': 'Panel Ground Fault',
    '014': 'Non-Alarm Message Overflow',
    '015': 'Ambush/Silent Alarm',
    '018': 'Alarm Message Overflow',
    '023': 'Local Panel test',
    '026': 'Auxiliary fuse Trouble',
    '027': 'Auxiliary Fuse Restored',
    '028': 'Telephone line 1 Fault',
    '029': 'Telephone line 1 Restore',
    '030': 'Telephone line 2 Fault',
    '031': 'Telephone line 2 Restore',
    '032': 'Supervised wireless Interference',
    '033': 'Early Morning Ambush',
    '034': 'Alarm Silenced',
    '035': 'Alarm Bell Normal', #not implemented per dmp docs
    '038': 'Bell Circuit Trouble',
    '039': 'Bell Circuit Restored',
    '040': 'Fire Alarm Message Overflow',
    '041': 'Panic Zone Alarm Overflow',
    '042': 'Burglary Zone Alarm Overflow',
    '043': 'Bell Fuse Trouble',
    '044': 'Fire/Burglary Trouble Overflow',
    '045': 'Abort Signal Received',
    '046': 'Zone Swinger Automatically Bypassed',
    '047': 'Zone Swinger Automatically Reset',
    '048': 'Backup Battery Critical - Last Message Before Poweroff',
    '049': 'Cancel Signal Received',
    '050': 'Supervised Wireless Trouble',
    '051': 'Remote Programming',
    '053': 'Bell Fuse Restored',
    '054': 'Unsuccessful Remote connect',
    '071': 'Time Request',
    '072': 'Network trouble',
    '073': 'Network Restoral',
    '074': 'Panel Tamper during Armed State',
    '077': 'Unauthorized Entry',
    '078': 'System Recently Armed',
    '079': 'Signal During Opened Period',
    '080': 'Exit Error',
    '083': 'Remote Programming Complete',
    '084': 'Remote Command Received',
    '086': 'Local programming',
    '087': 'Transmit failed - Messages Not Sent',
    '088': 'Automatic Test - Troubled system',
    '089': 'Supervised Wireless Restored',
    '091': 'Services Requested',
    '092': 'No Arm/Disarm Activity',
    '093': 'User activity Not detected',
    '094': 'Activity Check Enabled',
    '095': 'Activity Check disabled',
    '096': 'Alarm Verified',
    '097': 'Network Test OK',
    '101': 'Device Missing',
    '102': 'Device Restored',
    '121': 'Excessive Cellular communication',
    '122': 'Cell Communication Suppressed: Excessive data',
    #more for cell systems, i'm lazy

    #Holidays
    'HA': 'Holiday Schedule A',
    'HB': 'Holiday Schedule B',
    'HC': 'Holiday Schedule C',

    #User Code
    'AD': 'User Code Added',
    'CH': 'User Code Changed',
    'DE': 'User Code Deleted',

    #Service User
    'ST': 'Start Service User',
    'SP': 'Stop Service User',
}