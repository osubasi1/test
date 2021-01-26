def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """   
    # intances < 25 then reduce instance by half if it is not 1
    # Between 25 and 60 --> no action
    # larger than 60 then double the instance (limit is 2* 10^8)
    # If any action is taken then no check for 10 sec
    i = 0
    while i < len(averageUtil)-1:
        print("averageUtil[i] is:", averageUtil[i])
        if action(averageUtil[i],instances)[0]:
            instances = action(averageUtil[i],instances)[1]
            print("instances is:", instances)
            
            i += 9
        else:
            i += 1
    return instances
            
def action (utilTime, instance):
    
    isAction = False
    if utilTime < 25:
        if instance > 1:
            instance = (instance+1) //2
            isAction = True
    elif utilTime > 60:
        instance = instance*2
        isAction = True
        if instance > 2* 10**8:
            instance = 2* 10**8
            
    return isAction,instance
        
print(finalInstances(1,[30, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89, 15, 18, 18, 19, 89]))
