#binary tree node
class Node:
    father = None
    left = None
    right = None
    key = 0
    def __init__(self,key,father = None,left = None,right = None):
        super().__init__()
        self.father = father
        self.left = left
        self.right = right
        self.key = key
#a kind of simulation of a real procedure
class Procedure:
    __context = {'steps':[]}
    __next = 0
    def __init__(self,context,steps):
        super().__init__()
        context['steps'] = steps
        self.__context = context

    def nextStep(self):
        tem = self.__context['steps'][self.__next](self.__context) #do as a function
        self.__next = self.__next + 1
        return tem

    def isComplete(self):
        if len(self.__context['steps']) < self.__next + 1:
            return True
        else:
            return False

#a stack used to store doing procedures
class ProcedureStack:
    __allProcedures = []
    def push(self, procedure):
        self.__allProcedures.append(procedure)
    def pop(self):
        self.__allProcedures.pop(-1)
    def top(self):
        return self.__allProcedures[-1]
    def isEmpty(self):
        if len(self.__allProcedures) <= 0:
            return True
        else:
            return False

#trditional recursion (used to test binary tree)
def PrintRecursion(root):
    if root.left == None:
        print(root.key)
        return
    PrintRecursion(root.left)
    print(root.key)
    PrintRecursion(root.right)

#step function1 in recursion simulation
def ProbeLeft(context):
    stack = context['stack']
    root = context['root']
    steps = context['steps']
    left = root.left

    if left == None :
        return True

    newContext  = {'root':root.left,'stack':stack}
    newProcedure = Procedure(newContext,steps)
    stack.push(newProcedure)
    return False
#step function2 in recursion simulation
def PrintKey(context):
    root = context['root']
    print(root.key)
    return True
#step function3 in recursion simulation
def ProbeRight(context):
    stack = context['stack']
    root = context['root']
    steps = context['steps']
    right = root.right

    if right == None :
        return True

    newContext  = {'root':root.right,'stack':stack}
    newProcedure = Procedure(newContext,steps)
    stack.push(newProcedure)

    return False


#initalize the testing binary tree
node1 = Node(5)
node1L = Node(4,node1)
node1R = Node(6,node1)
node1.left = node1L
node1.right = node1R

node1LL = Node(3,node1L)
node1LR = Node(8,node1L)
node1L.left = node1LL
node1L.right = node1LR

#initalization of recursion
recursionStack = ProcedureStack()
usingSteps = [ProbeLeft,PrintKey,ProbeRight]
rootPro = Procedure({"root":node1,'stack':recursionStack},usingSteps)
recursionStack.push(rootPro)

#simulate the real process of real recursion

while not recursionStack.isEmpty():
    top = recursionStack.top()
    while True:
        if top.isComplete():
            recursionStack.pop()
            break
        if not top.nextStep() :
            break



