
#!/usr/bin/env python
""" generated source for module MainActivity """

import io

import math
 

class Coordinates(object):
    """ generated source for class Coordinates """

    def __init__(self, c):
        """ generated source for method __init__ """
        coord  = []
        for i in c:
            coord.append(i)
            i+=1
        self.coords = coord

    def __hash__(self):
        return hash(str(self.coords))
        
    def __eq__(self, other):
        other_list = (other).coords
        if len(other_list) != len(self.coords):
            return False
        i = 0
        while i < len(self.coords):
            if int(self.coords[i]) != int(other_list[i]):
                return False
            i += 1
        return True

    def getCoords(self):
        coord = []
        for c in self.coords:
            coord.append(c)
        return coord

    def getDimension(self, d):
        """ generated source for method getDimension """
        if self.coords != None and len(self.coords) > d:
            return self.coords[d]
        else:
           # print "Cannot get selected value"
            return None

    def setDimension(self, d, val):
        """ generated source for method setDimension """
        if self.coords != None and len(self.coords) > d:
            self.coords[d] = val
        else:
            print "Cannot set selected value"

    def getSize(self):
        """ generated source for method getSize """
        return len(self.coords)

    def equals(self, other):
        """ generated source for method equals """

        other_list = (other).coords
        if len(other_list) != len(self.coords):
            return False
        i = 0
        while i < len(self.coords):
            if int(self.coords[i]) != int(other_list[i]):
                return False
            i += 1
        return True

    def __str__(self):
        """ generated source for method toString """
        return self.coords.__str__()
# ============================================================================================================================================================================

class ATTRIBUTE:
    """ generated source for enum ATTRIBUTE """
    DENSE = u'DENSE'
    TRANSITIONAL = u'TRANSITIONAL'
    SPARSE = u'SPARSE'

