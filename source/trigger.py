import sys
import time
import argparse
import traceback
import os
import subprocess


from pyndn import Interest
from pyndn import Data
from pyndn import Exclude
from pyndn import Name
from pyndn import Face
from pyndn import InterestFilter
from pyndn.security import KeyChain
from modules.tools.enumerate_publisher import EnumeratePublisher

# from NOMAD import enumerate_publisher
class trigger(object):
    def __init__(self):

        self.script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
        self.script_dir = os.path.split(self.script_path)[0] #i.e. /path/to/dir/
        self.Datamessage_size = 8000 #8kB --> Max Size from NDN standard

        prefix_serviceDiscovery = "/sm/service_discovery"
        self.prefix_serviceDiscovery = Name(prefix_serviceDiscovery)

        prefix_serviceRegistration = "/sm/service_registration"
        self.prefix_serviceRegistration = Name(prefix_serviceRegistration)

        prefix_serviceMigration = "/sm/service_migration"
        self.prefix_serviceMigration = Name(prefix_serviceMigration)

        prefix_serviceMigrationPush = "/sm/service_migration/push"
        self.prefix_serviceMigrationPush = Name(prefix_serviceMigrationPush)

        prefix_trigger = "/trigger"
        self.prefix_trigger = Name(prefix_trigger)

        prefix_start_DTN_demo = "/sm/start_DTN_demo"
        self.prefix_start_DTN_demo = Name(prefix_start_DTN_demo)

        prefix_serviceMigration_KEBAPP = "/kebapp/maps/routefinder/"
        self.prefix_serviceMigration_KEBAPP = Name(prefix_serviceMigration_KEBAPP)

        self.prefix_DE = "/picasso/start_de/"
        self.prefix_DE = Name(prefix_DE)

        #prefix_deployment_pull = "/picasso/service_deployment_pull/"
        #self.prefix_deployment_pull = Name(prefix_deployment_pull)

        # Default configuration of NDN
        self.outstanding = dict()
        self.isDone = False
        self.keyChain = KeyChain()
        self.face = Face("127.0.0.1")

        self.face.setCommandSigningInfo(self.keyChain, \
                                        self.keyChain.getDefaultCertificateName())
        #self.face.registerPrefix(self.prefix_deployment_pull, self.onInterest_PullService, self.onRegisterFailed)
        #print "Registering prefix : " + self.prefix_deployment_pull.toUri()

    def run(self):
        try:
            # send Interest message to retrieve data
            #self.sendNextInterest(self.prefix_serviceMigration)
            print 'Available services'
            print '   (1) uhttpd'
            print '   (2) umobilestore'
            service_name = raw_input('Choose service to be deployed')

            if service_name == 'uhttpd':
                print 'Start deploying uhttpd'
            if service_name == 'umobilestore':
                print 'Start deploying umobilestore'
            else:
                print 'Chosen service is not available'
            name_prefix = self.prefix_DE+service_name+'.tar'
            self.sendPushInterest(name_prefix)

            # while not self.isDone:
            #     self.face.processEvents()
            #     time.sleep(0.01)

        except RuntimeError as e:
            print "ERROR: %s" % e


if __name__ == '__main__':

    try:

        trigger().run()

    except:
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)



