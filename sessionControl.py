'''
@auther: exoticknight, JP

'''
import XenAPI

# session
__session = ''
__xenapi = ''

def get_connection(url, userName, password):
    '''
    get the session from the master of the pool
    '''
    try:
        __session = XenAPI.Session(url)
        __session.xenapi.login_with_password(userName, password)
        __xenapi = __session.xenapi
    except:
        # logout and reset the __session
        print 'Failed to get connection!'
        __session.xenapi.session.logout()
        __session = ''

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

def absort_connection():
    '''
    close the session
    '''
    try:
        __session.xenapi.session.logout()
    except:
        pass
