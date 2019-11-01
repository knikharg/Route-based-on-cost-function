
#!/usr/local/bin/python3
# route.py : Road trip!
#
# Code by: Kasturi Nikharge (knikharg), Vrinda Mathur(vrmath), Neha Tayade (ntayade)

#from math import radians, cos, sin, asin, sqrt
         
import heapq
import sys 

class Graph(object):
    def __init__(self,graph):
        if graph == None:
            graph = {}
        self.graph = graph
        
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node]=[]
    
    def add_edge(self,node1,node2,length,speed,highway_name):
        gas_gallons=float(length)/(float(400/150) * float(speed) * float(1-(float(speed)/150))**4)
        if node1 in self.graph:
            self.graph[node1].append((node2,length,float(length)/float(speed),gas_gallons))
        else:
            self.graph[node1] = [(node2,length,float(length)/float(speed),gas_gallons)]
        if node2 in self.graph:
            self.graph[node2].append((node1,length,float(length)/float(speed),gas_gallons))
        else:
            self.graph[node2] = [(node1,length,float(length)/float(speed),gas_gallons)]
            
    def edges(self,node):
        return self.graph[node]

  
#gets successors for current and pops out the one with least fN     
def successors(fN,route_so_far,distance,time,total_gas_gallons):
    city=route_so_far.split()[-1]
    possible_path=g.edges(city)
    if sysargv2 =="time":
        return [(time + float(node[1])/float(node[2]),*node,) for node in  possible_path]
    elif sysargv2 == "mpg":
        return [ (total_gas_gallons + node[3],*node) for node in  possible_path]
    elif sysargv2 == "distance":
        return [ (distance + float(node[1]), *node) for node in  possible_path]
    elif sysargv2 == "segments":
        return [ (len(str(route_so_far).split())+1, *node) for node in  possible_path]
        
def solve(graph):
    queue=[]
    blank=" "
    heapq.heappush(queue, (0,city1,0,0,0))
    while len(queue)>0:
        (fN,route_so_far,total_distance,total_time,total_gas_gallons) = heapq.heappop(queue)
        
        for (fN_path,path,distance,time,gas_gallons) in successors(fN,route_so_far,total_distance,total_time,total_gas_gallons):
            if path.split()[-1]== city2:
                return(len(route_so_far.split()),float(distance) + float(total_distance),float(time)+float(total_time), float(total_gas_gallons) + float(gas_gallons),route_so_far + blank + path)
            heapq.heappush(queue,(fN_path,route_so_far + blank + path,float(total_distance) + float(distance),float(total_time) + float(time),float(total_gas_gallons) +float(gas_gallons)))
    return False
    
            

if __name__ == "__main__":
    
    #===========================================================================
    # sysargv2 =sys.argv[2]
    # city1 = sys.argv[0]
    # city2 = sys.argv[1]
    #===========================================================================
    #citylist=[]
    sysargv2 = "distance"
    city2 = "Bloomington,_Indiana"
    city1 = "Las_Vegas,_Nevada"
    #===========================================================================
    # with open("city-gps", 'r') as file:
    #     for line in file:
    #         citylist.append([str(i) for i in line.split()])
    #===========================================================================
    g = Graph({})
    with open("road-segments", 'r') as file:
        for line in file:
            segment=[str(i) for i in line.split()]
            g.add_edge(segment[0], segment[1],segment[2],segment[3],segment[4])
    if city1==city2 or len(g.edges(city1))==0:
        print("Inf")
    else:
        output=solve(g.graph)
        print(str(int(output[0])) + " "+ str(int(output[1])) + " " + str(round(output[2],4)) + " " + str(round(output[3],4)) + " " + str(output[4])) if output!= False else print("Inf")
        
    
