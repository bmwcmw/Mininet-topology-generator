from mininet.topo import Topo, Node
class MyTopo( Topo ):
   def __init__( self, enable_all = True ):
       super( MyTopo, self ).__init__()
       s1=1
       h1=2
       h2=3
       s2=4
       h3=5
       h4=6
       s3=7
       h5=8
       h6=9
       s4=10
       h7=11
       h8=12
       s5=13
       h9=14
       h10=15

       self.add_node( s1, Node( is_switch=True ) )
       self.add_node( h1, Node( is_switch=False ) )
       self.add_node( h2, Node( is_switch=False ) )
       self.add_node( s2, Node( is_switch=True ) )
       self.add_node( h3, Node( is_switch=False ) )
       self.add_node( h4, Node( is_switch=False ) )
       self.add_node( s3, Node( is_switch=True ) )
       self.add_node( h5, Node( is_switch=False ) )
       self.add_node( h6, Node( is_switch=False ) )
       self.add_node( s4, Node( is_switch=True ) )
       self.add_node( h7, Node( is_switch=False ) )
       self.add_node( h8, Node( is_switch=False ) )
       self.add_node( s5, Node( is_switch=True ) )
       self.add_node( h9, Node( is_switch=False ) )
       self.add_node( h10, Node( is_switch=False ) )

       self.add_edge( s1,s2)
       self.add_edge( s1,s3)
       self.add_edge( s1,s4)
       self.add_edge( s1,s5)


       self.add_edge(s2,h1 )
       self.add_edge(s3,h2 )
       self.add_edge(s4,h3 )
       self.add_edge(s5,h4 )
       self.add_edge(s2,h5 )
       self.add_edge(s3,h6 )
       self.add_edge(s4,h7 )
       self.add_edge(s5,h8 )
       self.add_edge(s2,h9 )
       self.add_edge(s3,h10 )

       self.enable_all()
topos = { 'mytopo': ( lambda: MyTopo() ) }
