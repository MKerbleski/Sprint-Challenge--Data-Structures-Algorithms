class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #make function a lambda function
    #have the callback iterate over eact item in depth first order utilizing stack data structure. 
    
    # print('\nnew depth')
    # print(self.value, 'value')
    if self.value != None:
      cb(self.value)
      # print(self.value, 'appended')
      if self.left != None:
        # print(self.left.value, 'self.left.value')
        if self.left.left != None: 
          # print('self.left.left exists next line should be new depth')
          self.left.depth_first_for_each(cb)
        else: 
          cb(self.left.value)
          # print(self.left.value, 'self.left.value appended')
          if self.left.right != None:
            # print('something is self.left.right')
            # print('self.left.right.depth to be called')
            self.left.right.depth_first_for_each(cb)
      if self.right != None:
        # print(self.right.value, 'value-right')
        self.right.depth_first_for_each(cb)
        # print(self.right.value, 'right')  
    else: 
      print('no left of right values')

    # go left until you can go left no more 
    #then go back a step and go right 
    #repeat until everything is hit
  
  def breadth_first_for_each(self, cb):
    #make function a lambda function
    #same as above but with bredth first 
    global queue
    global data
    global level

    queue = []
    data = {
      0:[],
      1:[],
      2:[]
    }
  
    level = 0
   
    return self._inner_(self, level)

    [cb(i) for i in queue]
    #go left first than right
    #then repeat with children of the left 
      #followed by children of the right 
    #repeat until all done. 
    pass

  def _inner_(self, level):
    print('\ninner level', level)
    if self.value != None:
      data[level].append(self.value)
      print("data", data)
      if self.left != None:
        return self.left.inner(level +1)
      if self.right != None:
        return self.right.inner(level +1)
        # queue.append(self.right.value)
      print(self.left.value)
      if self.left.left:
        queue.append(self.left.left.value)
      if self.left.right != None:
        queue.append(self.left.right.value)
      if self.right.left != None:
        queue.append(self.right.left.value)
      if self.right.right != None:
        queue.append(self.right.right.value)
      if self.right != None:
        print('b')
      else:
        print("self.left.left.value none")


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
