filename=raw_input("Enter the name of the file to output your topology:")
ofile = open(filename,"w")

def fullMesh(nSwitches):
    #setting ids
    hid=1
    mnid=1
    for i in range(nSwitches):
        sid=i+1
        sName="s"+str(sid)
        ofile.write("       ")
        ofile.write(sName+"="+str(mnid)+"\n")
        mnid+=1
        h1Name="h"+str(hid)
        ofile.write("       ")
        ofile.write(h1Name+"="+str(mnid)+"\n")
        mnid+=1
        hid+=1
        h2Name="h"+str(hid)
        ofile.write("       ")
        ofile.write(h2Name+"="+str(mnid)+"\n")
        mnid+=1
        hid+=1
        
    ofile.write("\n")
    #adding components to the topology
    hid=1
    for i in range(nSwitches):
        sid=i+1
        sName="s"+str(sid)
        ofile.write("       ")
        ofile.write("self.add_node( "+sName+", Node( is_switch=True ) )\n")
        h1Name="h"+str(hid)
        ofile.write("       ")
        ofile.write("self.add_node( "+h1Name+", Node( is_switch=False ) )\n")
        hid+=1
        h2Name="h"+str(hid)
        hid+=1
        ofile.write("       ")
        ofile.write("self.add_node( "+h2Name+", Node( is_switch=False ) )\n")

    ofile.write("\n")
    #linking switches to hosts
    hid=1
    for i in range(nSwitches):
        sid=i+1
        sName="s"+str(sid)
        h1Name="h"+str(hid)
        ofile.write("       ")
        ofile.write("self.add_edge("+ sName+","+h1Name+" )\n")
        hid+=1
        h2Name="h"+str(hid)
        ofile.write("       ")
        ofile.write("self.add_edge("+ sName+","+h2Name+" )\n")
        hid+=1
    ofile.write("\n")
    
    #linking switches to switches
    for i in range(1,nSwitches):
        for j in range(i+1,nSwitches+1):
            ofile.write("       self.add_edge( s"+str(i)+",s"+str(j)+")\n")
    
    ofile.write("\n")

def star(nSwitches):
    #setting ids
    hid=1
    mnid=1
    for i in range(nSwitches):
        sid=i+1
        sName="s"+str(sid)
        ofile.write("       ")
        ofile.write(sName+"="+str(mnid)+"\n")
        mnid+=1
        h1Name="h"+str(hid)
        ofile.write("       ")
        ofile.write(h1Name+"="+str(mnid)+"\n")
        mnid+=1
        hid+=1
        h2Name="h"+str(hid)
        ofile.write("       ")
        ofile.write(h2Name+"="+str(mnid)+"\n")
        mnid+=1
        hid+=1
        
    ofile.write("\n")
    #adding components to the topology
    hid=1
    for i in range(nSwitches):
        sid=i+1
        sName="s"+str(sid)
        ofile.write("       ")
        ofile.write("self.add_node( "+sName+", Node( is_switch=True ) )\n")
        h1Name="h"+str(hid)
        ofile.write("       ")
        ofile.write("self.add_node( "+h1Name+", Node( is_switch=False ) )\n")
        hid+=1
        h2Name="h"+str(hid)
        hid+=1
        ofile.write("       ")
        ofile.write("self.add_node( "+h2Name+", Node( is_switch=False ) )\n") 
           	
    ofile.write("\n")
    #linking 4 or less switchs to the switch #1
    s=2
    for i in range(s,nSwitches):
        if s>5:
			break
        ofile.write("       self.add_edge( s1"+",s"+str(s)+")\n")
    
    #linking remaining switches to the "leaves"
    ofile.write("\n")
    leaves={}
    nLeaves=nSwitches-1
    
    if nSwitches==1:
		leaves.append(1)
		nLeaves=1
    
    l=2    
    for i in range(nLeaves):
        leaves.append(l)
        l+=1
    
    s=0
    for i in range(nLeaves+1,nSwitches):
        ofile.write("       self.add_edge( s"+str(leaves[s])+",s"+str(i+1)+")\n")
        leaves[s]=i+1
        s+=1
        if s==4:
            s=0    			                		    

                                                            					         	    
ofile.write("from mininet.topo import Topo, Node\n")
ofile.write("class MyTopo( Topo ):\n")
ofile.write("   def __init__( self, enable_all = True ):\n")
ofile.write("       super( MyTopo, self ).__init__()\n")

#-------------------------------------------------------------------------------

nSwitches=int(raw_input("Enter the number of switches of your topology:"))
fullMesh(nSwitches)


ofile.write("       self.enable_all()\n")
ofile.write("topos = { 'mytopo': ( lambda: MyTopo() ) }\n")
	
ofile.close()
