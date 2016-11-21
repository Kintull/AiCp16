from MapManager import MapManager

def test():
    result = {}
    
    MapMgr = MapManager()
    #print sorted(MapMgr.all_blocks)
    
    #print "In test block_area:"
    MapMgr.block_area(MapMgr.top_blocks)
    #print sorted(MapMgr.all_blocks)
    if sorted(MapMgr.all_blocks)!= sorted([5, 6, 7, 21, 22, 32]):
        result['block_area'] = 'Fault'
        
    #print "In test unblock_area:"
    MapMgr.unblock_area(MapMgr.top_blocks)
    if sorted(MapMgr.all_blocks) != sorted([7,41,42,8,11,12,5,22,21,6,32]):
        #print sorted(MapMgr.all_blocks)
        #print sorted([7,41,42,8,11,12,5,22,21,6,32])
        result['unblock_area'] = 'Fault'
        
        
        
    if result == {}:
        return 'No faults'
    else:
        return result
    
if __name__ == "__main__":
    print test()
