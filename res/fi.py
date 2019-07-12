"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class FI_TOPO( Topo ):
    "FI Topology."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        left_host = self.addHost( 'h1' )
        right_host = self.addHost( 'h2' )
        vnf = self.addHost('sf')
        left_switch = self.addSwitch( 's1' )
        right_switch = self.addSwitch('s2')
        # # Add links
        # self.addLink( left_host, vnf )
        # self.addLink( vnf, main_switch )
        # self.addLink( right_host, main_switch)
        
        self.addLink(left_host,left_switch)
        self.addLink(left_switch,vnf)
        self.addLink(vnf,right_switch)
        self.addLink(right_host,right_switch)




topos = { 'fi_topo': ( lambda: FI_TOPO() ) }
