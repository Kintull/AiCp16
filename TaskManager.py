from MapManager import MapManager

MapMgr = MapManager()

mandatory_tasks = ['push_top','push_mid','push_bot']
addictional_tasks = ['take_rune','def_top','def_mid','def_bot']
task_queue = []

if !task_queue:
    task = mandatory_tasks[0]
    task_queue.append(task)
    

current_task = task_queue.pick()



if current_task == 'push_top':
    MapMgr.blockArea(MapMgr.top_blocks) #add top part of map to blocked area
    MapMgr.goTo(MapMgr.home) #go to the home location
    destination = MapMgr.getPushPoint('top') #get point where to go to
    