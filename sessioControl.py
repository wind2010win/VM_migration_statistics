import XenAPI
class sessionControl:
    
    # init the session
    session = XenAPI.xapi_local()
    
    # get the session by the init
    def __init__(self, url, userName, password):
        session = XenAPI.Session(url)
        session.xenapi.login_with_password(userName, password)

    # create a VM
    def create_VM():
        #do something
        pass

    # start a VM by uuid
    def start_VM_by_id(uuid):
        #do something
        pass

    # start a VM by name
    def start_vm_by_name(name):
        #do something
        pass
        
    # stop a VM by uuid
    def stop_VM_by_id(uuid):
        #do something
        pass

    # stop a VM by name
    def stop_VM_by_name(name):
        #do something
        pass

    # migrate a VM from source to destination
    # mode is either 'test' or 'statistics'
    def migrate_VM(source, destination, VM, mode):
        #do something
        pass
    
    # close the session
    def close_session():
        #do something
        pass
