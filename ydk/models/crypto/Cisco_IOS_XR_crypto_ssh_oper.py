""" Cisco_IOS_XR_crypto_ssh_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR crypto\-ssh package operational data.

This module contains definitions
for the following management objects\:
  ssh\: Crypto Secure Shell(SSH) data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Authen_Enum(Enum):
    """
    Authen_Enum

    SSH session authentication types

    """

    """

    Password

    """
    PASSWORD = 0

    """

    RSA public key encryption type

    """
    RSA_PUBLIC_KEY = 1

    """

    Keyboard interactive

    """
    KEYBOARD_INTERACTIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Authen_Enum']


class Cipher_Enum(Enum):
    """
    Cipher_Enum

    SSH session in and out cipher standards

    """

    """

    Advanced Encryption Standard(AES) 128 bits
    cipher block chaining(CBC)

    """
    AES128_CBC = 0

    """

    Advanced Encryption Standard(AES) 192 bits
    cipher block chaining(CBC)

    """
    AES192_CBC = 1

    """

    Advanced Encryption Standard(AES) 256 bits
    cipher block chaining(CBC)

    """
    AES256_CBC = 2

    """

    Triple Data Encryption Standard(DES) cipher
    block chaining(CBC)

    """
    TRIPLE_DES_CBC = 3


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Cipher_Enum']


class Connection_Enum(Enum):
    """
    Connection_Enum

    SSH channel connection types

    """

    """

    connection type not yet known

    """
    UNDEFINED = 0

    """

    Interactive Shell

    """
    SHELL = 1

    """

    Remote Command Execution

    """
    EXEC = 2

    """

    Secure Copy

    """
    SCP = 3

    """

    Secure File Transfer

    """
    SFTP_SUBSYSTEM = 4

    """

    Netconf Subsystem

    """
    NETCONF_SUBSYSTEM = 5


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Connection_Enum']


class Hostkey_Enum(Enum):
    """
    Hostkey_Enum

    SSH session authentication types

    """

    """

    Algorithm type DSS

    """
    SSH_DSS = 0

    """

    Algorithm type RSA

    """
    SSH_RSA = 1


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Hostkey_Enum']


class KexName_Enum(Enum):
    """
    KexName_Enum

    Different key\-exchange(kex) algorithms

    """

    """

    Diffie\-Hellman key exchange algorithm

    """
    DIFFIE_HELLMAN = 0

    """

    Password authenticated key agreement algorithm

    """
    PASSWORD_AUTHENTICATED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['KexName_Enum']


class Mac_Enum(Enum):
    """
    Mac_Enum

    Different Message Authentication Code(MAC)
    functions

    """

    """

    Hash\-based Message Authentication Code(HMAC)
    MD5 algorithm

    """
    HMAC_MD5 = 0

    """

    Hash\-based Message Authentication Code(HMAC)
    SHA1 algorithm

    """
    HMAC_SHA1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Mac_Enum']


class States_Enum(Enum):
    """
    States_Enum

    SSH session states

    """

    """

    SSH Open

    """
    OPEN = 1

    """

    SSH version OK

    """
    VERSION_OK = 2

    """

    Key exchange(KEX) init message exchanged

    """
    KEY_EXCHANGE_INITIALIZE = 3

    """

    Diffie\-Hellman(DH) secret is generated

    """
    KEY_EXCHANGE_DH = 4

    """

    New keys are received

    """
    NEW_KEYS = 5

    """

    Need more information to authenticate

    """
    AUTHENTICATE_INFORMATION = 6

    """

    The client successfully authenticated

    """
    AUTHENTICATED = 7

    """

    Channel has been successfully opened

    """
    CHANNEL_OPEN = 8

    """

    Allocated PTY

    """
    PTY_OPEN = 9

    """

    Opened an exec shell

    """
    SESSION_OPEN = 10

    """

    Received rekey request

    """
    REKEY = 11

    """

    Session is suspended

    """
    SUSPENDED = 12

    """

    Session has been closed

    """
    SESSION_CLOSED = 13


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['States_Enum']


class Version_Enum(Enum):
    """
    Version_Enum

    SSH state versions

    """

    """

    Version V2

    """
    V2 = 0

    """

    Version V1

    """
    V1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Version_Enum']



class Ssh(object):
    """
    Crypto Secure Shell(SSH) data
    
    .. attribute:: session
    
    	Crypto SSH session
    	**type**\: :py:class:`Session <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session>`
    
    

    """

    _prefix = 'crypto-ssh-oper'
    _revision = '2015-06-02'

    def __init__(self):
        self.session = Ssh.Session()
        self.session.parent = self


    class Session(object):
        """
        Crypto SSH session
        
        .. attribute:: brief
        
        	SSH session brief information
        	**type**\: :py:class:`Brief <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief>`
        
        .. attribute:: detail
        
        	SSH session detail information
        	**type**\: :py:class:`Detail <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail>`
        
        

        """

        _prefix = 'crypto-ssh-oper'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.brief = Ssh.Session.Brief()
            self.brief.parent = self
            self.detail = Ssh.Session.Detail()
            self.detail.parent = self


        class Brief(object):
            """
            SSH session brief information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\: :py:class:`IncomingSessions <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions>`
            
            .. attribute:: outgoing_sessions
            
            	List of outgoing sessions
            	**type**\: :py:class:`OutgoingSessions <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.incoming_sessions = Ssh.Session.Brief.IncomingSessions()
                self.incoming_sessions.parent = self
                self.outgoing_sessions = Ssh.Session.Brief.OutgoingSessions()
                self.outgoing_sessions.parent = self


            class IncomingSessions(object):
                """
                List of incoming sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of :py:class:`SessionBriefInfo <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.IncomingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_brief_info = YList()
                    self.session_brief_info.parent = self
                    self.session_brief_info.name = 'session_brief_info'


                class SessionBriefInfo(object):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\: :py:class:`Authen_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Authen_Enum>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\: :py:class:`Connection_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Connection_Enum>`
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\: :py:class:`States_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.States_Enum>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\: :py:class:`Version_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Version_Enum>`
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\: bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.authentication_type = None
                        self.channel_id = None
                        self.connection_type = None
                        self.host_address = None
                        self.node_name = None
                        self.session_id = None
                        self.session_state = None
                        self.user_id = None
                        self.version = None
                        self.vty_assigned = None
                        self.vty_line_number = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-brief-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.authentication_type is not None:
                            return True

                        if self.channel_id is not None:
                            return True

                        if self.connection_type is not None:
                            return True

                        if self.host_address is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.session_state is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        if self.version is not None:
                            return True

                        if self.vty_assigned is not None:
                            return True

                        if self.vty_line_number is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.session_brief_info is not None:
                        for child_ref in self.session_brief_info:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info']


            class OutgoingSessions(object):
                """
                List of outgoing sessions
                
                .. attribute:: session_brief_info
                
                	session brief info
                	**type**\: list of :py:class:`SessionBriefInfo <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_brief_info = YList()
                    self.session_brief_info.parent = self
                    self.session_brief_info.name = 'session_brief_info'


                class SessionBriefInfo(object):
                    """
                    session brief info
                    
                    .. attribute:: authentication_type
                    
                    	Authentication method
                    	**type**\: :py:class:`Authen_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Authen_Enum>`
                    
                    .. attribute:: channel_id
                    
                    	Channel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_type
                    
                    	Channel Connection Type
                    	**type**\: :py:class:`Connection_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Connection_Enum>`
                    
                    .. attribute:: host_address
                    
                    	Host address
                    	**type**\: str
                    
                    .. attribute:: node_name
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_state
                    
                    	SSH session state
                    	**type**\: :py:class:`States_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.States_Enum>`
                    
                    .. attribute:: user_id
                    
                    	User ID
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	SSH state version
                    	**type**\: :py:class:`Version_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Version_Enum>`
                    
                    .. attribute:: vty_assigned
                    
                    	Boolean indicating whether line VTY line number is valid
                    	**type**\: bool
                    
                    .. attribute:: vty_line_number
                    
                    	VTY line number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.authentication_type = None
                        self.channel_id = None
                        self.connection_type = None
                        self.host_address = None
                        self.node_name = None
                        self.session_id = None
                        self.session_state = None
                        self.user_id = None
                        self.version = None
                        self.vty_assigned = None
                        self.vty_line_number = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:outgoing-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-brief-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.authentication_type is not None:
                            return True

                        if self.channel_id is not None:
                            return True

                        if self.connection_type is not None:
                            return True

                        if self.host_address is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.session_state is not None:
                            return True

                        if self.user_id is not None:
                            return True

                        if self.version is not None:
                            return True

                        if self.vty_assigned is not None:
                            return True

                        if self.vty_line_number is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief/Cisco-IOS-XR-crypto-ssh-oper:outgoing-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.session_brief_info is not None:
                        for child_ref in self.session_brief_info:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:brief'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                    return True

                if self.incoming_sessions is not None and self.incoming_sessions.is_presence():
                    return True

                if self.outgoing_sessions is not None and self.outgoing_sessions._has_data():
                    return True

                if self.outgoing_sessions is not None and self.outgoing_sessions.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Brief']['meta_info']


        class Detail(object):
            """
            SSH session detail information
            
            .. attribute:: incoming_sessions
            
            	List of incoming sessions
            	**type**\: :py:class:`IncomingSessions <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions>`
            
            .. attribute:: outgoing_connections
            
            	List of outgoing connections
            	**type**\: :py:class:`OutgoingConnections <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections>`
            
            

            """

            _prefix = 'crypto-ssh-oper'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.incoming_sessions = Ssh.Session.Detail.IncomingSessions()
                self.incoming_sessions.parent = self
                self.outgoing_connections = Ssh.Session.Detail.OutgoingConnections()
                self.outgoing_connections.parent = self


            class IncomingSessions(object):
                """
                List of incoming sessions
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of :py:class:`SessionDetailInfo <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.IncomingSessions.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_detail_info = YList()
                    self.session_detail_info.parent = self
                    self.session_detail_info.name = 'session_detail_info'


                class SessionDetailInfo(object):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\: :py:class:`Cipher_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Cipher_Enum>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\: :py:class:`Mac_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Mac_Enum>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\: :py:class:`KexName_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.KexName_Enum>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\: :py:class:`Cipher_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Cipher_Enum>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\: :py:class:`Mac_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Mac_Enum>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\: :py:class:`Hostkey_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Hostkey_Enum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.in_cipher = None
                        self.in_mac = None
                        self.key_exchange = None
                        self.out_cipher = None
                        self.out_mac = None
                        self.public_key = None
                        self.session_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.in_cipher is not None:
                            return True

                        if self.in_mac is not None:
                            return True

                        if self.key_exchange is not None:
                            return True

                        if self.out_cipher is not None:
                            return True

                        if self.out_mac is not None:
                            return True

                        if self.public_key is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:incoming-sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.session_detail_info is not None:
                        for child_ref in self.session_detail_info:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info']


            class OutgoingConnections(object):
                """
                List of outgoing connections
                
                .. attribute:: session_detail_info
                
                	session detail info
                	**type**\: list of :py:class:`SessionDetailInfo <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo>`
                
                

                """

                _prefix = 'crypto-ssh-oper'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.session_detail_info = YList()
                    self.session_detail_info.parent = self
                    self.session_detail_info.name = 'session_detail_info'


                class SessionDetailInfo(object):
                    """
                    session detail info
                    
                    .. attribute:: in_cipher
                    
                    	In cipher algorithm
                    	**type**\: :py:class:`Cipher_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Cipher_Enum>`
                    
                    .. attribute:: in_mac
                    
                    	In MAC
                    	**type**\: :py:class:`Mac_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Mac_Enum>`
                    
                    .. attribute:: key_exchange
                    
                    	Key exchange name
                    	**type**\: :py:class:`KexName_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.KexName_Enum>`
                    
                    .. attribute:: out_cipher
                    
                    	Out cipher algorithm
                    	**type**\: :py:class:`Cipher_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Cipher_Enum>`
                    
                    .. attribute:: out_mac
                    
                    	Out MAC
                    	**type**\: :py:class:`Mac_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Mac_Enum>`
                    
                    .. attribute:: public_key
                    
                    	Host key algorithm
                    	**type**\: :py:class:`Hostkey_Enum <ydk.models.crypto.Cisco_IOS_XR_crypto_ssh_oper.Hostkey_Enum>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'crypto-ssh-oper'
                    _revision = '2015-06-02'

                    def __init__(self):
                        self.parent = None
                        self.in_cipher = None
                        self.in_mac = None
                        self.key_exchange = None
                        self.out_cipher = None
                        self.out_mac = None
                        self.public_key = None
                        self.session_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections/Cisco-IOS-XR-crypto-ssh-oper:session-detail-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.in_cipher is not None:
                            return True

                        if self.in_mac is not None:
                            return True

                        if self.key_exchange is not None:
                            return True

                        if self.out_cipher is not None:
                            return True

                        if self.out_mac is not None:
                            return True

                        if self.public_key is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                        return meta._meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail/Cisco-IOS-XR-crypto-ssh-oper:outgoing-connections'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.session_detail_info is not None:
                        for child_ref in self.session_detail_info:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                    return meta._meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session/Cisco-IOS-XR-crypto-ssh-oper:detail'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.incoming_sessions is not None and self.incoming_sessions._has_data():
                    return True

                if self.incoming_sessions is not None and self.incoming_sessions.is_presence():
                    return True

                if self.outgoing_connections is not None and self.outgoing_connections._has_data():
                    return True

                if self.outgoing_connections is not None and self.outgoing_connections.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
                return meta._meta_table['Ssh.Session.Detail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-crypto-ssh-oper:ssh/Cisco-IOS-XR-crypto-ssh-oper:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.brief is not None and self.brief._has_data():
                return True

            if self.brief is not None and self.brief.is_presence():
                return True

            if self.detail is not None and self.detail._has_data():
                return True

            if self.detail is not None and self.detail.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
            return meta._meta_table['Ssh.Session']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-crypto-ssh-oper:ssh'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.session is not None and self.session._has_data():
            return True

        if self.session is not None and self.session.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.crypto._meta import _Cisco_IOS_XR_crypto_ssh_oper as meta
        return meta._meta_table['Ssh']['meta_info']

