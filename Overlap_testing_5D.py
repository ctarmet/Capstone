import numpy as np

def original_polytope(n):
    # Important that the first 2 vertices constitute an edge that is parallel with 5th dim-axis
    # That is, a pair of coordinates that only differs in the 5th dim-value
    # Also, the first vertex should have a smaller 5D-value compared to the second vertex
    
    if n == 6: # Regular 5-simplex
        a = 1 / np.sqrt(15)
        b = 1 / np.sqrt(10)
        c = 1 / np.sqrt(6)
        d = 1 / np.sqrt(3)

        vertices = np.array([[a, b, c, d, -1,], [a, b, c, d, 1], [a, b, c, -2*d, 0], [a, b, - np.sqrt(3)/np.sqrt(2), 0, 0], [a, - (2*np.sqrt(2))/np.sqrt(5), 0, 0, 0], [- np.sqrt(5)/np.sqrt(3), 0, 0, 0, 0]])
        return vertices
    
    if n == 10: # Regular 5-orthoplex
        vertices = np.array([[0,0,0,0,-1], [0,0,0,0,1], [0,0,0,-1,0], [0,0,0,1,0], [0,0,-1,0,0], [0,0,1,0,0], [0,-1,0,0,0], [0,1,0,0,0], [-1,0,0,0,0], [1,0,0,0,0]])
        return vertices
    
    if n == 32: # Regular 5-cube
        vertices = np.array([[-1,-1,-1,-1,-1], [-1,-1,-1,-1,1], [-1,-1,-1,1,-1], [-1,-1,-1,1,1], [-1,-1,1,-1,-1], [-1,-1,1,-1,1], [-1,-1,1,1,-1], [-1,-1,1,1,1], [-1,1,-1,-1,-1], [-1,1,-1,-1,1], [-1,1,-1,1,-1], [-1,1,-1,1,1], [-1,1,1,-1,-1], [-1,1,1,-1,1], [-1,1,1,1,-1], [-1,1,1,1,1], [1,-1,-1,-1,-1], [1,-1,-1,-1,1], [1,-1,-1,1,-1], [1,-1,-1,1,1], [1,-1,1,-1,-1], [1,-1,1,-1,1], [1,-1,1,1,-1], [1,-1,1,1,1], [1,1,-1,-1,-1], [1,1,-1,-1,1], [1,1,-1,1,-1], [1,1,-1,1,1], [1,1,1,-1,-1], [1,1,1,-1,1], [1,1,1,1,-1], [1,1,1,1,1]])
        return vertices
    

def affine(vertices, r, n):
    # Determine the coordinates of the scaled vertices after each affine transformation
    scaled_vertices = []
    for i in range(n):
        fixed_vertex = vertices[i]
        transformation = (1-r)*vertices + r*fixed_vertex
        scaled_vertices.append(transformation)

    # Returns |V| sets of scaled coordinates. One set of |V| coordinates for each v_i in V
    return scaled_vertices


def overlap_test(n, r):
    """Iteratively increase r until there is no overlap.
    If the x-coordinates are not close enough, iteratively decrese r until 
    they are closer than the accepted error"""
    # Generate the original vertices
    vertices = original_polytope(n)
    original_side_length = get_side_length(vertices)
    print(f"Original side length: {original_side_length}")

    # iterate over r starting at an initial point and going towards 1
    while r < 1:
        print(f"\nChecking for r = {r}")

        # Find the scaled vertices for this r
        scaled_vertices = affine(vertices, r, n)

        # Only needed to check the 5D-coords of two regions because of the symmetry
        # We use the indicies 0 and 1 since they are 2 vertices that gives an edge parallel to the 5D-axis
        # See original_polytope comments for better understanding
        region1 = scaled_vertices[0]
        region2 = scaled_vertices[1]

        # Initialize the list of 5D-values for the 2 regions
        region1_5D = []
        region2_5D = []

        # Find the 5D-values of the transformed vertices
        for i in range(len(region1)):
            coord = region1[i]
            region1_5D.append(coord[4])
        
        for i in range(len(region2)):
            coord = region2[i]
            region2_5D.append(coord[4])

        r1max = max(region1_5D) # The largest 5D-value of the first region
        r2min = min(region2_5D) # The smallest 5D-value of the second region

        # Calculate dm in conjectured ropt formula. Note that these are the original polytopes vertex-coordinates
        dim_5s = []
        for i in range(n):
            vertex = vertices[i]
            dim_5s.append(vertex[4])
            
        # Since all polytopes are oriented with the edge between vertices[0] and vertices[1] being parallel with the x-axis
        dm = max(dim_5s) - min(dim_5s)

        
        # Check if overlap occurs
        if r1max - r2min > 0.000001:
            print(f"Overlap detected at r = {r}")

            # Increase r and continue
            r += 0.00001

        elif abs(r1max - r2min) < 0.000001: # Accepted error. Will give at least 5 correct decimals
            print(f"Experimental Optimal Ratio Achieved\nr = {r}")
            # Print conjectured optimal ratio, and dm in terms of edge length
            print(f"Conjectured Optimal Ratio: {dm/(dm + original_side_length)}")
            edgelength = get_side_length(vertices)
            print(f"dm in terms of edge length: {dm/edgelength} * edgelength") 

            return r

        else:
            # Regions are no longer touching
            print(f"Regions not touching for r = {r}")

            r -= 0.0000001
            

def get_side_length(vertices):
    # Compute the side length of a polygon determined by it's vertices
     return np.linalg.norm(vertices[0] - vertices[1])


overlap_test(32, 0.49)

