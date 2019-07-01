import pickle 
# nodeData={
# "name":"N1",
# "position":(0,0),
# "children":[],
# "distances":{},
# "direction":"follow",#or "left" or "follow",
# "decision":False # orFalse
# }

# class Node:
#     def __init__(self,name):
#         self.name = name
#         self.position=None
#         self.children=[]
#         self.distances={}
#         self.isDecision=False
        
#     def addNodeData(self, nodeData):
#         self.position= nodeData['position']
#         self.children= nodeData['children']
#         self.distances= nodeData['distances']
#         self.isDecision= nodeData['decision']

#     def printNode(self):
#         print("Node Name: ", self.name)
#         print("Node Postion: ", self.position)
#         print("Node Children: ", self.children)
#         print("Node Distances: ", self.distances.values())
#         print("is Node a Decision node: ", self.isDecision) 

# Load Pickled Data
dbfile = open('graghData', 'rb')      
db = pickle.load(dbfile) 
print(db['N1'])
# for keys in db: 
#     print(keys, '=>', db[keys]) 
dbfile.close() 