#  Characteristic vector of a grid
class Grid(object):
    """ generated source for class Grid """

    visited = False
    last_time_updated = 0
    last_time_element_added = 0
    grid_density = 0.0
    grid_attribute = ATTRIBUTE.SPARSE
    attraction_list = list()
    cluster = -1
    attributeChanged = False
    DIMENSION =0
    DIMENSION_UPPER_RANGE =0 
    DIMENSION_LOWER_RANGE =0 
    DIMENSION_PARTITION = 0
    TOTAL_GRIDS =0
    decay_factor =0 
    dense_threshold =0 
    sparse_threshold =0
    correlation_threshold =0
    

    def __init__(self, v, c, tg, D, attr, dim, dim_upper, dim_lower, dim_par, total_grids, decay, d_thres, s_thres,c_thres):
        """ generated source for method __init__ """
        self.visited = v
        self.cluster = c
        self.last_time_updated = tg
        self.grid_density = D
        self.grid_attribute = attr
        self.DIMENSION = dim
        self.DIMENSION_UPPER_RANGE = dim_upper 
        self.DIMENSION_LOWER_RANGE =dim_lower 
        self.DIMENSION_PARTITION = dim_par
        self.TOTAL_GRIDS = total_grids
        self.decay_factor = decay
        self.dense_threshold = d_thres
        self.sparse_threshold = s_thres
        self.correlation_threshold = c_thres
        '''
        attr_l = list()
        i =0 
        while i < 2*dim +1:
            attr_l[i] = 1
            i += 1
        '''
        self.attraction_list = list()


    def __hash__(self):
        return hash(str(self.name))
    
    def __eq__(self, other):
        return str(self.name) == str(other.name)


    def setVisited(self, v):
        """ generated source for method setVisited """
        self.visited = v

    def isVisited(self):
        """ generated source for method isVisited """
        return self.visited

    def setCluster(self, c):
        """ generated source for method setCluster """
        self.cluster = c

    def getCluster(self):
        """ generated source for method getCluster """
        return self.cluster

    def setLastTimeUpdated(self, tg):
        """ generated source for method setLastTimeUpdated """
        self.last_time_updated = tg

    def getLastTimeUpdated(self):
        """ generated source for method getLastTimeUpdated """
        return self.last_time_updated

    def setLastTimeElementAdded(self, tg):
        """ generated source for method setLastTimeElementAdded """
        self.last_time_element_added = tg

    def getLastTimeElementAdded(self):
        """ generated source for method getLastTimeElementAdded """
        return self.last_time_element_added

    def getGridDensity(self):
        """ generated source for method getGridDensity """
        return self.grid_density

    def updateGridDensity(self, time):
        """ generated source for method updateGridDensity """
        self.grid_density = self.grid_density * (math.pow(self.decay_factor, time - self.last_time_updated)) + 1

    def updateDecayedGridDensity(self, time):
        """ generated source for method updateDecayedGridDensity """
        self.grid_density = self.grid_density * (math.pow(self.decay_factor, time - self.last_time_updated))

    def isAttributeChangedFromLastAdjust(self):
        """ generated source for method isAttributeChangedFromLastAdjust """
        return self.attributeChanged

    def setAttributeChanged(self, val):
        """ generated source for method setAttributeChanged """
        self.attributeChanged = val

    def isDense(self):
        """ generated source for method isDense """
        #print " Call is DENSE"
        return self.grid_attribute == ATTRIBUTE.DENSE

    def isTransitional(self):
        """ generated source for method isTransitional """
        return self.grid_attribute == ATTRIBUTE.TRANSITIONAL

    def isSparse(self):
        """ generated source for method isSparse """
        return self.grid_attribute == ATTRIBUTE.SPARSE

    def getGridAttribute(self):
        """ generated source for method getGridAttribute """
        str_ = ""
        if self.isDense():
            str_ = "DENSE"
        if self.isTransitional():
            str_ = "TRANSITIONAL"
        if self.isSparse():
            str_ = "SPARSE"
        return str_

    def updateGridAttribute(self):
        """ generated source for method updateGridAttribute """
        avg_density = 1.0 / (self.TOTAL_GRIDS * (1 - self.decay_factor))
        if self.grid_attribute != ATTRIBUTE.DENSE and self.grid_density >= self.dense_threshold * avg_density:
            self.attributeChanged = True
            self.grid_attribute = ATTRIBUTE.DENSE
        elif self.grid_attribute != ATTRIBUTE.SPARSE and self.grid_density <= self.sparse_threshold * avg_density:
            self.attributeChanged = True
            self.grid_attribute = ATTRIBUTE.SPARSE
        elif self.grid_attribute != ATTRIBUTE.TRANSITIONAL and self.grid_density > self.sparse_threshold * avg_density and self.grid_density < self.dense_threshold * avg_density:
            self.attributeChanged = True
            self.grid_attribute = ATTRIBUTE.TRANSITIONAL

    def setInitialAttraction(self, attrL):
        """ generated source for method setInitialAttraction """
        for i in attrL:
            self.attraction_list.append(i)


    def normalizeAttraction(self, attr_list):
        """ generated source for method normalizeAttraction """

        total_attr = 0.0
        i = 0
        while i < 2 * self.DIMENSION + 1:
            total_attr += attr_list[i]
            i += 1
        if total_attr <= 0:
            return
        attr = float()
        #  normalize
        i = 0
        while i < 2 * self.DIMENSION + 1:
            attr = attr_list[i]
            attr_list[i]= attr / total_attr
            i += 1


    def getAttraction(self, data_coords, grid_coords):
        """ generated source for method getAttraction """
        attr_list = list()
        i = 0

        while i < 2 * self.DIMENSION + 1:
            attr_list.append(1.0)
            i += 1
        last_element = 2 * self.DIMENSION
        i = 0
        closeToBigNeighbour = False
        while i < len(grid_coords):
            upper_range = self.DIMENSION_UPPER_RANGE[i]
            lower_range = self.DIMENSION_LOWER_RANGE[i]
            num_of_partitions = self.DIMENSION_PARTITION[i]
            partition_width = (upper_range - lower_range) / (num_of_partitions);
            center = grid_coords[i]*partition_width + partition_width/2.0;
            radius = partition_width / 2.0
            epsilon = 0.6*radius
            if data_coords[i] > center:
                closeToBigNeighbour = True
            if (radius - epsilon) > abs(data_coords[i] - center):
                attr_list[2 * i] = 0.0
                attr_list[2 * i + 1] = 0.0
                attr_list[last_element] = 1.0
            else:
                if closeToBigNeighbour:
                    weight1 = ((epsilon - radius) + (data_coords[i] - center))
                    weight2 = ((epsilon + radius) - (data_coords[i] - center))
                    prev_attr = attr_list[2 * i]
                    attr_list[2 * i] = prev_attr * weight1
                    attr_list[2 * i + 1] = 0.0
                    k =0
                    while k < 2 * self.DIMENSION + 1:
                        if k != 2 * i and k != 2 * i + 1:
                            prev_attr = attr_list[k]
                            attr_list[k] = prev_attr * weight2
                        k = k + 1
                else:
                    weight1 = ((epsilon - radius) - (data_coords[i] - center))
                    weight2 = ((epsilon + radius) + (data_coords[i] - center))
                    prev_attr = attr_list[2 * i + 1]
                    attr_list[2 * i + 1] = prev_attr * weight1
                    attr_list[2 * i] =  0.0
                    k =0
                    while k < 2 * self.DIMENSION + 1:
                        if k != 2 * i and k != 2 * i + 1:
                            prev_attr = attr_list[k]
                            attr_list[k] = prev_attr * weight2
                        k = k + 1
            i += 1
        self.normalizeAttraction(attr_list)
        return attr_list

    def updateGridAttraction(self, attr_list, time):
        """ generated source for method updateGridAttraction """
        last = 2 * self.DIMENSION
        i = 0
        while i < 2 * self.DIMENSION + 1:
            attraction_decay1 = self.attraction_list[i]*(math.pow(self.decay_factor,(time -self.last_time_updated) ))
            attr_new = attr_list[i] + attraction_decay1
            if attraction_decay1 <= self.correlation_threshold and attr_new > self.correlation_threshold and i != last and not self.attributeChanged:
                self.setAttributeChanged(True)
            self.attraction_list[i] = attr_new
            i += 1

    def updateDecayedGridAttraction(self, time):
        """ generated source for method updateDecayedGridAttraction """
        i = 0
        while i < 2 * self.DIMENSION + 1:
            attraction_decay = self.attraction_list[i]*(math.pow(self.decay_factor,(time -self.last_time_updated) ))
            self.attraction_list[i] = attraction_decay
            i += 1

    def printGridAttraction(self, attrL):
        """ generated source for method printGridAttraction """
        print " GRID PRINT ATTRACTION"
        # Log.i(MY_TAG," print Attraction grid ");
        
        i = 0
        while i < 2 * self.DIMENSION + 1:
            print "Attraction at " 
            print i
            print attrL[i]
            i += 1
        # Log.i(MY_TAG, " Attraction at " + String.valueOf(i) + " is " + String.valueOf(attrL.get(i)));

    def printAttractionList(self):
        """ generated source for method printAttractionList """
        print " print ATRAACTION LIST"
        #print self.DIMENSION
        i = 0
        while i < 2 * self.DIMENSION + 1:
            print " Attraction at "
            print i
            print self.attraction_list[i]
            i+= 1
        #  Log.i(MY_TAG, " Attraction at " + String.valueOf(i) + " is " + String.valueOf(attraction_list.get(i)));

    def getAttractionAtIndex(self, i):
        """ generated source for method getAttractionAtIndex """
        return self.attraction_list[i]


