'''
@auther: exoticknight, JP

'''
import XenAPI

# session
class session():
    def __init__(self, url, user, pwd):
        self._url = url
        self._user = user
        self._pwd = pwd

    def get_connection(self):
        '''
        get the session from the master of the pool
        '''
        try:
            self._session = XenAPI.Session(self._url)
            self._session.xenapi.login_with_password(self._user, self._pwd)
        except XenAPI.Failure, e:
            # logout and reset the __session
            print e
            raise

    def absort_connection(self):
        '''
        close the session
        '''
        try:
            self._session.xenapi.session.logout()
        except XenAPI.Failure, e:
            print e
            raise

    def get_running_vm(self):
        '''
        return a dict of all running VMs in the pool
        '''
        try:
            vms = {}
            allVM = self._session.xenapi.VM.get_all()
            for vm in allVM:
                record = self._session.xenapi.VM.get_record(vm)
                if not record["is_control_domain"] and \
                   not 'Transfer' in record["name_label"] and \
                   not record["is_a_template"] and \
                   record["power_state"] == "Running":
                    vms[vm] = record
                    # print record["name_label"]
            return vms
        except XenAPI.Failure, e:
            print e
            self.absort_connection()
            raise

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


