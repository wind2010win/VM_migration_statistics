'''
@auther: exoticknight, JP
'''
import XenAPI

# session
__session = ''

def getConnection(url, userName, password):
    '''
    get the session by the init
    '''
    __session = XenAPI.Session(url)
    __session.xenapi.login_with_password(userName, password)

def create_VM():
    '''
    create a VM
    '''
    #do something
    pass

def start_VM_by_id(uuid):
    '''
    start a VM by uuid
    '''
    #do something
    pass

def start_vm_by_name(name):
    '''
    start a VM by name
    '''
    #do something
    pass
    
def stop_VM_by_id(uuid):
    '''
    stop a VM by uuid
    '''
    #do something
    pass

def stop_VM_by_name(name):
    '''
    stop a VM by name
    '''
    #do something
    pass

def migrate_VM(source, destination, VM, mode):
    '''
    migrate a VM from source to destination
    mode is either 'test' or 'statistics'
    '''
    #do something
    pass

def close_session():
    '''
    close the session
    '''
    #do something
    pass