# ============================================================================================================================================================================

class Clusterisation(object):
    """ generated source for class Clusterisation """
    gridList = {} 
    clusters = {}
    DIMENSION = 0
    DIMENSION_LOWER_RANGE = list()
    DIMENSION_UPPER_RANGE = list()
    DIMENSION_PARTITION = list()
    TOTAL_GRIDS = 1
    dense_threshold = 3.0

    #  Cm = 3.0
    sparse_threshold = 0.8

    #  Cl = 0.8
    time_gap = 0
    decay_factor = 0.998
    correlation_threshold = 0.0
    latestCluster = 0

    def __init__(self):
        """ generated source for method __init__ """
        self.DIMENSION = 0
        self.TOTAL_GRIDS = 1
        self.dense_threshold = 3.0
        self.sparse_threshold = 0.8
        self.time_gap = 0
        self.decay_factor = 0.998
        self.correlation_threshold = 0.0
        self.latestCluster = 0

        
    def printGridList(self):
        """ generated source for method printGridList """
        gridKeys = self.gridList
        
        for gKey in gridKeys:
            grid = self.gridList.get(gKey)
            if grid.isDense():
                print " Coordinates:" 
                print gKey
                print " Density:" 
                print grid.getGridDensity()
                print " Grid: DENSE" 
                print " Cluster: " 
                print grid.getCluster()
            if grid.isTransitional():
                print " Coordinates:" 
                print gKey 
                print " Density:"
                print grid.getGridDensity()
                print " Grid: TRANSITIONAL"
                print " Cluster: " 
                print grid.getCluster()
            if grid.isSparse():
                print " Coordinates:"
                print   gKey 
                print " Density:" 
                print grid.getGridDensity() 
                print " Grid: SPARSE" 
                print " Cluster: " 
                print grid.getCluster()

    def printGridAttraction(self):
        """ generated source for method printGridAttraction """
        gridKeys = self.gridList
        for gKey in gridKeys:
            grid = self.gridList.get(gKey)
            print gKey
            
            if grid.isDense():
                print " Coordinates: " 
                print gKey
                print " Density: " 
                print grid.getGridDensity() 
                print " Grid: DENSE"
            if grid.isTransitional():
                print " Coordinates: "
                print gKey
                print " Density: " 
                print grid.getGridDensity() 
                print " Grid: TRANSITIONAL"
            if grid.isSparse():
                print " Coordinates:"
                print gKey 
                print " Density: " 
                print grid.getGridDensity() 
                print "  Grid: SPARSE"
            
            grid.printAttractionList()

    def printClusters(self):
        """ generated source for method printClusters """
        clusterKeys = self.clusters
        
        for ckey in clusterKeys:
            gridCoords = self.clusters.get(ckey)
            print " Cluster Index: " + ckey.__str__() 
            for coord in gridCoords:
                print "   Coordinates: " 
                print coord


    ## working correctly
    def updateDimensionInfo(self, line):
        """ generated source for method updateDimensionInfo """
        dimensionInfo = line.split(",")
        length = len(dimensionInfo)
        self.DIMENSION = int(dimensionInfo[0])
        total_pairs = 0
        i = 1
        
        while i < (length - 2):
            self.DIMENSION_LOWER_RANGE.append(int(dimensionInfo[i]))
            self.DIMENSION_UPPER_RANGE.append(int(dimensionInfo[i + 1]))
            self.DIMENSION_PARTITION.append(int(dimensionInfo[i + 2]))
            self.TOTAL_GRIDS *= int(dimensionInfo[i + 2])
            i = i + 3
        factor = 0.0
        pairs = 0.0
        j = 0
        
        while j < self.DIMENSION:
            factor = self.TOTAL_GRIDS / self.DIMENSION_PARTITION[j]
            pairs = self.DIMENSION_PARTITION[j] - 1
            total_pairs += (factor) * (pairs)
            j += 1
        
        self.correlation_threshold = self.dense_threshold / (total_pairs * (1 - self.decay_factor))
 


    def getNeighbours(self, from_):
        """ generated source for method getNeighbours """
        neighbours = list()
        dim = 0
        while dim < from_.getSize():
            val = from_.getDimension(dim)
            bigger = Coordinates(from_)
            bigger.setDimension(dim, val + 1)
            if self.gridList.has_key(bigger):
                neighbours.append(bigger)
            smaller = Coordinates(from_)
            smaller.setDimension(dim, val - 1)
            if self.gridList.has_key(smaller):
                neighbours.append(smaller)
            dim += 1
        return neighbours

    def getDimensionBigNeighbours(self, from_, dim):
        """ generated source for method getDimensionBigNeighbours """
        coord = Coordinates(from_)
        val = coord.getDimension(dim)
        bigger = Coordinates(from_)
        bigger.setDimension(dim, val + 1)

        if self.gridList.has_key(bigger):
            return bigger
        return coord

    def getDimensionSmallNeighbours(self, from_, dim):
        """ generated source for method getDimensionSmallNeighbours """

        coord = Coordinates(from_)
        val = coord.getDimension(dim)
        smaller = Coordinates(from_)
        smaller.setDimension(dim, val - 1)

        if self.gridList.has_key(smaller):
            return smaller
        return coord

    def checkUnconnectedClusterAndSplit(self, clusterIndex):
        """ generated source for method checkUnconnectedClusterAndSplit """
        if not self.clusters.has_key(clusterIndex):
            return
        gridCoords = self.clusters[clusterIndex]
        grpCoords = {}
        if gridCoords.isEmpty():
            return
        dfsStack = Stack()
        dfsStack.push(gridCoords.iterator().next())
        while not dfsStack.empty():
            coords = dfsStack.pop()
            grid = self.gridList.get(coords)
            if grid.isVisited():
                continue 
            grid.setVisited(True)
            neighbours = getNeighbours(coords)
            for ngbr in neighbours:
                grpCoords.append(ngbr)
                dfsStack.push(ngbr)
        if len(grpCoords) == len(gridCoords):
            return
        newCluster = self.latestCluster + 1
        self.latestCluster += 1
        self.clusters[newCluster]= grpCoords
        for c in grpCoords:
            g = self.gridList.get(c)
            g.setCluster(newCluster)


    def findStronglyCorrelatedNeighbourWithMaxClusterSize(self, coord, onlyDense):
        """ generated source for method findStronglyCorrelatedNeighbourWithMaxClusterSize """
        resultCoord = Coordinates(coord)
        initCoord = Coordinates(coord)
        largestClusterSize = 0
        
        grid = self.gridList[initCoord]
        i = 0
        while i < self.DIMENSION:
            big_neighbour = self.getDimensionBigNeighbours(coord,i)
            
            small_neighbour = self.getDimensionSmallNeighbours(coord,i)

            if not big_neighbour.equals(initCoord):
                bigNeighbourGrid = self.gridList[big_neighbour]
                if not onlyDense or  bigNeighbourGrid.isDense():
                    bigNeighbourClusterIndex = bigNeighbourGrid.getCluster()

                    if not bigNeighbourClusterIndex == 0 and not bigNeighbourClusterIndex == grid.getCluster():

                        if bigNeighbourGrid.getAttractionAtIndex(2 * i + 1) > self.correlation_threshold and grid.getAttractionAtIndex(2 * i) > self.correlation_threshold:
                            if self.clusters.has_key(bigNeighbourClusterIndex):
                                bigNeighbourClusterGrids = self.clusters.get(bigNeighbourClusterIndex)
                                if len(bigNeighbourClusterGrids) >= largestClusterSize:
                                    largestClusterSize = len(bigNeighbourClusterGrids)
                                    resultCoord = big_neighbour

            if not small_neighbour.equals(initCoord):
                smallNeighbourGrid = self.gridList[small_neighbour]
                if not onlyDense or smallNeighbourGrid.isDense():
                    smallNeighbourClusterIndex = smallNeighbourGrid.getCluster()
                    if not smallNeighbourClusterIndex == 0 and not smallNeighbourClusterIndex == grid.getCluster():
                        if smallNeighbourGrid.getAttractionAtIndex(2 * i) > self.correlation_threshold and grid.getAttractionAtIndex(2 * i + 1) > self.correlation_threshold:
                            if self.clusters.has_key(smallNeighbourClusterIndex):        
                                smallNeighbourClusterGrids = self.clusters.get(smallNeighbourClusterIndex)
                                if len(smallNeighbourClusterGrids) >= largestClusterSize:
                                    largestClusterSize = len(smallNeighbourClusterGrids)
                                    resultCoord = small_neighbour
            i += 1
        return resultCoord






    def removeSporadicGrids(self, gridList, time):
        """ generated source for method removeSporadicGrids """
        removeGrids = list()
        gridListKeys = gridList.keys()
        for glKey in gridListKeys:
            grid = gridList.get(glKey)
            lastTimeElementAdded = grid.getLastTimeElementAdded()
            densityThresholdFunc = (self.sparse_threshold * (1 - math.pow(self.decay_factor, time - lastTimeElementAdded + 1))) / (self.TOTAL_GRIDS * (1 - self.decay_factor))
            grid.updateDecayedGridDensity(time)
            grid.updateGridAttribute()
            grid.updateDecayedGridAttraction(time)
            grid.setLastTimeUpdated(time)
            if grid.getGridDensity() < densityThresholdFunc:
                removeGrids.append(key)
        for index in removeGrids:
            gridList.remove(index)   


    def adjustClustering(self, gridList, time):
        """ generated source for method adjustClustering """
        gridListKeys = gridList.keys()
        for coordkey in gridListKeys:
            grid = gridList.get(coordkey)
            key = coordkey.getCoords()

            if not grid.isAttributeChangedFromLastAdjust():
                continue 
            
            gridCluster = grid.getCluster()
            if grid.isSparse():
                if self.clusters.has_key(gridCluster):
                    clusterCoords = self.clusters.get(gridCluster)
                    grid.setCluster(0)
                    del clusterCoords[key]
                    self.checkUnconnectedClusterAndSplit(gridCluster)
            elif grid.isDense():
                neighbourCoords = self.findStronglyCorrelatedNeighbourWithMaxClusterSize(key, False);

                if not self.gridList.has_key(neighbourCoords) or neighbourCoords.equals(coordkey):

                    if not self.clusters.has_key(gridCluster):
                    
                        clusterIndex = self.latestCluster + 1
                        self.latestCluster += 1
                        coordset = []
                        coordset.append(key)
                        self.clusters[clusterIndex] = coordset
                        grid.setCluster(clusterIndex)
                    grid.setAttributeChanged(False)
                    continue

                neighbour = self.gridList.get(neighbourCoords)

                neighbourClusterIndex = neighbour.getCluster()
                if not self.clusters.has_key(neighbourClusterIndex):
                    continue 

                neighbourClusterGrids = self.clusters.get(neighbourClusterIndex)
                if neighbour.isDense():
                    if not self.clusters.has_key(gridCluster):
                        grid.setCluster(neighbourClusterIndex)
                        self.clusters[neighbourClusterIndex].append(key)
                    else:
                        currentClusterGrids = self.clusters.get(gridCluster)
                        size1 = 0
                        
                        for val in currentClusterGrids:
                            size1 +=1

                        size2 = 0
                        
                        for val in neighbourClusterGrids:
                            size2 +=1

                        if size2 >= size1:
                            for c in currentClusterGrids:
                                coord = Coordinates(c)
                                g = self.gridList.get(coord)
                                g.setCluster(neighbourClusterIndex)
                                self.clusters[neighbourClusterIndex].append(c)
                            del self.clusters[gridCluster]
                        else:
                            for c in neighbourClusterGrids:
                                g = self.gridList.get(c)
                                g.setCluster(gridCluster)
                                self.clusters[gridCluster].append(c)
                            del self.clusters[neighbourClusterIndex]
                elif neighbour.isTransitional():
                    if not self.clusters.has_key(gridCluster):
                        grid.setCluster(neighbourClusterIndex)
                        self.clusters[neighbourClusterIndex].append(key)
                    else:
                        currentClusterGrids = self.clusters.get(gridCluster)
                        if len(currentClusterGrids) >= len(neighbourClusterGrids):
                            self.clusters[gridCluster].append(neighbourCoords)
                            clusterGrid = clusters[neighbourClusterIndex]
                            del clusterGrid[neighbourCoords]
            elif grid.isTransitional():
                if self.clusters.has_key(gridCluster):
                    del self.clusters[gridCluster]
                neighbourCoords = self.findStronglyCorrelatedNeighbourWithMaxClusterSize(key, True);
                if not self.gridList.has_key(neighbourCoords) or neighbourCoords.equals(coordkey):
                    grid.setAttributeChanged(False)
                    grid.setCluster(0)
                    continue 
                
                neighbour = self.gridList.get(neighbourCoords)
                neighbourClusterIndex = neighbour.getCluster()
                if self.clusters.has_key(neighbourClusterIndex):
                    self.clusters[neighbourClusterIndex].append(key)
            grid.setAttributeChanged(False)
    

    def mapDataToGrid(self, line, time):
        """ generated source for method mapDataToGrid """
        dataInfo = line.split(",")
        datalength = len(dataInfo)
        if datalength != self.DIMENSION:
            return
        grid_coords = list()
        data_coords = list()
        data = 0.0
        grid_Width = 0.0
        dim_index = 0
        i = 0
        while i < datalength:
            data = float(dataInfo[i])
            data_coords.append(data)
            if data >= self.DIMENSION_UPPER_RANGE[i] or data < self.DIMENSION_LOWER_RANGE[i]:
                return
            grid_Width = (self.DIMENSION_UPPER_RANGE[i] - self.DIMENSION_LOWER_RANGE[i]) / (self.DIMENSION_PARTITION[i])
            dim_index = int(math.floor((data - self.DIMENSION_LOWER_RANGE[i]) / grid_Width))
            grid_coords.append(dim_index)
            i += 1

        
        gridCoords = Coordinates(grid_coords)

        if not self.gridList.has_key(gridCoords):
            g = Grid(False,0,time,1,ATTRIBUTE.SPARSE, self.DIMENSION, self.DIMENSION_UPPER_RANGE, self.DIMENSION_LOWER_RANGE, self.DIMENSION_PARTITION, self.TOTAL_GRIDS, self.decay_factor, self.dense_threshold, self.sparse_threshold, self.correlation_threshold)
            attrL = g.getAttraction(data_coords, grid_coords)
            g.setInitialAttraction(attrL)
            self.gridList[gridCoords] = g
        else:
            g = self.gridList[gridCoords]
            gridCoords = None
            g.updateGridDensity(time)
            g.updateGridAttribute()
            attrL = g.getAttraction(data_coords, grid_coords)
            g.updateGridAttraction(attrL, time)
            g.setLastTimeUpdated(time)
        

                
    def readFromFile(self):
        print "ReadFromFile"
        time =0
        first = True
        with open('rand.txt') as fp:
            for line in fp:
                if first:
                    first = False
                    self.updateDimensionInfo(line)
                    dense_to_sparse_time = math.log(self.sparse_threshold / self.dense_threshold) / math.log(self.decay_factor)
                    sparse_to_dense_time = math.log((self.TOTAL_GRIDS - self.dense_threshold) / (self.TOTAL_GRIDS - self.sparse_threshold)) / math.log(self.decay_factor)
                    self.time_gap = int(min(dense_to_sparse_time, sparse_to_dense_time))
                else:
                    self.mapDataToGrid(line, time)
                    if time > 0:
                        
                        if time % self.time_gap == 0:
                            self.removeSporadicGrids(self.gridList, time)
                            self.adjustClustering(self.gridList, time)
                time += 1
        print " =====Clusters====="
        self.printClusters()
        print " ======Grid List ===="
        self.printGridList()
        print " =====Attraction======"
        self.printGridAttraction()

 

cluster = Clusterisation()
cluster.readFromFile()
